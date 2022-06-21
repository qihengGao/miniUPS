import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miniUPS.settings")
if django.VERSION >= (1, 7):
    django.setup()

import sys
from concurrent.futures import ThreadPoolExecutor
import socket
from threading import Thread
import threading
import time
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint
from protos import world_ups_pb2 as World_UPS
from protos import UA_pb2 as UA
import PBwrapper
from django.db.models import Q
import website.models as md
from django.core.mail import EmailMultiAlternatives  # 这样可以发送HTML格式的内容了
from django.conf import settings  # 将settings的内容引进



executer = ThreadPoolExecutor(40)
lock = threading.Lock()
lock_socket_world = threading.Lock()
lock_socket_amz = threading.Lock()

request_map = {}
seq_num = 0
world_id = None


def get_socket_to_amz():
    ups_host = '0.0.0.0'
    ip_port_amz = (ups_host, 55555)
    listen_to_amz = socket.socket()
    try:
        listen_to_amz.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_to_amz.bind(ip_port_amz)
        listen_to_amz.listen(5)
        socket_to_amz, address = listen_to_amz.accept()
        print("connect to amz" + "\n")
        return socket_to_amz
    except:
        print("having problem in connecting to amz\n")
        listen_to_amz.close()
        sys.exit(1)


def get_socket_to_world():
    world_host = 'vcm-25953.vm.duke.edu'
    ip_port_w = (world_host, 12345)
    socket_to_world = socket.socket()
    try:
        socket_to_world.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        socket_to_world.connect(ip_port_w)
        print("connect to world" + "\n")
        return socket_to_world
    except:
        print("having problem in connectiong to world\n")
        socket_to_world.close()
        sys.exit(1)


def get_seqnum() -> int:
    global seq_num
    lock.acquire()
    to_ret = seq_num
    seq_num += 1
    lock.release()
    return to_ret


def dock_amz(socket_to_world, socket_to_amz):
    print("dock to amz")
    count = 0
    while True:
        print("recv from amz: " + str(count))
        count += 1
        au_msg, is_socket_closed = recv_from_amz(socket_to_amz)
        if is_socket_closed:
            break
        if not au_msg:
            continue
        executer.submit(handle_amz, au_msg,
                        socket_to_world, socket_to_amz)
    print("dock amz ends")


def dock_world(socket_to_world, socket_to_amz):
    print("dock to world")
    while True:
        u_resp, is_socket_close = recv_from_world(socket_to_world)
        if is_socket_close:
            break
        if not u_resp:
            continue
        executer.submit(handle_world, u_resp,
                        socket_to_world, socket_to_amz)
    print("dock world ends")


def dock_frontend(socket_to_world, socket_to_amz):
    try:
        print("dock to frontend")
        ip_port_frontend = ('0.0.0.0', 8888)
        s_to_frontend = socket.socket()
        s_to_frontend.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_to_frontend.bind(ip_port_frontend)
        s_to_frontend.listen(5)
        while True:
            frontend, _ = s_to_frontend.accept()
            t = Thread(target=handle_frontend, args=(
                frontend, socket_to_world, socket_to_amz))
            # t.setDaemon(True)
            t.start()
    except Exception as ex:
        print(ex)


"""
Helper function for writing, write msg to socket_
"""


def write_msg(socket_, msg):
    string_msg = msg.SerializeToString()
    _EncodeVarint(socket_.send, len(string_msg), None)
    socket_.send(string_msg)

# Helper function for receiving, recv from socket_


def recv_msg(socket_) -> str:
    var_int_buff = []
    while True:
        buf = socket_.recv(1)
        if len(buf) <= 0:  # socket closes
            return None, True
        var_int_buff += buf
        print(str(var_int_buff))
        try:
            msg_len, new_pos = _DecodeVarint32(var_int_buff, 0)
            if new_pos != 0:
                break
        except IndexError:
            print("Error in decoding msg\n")
            return None, False
    print("msg_len: " + str(msg_len) + "\n")
    whole_message = socket_.recv(msg_len)
    return whole_message, False


