import requests,time,colorama,json,random,string
from colorama import Fore,init
init()

normal_color = "\33[00m"
info_color = "\033[1;33m"
red_color = "\033[1;31m"
green_color = "\033[1;32m"
whiteB_color = "\033[1;37m"
detect_color = "\033[1;34m"
banner_color="\033[1;33;40m"
end_banner_color="\33[00m"

print('''


████████ ██ ██   ██       ██████  ██   ██ 
   ██    ██ ██  ██       ██  ████  ██ ██  
   ██    ██ █████  █████ ██ ██ ██   ███   
   ██    ██ ██  ██       ████  ██  ██ ██  
   ██    ██ ██   ██       ██████  ██   ██       
                            
Report on Tiktok accounts at crazy speed 1.3v
------------------------------------------
''')
print(red_color+'Developer ~ Falah - 0xfff0800')
print(green_color+'Always strive for the best')
print('------------------------------------------')
print('')
message = input('رسالتك للدعم الفني بالانجليزي : ')
emm = input('ضع اميلك لكي تتلقي رد شركة : ')

class report:
    def __init__(self):
        self.session = requests.Session()
        self.site_key = "6Ldt4CkUAAAAAJuBNvKkEcx7OcZFLfrn9cMkrXR8"
        self.url = "https://support.tiktok.com/"
        self.contents = open('config.json', 'r',encoding="latin-1",errors='ignore')
        self.data = json.load(self.contents)
        self.sessionid = self.data['sessionid']
        self.user = self.data['user']
        
        dd = ''+ self.user +''
        url = "https://social-media-data-tt.p.rapidapi.com/live/user?username="+dd+""
        payload = ""
        headers = {'Host': 'social-media-data-tt.p.rapidapi.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'x-rapidapi-key': '9c363ae588mshd71440a101292d4p1c4061jsn32d687f5b44f',
           'x-rapidapi-host': 'social-media-data-tt.p.rapidapi.com'
           }

        response = requests.request ("GET", url, data=payload, headers=headers)
        info = json.loads(response.text)

        
        
        post = str(info["uid"])
        post1 = str(info["nickname"])
        post2 = str(info["unique_id"])

        print ("")
        print (" -" * 15)
        print ("")
        print ('user : ',post2)
        print ('name : ',post1)
        print ('id : ', post)
        with open('idreP.txt', 'a') as x:
                      x.write(post + '\n')
        print (" -" * 15)
        print ("")


    def captcha(self):
        try:
            captcha_id = self.session.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format( self.site_key, self.url)).text.split('|')[1]
            recaptcha_answer = self.session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(self.API_KEY, captcha_id)).text
            print(Fore.YELLOW+"[Solving] captcha solving...")
            while 'CAPCHA_NOT_READY' in recaptcha_answer:
                time.sleep(5)
                recaptcha_answer = self.session.get("http://2captcha.com/res.php?key={}&action=get&id={}".format(self.API_KEY, captcha_id)).text
            recaptcha_answer = recaptcha_answer.split('|')[1]
            return recaptcha_answer
        except Exception as e:
            print(e)


    def email_gen(self):
        ran = ('').join(random.choices(string.ascii_letters + string.digits, k=8))
        email = (""+emm+"")
        return email
   
    
    def report(self):
        count=0
        emails = self.email_gen()
        answer1 = self.captcha()
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
            "Host":"www.tiktok.com",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate",
			"Origin":"https://www.tiktok.com",
            "Content-Type": "application/json",
            "tt-csrf-token": "IomywYjG1Zh2Uu8SXWZs_RwG",
			"Referer":"https://www.tiktok.com/legal/report/privacy?lang=en",
            "Cookie":"tt_webid_v2=6914693436357379585; tt_webid=6914693436357379585; ttwid=1%7C2-fqkIND0Hmv6t8lD-W3LQmVxyja6MekJrNltb1FRw0%7C1609952624%7C47e1b33eaa433c4913987dbac401aecc120102cf2112d7c91ca796c4f25788ad; passport_csrf_token=c187e0aa10568c1316e6eab170204561; passport_csrf_token_default=c187e0aa10568c1316e6eab170204561; MONITOR_WEB_ID=6914693436357379585; odin_tt=429b732da594e3c35e9ea01e11bead4fdd8c67d82d6f0373bb396e619d4012a4cf4c60aecf69cde6cdd88c30fb8fefac2d36d72ef8a56bb6afe5513b74754d8d; sid_guard="+self.sessionid+"%7C1609977359%7C5184000%7CSun%2C+07-Mar-2021+23%3A55%3A59+GMT; uid_tt=49051b57d7d56e1ee0db6efe463c8a0962100506fbb6710fd18e3322d775dde2; uid_tt_ss=49051b57d7d56e1ee0db6efe463c8a0962100506fbb6710fd18e3322d775dde2; sid_tt="+self.sessionid+"; sessionid="+self.sessionid+"; sessionid_ss="+self.sessionid+"; store-idc=alisg; store-country-code=sa; d_ticket=071a0d3c9e167b6e717ba021e0b1274accd58; passport_auth_status=1ed13bc810dedde7ecceeaf1e728a206%2C; passport_auth_status_ss=1ed13bc810dedde7ecceeaf1e728a206%2C; tt_csrf_token=IomywYjG1Zh2Uu8SXWZs_RwG; s_v_web_id=verify_kjn54r4m_SHmp0n2w_eko4_4g5s_9lf2_x0fGafXzyYXN"
        }
        dd="idreP.txt"
        password = open(dd).read().splitlines()



        for password in password:
              url = ("https://www.tiktok.com/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web&referer=&root_referer=&user_agent=Mozilla%2F5.0+(Macintosh%3B+Intel+Mac+OS+X+10.15%3B+rv:84.0)+Gecko%2F20100101+Firefox%2F84.0&cookie_enabled=true&screen_width=1680&screen_height=1050&browser_language=en-US&browser_platform=MacIntel&browser_name=Mozilla&browser_version=5.0+(Macintosh)&browser_online=true&ac=&timezone_name=Asia%2FRiyadh&priority_region=SA&verifyFp=verify_kjn54r4m_SHmp0n2w_eko4_4g5s_9lf2_x0fGafXzyYXN&appId=1233&region=SA&appType=m&isAndroid=false&isMobile=false&isIOS=false&OS=mac&did=6914693436357379585&tt-web-region=SA&uid=6870709390007485441")
              data ='{"reason":311,"object_id":"'+password+'","owner_id":"'+password+'","report_type":"user"}'
              response = requests.request  ("POST", url, data=data, headers=headers )
        if 'statusCode' in response.text:
            count += 1
            print(Fore.GREEN+"[Success] تم ارسال التقرير {}")
            print('[Success] اميلك -> '+emails)
            print('[Success] رسالتك لدعم -> '+message)
        elif "phone_number" in response.text:
            print(Fore.RED+"[Error] لا يمكن إرسال التقرير")
			
if __name__ == "__main__":
    while True:
        start = report()
        start.report()
