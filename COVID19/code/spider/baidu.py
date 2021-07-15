from selenium.webdriver import Chrome, ChromeOptions
import pymysql
import time
import traceback
import sys


def connectSQL():
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="123456",
                           db="cov",
                           charset="utf8")
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()


def baidu_hot():
    option = ChromeOptions()
    option.add_argument("--headless")
    option.add_argument('--no-sandbox')
    url = "https://voice.baidu.com/act/virussearch/virussearch?from=osari_map&tab=0&infomore=1"
    browser = Chrome(options=option, executable_path="./chromedriver83.exe")
    browser.get(url)
    dl = browser.find_element_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/div')
    dl.click()
    time.sleep(1)
    c = browser.find_elements_by_xpath('//*[@id="ptab-0"]/div/div[1]/section/a/div/span[2]')
    context = [i.text for i in c]
    return context


def updateHotSearch():
    cursor = None
    conn = None
    try:
        context = baidu_hot()
        print(f"{time.asctime()}开始更新热搜数据")
        conn, cursor = connectSQL()
        sql = "insert into hotsearch(dt,content) values(%s,%s)"
        ts = time.strftime("%Y-%m-%d %X")
        for i in context:
            cursor.execute(sql, (ts, i))
        conn.commit()
        print(f"{time.asctime()}数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == "__main__":
    updateHotSearch()
    l = len(sys.argv)
    if l == 1:
        zqh = """
        请输入参数(函数名称+函数注释+推荐爬取频率：分、时、日、月、周)
        参数说明：
            updateHotSearch 更新疫情热搜数据(*/5 * * * *)
        """
        print(zqh)
    else:
        order = sys.argv[1]
        if order == "updateHotSearch":
            updateHotSearch()
