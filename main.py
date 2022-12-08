#!/usr/bin/python3

# apt install sshpass python3 python3-pip
# pip3 install paramiko

import os
import paramiko
import time
from datetime import datetime, date

UserName = "root"
Password = ""
Host = "localhost"
Port = 22
SrcDir = "/home/src"
DestDir = "/home/dest"
Retention = 3 #In Day
NameHost = os.uname()[1]
datenow = datetime.now()
dt_string = datenow.strftime("%Y-%m-%d-%H-%M")

def createFolder():
    ssh = paramiko.SSHClient()
    # ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(Host, Port, UserName, Password)
    time.sleep(5)
    CreateDestRet = "mkdir -p " + DestDir + "/" + NameHost + "/" + dt_string + " ; find " + DestDir + "/" + NameHost + "/* -mtime +" + str(Retention) + " -delete"
    stdin, stdout, stderr = ssh.exec_command(CreateDestRet)
    print('Create directory')
    ssh.close()

def copyFile():
    ScpAction = "sshpass -p \"" + Password + "\" scp -r -p " + SrcDir + " " + UserName + "@" + Host + ":" + DestDir + "/" + NameHost + "/" + dt_string
    print("Data Copy")
    scp = os.system(ScpAction)

createFolder()
copyFile()