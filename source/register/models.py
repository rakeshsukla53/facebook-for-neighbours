from django.db import models
from django.db.models.signals import pre_save

# Create your models here.

class Hood(models.Model):
    hid = models.IntegerField(primary_key=True)
    hname = models.CharField(max_length=100)
    hcity = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.hid)


class Registration(models.Model):
    uname = models.CharField(max_length=100, blank=False, null=False)
    upassword = models.CharField(max_length=100, blank=False, null=False)
    uphone = models.CharField(max_length=20, blank=True, null=True)
    uhid = models.ForeignKey('Hood', default='')
    uemail = models.EmailField(blank=False, null=False, default='rrs402@nyu.edu')
    uintro = models.TextField(null=True, blank=True)
    uphoto = models.ImageField(upload_to='', blank=False, null=False, default='static/img/natural_join_is_inner_join.png')
    uhood = models.CharField(max_length=100, default='Brooklyn')
    uaddress = models.CharField(max_length=100, default='ABC')
    # django automatically uses the media root which you have declared in your settings, define that to `upload_to`

    def __unicode__(self):
        return self.uname


class Block(models.Model):
    bid = models.IntegerField(primary_key=True)
    hid = models.ForeignKey('Hood')
    bname = models.CharField(max_length=100)

    def __unicode__(self):
        return self.bname


class History(models.Model):

    uid = models.ForeignKey('Registration')
    login_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    logout_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    session = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return unicode(self.uid)


class Friend(models.Model):
    class Meta:
        unique_together = (('fuid1', 'fuid2'),)

    fuid1 = models.ForeignKey('Registration')
    fuid2 = models.ForeignKey('Registration', related_name='+')
    hid = models.ForeignKey('Hood')
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return unicode(self.status)


class Neighbour(models.Model):
    class Meta:
        unique_together = (('nuid1', 'nuid2'),)
    nuid1 = models.ForeignKey('Registration')
    nuid2 = models.ForeignKey('Registration', related_name='+')
    hid = models.ForeignKey('Hood')


class AuthBlock(models.Model):
    uid = models.ForeignKey('Registration')
    bid = models.ForeignKey('Block', related_name='+')
    uapproved = models.BooleanField(default=False)
    total_request_required = models.IntegerField()
    approval_received = models.IntegerField()
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.status)

class Thread(models.Model):
    TID_CHOICES = (
        ('HOOD', 'Hood'),
        ('BLOCK', 'Block'),
        ('FRIEND', 'Friend'),
        ('NEIGHBOUR', 'Neighbour')
    )

    tid = models.AutoField(primary_key=True)
    ttype = models.CharField(max_length=10, choices=TID_CHOICES)
    tauthor = models.ForeignKey('Registration')
    tdate = models.DateTimeField(auto_now=True)
    tdesc = models.TextField()

    def __unicode__(self):
        return unicode(self.tid)

class Message(models.Model):

    tid = models.ForeignKey(Thread)
    mdate = models.DateTimeField(auto_now=True)
    mauthor = models.ForeignKey(Registration)
    mtext = models.TextField()

    def __unicode__(self):
        return unicode(self.mtext)

class Authorize(models.Model):
    tid = models.ForeignKey(Thread)
    author = models.ForeignKey(Registration)
    auth_user = models.CommaSeparatedIntegerField(max_length=100)
    hid = models.ForeignKey(Hood)

def registration_pre_save_receiver(sender, instance, *args, **kwargs):
    # print sender
    # print instance.uhood
    # print instance.uaddress
    # print instance.uname

    for i in Hood.objects.all():
        # print i
        if i.hname.strip() in instance.uaddress.strip():
            instance.uhood = i.hname
            instance.uhid = i  # it has to be hood instance

            print i.hid
    # instance.save()

pre_save.connect(registration_pre_save_receiver, sender=Registration)




