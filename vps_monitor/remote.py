# -*- coding: utf-8 -*-

import paramiko

#记录日志
paramiko.util.log_to_file('/tmp/test')

#建立连接
ssh = paramiko.SSHClient()

#缺失host_knows时的处理方法
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程客户机器
try:
    ssh.connect('vps.jiangzifan.com',port=22,username='test',password='jzf19921222',compress=True)
except Exception, e:
    print e

#获取远程命令执行结果
def viewMemory():
    return ssh.exec_command('free')[1].read()

def viewNetwork():
    return ssh.exec_command('ifconfig')[1].read()

def viewDisk():
    return ssh.exec_command('df -h')[1].read()
