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


def worldFourNumber():
    sql = "    select `nowConfirm`, `confirm`, `heal`, `dead`, `nowConfirmAdd`, `confirmAdd`, `healAdd`, `deadAdd` " \
          "from globalStatis order by lastUpdateTime desc limit 1 "
    res = query(sql)
    return res[0]


def worldMapNoChina():
    sql = "select name,nowConfirm,confirm,heal,dead " \
          "from foreignList " \
          "where lastUpdateTime = (select lastUpdateTime from foreignList order by lastUpdateTime desc limit 1)"
    res = query(sql)
    return res


def worldMapChina():
    sql = "select nowConfirmTotal,confirmTotal,healTotal,deadTotal " \
          "from chinaTotalAndChinaAdd " \
          "where lastUpdateTime = (select lastUpdateTime from chinaTotalAndChinaAdd order by lastUpdateTime desc limit 1)"
    res = query(sql)
    return res


def globalCumulativeTrend():
    sql = "select date,confirm,heal,dead,newAddConfirm from globalDailyHistory"
    res = query(sql)
    return res


def globalCumulativeCureMortality():
    sql = "select date,healRate,deadRate  from globalDailyHistory"
    res = query(sql)
    return res


def foreignCumulativeDiagnosisTop10Countries():
    sql = "select name,nowConfirm,confirm,heal,dead " \
          "from foreignList " \
          "where lastUpdateTime=(select lastUpdateTime from foreignList order by lastUpdateTime desc limit 1)  	" \
          "order by confirm desc " \
          "limit 10"
    h = query(sql)
    return h


def theTop10CountriesGrewFastestInSevenDays():
    sql = "select nation,day7,day,rate " \
          "from countryConfirmWeekCompareRankList " \
          "where lastUpdateTime=(select lastUpdateTime from countryConfirmWeekCompareRankList order by lastUpdateTime desc limit 1)  	" \
          "order by rate desc"
    res = query(sql)
    return res


def overseasCountriesWithMoreThan10000ConfirmedCases():
    sql = "select name,confirm " \
          "from foreignList " \
          "where lastUpdateTime=(select lastUpdateTime from foreignList order by lastUpdateTime desc limit 1) " \
          "and confirm > 10000 " \
          "order by confirm desc"
    res = query(sql)
    return res


def overseasCountriesWithMoreThan10000HaveBeenConfirmedCases():
    sql = "select name,nowConfirm " \
          "from foreignList " \
          "where lastUpdateTime=(select lastUpdateTime from foreignList order by lastUpdateTime desc limit 1)  	 " \
          "and nowConfirm > 10000 " \
          "order by nowConfirm desc"
    res = query(sql)
    return res


def newCasesInTheTop10CountriesWithin24Hours():
    sql = " select nation,addConfirm from countryAddConfirmRankList " \
          "where lastUpdateTime=(select lastUpdateTime from cityDetails " \
          "order by lastUpdateTime desc limit 1) "
    res = query(sql)
    return res


def theNumberOfForeignCountriesWithConfirmedCases():
    sql = "select continent,count(id) " \
          "from foreignList " \
          "where lastUpdateTime=(select lastUpdateTime from foreignList order by lastUpdateTime desc limit 1) " \
          "and nowConfirm > 0 " \
          "group by continent " \
          "order by count(id) desc"
    res = query(sql)
    return res
