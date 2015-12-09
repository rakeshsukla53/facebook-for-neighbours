from django.db import models

# Create your models here.

class Hood(models.Model):
    hid = models.IntegerField(primary_key=True)
    hname = models.CharField(max_length=100)
    hcity = models.CharField(max_length=100)

    def __unicode__(self):
        return self.hname

class Registration(models.Model):
    uname = models.CharField(max_length=100, blank=False, null=False)
    upassword = models.CharField(max_length=100, blank=False, null=False)
    uphone = models.IntegerField(blank=True, null=True)
    uhid = models.ForeignKey('Hood', blank=False, null=False, default='ABC')
    uemail = models.EmailField(blank=False, null=False, default='rrs402@nyu.edu')
    uintro = models.TextField(null=True, blank=True)
    uphoto = models.ImageField(upload_to='', blank=False, null=False, default='static/img/natural_join_is_inner_join.png')
    uhood = models.CharField(max_length=10, null=True)
    uaddress = models.CharField(max_length=100, default='ABC')
    # django automatically uses the media root which you have declared in your settings, define that to `upload_to`

    def __unicode__(self):
        return self.uname

class Block(models.Model):
    bid = models.IntegerField(primary_key=True)
    hid = models.ForeignKey('Hood', default='ABC')
    bname = models.CharField(max_length=100)

    def __unicode__(self):
        return self.bname









