#!/usr/bin/python3

#install sshpass

import os
import paramiko #pip3 install paramiko
import time
from datetime import datetime, date

UserName = "root"
Password = "password"
Host = "localhost"
Port = 22
DestDir = "/home/dest"
SrcDir = "/home/src"
Retention = 3 #In Day

NameHost = os.uname()[1]

datenow = datetime.now()
dt_string = datenow.strftime("%Y-%m-%d-%H-%M")

ssh = paramiko.SSHClient()

# ssh.load_system_host_keys()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(Host, Port, UserName, Password)

time.sleep(5)
print('connected')
CreateDestRet = "mkdir -p " + DestDir + "/" + NameHost + "/" + dt_string + " ; find " + DestDir + "/" + NameHost + "/* -mtime +" + str(Retention) + " -delete"
print(CreateDestRet)
stdin, stdout, stderr = ssh.exec_command(CreateDestRet)

def execute():
       print('Create directory')

execute()
ssh.close()

ScpAction = "sshpass -p \"" + Password + "\" scp -r -p " + SrcDir + " " + UserName + "@" + Host + ":" + DestDir + "/" + NameHost + "/" + dt_string
print(ScpAction)
scp = os.system(ScpAction) 
print(scp)
