import pymysql


def connectSQL():
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="123456",
                           db="cov",
                           charset="utf8")
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def query(sql, *args):
    conn, cursor = connectSQL()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res


def time():
    sql = "select lastUpdateTime from chinaTotalAndChinaAdd order by lastUpdateTime desc limit 1 "
    res = query(sql)
    return res[0]


def chinaEightNumber():
    sql = "select `confirmTotal`, " \
          "`healTotal`, " \
          "`deadTotal`, " \
          "`nowConfirmTotal`, " \
          "`suspectTotal`, " \
          "`nowSevereTotal`, " \
          "`importedCaseTotal`, " \
          "`noInfectTotal`, " \
          "`confirmAdd`, " \
          "`healAdd`, " \
          "`deadAdd`, " \
          "`nowConfirmAdd`, " \
          "`suspectAdd`, " \
          "`nowSevereAdd`, " \
          "`importedCaseAdd`, " \
          "`noInfectAdd` " \
          "from chinaTotalAndChinaAdd " \
          "order by lastUpdateTime desc " \
          "limit 1 "
    res = query(sql)
    return res[0]


def chinaMap():
    sql = "select provinceName,confirmToday,nowConfirmTotal,confirmTotal,healTotal,deadTotal " \
          "from provinceDetails " \
          "where lastUpdateTime = (select lastUpdateTime from provinceDetails order by lastUpdateTime desc limit 1)"
    res = query(sql)
    return res


def chinaProvinceMap():
    sql = "select cityName,confirmToday,nowConfirmTotal,confirmTotal,healTotal,deadTotal from cityDetails " \
          "where lastUpdateTime=(select lastUpdateTime from cityDetails order by lastUpdateTime desc limit 1)  "
    res = query(sql)
    return res


def nationalTotal():
    sql = "select " \
          "date," \
          "confirmChinaDayList," \
          "healChinaDayList," \
          "deadChinaDayList, " \
          "importedCaseChinaDayList" \
          " from chinaDayListAndChinaDayAddList "
    res = query(sql)
    return res


def dailyAdditionsNationwide():
    sql = "select " \
          "date," \
          "confirmChinaDayAddList," \
          "healChinaDayAddList," \
          "deadChinaDayAddList, " \
          "importedCaseChinaDayAddList" \
          " from chinaDayListAndChinaDayAddList "
    res = query(sql)
    return res


def dailyCasesNationwide():
    sql = "select " \
          "date," \
          "suspectChinaDayList," \
          "noInfectChinaDayList," \
          "nowConfirmChinaDayList," \
          "nowSevereChinaDayList " \
          "from chinaDayListAndChinaDayAddList "
    res = query(sql)
    return res


def nationalCumulativeCureMortalityRate():
    sql = "select date,healRateChinaDayList,deadRateChinaDayList " \
          "from chinaDayListAndChinaDayAddList "
    res = query(sql)
    return res


def detailedDataByProvince():
    sql = "select provinceName,confirmTotal,healTotal,deadTotal,healRateTotal,deadRateTotal " \
          "from provinceDetails " \
          "where lastUpdateTime=(select lastUpdateTime from provinceDetails order by lastUpdateTime desc limit 1)  	" \
          "order by confirmTotal desc"
    res = query(sql)
    return res


def cumulativeNumberOfConfirmedCasesInAllProvinces():
    sql = "select provinceName,confirmTotal " \
          "from provinceDetails " \
          "where lastUpdateTime=(select lastUpdateTime from provinceDetails order by lastUpdateTime desc limit 1) " \
          "order by confirmTotal desc"
    res = query(sql)
    return res


def currentConfirmedDataInAllProvinces():
    sql = "select provinceName,nowConfirmTotal,confirmToday,suspectTotal " \
          "from provinceDetails " \
          "where lastUpdateTime=(select lastUpdateTime from provinceDetails order by lastUpdateTime desc limit 1)  	" \
          "order by nowConfirmTotal desc"
    res = query(sql)
    return res


def existingDiagnosticClassificationInChina():
    sql = "select gat,import,province  " \
          "from nowConfirmStatis " \
          "where lastUpdateTime=(select lastUpdateTime from nowConfirmStatis order by lastUpdateTime desc limit 1)"
    res = query(sql)
    return res


def totalNumberOfOverseasImportsFromTop10Provinces():
    sql = "select province,importedCase " \
          "from importStatis " \
          "where lastUpdateTime=(select lastUpdateTime from importStatis order by lastUpdateTime desc limit 1) "
    res = query(sql)
    return res


def eachProvinceComparesYesterdayData():
    sql = "select province,nowConfirm,confirmAdd,heal,dead,zero " \
          "from provinceCompare " \
          "where lastUpdateTime=(select lastUpdateTime from provinceCompare order by lastUpdateTime desc limit 1)  	" \
          "order by zero desc"
    res = query(sql)
    return res


