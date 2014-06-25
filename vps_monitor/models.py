#coding=utf8

from django.db import models
from django.contrib import admin

class Remote(models.Model):
    address = models.TextField()
    port = models.IntegerField()
    username = models.TextField()
    password = models.TextField()

    def __unicode__(self): 
        return self.username + '@' + self.address + ':' + str(self.port)

admin.site.register(Remote)
