from flask import Flask, current_app
from flask import render_template
from flask import jsonify
from jieba.analyse import extract_tags
import string
from DB import chinaSQL
from DB import worldSQL

app = Flask(__name__, template_folder='../../web', static_folder='../../static')


@app.route('/', methods=["get", "post"])
def hello_world():
    return render_template("china.html")


@app.route('/china', methods=["get", "post"])
def china():
    return render_template("china.html")


@app.route('/world', methods=["get", "post"])
def world():
    return render_template("world.html")


@app.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('image/favicon-32x32-sun.ico')


@app.route("/time")
def time():
    data = chinaSQL.time()
    return str(data[0])


@app.route("/chinaEightNumber")
def chinaEightNumber():
    data = chinaSQL.chinaEightNumber()
    return jsonify({"confirmTotal": data[0],
                    "healTotal": data[1],
                    "deadTotal": data[2],
                    "nowConfirmTotal": data[3],
                    "suspectTotal": data[4],
                    "nowSevereTotal": data[5],
                    "importedCaseTotal": data[6],
                    "noInfectTotal": data[7],
                    "confirmAdd": data[8],
                    "healAdd": data[9],
                    "deadAdd": data[10],
                    "nowConfirmAdd": data[11],
                    "suspectAdd": data[12],
                    "nowSevereAdd": data[13],
                    "importedCaseAdd": data[14],
                    "noInfectAdd": data[15]
                    })


@app.route('/chinaMap', methods=['GET'])
def chinaMap():
    data = chinaSQL.chinaMap()
    confirmToday, nowConfirmTotal, confirmTotal, healTotal, deadTotal = [], [], [], [], []
    for a, b, c, d, e, f in data:
        confirmToday.append({"name": a, "value": b})
        nowConfirmTotal.append({"name": a, "value": c})
        confirmTotal.append({"name": a, "value": d})
        healTotal.append({"name": a, "value": e})
        deadTotal.append({"name": a, "value": f})
    return jsonify({"confirmToday": confirmToday, "nowConfirmTotal": nowConfirmTotal,
                    "confirmTotal": confirmTotal, "healTotal": healTotal, "deadTotal": deadTotal})


@app.route('/chinaProvinceMap', methods=['GET'])
def chinaProvinceMap():
    data = chinaSQL.chinaProvinceMap()
    confirmToday, nowConfirmTotal, confirmTotal, healTotal, deadTotal = [], [], [], [], []
    for a, b, c, d, e, f in data:
        confirmToday.append({"name": a + "市", "value": b})
        nowConfirmTotal.append({"name": a + "市", "value": c})
        confirmTotal.append({"name": a + "市", "value": d})
        healTotal.append({"name": a + "市", "value": e})
        deadTotal.append({"name": a + "市", "value": f})
    return jsonify({"confirmToday": confirmToday, "nowConfirmTotal": nowConfirmTotal,
                    "confirmTotal": confirmTotal, "healTotal": healTotal, "deadTotal": deadTotal})


@app.route("/nationalTotal")
def nationalTotal():
    data = chinaSQL.nationalTotal()
    day, \
    confirmChinaDayList, \
    healChinaDayList, \
    deadChinaDayList, \
    importedCaseChinaDayList = [], [], [], [], []
    for a, b, c, d, e in data:
        day.append(a.strftime("%m-%d"))
        confirmChinaDayList.append(b)
        healChinaDayList.append(c)
        deadChinaDayList.append(d)
        importedCaseChinaDayList.append(e)
    return jsonify({"day": day,
                    "confirmChinaDayList": confirmChinaDayList,
                    "healChinaDayList": healChinaDayList,
                    "deadChinaDayList": deadChinaDayList,
                    "importedCaseChinaDayList": importedCaseChinaDayList
                    })


@app.route("/dailyAdditionsNationwide")
def dailyAdditionsNationwide():
    data = chinaSQL.dailyAdditionsNationwide()
    day, \
    confirmChinaDayAddList, \
    healChinaDayAddList, \
    deadChinaDayAddList, \
    importedCaseChinaDayAddList = [], [], [], [], []
    for a, b, c, d, e in data[7:]:
        day.append(a.strftime("%m-%d"))
        confirmChinaDayAddList.append(b)
        healChinaDayAddList.append(c)
        deadChinaDayAddList.append(d)
        importedCaseChinaDayAddList.append(e)
    return jsonify({"day": day,
                    "confirmChinaDayAddList": confirmChinaDayAddList,
                    "healChinaDayAddList": healChinaDayAddList,
                    "deadChinaDayAddList": deadChinaDayAddList,
                    "importedCaseChinaDayAddList": importedCaseChinaDayAddList
                    })


