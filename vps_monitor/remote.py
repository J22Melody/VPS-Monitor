# -*- coding: utf-8 -*-

from models import Remote
import Pyro4

Pyro4.config.HMAC_KEY = '123456'

remote_list = Remote.objects.all()

monitors = {

}

for remote in remote_list:
    url = "PYRO:monitor@" + remote.address + ":7555"
    monitors[str(remote.id)] = Pyro4.Proxy(url)
