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

    chinaTotalAndChinaAdd = {}
    lastUpdateTime = data_all_h5["lastUpdateTime"]
    confirmTotal = data_all_h5["chinaTotal"]["confirm"]
    healTotal = data_all_h5["chinaTotal"]["heal"]
    deadTotal = data_all_h5["chinaTotal"]["dead"]
    nowConfirmTotal = data_all_h5["chinaTotal"]["nowConfirm"]
    suspectTotal = data_all_h5["chinaTotal"]["suspect"]
    nowSevereTotal = data_all_h5["chinaTotal"]["nowSevere"]
    importedCaseTotal = data_all_h5["chinaTotal"]["importedCase"]
    noInfectTotal = data_all_h5["chinaTotal"]["noInfect"]
    confirmAdd = data_all_h5["chinaAdd"]["confirm"]
    healAdd = data_all_h5["chinaAdd"]["heal"]
    deadAdd = data_all_h5["chinaAdd"]["dead"]
    nowConfirmAdd = data_all_h5["chinaAdd"]["nowConfirm"]
    suspectAdd = data_all_h5["chinaAdd"]["suspect"]
    nowSevereAdd = data_all_h5["chinaAdd"]["nowSevere"]
    importedCaseAdd = data_all_h5["chinaAdd"]["importedCase"]
    noInfectAdd = data_all_h5["chinaAdd"]["noInfect"]
    chinaTotalAndChinaAdd[lastUpdateTime] = {"confirmTotal": confirmTotal,
                                             "healTotal": healTotal,
                                             "deadTotal": deadTotal,
                                             "nowConfirmTotal": nowConfirmTotal,
                                             "suspectTotal": suspectTotal,
                                             "nowSevereTotal": nowSevereTotal,
                                             "importedCaseTotal": importedCaseTotal,
                                             "noInfectTotal": noInfectTotal,
                                             "confirmAdd": confirmAdd,
                                             "healAdd": healAdd,
                                             "deadAdd": deadAdd,
                                             "nowConfirmAdd": nowConfirmAdd,
                                             "suspectAdd": suspectAdd,
                                             "nowSevereAdd": nowSevereAdd,
                                             "importedCaseAdd": importedCaseAdd,
                                             "noInfectAdd": noInfectAdd
                                             }

    provinceDetails = []
    lastUpdateTime = data_all_h5["lastUpdateTime"]
    data_country = data_all_h5["areaTree"]
    data_province = data_country[0]["children"]
    for pro_infos in data_province:
        provinceName = pro_infos["name"]
        confirmToday = pro_infos["today"]["confirm"]
        confirmCutsToday = pro_infos["today"]["confirmCuts"]
        nowConfirmTotal = pro_infos["total"]["nowConfirm"]
        confirmTotal = pro_infos["total"]["confirm"]
        suspectTotal = pro_infos["total"]["suspect"]
        deadTotal = pro_infos["total"]["dead"]
        deadRateTotal = pro_infos["total"]["deadRate"]
        healTotal = pro_infos["total"]["heal"]
        healRateTotal = pro_infos["total"]["healRate"]
        provinceDetails.append([lastUpdateTime,
                                provinceName,
                                confirmToday,
                                confirmCutsToday,
                                nowConfirmTotal,
                                confirmTotal,
                                suspectTotal,
                                deadTotal,
                                deadRateTotal,
                                healTotal,
                                healRateTotal
                                ])

    cityDetails = []
    lastUpdateTime = data_all_h5["lastUpdateTime"]
    data_country = data_all_h5["areaTree"]
    data_province = data_country[0]["children"]
    for pro_infos in data_province:
        provinceName = pro_infos["name"]
        for city_infos in pro_infos["children"]:
            cityName = city_infos["name"]
            confirmToday = city_infos["today"]["confirm"]
            confirmCutsToday = city_infos["today"]["confirmCuts"]
            nowConfirmTotal = city_infos["total"]["nowConfirm"]
            confirmTotal = city_infos["total"]["confirm"]
            suspectTotal = city_infos["total"]["suspect"]
            deadTotal = city_infos["total"]["dead"]
            deadRateTotal = city_infos["total"]["deadRate"]
            healTotal = city_infos["total"]["heal"]
            healRateTotal = city_infos["total"]["healRate"]
            cityDetails.append([lastUpdateTime,
                                provinceName,
                                cityName,
                                confirmToday,
                                confirmCutsToday,
                                nowConfirmTotal,
                                confirmTotal,
                                suspectTotal,
                                deadTotal,
                                deadRateTotal,
                                healTotal,
                                healRateTotal
                                ])

    return chinaTotalAndChinaAdd, \
           provinceDetails, \
           cityDetails