def write_to_world(socket_to_world, msg):
    # if (not msg.Is("UConnect")):
    #     Ucommands = World_UPS.UCommands()
    #     if(msg.Is("UGoPickup")):
    #         Ucommands.pickups.append(msg)
    #     if(msg.Is("UGoDeliver")):
    #         Ucommands.deliveries.append(msg)
    #     if(msg.Is("UQuery")):
    #         Ucommands.queries.append(msg)
    #     write_msg(to_world_socket, Ucommands)
    # else:
    # TODO: set simspeed, disconnect, acks
    # write_msg(socket_to_world, msg)
    string_msg = msg.SerializeToString()
    lock_socket_world.acquire()
    _EncodeVarint(socket_to_world.send, len(string_msg), None)
    socket_to_world.send(string_msg)
    lock_socket_world.release()


def write_to_amz(socket_to_amz, msg: UA.UAmessage):
    # write_msg(to_amazom_socket, msg)
    string_msg = msg.SerializeToString()
    lock_socket_amz.acquire()
    _EncodeVarint(socket_to_amz.send, len(string_msg), None)
    socket_to_amz.send(string_msg)
    lock_socket_amz.release()

# Recv from world's response after successfully connected


def recv_from_world(to_world_socket):
    whole_message, is_socket_closed = recv_msg(to_world_socket)
    if is_socket_closed:
        return None, True
    world_res = World_UPS.UResponses()
    try:
        world_res.ParseFromString(whole_message)
        print("------------------- recv from world -------------------")
        print(str(world_res))

        return world_res, False
    except:
        print("------------------- Error parsing message from world -------------------")
        return None, False


def recv_from_amz(socket_to_amazom) -> UA.AUmessage:
    whole_message, is_socket_closed = recv_msg(socket_to_amazom)
    if is_socket_closed:
        return None, True
    au_msg = UA.AUmessage()
    try:
        au_msg.ParseFromString(whole_message)
        print("-------------------recv from amz -------------------" )
        print(str(au_msg))
        return au_msg, False
    except:
        print("Error parsing message from amz\n")
        return None, False


def connect_to_word(truck_num, socket_to_world) -> bool:
    msg = World_UPS.UConnect()
    msg.isAmazon = False
    id_to_pos = []
    for i in range(truck_num):
        truck_to_add = msg.trucks.add()
        truck_to_add.id = i + 1
        x_ = 0
        y_ = 0
        truck_to_add.x = x_
        truck_to_add.y = y_
        id_to_pos.append([x_, y_])
    msg.isAmazon = False
    write_msg(socket_to_world, msg)  # no need for repeat
    uconnected_str, _ = recv_msg(socket_to_world)
    print("------------------- recv from world -------------------")
    print(str(uconnected_str))
    uconnected = World_UPS.UConnected()
    uconnected.ParseFromString(uconnected_str)
    print("world id: " + str(uconnected.worldid))
    print("result: " + str(uconnected.result))
    world_id = uconnected.worldid
    if uconnected.result == "connected!":
        print("connect to world " + str(world_id) + " successfully\n")
        # write truck to db
        for val in id_to_pos:
            new_truck = md.Truck()
            new_truck.status = "IDLE"
            new_truck.x = val[0]
            new_truck.y = val[1]
            new_truck.save()
            print(str(new_truck) + "saved")
        return world_id, True
    return world_id, False


def reconnect_to_word(world_id, socket_to_world) -> bool:
    msg = World_UPS.UConnect()
    msg.worldid = world_id
    msg.isAmazon = False
    write_msg(socket_to_world, msg)
    uconnected_str, _ = recv_msg(socket_to_world)
    print("receive from world: " + str(uconnected_str) + "\n")
    uconnected = World_UPS.UConnected()
    uconnected.ParseFromString(uconnected_str)
    print("world id: " + str(uconnected.worldid))
    print("result: " + uconnected.result)
    if uconnected.result == "connected!":
        print("reconnect to world " + str(world_id) + " successfully\n")
        return world_id, True
    return world_id, False