@app.route("/dailyCasesNationwide")
def dailyCasesNationwide():
    data = chinaSQL.dailyCasesNationwide()
    day, \
    suspectChinaDayList, \
    noInfectChinaDayList, \
    nowConfirmChinaDayList, \
    nowSevereChinaDayList = [], [], [], [], []
    for a, b, c, d, e in data[7:]:
        day.append(a.strftime("%m-%d"))
        suspectChinaDayList.append(b)
        noInfectChinaDayList.append(c)
        nowConfirmChinaDayList.append(d)
        nowSevereChinaDayList.append(e)
    return jsonify({"day": day,
                    "suspectChinaDayList": suspectChinaDayList,
                    "noInfectChinaDayList": noInfectChinaDayList,
                    "nowConfirmChinaDayList": nowConfirmChinaDayList,
                    "nowSevereChinaDayList": nowSevereChinaDayList
                    })


@app.route("/nationalCumulativeCureMortalityRate")
def nationalCumulativeCureMortalityRate():
    data = chinaSQL.nationalCumulativeCureMortalityRate()
    day, \
    healRateChinaDayList, \
    deadRateChinaDayList = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime("%m-%d"))
        healRateChinaDayList.append(b)
        deadRateChinaDayList.append(c)
    return jsonify({"day": day,
                    "healRateChinaDayList": healRateChinaDayList,
                    "deadRateChinaDayList": deadRateChinaDayList
                    })


@app.route("/detailedDataByProvince")
def detailedDataByProvince():
    data = chinaSQL.detailedDataByProvince()
    provinceName, \
    confirmTotal, \
    healTotal, \
    deadTotal, \
    healRateTotal, \
    deadRateTotal = [], [], [], [], [], []
    for a, b, c, d, e, f in data:
        provinceName.append(a)
        confirmTotal.append(b)
        healTotal.append(c)
        deadTotal.append(d)
        healRateTotal.append(e)
        deadRateTotal.append(f)
    return jsonify({"provinceName": provinceName,
                    "confirmTotal": confirmTotal,
                    "healTotal": healTotal,
                    "deadTotal": deadTotal,
                    "healRateTotal": healRateTotal,
                    "deadRateTotal": deadRateTotal
                    })


@app.route("/cumulativeNumberOfConfirmedCasesInAllProvinces")
def cumulativeNumberOfConfirmedCasesInAllProvinces():
    data = chinaSQL.cumulativeNumberOfConfirmedCasesInAllProvinces()
    provincedetails = []
    for provinceName, confirmTotal in data:
        provincedetails.append({"name": provinceName, "value": confirmTotal})
    return jsonify({"data": provincedetails})


@app.route("/currentConfirmedDataInAllProvinces")
def currentConfirmedDataInAllProvinces():
    data = chinaSQL.currentConfirmedDataInAllProvinces()
    provinceName, \
    nowConfirmTotal, \
    confirmToday, \
    suspectTotal = [], [], [], []
    for a, b, c, d in data:
        provinceName.append(a)
        nowConfirmTotal.append(b)
        confirmToday.append(c)
        suspectTotal.append(d)
    return jsonify({"provinceName": provinceName,
                    "nowConfirmTotal": nowConfirmTotal,
                    "confirmToday": confirmToday,
                    "suspectTotal": suspectTotal
                    })


@app.route("/existingDiagnosticClassificationInChina")
def existingDiagnosticClassificationInChina():
    data = chinaSQL.existingDiagnosticClassificationInChina()
    nowconfirmstatis = []
    nowconfirmstatis.append({"name": '港澳台现存确诊', "value": data[0][0]})
    nowconfirmstatis.append({"name": '境外输入现存确诊', "value": data[0][1]})
    nowconfirmstatis.append({"name": '31省本土现有确诊', "value": data[0][2]})
    return jsonify({"data": nowconfirmstatis})


@app.route("/totalNumberOfOverseasImportsFromTop10Provinces")
def totalNumberOfOverseasImportsFromTop10Provinces():
    data = chinaSQL.totalNumberOfOverseasImportsFromTop10Provinces()
    importstatis = []
    for province, importedCase in data:
        importstatis.append({"name": province, "value": importedCase})

    return jsonify({"data": importstatis})


