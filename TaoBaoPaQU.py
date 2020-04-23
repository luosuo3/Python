import logging
from time import sleep

import pymysql
import requests
import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def mistaken():
    try:
        print('*****循环跳过，本页无内容*****')
        # 如果淘宝拦截粘贴主要代码无限请求

        print('——————————正常运行——————————')
    except:
        mistaken()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'Accept-Language':'zh-CN,zh;q=0.9','cookie': '_samesite_flag_=true; cookie2=1d6528e74b5f04164e6ad3d971c8f7aa; t=98e2500450761d703a699b21f2c1c4cb; _tb_token_=eb1eee11b43e6; tfstk=czYfB26UB-2XiI2OPKGP0mWlrBbOZDE5aP6yG3L17aL7C9OfiraFd_Pci8aRv_1..; cna=Es4eF8Y4jW0CAWURlD4oRd97; sgcookie=E7dwSugJbRo%2BC%2BWDKMWNM; unb=3375541664; uc3=nk2=rLO1ZIQhg4OzQw%3D%3D&vt3=F8dBxdGKMW96sedqg4I%3D&id2=UNN65ecHdCuNcA%3D%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; csg=1baa7909; lgc=%5Cu778E%5Cu95F9%5Cu817E%5Cu62C9%5Cu62C9; cookie17=UNN65ecHdCuNcA%3D%3D; dnk=%5Cu778E%5Cu95F9%5Cu817E%5Cu62C9%5Cu62C9; skt=8cbabf431c50fdac; existShop=MTU4NzAxMTYwNg%3D%3D; uc4=id4=0%40UgQycrW8yO3UA5jAlq%2FhHOpdrK7c&nk4=0%40rp0ClXHGLTUwbfmaqpudQAR5YAMU; tracknick=%5Cu778E%5Cu95F9%5Cu817E%5Cu62C9%5Cu62C9; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=%E6%8B%8940; _nk_=%5Cu778E%5Cu95F9%5Cu817E%5Cu62C9%5Cu62C9; cookie1=Vy66jkhi5Ih1So6V%2F4Mj3Ojiht11GCUqhYPz%2B5PaKq4%3D; thw=cn; mt=ci=17_1; v=0; uc1=pas=0&cookie15=URm48syIIVrSKA%3D%3D&cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie14=UoTUPczzxbqsMQ%3D%3D&cookie21=W5iHLLyFe3xm&existShop=false; enc=GvcjFI%2BlA8fY4WFa0SoJ%2BvgdU1GlHf9RqXwoJOa6zFSgB8k4svOIKxGfj8qnoaDV6ceY3pASAqIrXO%2Blo07XrA%3D%3D; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; JSESSIONID=9D950162B180B554B354D21F8821CC49; l=eBS4d8SmQAW6Dc2oBOfwIO86VqQOSIRAguzMCEWpiT5POPCH5yNCWZXurgTMC3Gch6VkRufuw33TBeYBqSfcSQLy2j-la_kmn; isg=BEJCOyZTqIrIr7TWXNlBqX-6k0ikE0YtAtTpRoxbbrVj3-JZdKOWPcidi9qjj77F'}
chrome_driver=r"C:\Users\wzlx7\PycharmProjects\untitled3\venv\Scripts\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver)
driver.get('https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9e0QMVl&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F')
wait = WebDriverWait(driver, 10)
# 不加载图片,加快访问速度
ch_options = webdriver.ChromeOptions()
ch_options.add_experimental_option("prefs", {"profile.mamaged_default_content_settings.images": 2})
#浏览器为开发者模式防止淘宝识别
ch_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 禁用浏览器正在被自动化程序控制的提示
ch_options.add_argument('--disable-infobars')

