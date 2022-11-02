#-*- codeing = utf-8 -*-
#@Time : 2020/3/3 17:51
#@Author : 李巍
#@File : spider.py
#@Software: PyCharm

from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL，获取网页数据
import xlwt     #进行excel操作
import sqlite3  #进行SQLite数据库操作



def main():
    baseurl = "http://sports.ladbrokes.com/competitions/football/english/premier-league"
    #1.爬取网页
    datalist = getData(baseurl)
    #savepath = "豆瓣电影Top250.xls"
    # dbpath = "movie.db"
    #3.保存数据
    #saveData(datalist,savepath)
    # saveData2DB(datalist,dbpath)

    #askURL("https://movie.douban.com/top250?start=")

#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')     #创建正则表达式对象，表示规则（字符串的模式）
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)   #re.S 让换行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#找到评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)



#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,1):       #调用获取页面信息的函数，10次
        url = baseurl + str(i*25)
        url = baseurl
        html = askURL(url)      #保存获取到的网页源码

         # 2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="container-inner-content"):     #查找符合要求的字符串，形成列表
            print(item)   #测试：查看电影item全部信息
            data = []    #保存一部电影的所有信息
            item = str(item)

            #影片详情的链接
            link = re.findall(findLink,item)[0]     #re库用来通过正则表达式查找指定的字符串
            data.append(link)                       #添加链接

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)                     #添加图片

            titles = re.findall(findTitle,item)     #片名可能只有一个中文名，没有外国名
            if(len(titles) == 2):
                ctitle = titles[0]                  #添加中文名
                data.append(ctitle)
                otitle = titles[1].replace("/","")  #去掉无关的符号
                data.append(otitle)                 #添加外国名
            else:
                data.append(titles[0])
                data.append(' ')        #外国名字留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)                        #添加评分

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)                       #提加评价人数

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")    #去掉句号
                data.append(inq)                # 添加概述
            else:
                data.append(" ")                #留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)   #去掉<br/>
            bd = re.sub('/'," ",bd)     #替换/
            data.append(bd.strip())     #去掉前后的空格

            datalist.append(data)       #把处理好的一部电影信息放入datalist

    return datalist



#得到指定一个URL的网页内容
def askURL(url):
    # 模拟浏览器头部信息，向豆瓣服务器发送消息
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "cookie" :"QuantumMetricSessionID=10ae88eb0af3cd5a35d85aa5721dad4d; QuantumMetricUserID=617d99a846b1de6d27cd38e29d3a3f23; ASP.NET_SessionId=htwt4yjmmamjqgf0hr3xeppz; trc.cid=7fc40d934f084eb18c5d92027c6a2652; usersettings=cid=en-GB&vc=1&sst=2022-10-29T08:44:03.7184295Z&psst=0001-01-01T00:00:00.0000000Z&lsid=htwt4yjmmamjqgf0hr3xeppz; isLanguageChanged=false; lang=en; __cf_bm=vm5UktHrt3O8hTGCbt4ewdNjLq0bxKGmpaGY7r8LG2k-1667033043-0-AXjjh/FB8nxvjTQL9oQ9MuYik2bZqH9SVP6SxOjUqCBqwB/l4kahqyiz+5k931i5+O6PKnHb0pni38vbHfM/Nl4=; DAPROPS=\"sjs.webGlRenderer:ANGLE (Intel, Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdeviceAspectRatio:16/9|sdevicePixelRatio:1|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:0|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|buserMedia:1|bjs.battery:0\"; lastKnownProduct=%7B%22url%22%3A%22https%3A%2F%2Fsports.ladbrokes.com%2Fen%22%2C%22name%22%3A%22sports%22%2C%22previous%22%3A%22unknown%22%2C%22platformProductId%22%3A%22SPORTSBOOK%22%7D; tq=%5B%5D; kndctr_6B47D0245A26653C0A495CDC_AdobeOrg_identity=CiY1MTU3NTQ5NTk4MjEzNDIwMDUyMzIzNjMyODQ0MDY3MjUzNDIwN1IOCNfGppfCMBgBKgNPUjKgAdfGppfCMPAB18aml8Iw; kndctr_6B47D0245A26653C0A495CDC_AdobeOrg_cluster=or2; AMCV_6B47D0245A26653C0A495CDC%40AdobeOrg=MCMID|51575495982134200523236328440672534207; RT=\"z=1&dm=ladbrokes.com&si=9e40fc4f-2c05-452e-9fcc-eb749ccfe5dd&ss=l9tofkiw&sl=1&tt=756&bcn=%2F%2F17de4c10.akstat.io%2F&ld=7jb\"; _gcl_au=1.1.801591483.1667033054; _ga=GA1.2.1873787225.1667033055; _gid=GA1.2.1027760065.1667033055; _dc_gtm_UA-25272412-41=1; _sp_ses.4692=*; _sp_id.4692=9611e35b-fe17-43ee-9f20-1c9f54fb66ab.1667033056.1.1667033056.1667033056.719bb2d4-d2c2-4143-a1ec-e66dcff8982f; _scid=cde0a6d3-6d47-4bea-aaff-e19c30898424; _uetsid=df6ed370576511ed84432ff681591652; _uetvid=df6f1500576511edabcbed3c3461d15a; medallia-random-id=19; hq=%5B%7B%22name%22%3A%22homescreen%22%2C%22shouldShow%22%3Afalse%7D%5D; _sctr=1|1666972800000; OptanonConsent=isIABGlobal=false&datestamp=Sat+Oct+29+2022+16%3A44%3A23+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=6.17.0&hosts=&landingPath=https%3A%2F%2Fsports.ladbrokes.com%2Fcompetitions%2Ffootball%2Fenglish%2Fpremier-league&groups=C0001%3A1%2CC0004%3A1%2CC0002%3A1%2CC0003%3A1",
        # ":authority":"sports.ladbrokes.com"
    }
                            #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url=url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print("html start ------------------------------------")
        print(html)
        print("html end ------------------------------------")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html




#保存数据
def saveData(datalist,savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250',cell_overwrite_ok=True)    #创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])      #数据

    book.save(savepath)       #保存


def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250 (
                info_link,pic_link,cname,ename,score,rated,instroduction,info) 
                values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()







def init_db(dbpath):
    sql = '''
        create table movie250 
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric ,
        rated numeric ,
        instroduction text,
        info text
        )
    
    '''  #创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()



if __name__ == "__main__":          #当程序执行时
#调用函数
    main()
    #init_db("movietest.db")
    print("爬取完毕！")