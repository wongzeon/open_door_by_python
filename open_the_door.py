#coding:utf8
import requests

#获取账号token
get_token_url = 'https://xcx.nsspmj.cn:8020/system/user/getToken/抓包获取?requestData=抓包获取'
get_token_header = {
'Host': 'xcx.nsspmj.cn:8020',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
'content-type': 'application/json',
'withEncrypt': "1",
'Referer': 'https://servicewechat.com/wx抓包获取/25/page-frame.html',
'Accept-Encoding': 'gzip, deflate, br'
}
req_get_token = requests.get(get_token_url, headers=get_token_header)
get_token = req_get_token.json()
final_token = get_token['data']['token']

#获取开门令牌
get_secret_url = 'https://xcx.nsspmj.cn:8020/openDoor/getOpenDoorSecret/抓包获取'
get_secret_header = {
'Host': 'xcx.nsspmj.cn:8020',
'Connection': 'keep-alive',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
'content-type': 'application/json',
'Referer': 'https://servicewechat.com/wx抓包获取/25/page-frame.html',
'Accept-Encoding': 'gzip, deflate, br'
}
req_get_secret = requests.get(get_secret_url, headers=get_secret_header)
get_secret = req_get_secret.json()
final_secret = get_secret['data']

#发起开门请求
oepn_door_header = {
    'Host': 'xcx.nsspmj.cn:8020',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'Content-Length': "561",
    'content-type': 'application/json',
    'Referer': 'https://servicewechat.com/wx抓包获取/25/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br'
}
open_door_content = {
  "houseHostId": "抓包获取",
  "openId": "wx抓包获取",
  "openDoorSecret": final_secret
}
open_door_url = 'https://xcx.nsspmj.cn:8020/openDoor/commandByhouseHostId?token='+ final_token
opend_door = requests.post(open_door_url, json=open_door_content, headers=oepn_door_header)
print(opend_door.json())
