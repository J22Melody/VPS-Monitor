# -*- coding: utf-8 -*-

import paramiko

# 记录日志
paramiko.util.log_to_file('/tmp/test')

# 单例
SSH_list = {

}

class SSH:
    def __init__(self, **options):
        #建立连接
        ssh = paramiko.SSHClient()

        #缺失host_knows时的处理方法
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #连接远程客户机器
        try:
            ssh.connect(**options)
            self.ssh = ssh
        except Exception, e:
            print e

    @staticmethod
    def getInstance(**options):
        hostname = options.get('hostname')
        instance = SSH_list.get(hostname)
        if instance == None:
            instance = SSH_list[hostname] = SSH(**options)
        return instance

    def execCommand(self, command):
        return self.ssh.exec_command(command)[1].read()


# test

if __name__ == '__main__':
    remote = SSH.getInstance(**{'hostname': 'vps.jiangzifan.com', 'port': 22, 'username': 'test', 'password': 'jzf19921222'})
    remote = SSH.getInstance(**{'hostname': 'vps.jiangzifan.com', 'port': 22, 'username': 'test', 'password': 'jzf19921222'})
    print remote.execCommand('df -h')
