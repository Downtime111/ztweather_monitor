import requests
import pymysql
import time
import json
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


def tencent():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
    url_h5 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    r_h5 = requests.get(url_h5, headers)
    res_url_h5 = json.loads(r_h5.text)
    data_all_h5 = json.loads(res_url_h5['data'])
    url_other = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
    r_urlother = requests.get(url_other, headers)
    res_url_other = json.loads(r_urlother.text)
    data_all_other = json.loads(res_url_other['data'])

    chinaDayListAndchinaDayAddList = {}
    for i in data_all_other["chinaDayList"]:
        date = "2020." + i["date"]
        tup = time.strptime(date, "%Y.%m.%d")
        date = time.strftime("%Y-%m-%d", tup)
        confirmChinaDayList = i["confirm"]
        suspectChinaDayList = i["suspect"]
        deadChinaDayList = i["dead"]
        healChinaDayList = i["heal"]
        nowConfirmChinaDayList = i["nowConfirm"]
        nowSevereChinaDayList = i["nowSevere"]
        importedCaseChinaDayList = i["importedCase"]
        deadRateChinaDayList = i["deadRate"]
        healRateChinaDayList = i["healRate"]
        noInfectChinaDayList = i["noInfect"]
        chinaDayListAndchinaDayAddList[date] = {"confirmChinaDayList": confirmChinaDayList,
                                                "suspectChinaDayList": suspectChinaDayList,
                                                "deadChinaDayList": deadChinaDayList,
                                                "healChinaDayList": healChinaDayList,
                                                "nowConfirmChinaDayList": nowConfirmChinaDayList,
                                                "nowSevereChinaDayList": nowSevereChinaDayList,
                                                "importedCaseChinaDayList": importedCaseChinaDayList,
                                                "deadRateChinaDayList": deadRateChinaDayList,
                                                "healRateChinaDayList": healRateChinaDayList,
                                                "noInfectChinaDayList": noInfectChinaDayList
                                                }
    for i in data_all_other["chinaDayAddList"]:
        date = "2020." + i["date"]
        tup = time.strptime(date, "%Y.%m.%d")
        date = time.strftime("%Y-%m-%d", tup)
        confirmChinaDayAddList = i["confirm"]
        suspectChinaDayAddList = i["suspect"]
        deadChinaDayAddList = i["dead"]
        healChinaDayAddList = i["heal"]
        importedCaseChinaDayAddList = i["importedCase"]
        noInfectChinaDayAddList = i["infect"]
        deadRateChinaDayAddList = i["deadRate"]
        healRateChinaDayAddList = i["healRate"]
        chinaDayListAndchinaDayAddList[date].update({"confirmChinaDayAddList": confirmChinaDayAddList,
                                                     "suspectChinaDayAddList": suspectChinaDayAddList,
                                                     "deadChinaDayAddList": deadChinaDayAddList,
                                                     "healChinaDayAddList": healChinaDayAddList,
                                                     "importedCaseChinaDayAddList": importedCaseChinaDayAddList,
                                                     "noInfectChinaDayAddList": noInfectChinaDayAddList,
                                                     "deadRateChinaDayAddList": deadRateChinaDayAddList,
                                                     "healRateChinaDayAddList": healRateChinaDayAddList
                                                     })

    dailyNewAddHistory = {}
    for i in data_all_other["dailyNewAddHistory"]:
        date = "2020." + i["date"]
        tup = time.strptime(date, "%Y.%m.%d")
        date = time.strftime("%Y-%m-%d", tup)
        hubei = i["hubei"]
        country = i["country"]
        notHubei = i["notHubei"]
        dailyNewAddHistory[date] = {"hubei": hubei,
                                    "country": country,
                                    "notHubei": notHubei
                                    }

    dailyHistory = {}
    for i in data_all_other["dailyHistory"]:
        date = "2020." + i["date"]
        tup = time.strptime(date, "%Y.%m.%d")
        date = time.strftime("%Y-%m-%d", tup)
        hubeiDead = i["hubei"]["dead"]
        hubeiHeal = i["hubei"]["heal"]
        hubeiNowConfirm = i["hubei"]["nowConfirm"]
        hubeiDeadRate = i["hubei"]["deadRate"]
        hubeiHealRate = i["hubei"]["healRate"]
        notHubeiDead = i["notHubei"]["dead"]
        notHubeiHeal = i["notHubei"]["heal"]
        notHubeiNowConfirm = i["notHubei"]["nowConfirm"]
        notHubeiDeadRate = i["notHubei"]["deadRate"]
        notHubeiHealRate = i["notHubei"]["healRate"]
        countryDead = i["country"]["dead"]
        countryHeal = i["country"]["heal"]
        countryNowConfirm = i["country"]["nowConfirm"]
        countryDeadRate = i["country"]["deadRate"]
        countryHealRate = i["country"]["healRate"]
        dailyHistory[date] = {"hubeiDead": hubeiDead,
                              "hubeiHeal": hubeiHeal,
                              "hubeiNowConfirm": hubeiNowConfirm,
                              "hubeiDeadRate": hubeiDeadRate,
                              "hubeiHealRate": hubeiHealRate,
                              "notHubeiDead": notHubeiDead,
                              "notHubeiHeal": notHubeiHeal,
                              "notHubeiNowConfirm": notHubeiNowConfirm,
                              "notHubeiDeadRate": notHubeiDeadRate,
                              "notHubeiHealRate": notHubeiHealRate,
                              "countryDead": countryDead,
                              "countryHeal": countryHeal,
                              "countryNowConfirm": countryNowConfirm,
                              "countryDeadRate": countryDeadRate,
                              "countryHealRate": countryHealRate,
                              }

    wuhanDayList = {}
    for i in data_all_other["wuhanDayList"]:
        date = "2020." + i["date"]
        tup = time.strptime(date, "%Y.%m.%d")
        date = time.strftime("%Y-%m-%d", tup)
        wuhan = i["wuhan"]["confirmAdd"]
        notWuhan = i["notWuhan"]["confirmAdd"]
        notHubei = i["notHubei"]["confirmAdd"]
        wuhanDayList[date] = {"wuhan": wuhan,
                              "notWuhan": notWuhan,
                              "notHubei": notHubei
                              }

    provinceCompare = []
    lastUpdateTime = data_all_h5["lastUpdateTime"]
    data_provinceCompare = data_all_other["provinceCompare"]
    for pro_infos in data_provinceCompare:
        province = pro_infos
        nowConfirm = data_provinceCompare[pro_infos]["nowConfirm"]
        confirmAdd = data_provinceCompare[pro_infos]["confirmAdd"]
        dead = data_provinceCompare[pro_infos]["dead"]
        heal = data_provinceCompare[pro_infos]["heal"]
        zero = data_provinceCompare[pro_infos]["zero"]
        provinceCompare.append([lastUpdateTime,
                                province,
                                nowConfirm,
                                confirmAdd,
                                dead,
                                heal,
                                zero
                                ])

    nowConfirmStatis = {}
    lastUpdateTime = data_all_h5["lastUpdateTime"]
    gat = data_all_other["nowConfirmStatis"]["gat"]
    importCase = data_all_other["nowConfirmStatis"]["import"]
    province = data_all_other["nowConfirmStatis"]["province"]
    nowConfirmStatis[lastUpdateTime] = {"gat": gat,
                                        "import": importCase,
                                        "province": province
                                        }

    return chinaDayListAndchinaDayAddList, \
           dailyNewAddHistory, \
           dailyHistory, \
           wuhanDayList, \
           provinceCompare, \
           nowConfirmStatis