def insertChinaTotalAndChinaAdd():
    cursor = None
    conn = None
    try:
        dictData = tencent()[0]
        print(f"{time.asctime()}开始插入国内累计数据和较昨日数据")
        conn, cursor = connectSQL()
        sql = "insert into chinaTotalAndChinaAdd values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for key, value in dictData.items():
            cursor.execute(sql, [key,
                                 value.get("confirmTotal"),
                                 value.get("healTotal"),
                                 value.get("deadTotal"),
                                 value.get("nowConfirmTotal"),
                                 value.get("suspectTotal"),
                                 value.get("nowSevereTotal"),
                                 value.get("importedCaseTotal"),
                                 value.get("noInfectTotal"),
                                 value.get("confirmAdd"),
                                 value.get("healAdd"),
                                 value.get("deadAdd"),
                                 value.get("nowConfirmAdd"),
                                 value.get("suspectAdd"),
                                 value.get("nowSevereAdd"),
                                 value.get("importedCaseAdd"),
                                 value.get("noInfectAdd")
                                 ])
        conn.commit()
        print(f"{time.asctime()}插入国内累计数据和较昨日数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateChinaTotalAndChinaAdd():
    cursor = None
    conn = None
    try:
        dictData = tencent()[0]
        conn, cursor = connectSQL()
        sql = "insert into chinaTotalAndChinaAdd values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirmTotal from chinaTotalAndChinaAdd where lastUpdateTime=%s"
        for key, value in dictData.items():
            if not cursor.execute(sql_query, key):
                cursor.execute(sql, [key,
                                     value.get("confirmTotal"),
                                     value.get("healTotal"),
                                     value.get("deadTotal"),
                                     value.get("nowConfirmTotal"),
                                     value.get("suspectTotal"),
                                     value.get("nowSevereTotal"),
                                     value.get("importedCaseTotal"),
                                     value.get("noInfectTotal"),
                                     value.get("confirmAdd"),
                                     value.get("healAdd"),
                                     value.get("deadAdd"),
                                     value.get("nowConfirmAdd"),
                                     value.get("suspectAdd"),
                                     value.get("nowSevereAdd"),
                                     value.get("importedCaseAdd"),
                                     value.get("noInfectAdd")
                                     ])
        conn.commit()
        print(f"{time.asctime()}国内累计数据和较昨日数据的历史数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateProvinceDetails():
    cursor = None
    conn = None
    try:
        listData = tencent()[1]
        conn, cursor = connectSQL()
        sql = "insert into provinceDetails(" \
              "lastUpdateTime," \
              "provinceName," \
              "confirmToday," \
              "confirmCutsToday," \
              "nowConfirmTotal," \
              "confirmTotal," \
              "suspectTotal," \
              "deadTotal," \
              "deadRateTotal," \
              "healTotal," \
              "healRateTotal) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select lastUpdateTime from provinceDetails order by id desc limit 1)'
        cursor.execute(sql_query, listData[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新省级最新数据")
            for item in listData:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新省级最新数据完毕")
        else:
            print(f"{time.asctime()}已是省级最新数据！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateCityDetails():
    cursor = None
    conn = None
    try:
        listData = tencent()[2]
        conn, cursor = connectSQL()
        sql = "insert into cityDetails(" \
              "lastUpdateTime," \
              "provinceName," \
              "cityName," \
              "confirmToday," \
              "confirmCutsToday," \
              "nowConfirmTotal," \
              "confirmTotal," \
              "suspectTotal," \
              "deadTotal," \
              "deadRateTotal," \
              "healTotal," \
              "healRateTotal) " \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select lastUpdateTime from cityDetails order by id desc limit 1)'
        cursor.execute(sql_query, listData[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新市级最新数据")
            for item in listData:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新市级最新数据完毕")
        else:
            print(f"{time.asctime()}已是市级最新数据！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == "__main__":
    updateChinaTotalAndChinaAdd()
    updateProvinceDetails()
    updateCityDetails()
    l = len(sys.argv)
    if l == 1:
        zqh = """
        请输入参数(函数名称+函数注释+推荐爬取频率：分、时、日、月、周)
        参数说明：  
            updateChinaTotalAndChinaAdd  更新国内累计数据和较昨日数据(*/5 * * * *)
            updateProvinceDetails 更新省级历史数据(5 */2 * * *)
            updateCityDetails 更新市级历史数据(10 */3 * * *)
        """
        print(zqh)
    else:
        order = sys.argv[1]
        if order == "updateChinaTotalAndChinaAdd":
            updateChinaTotalAndChinaAdd()
        elif order == "updateProvinceDetails":
            updateProvinceDetails()
        elif order == "updateCityDetails":
            updateCityDetails()
