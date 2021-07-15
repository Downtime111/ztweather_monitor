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
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    url_h5 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    r_h5 = requests.get(url_h5, headers)
    res_url_h5 = json.loads(r_h5.text)
    data_all_h5 = json.loads(res_url_h5['data'])
    url_foreign = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'
    r_urlforeign = requests.get(url_foreign, headers)
    res_url_foreign = json.loads(r_urlforeign.text)
    data_all_foreign = json.loads(res_url_foreign['data'])
    foreignList = []
    lastUpdateTime = data_all_h5["lastUpdateTime"]
    data_foreignList = data_all_foreign["foreignList"]
    for for_infos in data_foreignList:
        name = for_infos["name"]
        continent = for_infos["continent"]
        date = "2020." + for_infos["date"]
        tup = time.strptime(date, "%Y.%m.%d")
        date = time.strftime("%Y-%m-%d", tup)
        confirmAdd = for_infos["confirmAdd"]
        confirmAddCut = for_infos["confirmAddCut"]
        confirm = for_infos["confirm"]
        suspect = for_infos["suspect"]
        dead = for_infos["dead"]
        heal = for_infos["heal"]
        nowConfirm = for_infos["nowConfirm"]
        confirmCompare = for_infos["confirmCompare"]
        nowConfirmCompare = for_infos["nowConfirmCompare"]
        healCompare = for_infos["healCompare"]
        deadCompare = for_infos["deadCompare"]
        foreignList.append([lastUpdateTime,
                            name,
                            continent,
                            date,
                            confirmAdd,
                            confirmAddCut,
                            confirm,
                            suspect,
                            dead,
                            heal,
                            nowConfirm,
                            confirmCompare,
                            nowConfirmCompare,
                            healCompare,
                            deadCompare
                            ])

    globalStatis = {}
    lastUpdateTime = data_all_foreign["globalStatis"]["lastUpdateTime"]
    nowConfirm = data_all_foreign["globalStatis"]["nowConfirm"]
    confirm = data_all_foreign["globalStatis"]["confirm"]
    heal = data_all_foreign["globalStatis"]["heal"]
    dead = data_all_foreign["globalStatis"]["dead"]
    nowConfirmAdd = data_all_foreign["globalStatis"]["nowConfirmAdd"]
    confirmAdd = data_all_foreign["globalStatis"]["confirmAdd"]
    healAdd = data_all_foreign["globalStatis"]["healAdd"]
    deadAdd = data_all_foreign["globalStatis"]["deadAdd"]
    globalStatis[lastUpdateTime] = {"nowConfirm": nowConfirm,
                                    "confirm": confirm,
                                    "heal": heal,
                                    "dead": dead,
                                    "nowConfirmAdd": nowConfirmAdd,
                                    "confirmAdd": confirmAdd,
                                    "healAdd": healAdd,
                                    "deadAdd": deadAdd
                                    }

    globalDailyHistory = {}
    for i in data_all_foreign["globalDailyHistory"]:
        date = "2020." + i["date"]
        tup = time.strptime(date, "%Y.%m.%d")
        date = time.strftime("%Y-%m-%d", tup)
        confirm = i["all"]["confirm"]
        dead = i["all"]["dead"]
        heal = i["all"]["heal"]
        newAddConfirm = i["all"]["newAddConfirm"]
        deadRate = i["all"]["deadRate"]
        healRate = i["all"]["healRate"]
        globalDailyHistory[date] = {"confirm": confirm,
                                    "dead": dead,
                                    "heal": heal,
                                    "newAddConfirm": newAddConfirm,
                                    "deadRate": deadRate,
                                    "healRate": healRate
                                    }

    importStatis = []
    lastUpdateTime = data_all_h5["lastUpdateTime"]
    data_importStatisTopList = data_all_foreign["importStatis"]["TopList"]
    for import_infos in data_importStatisTopList:
        province = import_infos["province"]
        importedCase = import_infos["importedCase"]
        importStatis.append([lastUpdateTime,
                             province,
                             importedCase
                             ])

    countryAddConfirmRankList = []
    lastUpdateTime = data_all_h5["lastUpdateTime"]
    data_countryAddConfirmRankList = data_all_foreign["countryAddConfirmRankList"]
    for country_infos in data_countryAddConfirmRankList:
        nation = country_infos["nation"]
        addConfirm = country_infos["addConfirm"]
        countryAddConfirmRankList.append([lastUpdateTime,
                                          nation,
                                          addConfirm
                                          ])

    countryConfirmWeekCompareRankList = []
    lastUpdateTime = data_all_h5["lastUpdateTime"]
    data_countryConfirmWeekCompareRankList = data_all_foreign["countryConfirmWeekCompareRankList"]
    for country_infos in data_countryConfirmWeekCompareRankList:
        nation = country_infos["nation"]
        day = country_infos["day"]
        day7 = country_infos["day7"]
        rate = country_infos["rate"]
        countryConfirmWeekCompareRankList.append([lastUpdateTime,
                                                  nation,
                                                  day,
                                                  day7,
                                                  rate
                                                  ])

    return foreignList, \
           globalStatis, \
           globalDailyHistory, \
           importStatis, \
           countryAddConfirmRankList, \
           countryConfirmWeekCompareRankList