@app.route("/eachProvinceComparesYesterdayData")
def eachProvinceComparesYesterdayData():
    data = chinaSQL.eachProvinceComparesYesterdayData()
    province, \
    nowConfirm, \
    confirmAdd, \
    heal, \
    dead, \
    zero = [], [], [], [], [], []
    for a, b, c, d, e, f in data:
        province.append(a)
        nowConfirm.append(b)
        confirmAdd.append(c)
        heal.append(d)
        dead.append(e)
        zero.append(f)
    return jsonify({"province": province,
                    "nowConfirm": nowConfirm,
                    "confirmAdd": confirmAdd,
                    "heal": heal,
                    "dead": dead,
                    "zero": zero
                    })


@app.route("/hubeiNonHubeiNationalCumulativeData")
def hubeiNonHubeiNationalCumulativeData():
    data = chinaSQL.hubeiNonHubeiNationalCumulativeData()
    day, \
    hubeiNowConfirm, \
    hubeiHeal, \
    hubeiDead, \
    notHubeiNowConfirm, \
    notHubeiHeal, \
    notHubeiDead, \
    countryNowConfirm, \
    countryHeal, \
    countryDead = [], [], [], [], [], [], [], [], [], []
    for a, b, c, d, e, f, g, h, i, j in data:
        day.append(a.strftime("%m-%d"))
        hubeiNowConfirm.append(b)
        hubeiHeal.append(c)
        hubeiDead.append(d)
        notHubeiNowConfirm.append(e)
        notHubeiHeal.append(f)
        notHubeiDead.append(g)
        countryNowConfirm.append(h)
        countryHeal.append(i)
        countryDead.append(j)
    return jsonify({"day": day,
                    "hubeiNowConfirm": hubeiNowConfirm,
                    "hubeiHeal": hubeiHeal,
                    "hubeiDead": hubeiDead,
                    "notHubeiNowConfirm": notHubeiNowConfirm,
                    "notHubeiHeal": notHubeiHeal,
                    "notHubeiDead": notHubeiDead,
                    "countryNowConfirm": countryNowConfirm,
                    "countryHeal": countryHeal,
                    "countryDead": countryDead
                    })


@app.route("/hubeiNonHubeiNationalCureMortalityRate")
def hubeiNonHubeiNationalCureMortalityRate():
    data = chinaSQL.hubeiNonHubeiNationalCureMortalityRate()
    day, \
    hubeiHealRate, \
    hubeiDeadRate, \
    notHubeiHealRate, \
    notHubeiDeadRate, \
    countryHealRate, \
    countryDeadRate = [], [], [], [], [], [], []
    for a, b, c, d, e, f, g in data:
        day.append(a.strftime("%m-%d"))
        hubeiHealRate.append(b)
        hubeiDeadRate.append(c)
        notHubeiHealRate.append(d)
        notHubeiDeadRate.append(e)
        countryHealRate.append(f)
        countryDeadRate.append(g)
    return jsonify({"day": day,
                    "hubeiHealRate": hubeiHealRate,
                    "hubeiDeadRate": hubeiDeadRate,
                    "notHubeiHealRate": notHubeiHealRate,
                    "notHubeiDeadRate": notHubeiDeadRate,
                    "countryHealRate": countryHealRate,
                    "countryDeadRate": countryDeadRate
                    })


@app.route("/hubeiNonHubeiNationalDailyNew")
def hubeiNonHubeiNationalDailyNew():
    data = chinaSQL.hubeiNonHubeiNationalDailyNew()
    day, \
    hubei, \
    notHubei, \
    country = [], [], [], []
    for a, b, c, d in data[7:]:
        day.append(a.strftime("%m-%d"))
        hubei.append(b)
        notHubei.append(c)
        country.append(d)
    return jsonify({"day": day,
                    "hubei": hubei,
                    "notHubei": notHubei,
                    "country": country
                    })


@app.route("/wuhanNotWuhanNotHubeiNewlyConfirmed")
def wuhanNotWuhanNotHubeiNewlyConfirmed():
    data = chinaSQL.wuhanNotWuhanNotHubeiNewlyConfirmed()
    day, \
    wuhan, \
    notWuhan, \
    notHubei = [], [], [], []
    for a, b, c, d in data:
        day.append(a.strftime("%m-%d"))
        wuhan.append(b)
        notWuhan.append(c)
        notHubei.append(d)
    return jsonify({"day": day,
                    "wuhan": wuhan,
                    "notWuhan": notWuhan,
                    "notHubei": notHubei
                    })


