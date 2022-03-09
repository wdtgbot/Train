import requests
import re


class Crm_token(object):
    try:
        username = int(input("请输入登录手机号：\n"))
        password = input("请输入登录密码：\n")
    except Exception as error:
        print("登录信息输入错误，错误信息%s" % (error))
    
    def __init__(self):
        self.url_login_in = 'http://xxxx'
        self.login_server = 'http://xxx/cas/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.Imh0dHA6XC9cLzQ3LjEwNi4xNzguNDk6ODA4MlwvIg.8HSZHPyW7byY-MOVtFhdsiy_cpigL3RcStk9hGa8Su8'
        self.return_url = "http://xxxx/?return_url=xxx/"
    
    def get_token(self, username=username, password=password):
        headers_check_login = {"Content-Type": "application/x-www-form-urlencoded"}
        url_check_login = 'http://xxxx/Auth/checkLogin'  # 用户名密码验证接口
        check_login_data = 'username=%d&password=%s' % (username, password)
        request_check_login = requests.post(url=url_check_login, headers=headers_check_login, data=check_login_data)
        response_login_message = request_check_login.json()
        # print(response_login_message)
        if response_login_message['msg'] == '成功' and response_login_message['code'] == 200:
            print('begin---login---')
            try:
                session = requests.Session()  # 建立session会话
                headers1 = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36",
                    "Referer": self.return_url, "Content-Type": 'application/x-www-form-urlencoded'}
                url_login_1 = self.url_login_in + '/CAS_server/login?action=getlt&service=%s&callback=jQuery33105752563290575323_1551706407492&_=1551706407493' % (
                    self.login_server)
                request1 = session.request("GET", url=url_login_1, headers=headers1, data=None)  # 登录前动态参数获取url
                response1 = request1.text
                get_shouquan_str1 = eval(re.search('{.*}', response1).group())  # 匹配出字典内的内容并用eval方法将str转换为dict
                get_lt = get_shouquan_str1['lt']  # 提取授权参数1
                get_execution = get_shouquan_str1['execution']  # 提取授权参数2
                cookies_login_1 = request1.cookies.get_dict()  # 获取cookie：JSESSIONID
                seesionId = cookies_login_1['JSESSIONID']
                requestSeesionId = str('JSESSIONID=' + seesionId)  # 拼接为请求可用的cookie值
                # print(requestSeesionId)
                # print(get_lt)
                # print(get_execution)
                headers2 = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36",
                    "Content-Type": 'application/x-www-form-urlencoded', "Cookie": requestSeesionId,
                    "Referer": self.return_url}
                url_login_2 = self.url_login_in + '/CAS_server/login?service=%s' % (self.login_server)
                # 请求信息头必须传cookie，否则会一直返回登录页面
                login_data = 'lt=%s&execution=%s&_eventId=submit&username=%s&password=%s&submit=登录' % (
                get_lt, get_execution, username, password)
                # login_data='lt=%s&execution=%s&_eventId=submit&username=%d&password=%s'%(get_lt,get_execution,username,password)
                # 登录body，将获取到对的两个动态参数也传进去
                request2 = session.post(url=url_login_2, headers=headers2, data=login_data.encode(),
                                        allow_redirects=False)
                # allow_redirects=False,禁止请求重定向：为了获取重定向url，requests模块默认请求重定向
                # request2=session.post(url=url_login_2,headers=headers2,data=login_data.encode(),allow_redirects=True)
                response2 = request2.text
                responseHeaders2 = request2.headers  # 获取reponse header
                # print(response2)
                # print(responseHeaders2)
                url_chongdingxiang_st = responseHeaders2["location"]  # 获取重定向url
                requests3 = session.get(url=url_chongdingxiang_st, headers=headers2, data=None, allow_redirects=False)
                response3 = requests3.text
                responseHeaders3 = requests3.headers
                php_session_cookie = responseHeaders3['Set-Cookie']  # 获取php_session
                php_session_id = re.search("(\w*\W*\w*)", php_session_cookie).group()  # 用正则匹配出所需要的php_session_id
                # print(php_session_id)
                # print(responseHeaders3)
                url_chongdingxiang_get_ticket = responseHeaders3['location']  # 获取重定向url
                headers3 = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36",
                    "Content-Type": 'application/x-www-form-urlencoded', "Set-Cookie": php_session_id,
                    "Referer": self.return_url}
                requests4 = session.get(url=url_chongdingxiang_get_ticket, headers=headers3, data=None,
                                        allow_redirects=False)
                response4 = requests4.text
                responseHeaders4 = requests4.headers
                # print(responseHeaders4)
                url_chongdingxiang_ticket = responseHeaders4['location']  # 获取重定向url
                requests5 = session.get(url=url_chongdingxiang_ticket, headers=headers3, data=None,
                                        allow_redirects=False)
                response5 = requests5.text
                responseHeaders5 = requests5.headers
                # print(responseHeaders5)
                # print(response5)
                ticket_data = re.search('(ticket.*)', url_chongdingxiang_ticket).group()  # 用正则匹配出ticket以及对应的value
                headers4 = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36",
                    "Content-Type": 'application/x-www-form-urlencoded',
                    "Referer": url_chongdingxiang_ticket}  # 将headers来源地址更改为url_chongdingxiang_ticket
                url_get_token = 'http://xxxx/Auth/login'  # 登录接口
                requests_get_token = session.post(url=url_get_token, headers=headers3, data=ticket_data)
                reponse6 = requests_get_token.json()
                crm_system_token = reponse6['data']['token']
                print('login---susscess---')
                print('当前登陆手机号为:%s,token为:\n%s' % (username, crm_system_token))
                return crm_system_token
            except BaseException as error:
                print('登录错误，token获取失败，\n错误信息：%s' % (error))
        else:
            print(response_login_message)


if __name__ == "__main__":
    tk = Crm_token()
    tk.get_token()