"""
send ack back to each item in UResponses structs
"""


def handle_world_send_ack(u_rsp, socket_to_world):
    seqnum_list = []
    for u_finished in u_rsp.completions:
        print("259 before u_finished: " + str(seqnum_list))
        seqnum_list.append(u_finished.seqnum)
        print("after u_finished: " + str(seqnum_list))

    for u_delivery_made in u_rsp.delivered:
        print("264 before u_delivery_made: " + str(seqnum_list))
        seqnum_list.append(u_delivery_made.seqnum)
        print("after u_delivery_made: " + str(seqnum_list))

    # for ack_ in u_rsp.acks:
    #     print("before ack_: " + str(seqnum_list) + "\n")
    #     seqnum_list.append(ack_)
    #     print("after ack_: " + str(seqnum_list) + "\n")

    for trcuk_status in u_rsp.truckstatus:
        print("274 before trcuk_status: " + str(seqnum_list))
        seqnum_list.append(trcuk_status.seqnum)
        print("276 after trcuk_status: " + str(seqnum_list))

    for err_ in u_rsp.error:
        print("279 before err_: " + str(seqnum_list))
        seqnum_list.append(err_.seqnum)
        print("281 after err_: " + str(seqnum_list))

    if seqnum_list:
        u_commands = World_UPS.UCommands()
        u_commands.acks.extend(seqnum_list)
        # synchronized out?
        write_to_world(socket_to_world, u_commands)


"""
Handle UFinished
"""


def handle_world_finished(u_finished, socket_to_world, socket_to_amz):
    # save hanlded response from world
    world_res = md.WorldRes()
    world_res.seqnum = u_finished.seqnum
    world_res.save()
    truck_id_ = u_finished.truckid
    print("301 World tells truck[" + str(truck_id_) +
          "]: " + str(u_finished.status))
    truck_status = u_finished.status
    print("304 truck[" + str(truck_id_) + "]'s status: " + truck_status)
    # renew truck's status
    # lock on row?
    truck = md.Truck.objects.filter(truckid=truck_id_).first()
    truck.status = truck_status
    truck.save()
    if truck_status == "ARRIVE WAREHOUSE":
        try:
            # delete truck from Assigned Truck
            assigned_truck = md.AssignedTruck.objects.get(truckid = truck).delete()
            # tell amz truck has arrived
            send_arrive = PBwrapper.send_arrive(
                truck_id_, u_finished.x, u_finished.y)
            ua_msg = UA.UAmessage()
            ua_msg.send_arrive.CopyFrom(send_arrive)
            print("317 send to amz: " + str(ua_msg))
            # lock on socket?
            write_to_amz(socket_to_amz, ua_msg)
            # update truck & package status to loading
            truck.status = "LOADING"
            truck.save()
            packages = md.Package.objects.filter(
                truckid=truck.truckid).filter(status="in WH")
            
            if packages:
                for package in packages:
                    package.status = "loading"
                    package.save()
        except Exception as ex:
            print(ex)

# send mail to user when package delivered