button=driver.find_element_by_class_name('weibo-login')
button.click()
USERNAME = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(2) > div >input')))
USERNAME.send_keys('淘宝账号')
PASSWORD = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(3) > div > input')))
PASSWORD.send_keys('淘宝密码')
button=driver.find_element_by_class_name('W_btn_g')
button.click()
sleep(5)
db = pymysql.connect("localhost", "root", "521986", "python",use_unicode=True, charset="utf8")
cursor = db.cursor()
print("请输入爬取的商品")
s=input()
key=driver.find_element_by_xpath("//*[@id='q']")
key.send_keys(s)
key.send_keys(Keys.ENTER)
sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)");
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
a_all=soup.select('#J_NavCommonRowItems_0 > a')
list1=[]
list2=[]
dict1={}
for n in  a_all:
    list1.append(n.get("title"))
    list2.append(n.get("data-value"))
dict1=dict(zip(list1,list2))
print("如果要精确查找请选择控制台的类别,如果继续模糊查找请输入0！")
print(list1)
s=input()
if(s!='0'):
   s=str(dict1.get(s))
   url=driver.current_url
   s=s.split(':')[0]+'%3A'+s.split(':')[1]
   new_url=url+'&cps=yes&ppath='+s
   driver.get(new_url)
for l in range(100):
    sliding_step = 500
    js="var q=document.documentElement.scrollTop={}".format(str(sliding_step))
    driver.execute_script(js)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    html1=driver.page_source
    soup1=BeautifulSoup(html1,'lxml')
    a_all1=soup1.find_all('a',attrs={'class':'J_ClickStat'})

    b = False
    for n in a_all1:
        b = bool(1-b)
        if (b):
            continue

        try:

         id=str(n.get("data-nid"))
         href='https://'+str(n.get("href")).split('//')[1]
         title1=str(n.get_text()).strip()
         urllib3.disable_warnings()
         logging.captureWarnings(True)
         html=requests.get(href,headers=headers,verify=False).text
         soup2=BeautifulSoup(html,'lxml')
         type=str(href.split('//')[1].split('/')[0]).strip()
         list3=['one','two','three','four']

         if(type=='item.taobao.com'):
            li_all=soup2.select('#attributes > ul > li')
            print("淘宝爬取")
            k=0
            for i in li_all:
              list3[k]=str(i.get("title"))
              k=k+1
              if(k==4):
                break
            print(list3)
         if(type=='detail.tmall.com'):
            li_all=soup2.select('#J_AttrUL > li')
            print("天猫爬取")
            print(li_all)
            k=0
            for i in li_all:
                list3[k]=str(i.get("title"))
                k=k+1
                if(k==4):
                    break
        except:
            print("重新爬取")
            # mistaken()
        print('商品标题:'+title1)
        print('商品编号:'+id)
        print('商品链接:'+href)
        print('商品详细信息:')
        print(list3)
        print("______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
        sql = "INSERT INTO message (goodsid,title,href)VALUES ('%s', '%s','%s')"%(str(id),str(title1),str(href))
        cursor.execute(sql)
        db.commit()
        sql = "INSERT INTO goods(goodsid, goodsname, other1,other2,other3)VALUES ('%s', '%s','%s','%s','%s')"%(str(id),str(list3[0]),str(list3[1]),str(list3[2]),str(list3[3]))
        cursor.execute(sql)
        db.commit()
        sleep(2)
    try:
        button=driver.find_element_by_class_name('J_Ajax num icon-tag')
        button.click()
    except:sleep(3)


def dataSelect():
    print("模糊查询：请输入要查询的关键字！")
    a=input()
    db = pymysql.connect("localhost", "root", "521986", "pythondata",use_unicode=True, charset="utf8")
    sql="select * from message where  title like '%" + str(a)+"%"
    cursor.execute(sql)
    db.commit()
    print(cursor.fetchall())
    cursor.close()

    print("精确查询：请输入您想查询的关键字：")
    a=input()
    db = pymysql.connect("localhost", "root", "521986", "pythondata",use_unicode=True, charset="utf8")
    sql="select * from goods where  goodsname like  ='"+str(a)+"'"
    cursor.execute(sql)
    db.commit()
    print(cursor.fetchall())
    cursor.close()