def insertChinaDayListAndChinaDayAddList():
    cursor = None
    conn = None
    try:
        dic = tencent()[0]
        print(f"{time.asctime()}开始插入按时间分条的全国累计数据和每日新增数据")
        conn, cursor = connectSQL()
        sql = "insert into chinaDayListAndChinaDayAddList values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for key, value in dic.items():
            cursor.execute(sql, [key,
                                 value.get("confirmChinaDayList"),
                                 value.get("suspectChinaDayList"),
                                 value.get("deadChinaDayList"),
                                 value.get("healChinaDayList"),
                                 value.get("nowConfirmChinaDayList"),
                                 value.get("nowSevereChinaDayList"),
                                 value.get("importedCaseChinaDayList"),
                                 value.get("deadRateChinaDayList"),
                                 value.get("healRateChinaDayList"),
                                 value.get("noInfectChinaDayList"),
                                 value.get("confirmChinaDayAddList"),
                                 value.get("suspectChinaDayAddList"),
                                 value.get("deadChinaDayAddList"),
                                 value.get("healChinaDayAddList"),
                                 value.get("importedCaseChinaDayAddList"),
                                 value.get("noInfectChinaDayAddList"),
                                 value.get("deadRateChinaDayAddList"),
                                 value.get("healRateChinaDayAddList")
                                 ])
        conn.commit()
        print(f"{time.asctime()}插入按时间分条的全国累计数据和每日新增数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateChinaDayListAndChinaDayAddList():
    cursor = None
    conn = None
    try:
        dic = tencent()[0]
        print(f"{time.asctime()}开始更新按时间分条的全国累计数据和每日新增数据")
        conn, cursor = connectSQL()
        sql = "insert into chinaDayListAndChinaDayAddList values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirmChinaDayList from chinaDayListAndChinaDayAddList where date=%s"
        for key, value in dic.items():
            if not cursor.execute(sql_query, key):
                cursor.execute(sql, [key,
                                     value.get("confirmChinaDayList"),
                                     value.get("suspectChinaDayList"),
                                     value.get("deadChinaDayList"),
                                     value.get("healChinaDayList"),
                                     value.get("nowConfirmChinaDayList"),
                                     value.get("nowSevereChinaDayList"),
                                     value.get("importedCaseChinaDayList"),
                                     value.get("deadRateChinaDayList"),
                                     value.get("healRateChinaDayList"),
                                     value.get("noInfectChinaDayList"),
                                     value.get("confirmChinaDayAddList"),
                                     value.get("suspectChinaDayAddList"),
                                     value.get("deadChinaDayAddList"),
                                     value.get("healChinaDayAddList"),
                                     value.get("importedCaseChinaDayAddList"),
                                     value.get("noInfectChinaDayAddList"),
                                     value.get("deadRateChinaDayAddList"),
                                     value.get("healRateChinaDayAddList")
                                     ])
        conn.commit()
        print(f"{time.asctime()}按时间分条的全国累计数据和每日新增数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def insertDailyNewAddHistory():
    cursor = None
    conn = None
    try:
        dic = tencent()[1]
        print(f"{time.asctime()}开始插入湖北、全国、非湖北每日新增确诊数据")
        conn, cursor = connectSQL()
        sql = "insert into dailyNewAddHistory values(%s,%s,%s,%s)"
        for key, value in dic.items():
            cursor.execute(sql, [key,
                                 value.get("hubei"),
                                 value.get("country"),
                                 value.get("notHubei")
                                 ])
        conn.commit()
        print(f"{time.asctime()}插入湖北、全国、非湖北每日新增确诊数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateDailyNewAddHistory():
    cursor = None
    conn = None
    try:
        dic = tencent()[1]
        print(f"{time.asctime()}开始更新湖北、全国、非湖北每日新增确诊数据")
        conn, cursor = connectSQL()
        sql = "insert into dailyNewAddHistory values(%s,%s,%s,%s)"
        sql_query = "select hubei from dailyNewAddHistory where date=%s"
        for key, value in dic.items():
            if not cursor.execute(sql_query, key):
                cursor.execute(sql, [key,
                                     value.get("hubei"),
                                     value.get("country"),
                                     value.get("notHubei")
                                     ])
        conn.commit()
        print(f"{time.asctime()}按时间分条的湖北、全国、非湖北每日新增确诊数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def insertDailyHistory():
    cursor = None
    conn = None
    try:
        dic = tencent()[2]
        print(f"{time.asctime()}开始插入湖北、全国、非湖北累计汇总详细数据")
        conn, cursor = connectSQL()
        sql = "insert into dailyHistory values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for key, value in dic.items():
            cursor.execute(sql, [key,
                                 value.get("hubeiDead"),
                                 value.get("hubeiHeal"),
                                 value.get("hubeiNowConfirm"),
                                 value.get("hubeiDeadRate"),
                                 value.get("hubeiHealRate"),
                                 value.get("notHubeiDead"),
                                 value.get("notHubeiHeal"),
                                 value.get("notHubeiNowConfirm"),
                                 value.get("notHubeiDeadRate"),
                                 value.get("notHubeiHealRate"),
                                 value.get("countryDead"),
                                 value.get("countryHeal"),
                                 value.get("countryNowConfirm"),
                                 value.get("countryDeadRate"),
                                 value.get("countryHealRate"),
                                 ])
        conn.commit()
        print(f"{time.asctime()}插入湖北、全国、非湖北累计汇总详细数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateDailyHistory():
    cursor = None
    conn = None
    try:
        dic = tencent()[2]
        print(f"{time.asctime()}开始更新湖北、全国、非湖北累计汇总详细数据")
        conn, cursor = connectSQL()
        sql = "insert into dailyHistory values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select hubeiDead from dailyHistory where date=%s"
        for key, value in dic.items():
            if not cursor.execute(sql_query, key):
                cursor.execute(sql, [key,
                                     value.get("hubeiDead"),
                                     value.get("hubeiHeal"),
                                     value.get("hubeiNowConfirm"),
                                     value.get("hubeiDeadRate"),
                                     value.get("hubeiHealRate"),
                                     value.get("notHubeiDead"),
                                     value.get("notHubeiHeal"),
                                     value.get("notHubeiNowConfirm"),
                                     value.get("notHubeiDeadRate"),
                                     value.get("notHubeiHealRate"),
                                     value.get("countryDead"),
                                     value.get("countryHeal"),
                                     value.get("countryNowConfirm"),
                                     value.get("countryDeadRate"),
                                     value.get("countryHealRate"),
                                     ])
        conn.commit()
        print(f"{time.asctime()}按时间分条的湖北、全国、非湖北累计汇总详细数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def insertWuhanDayList():
    cursor = None
    conn = None
    try:
        dic = tencent()[3]
        print(f"{time.asctime()}开始插入每日 武汉、湖北非武汉、非湖北新增确诊数据")
        conn, cursor = connectSQL()
        sql = "insert into wuhanDayList values(%s,%s,%s,%s)"
        for key, value in dic.items():
            cursor.execute(sql, [key,
                                 value.get("wuhan"),
                                 value.get("notWuhan"),
                                 value.get("notHubei")
                                 ])
        conn.commit()
        print(f"{time.asctime()}插入每日 武汉、湖北非武汉、非湖北新增确诊数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateWuhanDayList():
    cursor = None
    conn = None
    try:
        dic = tencent()[3]
        print(f"{time.asctime()}开始更新每日 武汉、湖北非武汉、非湖北新增确诊数据")
        conn, cursor = connectSQL()
        sql = "insert into wuhanDayList values(%s,%s,%s,%s)"
        sql_query = "select wuhan from wuhanDayList where date=%s"
        for key, value in dic.items():
            if not cursor.execute(sql_query, key):
                cursor.execute(sql, [key,
                                     value.get("wuhan"),
                                     value.get("notWuhan"),
                                     value.get("notHubei")
                                     ])
        conn.commit()
        print(f"{time.asctime()}每日 武汉、湖北非武汉、非湖北新增确诊数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateProvinceCompare():
    cursor = None
    conn = None
    try:
        listData = tencent()[4]
        conn, cursor = connectSQL()
        sql = "insert into provinceCompare(" \
              "lastUpdateTime," \
              "province," \
              "nowConfirm," \
              "confirmAdd," \
              "dead," \
              "heal," \
              "zero) " \
              "values(%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select lastUpdateTime from provinceCompare order by id desc limit 1)'
        cursor.execute(sql_query, listData[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新各省级自身比较数据")
            for item in listData:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新各省级自身比较数据完毕")
        else:
            print(f"{time.asctime()}已是各省级自身比较最新数据！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def insertNowConfirmStatis():
    cursor = None
    conn = None
    try:
        dic = tencent()[5]
        print(f"{time.asctime()}开始插入港澳台、境外输入、31省本土现有确诊数据")
        conn, cursor = connectSQL()
        sql = "insert into nowConfirmStatis values(%s,%s,%s,%s)"
        for key, value in dic.items():
            cursor.execute(sql, [key,
                                 value.get("gat"),
                                 value.get("import"),
                                 value.get("province")
                                 ])
        conn.commit()
        print(f"{time.asctime()}插入港澳台、境外输入、31省本土现有确诊数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateNowConfirmStatis():
    cursor = None
    conn = None
    try:
        dic = tencent()[5]
        print(f"{time.asctime()}开始更新港澳台、境外输入、31省本土现有确诊数据")
        conn, cursor = connectSQL()
        sql = "insert into nowConfirmStatis values(%s,%s,%s,%s)"
        sql_query = "select gat from nowConfirmStatis where lastUpdateTime=%s"
        for key, value in dic.items():

            if not cursor.execute(sql_query, key):
                cursor.execute(sql, [key,
                                     value.get("gat"),
                                     value.get("import"),
                                     value.get("province")
                                     ])
        conn.commit()
        print(f"{time.asctime()}港澳台、境外输入、31省本土现有确诊数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == "__main__":
    updateChinaDayListAndChinaDayAddList()
    updateDailyNewAddHistory()
    updateDailyHistory()
    updateWuhanDayList()
    updateProvinceCompare()
    updateNowConfirmStatis()
    l = len(sys.argv)
    if l == 1:
        zqh = """
        请输入参数(函数名称+函数注释+推荐爬取频率：分、时、日、月、周)
        参数说明：  
            updateChinaDayListAndChinaDayAddList 更新按时间的累计数据和每日数据(15 */3 * * *)
            updateDailyNewAddHistory 更新按时间分条的湖北、全国、非湖北每日新增确诊数据(20 */3 * * *)
            updateDailyHistory 更新按时间分条的湖北、全国、非湖北累计汇总详细数据(25 */3 * * *)
            updateWuhanDayList 更新每日 武汉、湖北非武汉、非湖北新增确诊数据(30 */2 * * *)
            updateProvinceCompare 更新各省级自身比较数据(35 */3 * * *)
            updateNowConfirmStatis 更新港澳台、境外输入、31省本土现有确诊数据(40 */3 * * *)
        """
        print(zqh)
    else:
        order = sys.argv[1]
        if order == "updateChinaDayListAndChinaDayAddList":
            updateChinaDayListAndChinaDayAddList()
        elif order == "updateDailyNewAddHistory":
            updateDailyNewAddHistory()
        elif order == "updateDailyHistory":
            updateDailyHistory()
        elif order == "updateWuhanDayList":
            updateWuhanDayList()
        elif order == "updateProvinceCompare":
            updateProvinceCompare()
        elif order == "updateNowConfirmStatis":
            updateNowConfirmStatis()
