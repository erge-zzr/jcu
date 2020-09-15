import jenkins
import requests
import re

#获取本机外网IP地址
req=requests.get("http://txt.go.sohu.com/ip/soip")
req=req.text
ip = re.findall('window.sohu_user_ip="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"',req)
intranetIp=ip[0].split("=")[1].strip('"')
# print(intranetIp.strip('"'))

#注册jenkins slave
server = jenkins.Jenkins('http://101.37.146.125:8787',username="admin",password="123.com?")
user=server.get_whoami()
version=server.get_version()

params = {
    "port":22,
    'username': 'root',
    #'credentialsId': "834d0ef0-bf51-4f86-a4ed-2664155fd636",
    'credentialsId': "e3298c30-99aa-4657-8a31-a592fa1f0ede",
    'host': intranetIp
}

server.create_node(
    'Us_slave',
    nodeDescription="my test slave",
    remoteFS="/root/",
    labels="Us_slave",
    exclusive=True,
    launcher=jenkins.LAUNCHER_SSH,
    launcher_params = params
)