def send_mail(email):
    # user = md.User.objects.filter(email=email).first()
    print("353 send email to " + email)
    subject = 'Your package has been delivered!'
    # text_content = 'Your package has been delivered! Please go to the pick up loaction on time.'
    html_content = '''
    <p>Woo hoo! Your package has been delivered. Please go to the pick-up loaction on time.</p >
    <p>Enjoy with your </p >
    '''
    from_email = settings.DEFAULT_FROM_EMAIL
    to = []
    to.append(email)  # to = '', '', ''   可接多个邮箱地址
    msg = EmailMultiAlternatives(subject, html_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def handle_world_delievered(u_delivery_made, socket_to_world, socket_to_amz):
    try:
        print("326 " + str(u_delivery_made))
        # save hanlded response from world
        world_res = md.WorldRes()
        world_res.seqnum = u_delivery_made.seqnum
        world_res.save()

        package_id = u_delivery_made.packageid
        truck_id = u_delivery_made.truckid
        # update package status
        package = md.Package.objects.filter(shipment_id=package_id).first()
        print("345 to set as delievered: " + str(package))
        package.status = "delivered"
        package.save()
        print(str(package) + " saved")

        # send mail to user
        flag = not package.user
        flag_ = not flag
        print("386 package has user " + str(flag_))
        if package.user:
            print("389 user exists calling send_email()")
            send_mail(package.user.email)

        # update truck's pac_num
        truck = md.Truck.objects.filter(truckid=truck_id).first()
        print("352 to decrease pac_num: " + str(truck))
        truck.pac_num -= 1
        truck.save()
        print(str(truck) + " saved")

        # tell amz package delievered
        ua_msg = UA.UAmessage()
        ua_msg.pac_delivered.shipment_id = package_id
        print("360 send to amz: " + str(ua_msg))
        # lock on socket?
        write_to_amz(socket_to_amz, ua_msg)
    except Exception as ex:
        print(ex)


def is_acked(our_req_seq_num) -> bool:
    return md.AckedCommand.objects.filter(seqnum=our_req_seq_num).exists()


def res_handled(world_res_seq_num) -> bool:
    return md.WorldRes.objects.filter(seqnum=world_res_seq_num).exists()


def handle_world_truck_status(truck_status, socket_to_world, socket_to_amz):
    # save hanlded response from world
    world_res = md.WorldRes()
    world_res.seqnum = truck_status.seqnum
    world_res.save()

    truck = md.Truck.objects.filter(truckid=truck_status.truckid).first()
    truck.status = truck_status.status
    truck.x = truck_status.x
    truck.y = truck_status.y
    truck.save()
    return


def handle_world(u_rsp: World_UPS.UResponses, socket_to_world, socket_to_amz):
    print("recv from world: " + str(u_rsp))
    # send ack to world
    handle_world_send_ack(u_rsp, socket_to_world)

    for u_finished in u_rsp.completions:
        # renew truck's status
        # tell amz truck has arrived
        if not res_handled(u_finished.seqnum):
            handle_world_finished(u_finished, socket_to_world, socket_to_amz)
    for u_delivery_made in u_rsp.delivered:
        # renew truck's status
        # renew package's status -> delivered
        if not res_handled(u_delivery_made.seqnum):
            handle_world_delievered(
                u_delivery_made, socket_to_world, socket_to_amz)

    for ack_ in u_rsp.acks:
        # terminate the request from our side, where ack = seqnum of our req
        print("ack_: " + str(ack_) + "\n")
        if is_acked(ack_):
            continue
        print("saving acked num: " + str(ack_) + "\n")
        acked_command = md.AckedCommand()
        acked_command.seqnum = ack_
        acked_command.save()
        print("saved\n")

    for truck_status in u_rsp.truckstatus:
        if not res_handled(truck_status.seqnum):
            handle_world_truck_status(
                truck_status, socket_to_world, socket_to_amz)

    for err_ in u_rsp.error:
        print(err_)

    if u_rsp.HasField("finished") and u_rsp.finished:  # close connection
        print("disconnect successfully")


def pick_truck(wh_id):
    print("start to select truck")
    # avoid race condition on picking the same truck
    while True:
        try:
            # check whether already exist truck on the way to the WH
            assigned_truck = md.AssignedTruck.objects.filter(
                whid=wh_id).first()
            if assigned_truck:
                return assigned_truck.truckid.truckid
            # sort the result sorted from IDLE to DELIVERING, pick the 1st one
            truck = md.Truck.objects.filter(Q(status='IDLE') | Q(
                status='DELIVERING')).order_by('-status').first()
            print(truck)
            if truck:
                print("445 the picked truck is:" + str(truck))
                # update truck status to Traveling
                print("447 truck to update: " + str(truck))
                truck.status = 'TRAVELING'
                truck.save()
                print(str(truck) + " save successfully")
                return truck.truckid
            else:
                # if no truck meet requirement, wait for 5s and try again
                time.sleep(5)
                continue
        except Exception as ex:
            print(ex)


'''
verify the validation of ups username from Amazon
@return: true if username valid, false vice versa
'''


def verify_user(username, package):
    print("442 start to verify user: " + str(username))
    user = md.User.objects.filter(username=username).first()
    if user:
        # update package's username
        print("453 " + username + " in our db")
        package.user = user
        package.save()
        print("449 updated package = " + str(package))
        return True
    print("451 " + username + "is not in our db")
    return False


'''
handle World part for handle_amz_pickup
'''


def w_a_pickup(truck_id, wh_id, pickup, socket_to_world, socket_to_amz):
    print("461 constructing pickup ins to world...")
    try:
        # insert into DB: AssignedTrucks
        truck, not_assigned = md.AssignedTruck.objects.get_or_create(
            whid=wh_id, truckid=md.Truck.objects.filter(truckid=truck_id).first())
        # send pickup response to amazon
        a_pickup(truck_id, pickup, socket_to_amz)
        # global seqnum atomically increase seqnum += 1
        seqnum_ = get_seqnum()
        go_pickup = None
        # only send world UGoPickUp with a not_assigned truck
        if not_assigned:
            go_pickup = PBwrapper.go_pickup(truck_id, wh_id, seqnum_)
            print("468 send go_pickup = " + str(go_pickup))
        # send UCommands(UGoPickup) to World
        if not_assigned:
            u_commands = World_UPS.UCommands()
            u_commands.pickups.append(go_pickup)
            print("518 send to world: " + str(u_commands))
            while not is_acked(seqnum_):
                write_to_world(socket_to_world, u_commands)
                time.sleep(1)
    except Exception as ex:
        print(ex)


'''
handle Amazon part for handle_amz_pickup
'''


def a_pickup(truck_id, pickup: UA.APacPickup, socket_to_amz):
    try:
        ship_id = pickup.shipment_id
        # insert into DB: Package
        print("500 inserting package " + str(ship_id))
        truck = md.Truck.objects.filter(truckid=truck_id).first()
        package = md.Package()
        package.shipment_id = ship_id
        package.truckid = truck
        package.x = pickup.x
        package.y = pickup.y
        package.status = 'in WH'
        package.save()
        # update package with username if valid
        is_binded = False
        if pickup.HasField("ups_username"):
            is_binded = verify_user(pickup.ups_username, package)
        pac_pickup_res = PBwrapper.pac_pickup_res(
            package.tracking_id, is_binded, ship_id, truck_id)

        print("505 send pac_pickup_res = " + str(pac_pickup_res))
        # send response to Amazon
        ua_msg = UA.UAmessage()
        ua_msg.pickup_res.CopyFrom(pac_pickup_res)
        write_to_amz(socket_to_amz, ua_msg)
    except Exception as ex:
        print(ex)


'''
 handle Amazon request "APacPickup"
 @recv from Amazon:
    APacPickup: whid, shipment_id, ups_username, x, y
 @send to World:
    UGoPickup: truckid, whid, seqnum
 @send to Amazon:
    UPacPickupRes: tracking_id, is_binded, shipment_id, truck_id
'''


def handle_amz_pickup(pickup: UA.APacPickup, socket_to_world, socket_to_amz):

    print("528 received APacPickup = " + str(pickup))
    wh_id = pickup.whid
    # pick an idle or delivering truck to pickup
    lock.acquire()
    truck_id = pick_truck(wh_id)
    lock.release()

    # World part
    w_a_pickup(truck_id, wh_id, pickup, socket_to_world, socket_to_amz)
    return


'''
 handle Amazon request "ASendAllLoaded"
 @recv from Amazon:
    ASendAllLoaded: truckid, packages(x,y,shipment_id, 
                                        item(product_id, description, count))
 @send to World:
    UGoDeliver: truckid, packages(packageid,x,y), seqnum
'''


def handle_amz_all_loaded(all_loaded: UA.ASendAllLoaded, socket_to_world, socket_to_amz):
    # parse ASendAllLoaded, insert into db: Package
    print("570 handling all_loaded")
    try:
        pac_list = []
        for package in all_loaded.packages:
            ship_id = package.shipment_id
            print("ship_id of the package: " + str(ship_id))
            track = md.Package.objects.get(shipment_id=ship_id)
            print("576 process pack: " + str(package))
            print(str(track))
            for item in package.items:
                print("563 process item: " + str(item))
                # insert into fProduct
                item_ = md.Item.objects.create(
                    description=item.description, count=item.count, tracking_id=track)
                print("581 inserted item: " + str(item))
            # read pack's dest from db
            pac_list.append(PBwrapper.gene_package(
                ship_id, track.x, track.y))
            # track is_a package
            track.status = "loaded"
            track.save()
            print(track)
        # update the pac_num of loaded truck, change status back to AW
        print("598 update the pac_num of loaded truck " + str(all_loaded.truck_id))
        truck = md.Truck.objects.filter(truckid=all_loaded.truck_id).first()
        truck.status = "ARRIVE WAREHOUSE"
        truck.pac_num += len(pac_list)
        truck.save()
        print("603 " + str(truck) + " saved")
        
        
        # change truck & packages status to delivering after world handeled UGoDeliver
        print("658 packs " + str(ship_id) + " loaded, set packs & truck to delivering")
        truck.status = "DELIVERING"
        truck.save()
        for package in all_loaded.packages:
            ship_id = package.shipment_id
            package_ = md.Package.objects.get(shipment_id=ship_id)
            package_.status = "delivering"
            package_.save()
        seqnum_ = get_seqnum()
        go_deliver = PBwrapper.go_deliver(
            all_loaded.truck_id, pac_list, seqnum_)
        u_commands = World_UPS.UCommands()
        u_commands.deliveries.append(go_deliver)

        # global seqnum atomically increase
        # send Ucommands(UGoDeliver) to World
        while not is_acked(seqnum_):
            write_to_world(socket_to_world, u_commands)
            time.sleep(1)
        
    except Exception as ex:
        print(ex)


'''
 handle Amazon request "ABindUpsUser"
 @recv from Amazon:
    ABindUpsUser: shipment_id, ups_username
 @send to Amazon:
    UBindRes: shipment_id, is_binded
'''


def handle_amz_bindups(bind_upsuser: UA.ABindUpsUser, socket_to_world, socket_to_amz):
    try:
        print("bind_upsuser: " + str(bind_upsuser))
        print("603 start to rebinding user")
        ship_id = bind_upsuser.shipment_id
        package = md.Package.objects.filter(shipment_id=ship_id).first()
        # verify user validaty, update package is valid
        is_binded = verify_user(bind_upsuser.ups_username, package)
        bind_res = PBwrapper.bind_res(ship_id, is_binded)
        # send response to Amazon
        ua_msg = UA.UAmessage()
        ua_msg.bind_res.CopyFrom(bind_res)
        print("598 sending bind res " + str(ua_msg) + " to amz")
        write_to_amz(socket_to_amz, ua_msg)
        return
    except Exception as ex:
        print(ex)


def handle_amz(au_msg: UA.AUmessage, socket_to_world, socket_to_amz):
    # handle specific amazon request
    if au_msg.HasField("pickup"):
        handle_amz_pickup(au_msg.pickup, socket_to_world, socket_to_amz)
    if au_msg.HasField("all_loaded"):
        handle_amz_all_loaded(
            au_msg.all_loaded, socket_to_world, socket_to_amz)
    if au_msg.HasField("bind_upsuser"):
        handle_amz_bindups(au_msg.bind_upsuser, socket_to_world, socket_to_amz)
    return


'''
send worldid to Amazon
@send: 
    USendWorldId: worldid
'''


def a_worldid(socket_to_amz, worldid):
    # world_id_ = PBwrapper.send_WorldId(worldid)
    ua_msg = UA.UAmessage()
    ua_msg.world_id.world_id = worldid
    write_to_amz(socket_to_amz, ua_msg)
    return


def handle_frontend(frontend, socket_to_world, socket_to_amz):
    try:
        while True:
            data = frontend.recv(1024)
            if len(data) <= 0:
                frontend.close()
                return
            data = data.decode()
            info = data.split(",")
            print("710 recv from frontend: " + str(info))
            if info[0] == "change":  # change,truckid,packageid,x,y
                truck_id = int(info[1])
                package_id = int(info[2])
                x_ = int(info[3])
                y_ = int(info[4])
                pack = md.Package.objects.get(shipment_id=package_id)
                if pack.status == "delivering" or pack.status == "dilivered":
                    return
                print("720 Pack to edit: " + str(720))
                pack.x = x_
                pack.y = y_
                pack.save()
                print(str(pack) + " saved")
            elif info[0] == "resend":  # resend, ship_id
                ship_id = int(info[1])
                ua_msg = UA.UAmessage()
                ua_msg.resend_package.shipment_id = ship_id
                print("729 sent to amz: " + str(ua_msg))
                write_to_amz(socket_to_amz, ua_msg)
                pass
            else:
                print("I cannot understand")
    except Exception as ex:
        print(ex)


def main():
    if len(sys.argv) < 3:
        print(
            "Usage: python3 hello_world_amz.py create [truck_num] for create new world")
        print(
            "Usage: python3 hello_world_amz.py reconnect [world_id] for create new world")
        sys.exit(1)
    world_id = None
    # socket_to_world = None
    # socket_to_amz = None
    socket_to_world = get_socket_to_world()
    # send connect/reconnect to world
    retry = 5
    if sys.argv[1] == 'create':
        truck_num = int(sys.argv[2])
        print("# of trucks to create: " + str(truck_num))
        if truck_num <= 0:
            print("# of trucks should be positive")
            sys.exit(1)
        world_id, is_connected = connect_to_word(truck_num, socket_to_world)
        while retry and not is_connected:
            print("Connect to world failed, retrying...")
            world_id, is_connected = connect_to_word(
                truck_num, socket_to_world)
            retry -= 1
    elif sys.argv[1] == 'reconnect':
        world_id = int(sys.argv[2])
        world_id, is_connected = reconnect_to_word(world_id, socket_to_world)
        while retry and not is_connected:
            print("Connect to world failed, retrying...")
            world_id, is_connected = reconnect_to_word(
                world_id, socket_to_world)
            retry -= 1
    else:
        print("Please check your input: " + str(sys.argv) + "\n")
        print(
            "Usage: python3 hello_world_amz.py create [truck_num] for create new world" + "\n")
        print(
            "Usage: python3 hello_world_amz.py reconnect [world_id] for create new world" + "\n")
        sys.exit(1)

    if not retry:
        print("Failed to conenct the world" + "\n")
        sys.exit()

    socket_to_amz = get_socket_to_amz()
    # send the world_id to amz
    a_worldid(socket_to_amz, world_id)
    try:
        # start one thread to dock amz
        t_to_amz = Thread(target=dock_amz, args=(
            socket_to_world, socket_to_amz))
        # start one thread to dock world
        t_to_world = Thread(target=dock_world, args=(
            socket_to_world, socket_to_amz))

        t_to_frontend = Thread(target=dock_frontend, args=(
            socket_to_world, socket_to_amz))
        # t_to_frontend.setDaemon(True)
        # print("Is t_to_front set as Daemon? " + str(t_to_frontend.isDaemon()))
        t_to_world.start()
        t_to_amz.start()
        t_to_frontend.start()
        

    finally:
        t_to_world.join()
        t_to_amz.join()
        socket_to_world.close()
        socket_to_amz.close()


if __name__ == "__main__":
    main()
