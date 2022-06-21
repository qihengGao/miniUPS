from typing import List
from google.protobuf.internal.decoder import _DecodeVarint32
from google.protobuf.internal.encoder import _EncodeVarint
from protos import world_ups_pb2 as World_UPS
from protos import UA_pb2 as UA


# class PBgenerator:
#     def __init__(self, to_world_socket, to_amazom_socket) -> None:
#         self.to_world_socket = to_world_socket
#         self.to_amazom_socket = to_amazom_socket
#         self.pbParser = PBparser()
#         self.seqnum = 0

# generate protobuf send to World

def go_pickup(truckid, whid, seqnum) -> World_UPS.UGoPickup:
    Ugo_pickup = World_UPS.UGoPickup()
    Ugo_pickup.truckid = truckid
    Ugo_pickup.whid = whid
    Ugo_pickup.seqnum = seqnum
    return Ugo_pickup


def gene_package(packageid, x, y) -> World_UPS.UDeliveryLocation:
    Upackage = World_UPS.UDeliveryLocation()
    Upackage.packageid = packageid
    Upackage.x = x
    Upackage.y = y
    return Upackage


def go_deliver(truckid, packages: List[World_UPS.UDeliveryLocation], seqnum) -> World_UPS.UGoDeliver:
    Ugo_deliver = World_UPS.UGoDeliver()
    Ugo_deliver.truckid = truckid
    for package in packages:
        Ugo_deliver.packages.append(package)
    Ugo_deliver.seqnum = seqnum
    return Ugo_deliver


def query_truck(truckid, seqnum) -> World_UPS.UQuery:
    Uquery = World_UPS.UQuery()
    Uquery.truckid = truckid
    Uquery.seqnum = seqnum
    return Uquery

# generate protobuf send to Amazon


def send_WorldId(worldid) -> UA.USendWorldId:
    Usend_Worldid = UA.USendWorldId()
    Usend_Worldid.world_id = worldid
    return Usend_Worldid


def pac_pickup_res(tracking_id, is_binded, shipment_id, truck_id) -> UA.UPacPickupRes:
    UPac_pickup_res = UA.UPacPickupRes()
    UPac_pickup_res.tracking_id = tracking_id
    UPac_pickup_res.is_binded = is_binded
    UPac_pickup_res.shipment_id = shipment_id
    UPac_pickup_res.truck_id = truck_id
    return UPac_pickup_res


def send_arrive(truckid, x, y) -> UA.UsendArrive:
    Usend_arrive = UA.UsendArrive()
    Usend_arrive.truck_id = truckid
    Usend_arrive.x = x
    Usend_arrive.y = y
    return Usend_arrive


def pac_delivered(shipment_id) -> UA.UPacDelivered:
    Upac_delivered = UA.UPacDelivered()
    Upac_delivered.shipment_id = shipment_id
    return Upac_delivered


def bind_res(shipment_id, is_binded: bool) -> UA.UBindRes:
    Ubind_res = UA.UBindRes()
    Ubind_res.shipment_id = shipment_id
    Ubind_res.is_binded = is_binded
    return Ubind_res


def resend_package(shipment_id) -> UA.UResendPackage:
    Uresend_pac = UA.UResendPackage()
    Uresend_pac.shipment_id = shipment_id
    return Uresend_pac
