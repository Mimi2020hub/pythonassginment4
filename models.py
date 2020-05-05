from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting,on_delete=models.DO_NOTHING)
    meetingattendance=models.ManyToManyField(User)
    minutestext=models.TextField()
    
    def __str__(self):
        return str(self.meetingid)

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True,blank=True)
    resourceentrydate=models.DateField()
    resourceuserid=models.ManyToManyField(User)
    resourcedescription=models.TextField()  

    def __str__(self):
        return self.resourcename

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()
    eventuserid=models.ForeignKey(User, on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.eventtitle
