import requests
import os
from subprocess import run, PIPE
from time import sleep
#登录地址
post_addr="http://auth.dlut.edu.cn/eportal/InterFace.do?method=login"

#构造头部信息
//这里可能需要改cookie，你也可以尝试只修改学号和密码，你可以用错误的用户名和密码尝试去获取cookie
post_header={
		'Accept': '*/*',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
		'Connection': 'keep-alive',
		'Content-Length': '620',
		'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'Cookie': 'EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_COOKIE_SERVER=; EPORTAL_AUTO_LAND=; EPORTAL_COOKIE_USERNAME=/*你的学号*/; EPORTAL_COOKIE_PASSWORD=/*你的密码*/; EPORTAL_COOKIE_SERVER_NAME=%E8%AF%B7%E9%80%89%E6%8B%A9%E6%9C%8D%E5%8A%A1; EPORTAL_COOKIE_DOMAIN=; EPORTAL_COOKIE_SAVEPASSWORD=true; JSESSIONID=B33E7F0C2646407034D6C66BDABBFA44; whistlekey=gp7HRTEvwq715jHCQbmWS4RXZ6hSbRVXMjCKSzjK6Sw%3D; JSESSIONID=89C86EB29EABD02DABCB3712F24143E9',
		'Host': 'auth.dlut.edu.cn',
		'Origin': 'http://auth.dlut.edu.cn',
		'Referer': 'http://auth.dlut.edu.cn/eportal/index.jsp?wlanuserip=9c979d24d2fcacd2ebfd379e28cfaa9b&wlanacname=df066d169c39d07305dcabb988054834&ssid=&nasip=b7b559c9e7b461d404d0b61516e928ce&snmpagentip=&mac=3013a3e15b49de02f0ab033ba2d77fcd&t=wireless-v2&url=39ab723c65df156d962f79763648fffe3bb4360d1096557d&apmac=&nasid=df066d169c39d07305dcabb988054834&vid=1a712d5010b42e9a&port=82e8731c9db5590e&nasportid=b988a772be64b4c01f9ffc014127ea3918520fa316457e2fd3b90329f6465b0f4a96abf9f73f5764',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

}
//修改用户名和密码
post_data = {
		'userId': /*你的用户名*/,
		'password': /*你的密码*/,
        'service': '',
        'queryString': 'wlanuserip%3D9c979d24d2fcacd2ebfd379e28cfaa9b%26wlanacname%3Ddf066d169c39d07305dcabb988054834%26ssid%3D%26nasip%3Db7b559c9e7b461d404d0b61516e928ce%26snmpagentip%3D%26mac%3D3013a3e15b49de02f0ab033ba2d77fcd%26t%3Dwireless-v2%26url%3D39ab723c65df156d962f79763648fffe3bb4360d1096557d%26apmac%3D%26nasid%3Ddf066d169c39d07305dcabb988054834%26vid%3D1a712d5010b42e9a%26port%3D82e8731c9db5590e%26nasportid%3Db988a772be64b4c01f9ffc014127ea3918520fa316457e2fd3b90329f6465b0f4a96abf9f73f5764',
	    'operatorPwd': '',
        'operatorUserId': '',
        'validcode': ''
	}
if __name__ == '__main__':
	cnt = 1
	while True:

		r = os.system('ping -c 1 -W 1 www.baidu.com')//windows系统中，这里W改为w
		print(r)
		if r:
			print('relogin 第{}次'.format(cnt))
			response = requests.post(post_addr, data=post_data, headers=post_header)
			print(response.text)
			cnt += 1
		else:
			print('正常联网')
		sleep(60 * 1)  # 每半个小时检查一次



