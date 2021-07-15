function time() {
    $.ajax({
        url: "/time",
        timeout: 10000,
        success: function (data) {
            $("#time").html("数据更新时间 : " + data.toString())
        },
        error: function (xhr, type, errorThrown) {

        }
    });
}


function chinaEightNumber() {
    $.ajax({
        url: "/chinaEightNumber",
        success: function (data) {
            $(".xianyouquezhen").eq(0).text(data.nowConfirmAdd > -1 ? "+" + data.nowConfirmAdd : data.nowConfirmAdd);
            $(".wuzhengzhuang").eq(0).text(data.noInfectAdd > -1 ? "+" + data.noInfectAdd : data.noInfectAdd);
            $(".xianyouyisi").eq(0).text(data.suspectAdd > -1 ? "+" + data.suspectAdd : data.suspectAdd);
            $(".xianyouzhongzheng").eq(0).text(data.nowSevereAdd > -1 ? "+" + data.nowSevereAdd : data.nowSevereAdd);
            $(".jingwaishuru").eq(0).text(data.importedCaseAdd > -1 ? "+" + data.importedCaseAdd : data.importedCaseAdd);
            $(".leijiquezhen").eq(0).text(data.confirmAdd > -1 ? "+" + data.confirmAdd : data.confirmAdd);
            $(".leijizhiyu").eq(0).text(data.healAdd > -1 ? "+" + data.healAdd : data.healAdd);
            $(".leijisiwang").eq(0).text(data.deadAdd > -1 ? "+" + data.deadAdd : data.deadAdd);
            $(".xianyouquezhen").eq(1).text(data.nowConfirmTotal);
            $(".wuzhengzhuang").eq(1).text(data.noInfectTotal);
            $(".xianyouyisi").eq(1).text(data.suspectTotal);
            $(".xianyouzhongzheng").eq(1).text(data.nowSevereTotal);
            $(".jingwaishuru").eq(1).text(data.importedCaseTotal);
            $(".leijiquezhen").eq(1).text(data.confirmTotal);
            $(".leijizhiyu").eq(1).text(data.healTotal);
            $(".leijisiwang").eq(1).text(data.deadTotal);
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function chinaMap() {
    $.ajax({
        url: "/chinaMap",
        success: function (data) {
            ec_chinaMap_option.series[0].data = data.confirmToday;
            ec_chinaMap_option.series[1].data = data.nowConfirmTotal;
            ec_chinaMap_option.series[2].data = data.confirmTotal;
            ec_chinaMap_option.series[3].data = data.healTotal;
            ec_chinaMap_option.series[4].data = data.deadTotal;
            ec_chinaMap.setOption(ec_chinaMap_option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function nationalTotal() {
    $.ajax({
        url: "/nationalTotal",
        success: function (data) {
            ec_nationalTotal_Option.xAxis[0].data = data.day
            ec_nationalTotal_Option.series[0].data = data.confirmChinaDayList
            ec_nationalTotal_Option.series[1].data = data.healChinaDayList
            ec_nationalTotal_Option.series[2].data = data.deadChinaDayList
            ec_nationalTotal_Option.series[3].data = data.importedCaseChinaDayList
            ec_nationalTotal.setOption(ec_nationalTotal_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function dailyAdditionsNationwide() {
    $.ajax({
        url: "/dailyAdditionsNationwide",
        success: function (data) {
            ec_dailyAdditionsNationwide_Option.xAxis[0].data = data.day
            ec_dailyAdditionsNationwide_Option.series[0].data = data.confirmChinaDayAddList
            ec_dailyAdditionsNationwide_Option.series[1].data = data.healChinaDayAddList
            ec_dailyAdditionsNationwide_Option.series[2].data = data.deadChinaDayAddList
            ec_dailyAdditionsNationwide_Option.series[3].data = data.importedCaseChinaDayAddList
            ec_dailyAdditionsNationwide.setOption(ec_dailyAdditionsNationwide_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function outbreakOut() {
    $.ajax({
        url: "/outbreakOut",
        success: function (data) {
            ec_outbreakOut_option.series[0].data = data.kws;
            ec_outbreakOut.setOption(ec_outbreakOut_option);
        }
    })
}


function dailyCasesNationwide() {
    $.ajax({
        url: "/dailyCasesNationwide",
        success: function (data) {
            ec_dailyCasesNationwide_Option.xAxis[0].data = data.day
            ec_dailyCasesNationwide_Option.series[0].data = data.noInfectChinaDayList
            ec_dailyCasesNationwide_Option.series[1].data = data.nowSevereChinaDayList
            ec_dailyCasesNationwide_Option.series[2].data = data.suspectChinaDayList
            ec_dailyCasesNationwide_Option.series[3].data = data.nowConfirmChinaDayList
            ec_dailyCasesNationwide.setOption(ec_dailyCasesNationwide_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function nationalCumulativeCureMortalityRate() {
    $.ajax({
        url: "/nationalCumulativeCureMortalityRate",
        success: function (data) {
            ec_nationalCumulativeCureMortalityRate_Option.xAxis[0].data = data.day
            ec_nationalCumulativeCureMortalityRate_Option.series[0].data = data.healRateChinaDayList
            ec_nationalCumulativeCureMortalityRate_Option.series[1].data = data.deadRateChinaDayList
            ec_nationalCumulativeCureMortalityRate.setOption(ec_nationalCumulativeCureMortalityRate_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function urbanDataOfHubeiProvince() {
    $.ajax({
        url: "/urbanDataOfHubeiProvince",
        success: function (data) {
            ec_urbanDataOfHubeiProvince_Option.xAxis[0].data = data.cityName
            ec_urbanDataOfHubeiProvince_Option.series[0].data = data.confirmTotal
            ec_urbanDataOfHubeiProvince_Option.series[1].data = data.healTotal
            ec_urbanDataOfHubeiProvince_Option.series[2].data = data.deadTotal
            ec_urbanDataOfHubeiProvince.setOption(ec_urbanDataOfHubeiProvince_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function accumulativeDataExceptHubeiProvince() {
    $.ajax({
        url: "/accumulativeDataExceptHubeiProvince",
        success: function (data) {
            ec_accumulativeDataExceptHubeiProvince_Option.angleAxis[0].data = data.cityName
            ec_accumulativeDataExceptHubeiProvince_Option.series[0].data = data.confirmTotal
            ec_accumulativeDataExceptHubeiProvince_Option.series[1].data = data.healTotal
            ec_accumulativeDataExceptHubeiProvince_Option.series[2].data = data.deadTotal
            ec_accumulativeDataExceptHubeiProvince.setOption(ec_accumulativeDataExceptHubeiProvince_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function existingConfirmedTop20UrbanAreas() {
    $.ajax({
        url: "/existingConfirmedTop20UrbanAreas",
        success: function (data) {
            ec_existingConfirmedTop20UrbanAreas_Option.xAxis[0].data = data.cityName
            ec_existingConfirmedTop20UrbanAreas_Option.series[0].data = data.confirmToday
            ec_existingConfirmedTop20UrbanAreas_Option.series[1].data = data.nowConfirmTotal
            ec_existingConfirmedTop20UrbanAreas_Option.series[2].data = data.suspectTotal
            ec_existingConfirmedTop20UrbanAreas.setOption(ec_existingConfirmedTop20UrbanAreas_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function totalConfirmedTop20UrbanAreas() {
    $.ajax({
        url: "/totalConfirmedTop20UrbanAreas",
        success: function (data) {
            ec_totalConfirmedTop20UrbanAreas_Option.angleAxis[0].data = data.cityName
            ec_totalConfirmedTop20UrbanAreas_Option.series[0].data = data.deadRateTotal
            ec_totalConfirmedTop20UrbanAreas_Option.series[1].data = data.healRateTotal
            ec_totalConfirmedTop20UrbanAreas.setOption(ec_totalConfirmedTop20UrbanAreas_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function numberOfDeathsInCities() {
    $.ajax({
        url: "/numberOfDeathsInCities",
        success: function (data) {
            ec_numberOfDeathsInCities_Option.legend.data = data.data.name;
            ec_numberOfDeathsInCities_Option.series[0].data = data.data;
            ec_numberOfDeathsInCities.setOption(ec_numberOfDeathsInCities_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function hubeiNonHubeiNationalCumulativeData() {
    $.ajax({
        url: "/hubeiNonHubeiNationalCumulativeData",
        success: function (data) {
            ec_hubeiNonHubeiNationalCumulativeData_Option.xAxis[0].data = data.day
            ec_hubeiNonHubeiNationalCumulativeData_Option.series[0].data = data.hubeiNowConfirm
            ec_hubeiNonHubeiNationalCumulativeData_Option.series[1].data = data.hubeiHeal
            ec_hubeiNonHubeiNationalCumulativeData_Option.series[2].data = data.hubeiDead
            ec_hubeiNonHubeiNationalCumulativeData_Option.series[3].data = data.notHubeiNowConfirm
            ec_hubeiNonHubeiNationalCumulativeData_Option.series[4].data = data.notHubeiHeal
            ec_hubeiNonHubeiNationalCumulativeData_Option.series[5].data = data.notHubeiDead
            ec_hubeiNonHubeiNationalCumulativeData_Option.series[6].data = data.countryNowConfirm
            ec_hubeiNonHubeiNationalCumulativeData_Option.series[7].data = data.countryHeal
            ec_hubeiNonHubeiNationalCumulativeData_Option.series[8].data = data.countryDead
            ec_hubeiNonHubeiNationalCumulativeData.setOption(ec_hubeiNonHubeiNationalCumulativeData_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function hubeiNonHubeiNationalCureMortalityRate() {
    $.ajax({
        url: "/hubeiNonHubeiNationalCureMortalityRate",
        success: function (data) {
            ec_hubeiNonHubeiNationalCureMortalityRate_Option.xAxis[0].data = data.day
            ec_hubeiNonHubeiNationalCureMortalityRate_Option.series[0].data = data.hubeiHealRate
            ec_hubeiNonHubeiNationalCureMortalityRate_Option.series[1].data = data.hubeiDeadRate
            ec_hubeiNonHubeiNationalCureMortalityRate_Option.series[2].data = data.notHubeiHealRate
            ec_hubeiNonHubeiNationalCureMortalityRate_Option.series[3].data = data.notHubeiDeadRate
            ec_hubeiNonHubeiNationalCureMortalityRate_Option.series[4].data = data.countryHealRate
            ec_hubeiNonHubeiNationalCureMortalityRate_Option.series[5].data = data.countryDeadRate
            ec_hubeiNonHubeiNationalCureMortalityRate.setOption(ec_hubeiNonHubeiNationalCureMortalityRate_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function hubeiNonHubeiNationalDailyNew() {
    $.ajax({
        url: "/hubeiNonHubeiNationalDailyNew",
        success: function (data) {
            ec_hubeiNonHubeiNationalDailyNew_Option.xAxis[0].data = data.day
            ec_hubeiNonHubeiNationalDailyNew_Option.series[0].data = data.hubei
            ec_hubeiNonHubeiNationalDailyNew_Option.series[1].data = data.notHubei
            ec_hubeiNonHubeiNationalDailyNew_Option.series[2].data = data.country
            ec_hubeiNonHubeiNationalDailyNew.setOption(ec_hubeiNonHubeiNationalDailyNew_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function totalNumberOfOverseasImportsFromTop10Provinces() {
    $.ajax({
        url: "/totalNumberOfOverseasImportsFromTop10Provinces",
        success: function (data) {
            ec_totalNumberOfOverseasImportsFromTop10Provinces_Option.legend.data = data.data.name;
            ec_totalNumberOfOverseasImportsFromTop10Provinces_Option.series[0].data = data.data;
            ec_totalNumberOfOverseasImportsFromTop10Provinces.setOption(ec_totalNumberOfOverseasImportsFromTop10Provinces_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function existingDiagnosticClassificationInChina() {
    $.ajax({
        url: "/existingDiagnosticClassificationInChina",
        success: function (data) {
            ec_existingDiagnosticClassificationInChina_Option.series[0].data = data.data;
            ec_existingDiagnosticClassificationInChina.setOption(ec_existingDiagnosticClassificationInChina_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function eachProvinceComparesYesterdayData() {
    $.ajax({
        url: "/eachProvinceComparesYesterdayData",
        success: function (data) {
            ec_eachProvinceComparesYesterdayData_Option.xAxis[0].data = data.province;
            ec_eachProvinceComparesYesterdayData_Option.series[0].data = data.nowConfirm;
            ec_eachProvinceComparesYesterdayData_Option.series[1].data = data.confirmAdd;
            ec_eachProvinceComparesYesterdayData_Option.series[2].data = data.heal;
            ec_eachProvinceComparesYesterdayData_Option.series[3].data = data.dead;
            ec_eachProvinceComparesYesterdayData_Option.series[4].data = data.zero;
            ec_eachProvinceComparesYesterdayData.setOption(ec_eachProvinceComparesYesterdayData_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function detailedDataByProvince() {
    $.ajax({
        url: "/detailedDataByProvince",
        success: function (data) {
            ec_detailedDataByProvince_Option.xAxis[0].data = data.provinceName;
            ec_detailedDataByProvince_Option.series[0].data = data.confirmTotal;
            ec_detailedDataByProvince_Option.series[1].data = data.healTotal;
            ec_detailedDataByProvince_Option.series[2].data = data.deadTotal;
            ec_detailedDataByProvince_Option.series[3].data = data.healRateTotal;
            ec_detailedDataByProvince_Option.series[4].data = data.deadRateTotal;
            ec_detailedDataByProvince.setOption(ec_detailedDataByProvince_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function currentConfirmedDataInAllProvinces() {
    $.ajax({
        url: "/currentConfirmedDataInAllProvinces",
        success: function (data) {
            ec_currentConfirmedDataInAllProvinces_Option.xAxis[0].data = data.provinceName;
            ec_currentConfirmedDataInAllProvinces_Option.series[0].data = data.nowConfirmTotal;
            ec_currentConfirmedDataInAllProvinces_Option.series[1].data = data.confirmToday;
            ec_currentConfirmedDataInAllProvinces_Option.series[2].data = data.suspectTotal;
            ec_currentConfirmedDataInAllProvinces.setOption(ec_currentConfirmedDataInAllProvinces_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function provincesWithFatalCasesNationwide() {
    $.ajax({
        url: "/provincesWithFatalCasesNationwide",
        success: function (data) {
            ec_provincesWithFatalCasesNationwide_Option.legend.data = data.data.name;
            ec_provincesWithFatalCasesNationwide_Option.series[0].data = data.data;
            ec_provincesWithFatalCasesNationwide.setOption(ec_provincesWithFatalCasesNationwide_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function cumulativeNumberOfConfirmedCasesInAllProvinces() {
    $.ajax({
        url: "/cumulativeNumberOfConfirmedCasesInAllProvinces",
        success: function (data) {
            ec_cumulativeNumberOfConfirmedCasesInAllProvinces_Option.legend.data = data.data.name;
            ec_cumulativeNumberOfConfirmedCasesInAllProvinces_Option.series[0].data = data.data;
            ec_cumulativeNumberOfConfirmedCasesInAllProvinces.setOption(ec_cumulativeNumberOfConfirmedCasesInAllProvinces_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function wuhanNotWuhanNotHubeiNewlyConfirmed() {
    $.ajax({
        url: "/wuhanNotWuhanNotHubeiNewlyConfirmed",
        success: function (data) {
            ec_wuhanNotWuhanNotHubeiNewlyConfirmed_Option.xAxis[0].data = data.day
            ec_wuhanNotWuhanNotHubeiNewlyConfirmed_Option.series[0].data = data.wuhan
            ec_wuhanNotWuhanNotHubeiNewlyConfirmed_Option.series[1].data = data.notWuhan
            ec_wuhanNotWuhanNotHubeiNewlyConfirmed_Option.series[2].data = data.notHubei
            ec_wuhanNotWuhanNotHubeiNewlyConfirmed.setOption(ec_wuhanNotWuhanNotHubeiNewlyConfirmed_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


time()
chinaEightNumber()
chinaMap()
nationalTotal()
dailyAdditionsNationwide()
outbreakOut()
dailyCasesNationwide()
nationalCumulativeCureMortalityRate()
urbanDataOfHubeiProvince()
accumulativeDataExceptHubeiProvince()
existingConfirmedTop20UrbanAreas()
totalConfirmedTop20UrbanAreas()
numberOfDeathsInCities()
hubeiNonHubeiNationalCumulativeData()
hubeiNonHubeiNationalCureMortalityRate()
hubeiNonHubeiNationalDailyNew()
totalNumberOfOverseasImportsFromTop10Provinces()
existingDiagnosticClassificationInChina()
eachProvinceComparesYesterdayData()
detailedDataByProvince()
currentConfirmedDataInAllProvinces()
provincesWithFatalCasesNationwide()
cumulativeNumberOfConfirmedCasesInAllProvinces()
wuhanNotWuhanNotHubeiNewlyConfirmed()


setInterval(time, 1000000)
setInterval(chinaEightNumber, 1000000)
setInterval(chinaMap, 1000000)
setInterval(nationalTotal, 1000000)
setInterval(dailyAdditionsNationwide, 1000000)
setInterval(outbreakOut, 1000000)
setInterval(dailyCasesNationwide, 1000000)
setInterval(nationalCumulativeCureMortalityRate, 1000000)
setInterval(urbanDataOfHubeiProvince, 1000000)
setInterval(accumulativeDataExceptHubeiProvince, 1000000)
setInterval(existingConfirmedTop20UrbanAreas, 1000000)
setInterval(totalConfirmedTop20UrbanAreas, 1000000)
setInterval(numberOfDeathsInCities, 1000000)
setInterval(hubeiNonHubeiNationalCumulativeData, 1000000)
setInterval(hubeiNonHubeiNationalCureMortalityRate, 1000000)
setInterval(hubeiNonHubeiNationalDailyNew, 1000000)
setInterval(totalNumberOfOverseasImportsFromTop10Provinces, 1000000)
setInterval(existingDiagnosticClassificationInChina, 1000000)
setInterval(eachProvinceComparesYesterdayData, 1000000)
setInterval(detailedDataByProvince, 1000000)
setInterval(currentConfirmedDataInAllProvinces, 1000000)
setInterval(provincesWithFatalCasesNationwide, 1000000)
setInterval(cumulativeNumberOfConfirmedCasesInAllProvinces, 1000000)
setInterval(wuhanNotWuhanNotHubeiNewlyConfirmed, 1000000)