def updateForeignList():
    cursor = None
    conn = None
    try:
        listData = tencent()[0]
        conn, cursor = connectSQL()
        sql = "insert into foreignList(" \
              "lastUpdateTime," \
              "name," \
              "continent," \
              "date," \
              "confirmAdd," \
              "confirmAddCut," \
              "confirm," \
              "suspect," \
              "dead," \
              "heal," \
              "nowConfirm," \
              "confirmCompare," \
              "nowConfirmCompare," \
              "healCompare," \
              "deadCompare)" \
              "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select lastUpdateTime from foreignList order by id desc limit 1)'
        cursor.execute(sql_query, listData[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新不含中国的海外161左右国家最后一次更新的详细数据")
            for item in listData:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新不含中国的海外161左右国家最后一次更新的详细数据完毕")
        else:
            print(f"{time.asctime()}已是不含中国的海外161左右国家最后一次更新的详细数据最新数据！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def insertGlobalStatis():
    cursor = None
    conn = None
    try:
        dictData = tencent()[1]
        print(f"{time.asctime()}开始插入全球累计总数据")
        conn, cursor = connectSQL()
        sql = "insert into globalStatis values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for key, value in dictData.items():
            cursor.execute(sql, [key,
                                 value.get("nowConfirm"),
                                 value.get("confirm"),
                                 value.get("heal"),
                                 value.get("dead"),
                                 value.get("nowConfirmAdd"),
                                 value.get("confirmAdd"),
                                 value.get("healAdd"),
                                 value.get("deadAdd")
                                 ])
        conn.commit()
        print(f"{time.asctime()}插入全球累计总数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateGlobalStatis():
    cursor = None
    conn = None
    try:
        dictData = tencent()[1]
        conn, cursor = connectSQL()
        sql = "insert into globalStatis values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select nowConfirm from globalStatis where lastUpdateTime=%s"
        for key, value in dictData.items():
            if not cursor.execute(sql_query, key):
                cursor.execute(sql, [key,
                                     value.get("nowConfirm"),
                                     value.get("confirm"),
                                     value.get("heal"),
                                     value.get("dead"),
                                     value.get("nowConfirmAdd"),
                                     value.get("confirmAdd"),
                                     value.get("healAdd"),
                                     value.get("deadAdd")
                                     ])
        conn.commit()
        print(f"{time.asctime()}全球累计总数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def insertGlobalDailyHistory():
    cursor = None
    conn = None
    try:
        dic = tencent()[2]
        print(f"{time.asctime()}开始插入按时间分条的全球累计数据")
        conn, cursor = connectSQL()
        sql = "insert into globalDailyHistory values(%s,%s,%s,%s,%s,%s,%s)"
        for key, value in dic.items():
            cursor.execute(sql, [key,
                                 value.get("confirm"),
                                 value.get("dead"),
                                 value.get("heal"),
                                 value.get("newAddConfirm"),
                                 value.get("deadRate"),
                                 value.get("healRate")
                                 ])
        conn.commit()
        print(f"{time.asctime()}插入按时间分条的全球累计数据完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateGlobalDailyHistory():
    cursor = None
    conn = None
    try:
        dic = tencent()[2]
        print(f"{time.asctime()}开始更新按时间分条的全球累计数据")
        conn, cursor = connectSQL()
        sql = "insert into globalDailyHistory values(%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from globalDailyHistory where date=%s"
        for key, value in dic.items():
            if not cursor.execute(sql_query, key):
                cursor.execute(sql, [key,
                                     value.get("confirm"),
                                     value.get("dead"),
                                     value.get("heal"),
                                     value.get("newAddConfirm"),
                                     value.get("deadRate"),
                                     value.get("healRate")
                                     ])
        conn.commit()
        print(f"{time.asctime()}按时间分条的全球累计数据更新完毕")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateImportStatis():
    cursor = None
    conn = None
    try:
        listData = tencent()[3]
        conn, cursor = connectSQL()
        sql = "insert into importStatis(" \
              "lastUpdateTime," \
              "province," \
              "importedCase)" \
              "values(%s,%s,%s)"
        sql_query = 'select %s=(select lastUpdateTime from importStatis order by id desc limit 1)'
        cursor.execute(sql_query, listData[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始更新前10个输入病例省份，按照输入病例数量排序数据")
            for item in listData:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新前10个输入病例省份，按照输入病例数量排序数据完毕")
        else:
            print(f"{time.asctime()}已是前10个输入病例省份，按照输入病例数量排序最新数据！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateCountryAddConfirmRankList():
    cursor = None
    conn = None
    try:
        listData = tencent()[4]
        conn, cursor = connectSQL()
        sql = "insert into countryAddConfirmRankList(" \
              "lastUpdateTime," \
              "nation," \
              "addConfirm)" \
              "values(%s,%s,%s)"

        sql_query = 'select %s=(select lastUpdateTime from countryAddConfirmRankList order by id desc limit 1)'
        cursor.execute(sql_query, listData[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始插入24小时内新增确诊病例top10国家数据")
            for item in listData:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新24小时内新增确诊病例top10国家数据完毕")
        else:
            print(f"{time.asctime()}已是24小时内新增确诊病例top10国家最新数据！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


def updateCountryConfirmWeekCompareRankList():
    cursor = None
    conn = None
    try:
        listData = tencent()[5]
        conn, cursor = connectSQL()
        sql = "insert into countryConfirmWeekCompareRankList(" \
              "lastUpdateTime," \
              "nation," \
              "day," \
              "day7," \
              "rate)" \
              "values(%s,%s,%s,%s,%s)"
        sql_query = 'select %s=(select lastUpdateTime from countryConfirmWeekCompareRankList order by id desc limit 1)'
        cursor.execute(sql_query, listData[0][0])
        if not cursor.fetchone()[0]:
            print(f"{time.asctime()}开始插入累计确诊一周增长幅度最快top10国家")
            for item in listData:
                cursor.execute(sql, item)
            conn.commit()
            print(f"{time.asctime()}更新累计确诊一周增长幅度最快top10国家数据完毕")
        else:
            print(f"{time.asctime()}已是累计确诊一周增长幅度最快top10国家最新数据！")
    except:
        traceback.print_exc()
    finally:
        close_conn(conn, cursor)


if __name__ == "__main__":
    updateForeignList()
    updateGlobalStatis()
    updateGlobalDailyHistory()
    updateImportStatis()
    updateCountryAddConfirmRankList()
    updateCountryConfirmWeekCompareRankList()
    l = len(sys.argv)
    if l == 1:
        zqh = """
        请输入参数(函数名称+函数注释+推荐爬取频率：分、时、日、月、周)
        参数说明：  
            updateForeignList 更新不含中国的海外161左右国家最后一次更新的详细数据(*/10 * * * *)
            updateGlobalStatis 更新全球累计总数据(*/5 * * * *)
            updateGlobalDailyHistory 更新按时间分条的全球累计数据(45 */3 * * *)
            updateImportStatis 更新前10个输入病例省份数据(50 */2 * * *)
            updateCountryAddConfirmRankList 更新24小时内新增确诊病例top10国家数据(*/10 * * * *)
            updateCountryConfirmWeekCompareRankList 更新累计确诊一周增长幅度最快top10国家数据(55 */3 * * *)
        """
        print(zqh)
    else:
        order = sys.argv[1]
        if order == "updateForeignList":
            updateForeignList()
        elif order == "updateGlobalStatis":
            updateGlobalStatis()
        elif order == "updateGlobalDailyHistory":
            updateGlobalDailyHistory()
        elif order == "updateImportStatis":
            updateImportStatis()
        elif order == "updateCountryAddConfirmRankList":
            updateCountryAddConfirmRankList()
        elif order == "updateCountryConfirmWeekCompareRankList":
            updateCountryConfirmWeekCompareRankList()
