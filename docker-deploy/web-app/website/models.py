from django.db import models

# Do we need add a field which is world_id to differentiate different tests?
# same shipment id but at diff warehouse

# Create your models here.


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=128)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(blank=False, max_length=128)

    def __str__(self):
        return "name = " + self.name + " email = " + self.email


class Truck(models.Model):
    status_options = {
        ('IDLE', 'idle'),
        ('TRAVELING', 'traveling'),
        ('ARRIVE WAREHOUSE', 'arrive warehouse'),
        ('LOADING', 'loading'),
        ('DELIVERING', 'delivering')
    }
    truckid = models.AutoField(primary_key=True)
    x = models.IntegerField(blank=False)
    y = models.IntegerField(blank=False)
    status = models.CharField(
        blank=False, choices=status_options, max_length=128)
    pac_num = models.IntegerField(null=False, default=0)

    def __str__(self):
        return "truckid = " + str(self.truckid) + " status = " + self.status + " pac_num = " + str(self.pac_num)


class Package(models.Model):
    status_options = {
        ('in WH', 'in WH'),
        ('loading', 'loading'),
        ('loaded', 'loaded'),
        ('delivering', 'delivering'),
        ('delivered', 'delivered')
    }
    tracking_id = models.AutoField(primary_key=True)
    shipment_id = models.IntegerField(blank=False, unique=True)
    truckid = models.ForeignKey(to=Truck, verbose_name="FK_truck",
                                on_delete=models.CASCADE, default=None, blank=False, null=False)
    x = models.IntegerField(blank=False)  # destination addr
    y = models.IntegerField(blank=False)
    user = models.ForeignKey(to=User, verbose_name="FK_binded_user",
                             on_delete=models.SET_NULL, default=None, blank=True, null=True)  # user could be null
    status = models.CharField(
        blank=False, choices=status_options, max_length=128)

    def __str__(self):
        return "tracking_id = " + str(self.tracking_id) + " ship_id = " + str(self.shipment_id) + " truckid = " + str(self.truckid) + " status = " + self.status


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(blank=False, max_length=128)
    count = models.IntegerField(blank=False)
    tracking_id = models.ForeignKey(to=Package, verbose_name="FK_Package",
                                    on_delete=models.CASCADE, default=None, blank=False, null=False)

    def __str__(self):
        return "item description = " + self.description + " tracking_id = " + str(self.tracking_id)

# record trucks on the way to warehouse(truck status = traveling)


class AssignedTruck(models.Model):
    count = models.AutoField(primary_key=True)
    whid = models.IntegerField(blank=False, null=False)
    truckid = models.ForeignKey(to=Truck, verbose_name="FK_truck",
                                on_delete=models.CASCADE, default=None, blank=False, null=False)

    def __str__(self):
        return "whid = " + str(self.whid) + " truckid = " + str(self.truckid)

# handled response from world
# when we receive a response from world, check if the seqnum exists in this table
# ignore (continue) if exist


class WorldRes(models.Model):
    seqnum = models.IntegerField(primary_key=True)

# command acked by world
# we constantly send our command in a while loop
# before each repeatative sending we check if our seqnumed command has the matching
# ack num in this table, break loop if exist


class AckedCommand(models.Model):
    seqnum = models.IntegerField(primary_key=True)