def hubeiNonHubeiNationalCumulativeData():
    sql = "select date,hubeiNowConfirm,hubeiHeal,hubeiDead," \
          "notHubeiNowConfirm,notHubeiHeal,notHubeiDead," \
          "countryNowConfirm,countryHeal,countryDead " \
          "from dailyHistory"
    res = query(sql)
    return res


def hubeiNonHubeiNationalCureMortalityRate():
    sql = "select date,hubeiHealRate,hubeiDeadRate," \
          "notHubeiHealRate,notHubeiDeadRate," \
          "countryHealRate,countryDeadRate " \
          "from dailyHistory"
    res = query(sql)
    return res


def hubeiNonHubeiNationalDailyNew():
    sql = "select date,hubei,notHubei,country from dailyNewAddHistory"
    res = query(sql)
    return res


def wuhanNotWuhanNotHubeiNewlyConfirmed():
    sql = "select date,wuhan,notWuhan,notHubei from wuhanDayList"
    res = query(sql)
    return res


def totalConfirmedTop20UrbanAreas():
    sql = "select cityName,deadRateTotal,healRateTotal " \
          "from cityDetails " \
          "where lastUpdateTime=(select lastUpdateTime from cityDetails order by lastUpdateTime desc limit 1)  	" \
          "and cityName  !='地区待确认' " \
          "and cityName  !='境外输入' " \
          "and confirmTotal > 0 " \
          "order by confirmTotal desc " \
          "limit 20"
    res = query(sql)
    return res


def existingConfirmedTop20UrbanAreas():
    sql = "select cityName,nowConfirmTotal,confirmToday,suspectTotal " \
          "from cityDetails  " \
          "where lastUpdateTime=(select lastUpdateTime from cityDetails order by lastUpdateTime desc limit 1)  	" \
          "and cityName !='地区待确认'  " \
          "and cityName !='境外输入'  " \
          "order by nowConfirmTotal desc " \
          "limit 20"
    res = query(sql)
    return res


def urbanDataOfHubeiProvince():
    sql = "select cityName,confirmTotal,healTotal,deadTotal " \
          "from cityDetails " \
          "where lastUpdateTime=(select lastUpdateTime from cityDetails order by lastUpdateTime desc limit 1) " \
          "and cityName  !='地区待确认' " \
          "and cityName  !='境外输入' " \
          "and provinceName  ='湖北' " \
          "order by confirmTotal desc"
    res = query(sql)
    return res


def accumulativeDataExceptHubeiProvince():
    sql = "select cityName,confirmTotal,healTotal,deadTotal " \
          "from cityDetails " \
          "where lastUpdateTime=(select lastUpdateTime from cityDetails order by lastUpdateTime desc limit 1) " \
          "and cityName  !='地区待确认' " \
          "and cityName  !='境外输入' " \
          "and provinceName  !='湖北' " \
          "and confirmTotal  > 100 " \
          "order by confirmTotal desc "
    res = query(sql)
    return res


def provincesWithFatalCasesNationwide():
    sql = "select * " \
          "from (select count(*) as noDeadProvinceCount " \
          "from provinceDetails " \
          "where lastUpdateTime=(select lastUpdateTime from provinceDetails " \
          "order by lastUpdateTime desc limit 1)  	" \
          "and deadTotal = 0 " \
          "order by deadTotal desc) a ," \
          "(select count(*) as deadProvinceCount " \
          "from provinceDetails " \
          "where lastUpdateTime=(select lastUpdateTime from provinceDetails " \
          "order by lastUpdateTime desc limit 1)  	" \
          "and deadTotal > 0 " \
          "order by deadTotal desc) b "
    res = query(sql)
    return res


def numberOfDeathsInCities():
    sql = "select * " \
          "from (select count(*) as noDeadCityCount " \
          "from cityDetails " \
          "where lastUpdateTime=(select lastUpdateTime from cityDetails order by lastUpdateTime desc limit 1)  	" \
          "and cityName  !='地区待确认' and cityName  !='境外输入' and deadTotal = 0 order by deadTotal desc) a ," \
          "(select count(*) as deadCityCount " \
          "from cityDetails " \
          "where lastUpdateTime=(select lastUpdateTime from cityDetails order by lastUpdateTime desc limit 1)  	" \
          "and cityName  !='地区待确认' and cityName  !='境外输入' and deadTotal > 0 order by deadTotal desc) b "
    res = query(sql)
    return res


def outbreakOut():
    sql = 'select content from hotsearch order by id desc limit 20'
    res = query(sql)
    return res