@app.route("/totalConfirmedTop20UrbanAreas")
def totalConfirmedTop20UrbanAreas():
    data = chinaSQL.totalConfirmedTop20UrbanAreas()
    cityName, \
    deadRateTotal, \
    healRateTotal = [], [], []
    for a, b, c in data:
        cityName.append(a)
        deadRateTotal.append(b)
        healRateTotal.append(c)
    return jsonify({"cityName": cityName,
                    "deadRateTotal": deadRateTotal,
                    "healRateTotal": healRateTotal
                    })


@app.route("/existingConfirmedTop20UrbanAreas")
def existingConfirmedTop20UrbanAreas():
    data = chinaSQL.existingConfirmedTop20UrbanAreas()
    cityName, \
    nowConfirmTotal, \
    confirmToday, \
    suspectTotal = [], [], [], []
    for a, b, c, d in data:
        cityName.append(a)
        nowConfirmTotal.append(b)
        confirmToday.append(c)
        suspectTotal.append(d)
    return jsonify({"cityName": cityName,
                    "nowConfirmTotal": nowConfirmTotal,
                    "confirmToday": confirmToday,
                    "suspectTotal": suspectTotal
                    })


@app.route("/urbanDataOfHubeiProvince")
def urbanDataOfHubeiProvince():
    data = chinaSQL.urbanDataOfHubeiProvince()
    cityName, \
    confirmTotal, \
    healTotal, \
    deadTotal = [], [], [], []
    for a, b, c, d in data:
        cityName.append(a)
        confirmTotal.append(b)
        healTotal.append(c)
        deadTotal.append(d)
    return jsonify({"cityName": cityName,
                    "confirmTotal": confirmTotal,
                    "healTotal": healTotal,
                    "deadTotal": deadTotal
                    })


@app.route("/accumulativeDataExceptHubeiProvince")
def accumulativeDataExceptHubeiProvince():
    data = chinaSQL.accumulativeDataExceptHubeiProvince()
    cityName, \
    confirmTotal, \
    healTotal, \
    deadTotal = [], [], [], []
    for a, b, c, d in data:
        cityName.append(a)
        confirmTotal.append(b)
        healTotal.append(c)
        deadTotal.append(d)
    return jsonify({"cityName": cityName,
                    "confirmTotal": confirmTotal,
                    "healTotal": healTotal,
                    "deadTotal": deadTotal
                    })


@app.route("/provincesWithFatalCasesNationwide")
def provincesWithFatalCasesNationwide():
    data = chinaSQL.provincesWithFatalCasesNationwide()
    provincedetails = []
    provincedetails.append({"name": "无死亡病例省份数量", "value": data[0][0]})
    provincedetails.append({"name": "有死亡病例省份数量", "value": data[0][1]})
    return jsonify({"data": provincedetails})


@app.route("/numberOfDeathsInCities")
def numberOfDeathsInCities():
    data = chinaSQL.numberOfDeathsInCities()
    dataCityCount = []
    dataCityCount.append({"name": "无死亡病例城市数量", "value": data[0][0]})
    dataCityCount.append({"name": "有死亡病例城市数量", "value": data[0][1]})
    return jsonify({"data": dataCityCount})


@app.route("/outbreakOut")
def outbreakOut():
    data = chinaSQL.outbreakOut()
    d = []
    for i in data:
        k = i[0].rstrip(string.digits)
        v = i[0][len(k):]
        ks = extract_tags(k)
        for j in ks:
            if not j.isdigit():
                d.append({"name": j, "value": v})
    return jsonify({"kws": d})


@app.route("/worldFourNumber")
def worldFourNumber():
    data = worldSQL.worldFourNumber()
    return jsonify({"nowConfirm": data[0],
                    "confirm": data[1],
                    "heal": data[2],
                    "dead": data[3],
                    "nowConfirmAdd": data[4],
                    "confirmAdd": data[5],
                    "healAdd": data[6],
                    "deadAdd": data[7]
                    })


@app.route('/worldMapNoChina', methods=['GET'])
def worldMapNoChina():
    data = worldSQL.worldMapNoChina()
    nowConfirm, confirm, heal, dead = [], [], [], []
    for a, b, c, d, e in data:
        nowConfirm.append({"name": a, "value": b})
        confirm.append({"name": a, "value": c})
        heal.append({"name": a, "value": d})
        dead.append({"name": a, "value": e})
    data1 = worldSQL.worldMapChina()
    nowConfirm.append({"name": "中国", "value": data1[0][0]})
    confirm.append({"name": "中国", "value": data1[0][1]})
    heal.append({"name": "中国", "value": data1[0][2]})
    dead.append({"name": "中国", "value": data1[0][3]})
    return jsonify({"nowConfirm": nowConfirm,
                    "confirm": confirm,
                    "heal": heal,
                    "dead": dead
                    })


@app.route("/globalCumulativeTrend")
def globalCumulativeTrend():
    data = worldSQL.globalCumulativeTrend()
    day, \
    confirm, \
    heal, \
    dead, \
    newAddConfirm = [], [], [], [], []
    for a, b, c, d, e in data:
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        heal.append(c)
        dead.append(d)
        newAddConfirm.append(e)
    return jsonify({"day": day,
                    "confirm": confirm,
                    "heal": heal,
                    "dead": dead,
                    "newAddConfirm": newAddConfirm
                    })


@app.route("/globalCumulativeCureMortality")
def globalCumulativeCureMortality():
    data = worldSQL.globalCumulativeCureMortality()
    day, \
    healRate, \
    deadRate = [], [], []
    for a, b, c in data:
        day.append(a.strftime("%m-%d"))
        healRate.append(b)
        deadRate.append(c)
    return jsonify({"day": day,
                    "healRate": healRate,
                    "deadRate": deadRate
                    })


@app.route("/foreignCumulativeDiagnosisTop10Countries")
def foreignCumulativeDiagnosisTop10Countries():
    data = worldSQL.foreignCumulativeDiagnosisTop10Countries()
    name, \
    nowConfirm, \
    confirm, \
    heal, \
    dead = [], [], [], [], []
    for a, b, c, d, e in data:
        name.append(a)
        nowConfirm.append(b)
        confirm.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"name": name,
                    "nowConfirm": nowConfirm,
                    "confirm": confirm,
                    "heal": heal,
                    "dead": dead
                    })


@app.route("/theTop10CountriesGrewFastestInSevenDays")
def theTop10CountriesGrewFastestInSevenDays():
    data = worldSQL.theTop10CountriesGrewFastestInSevenDays()
    nation, \
    day7, \
    day, \
    rate = [], [], [], []
    for a, b, c, d in data:
        nation.append(a)
        day7.append(b)
        day.append(c)
        rate.append(d)
    return jsonify({"nation": nation,
                    "day7": day7,
                    "day0": day,
                    "rate": rate
                    })


@app.route("/overseasCountriesWithMoreThan10000ConfirmedCases")
def overseasCountriesWithMoreThan10000ConfirmedCases():
    data = worldSQL.overseasCountriesWithMoreThan10000ConfirmedCases()
    foreignlist = []
    for name, confirm in data:
        foreignlist.append({"name": name, "value": confirm})
    return jsonify({"data": foreignlist})


@app.route("/overseasCountriesWithMoreThan10000HaveBeenConfirmedCases")
def overseasCountriesWithMoreThan10000HaveBeenConfirmedCases():
    data = worldSQL.overseasCountriesWithMoreThan10000HaveBeenConfirmedCases()
    foreignlist = []
    for name, nowConfirm in data:
        foreignlist.append({"name": name, "value": nowConfirm})
    return jsonify({"data": foreignlist})


@app.route("/newCasesInTheTop10CountriesWithin24Hours")
def newCasesInTheTop10CountriesWithin24Hours():
    data = worldSQL.newCasesInTheTop10CountriesWithin24Hours()
    nationAddConfirm = []
    for nation, addConfirm in data:
        nationAddConfirm.append({"name": nation, "value": addConfirm})
    return jsonify({"data": nationAddConfirm})


@app.route("/theNumberOfForeignCountriesWithConfirmedCases")
def theNumberOfForeignCountriesWithConfirmedCases():
    data = worldSQL.theNumberOfForeignCountriesWithConfirmedCases()
    foreignlist = []
    for continent, count in data:
        foreignlist.append({"name": continent, "value": count})
    return jsonify({"data": foreignlist})


if __name__ == '__main__':
    app.run()
