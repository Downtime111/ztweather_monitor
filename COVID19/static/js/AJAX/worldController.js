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


function worldFourNumber() {
    $.ajax({
        url: "/worldFourNumber",
        success: function (data) {
            $(".xianyouquezhen2").eq(0).text(data.nowConfirmAdd > -1 ? "+" + data.nowConfirmAdd : data.nowConfirmAdd);
            $(".leijiquezhen2").eq(0).text(data.confirmAdd > -1 ? "+" + data.confirmAdd : data.confirmAdd);
            $(".leijizhiyu2").eq(0).text(data.healAdd > -1 ? "+" + data.healAdd : data.healAdd);
            $(".leijisiwang2").eq(0).text(data.deadAdd > -1 ? "+" + data.deadAdd : data.deadAdd);
            $(".xianyouquezhen2").eq(1).text(data.nowConfirm);
            $(".leijiquezhen2").eq(1).text(data.confirm);
            $(".leijizhiyu2").eq(1).text(data.heal);
            $(".leijisiwang2").eq(1).text(data.dead);
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function newCasesInTheTop10CountriesWithin24Hours() {
    $.ajax({
        url: "/newCasesInTheTop10CountriesWithin24Hours",
        success: function (data) {
            ec_newCasesInTheTop10CountriesWithin24Hours_Option.legend.data = data.data.name;
            ec_newCasesInTheTop10CountriesWithin24Hours_Option.series[0].data = data.data;
            ec_newCasesInTheTop10CountriesWithin24Hours.setOption(ec_newCasesInTheTop10CountriesWithin24Hours_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function theTop10CountriesGrewFastestInSevenDays() {
    $.ajax({
        url: "/theTop10CountriesGrewFastestInSevenDays",
        success: function (data) {
            ec_theTop10CountriesGrewFastestInSevenDays_Option.xAxis[0].data = data.nation;
            ec_theTop10CountriesGrewFastestInSevenDays_Option.series[0].data = data.day7;
            ec_theTop10CountriesGrewFastestInSevenDays_Option.series[1].data = data.day0;
            ec_theTop10CountriesGrewFastestInSevenDays_Option.series[2].data = data.rate;
            ec_theTop10CountriesGrewFastestInSevenDays.setOption(ec_theTop10CountriesGrewFastestInSevenDays_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function foreignCumulativeDiagnosisTop10Countries() {
    $.ajax({
        url: "/foreignCumulativeDiagnosisTop10Countries",
        success: function (data) {
            ec_foreignCumulativeDiagnosisTop10Countries_Option.yAxis[0].data = data.name
            ec_foreignCumulativeDiagnosisTop10Countries_Option.series[0].data = data.nowConfirm
            ec_foreignCumulativeDiagnosisTop10Countries_Option.series[1].data = data.confirm
            ec_foreignCumulativeDiagnosisTop10Countries_Option.series[2].data = data.heal
            ec_foreignCumulativeDiagnosisTop10Countries_Option.series[3].data = data.dead
            ec_foreignCumulativeDiagnosisTop10Countries.setOption(ec_foreignCumulativeDiagnosisTop10Countries_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function theNumberOfForeignCountriesWithConfirmedCases() {
    $.ajax({
        url: "/theNumberOfForeignCountriesWithConfirmedCases",
        success: function (data) {
            ec_theNumberOfForeignCountriesWithConfirmedCases_Option.legend.data = data.data.name
            ec_theNumberOfForeignCountriesWithConfirmedCases_Option.series[0].data = data.data
            ec_theNumberOfForeignCountriesWithConfirmedCases.setOption(ec_theNumberOfForeignCountriesWithConfirmedCases_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function overseasCountriesWithMoreThan10000ConfirmedCases() {
    $.ajax({
        url: "/overseasCountriesWithMoreThan10000ConfirmedCases",
        success: function (data) {
            ec_overseasCountriesWithMoreThan10000ConfirmedCases_Option.legend.data = data.data.name
            ec_overseasCountriesWithMoreThan10000ConfirmedCases_Option.series[0].data = data.data
            ec_overseasCountriesWithMoreThan10000ConfirmedCases.setOption(ec_overseasCountriesWithMoreThan10000ConfirmedCases_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function overseasCountriesWithMoreThan10000HaveBeenConfirmedCases() {
    $.ajax({
        url: "/overseasCountriesWithMoreThan10000HaveBeenConfirmedCases",
        success: function (data) {
            ec_overseasCountriesWithMoreThan10000HaveBeenConfirmedCases_Option.legend.data = data.data.name
            ec_overseasCountriesWithMoreThan10000HaveBeenConfirmedCases_Option.series[0].data = data.data
            ec_overseasCountriesWithMoreThan10000HaveBeenConfirmedCases.setOption(ec_overseasCountriesWithMoreThan10000HaveBeenConfirmedCases_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function globalCumulativeTrend() {
    $.ajax({
        url: "/globalCumulativeTrend",
        success: function (data) {
            ec_globalCumulativeTrend_Option.xAxis[0].data = data.day
            ec_globalCumulativeTrend_Option.series[0].data = data.confirm
            ec_globalCumulativeTrend_Option.series[1].data = data.heal
            ec_globalCumulativeTrend_Option.series[2].data = data.dead
            ec_globalCumulativeTrend_Option.series[3].data = data.newAddConfirm
            ec_globalCumulativeTrend.setOption(ec_globalCumulativeTrend_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function globalCumulativeCureMortality() {
    $.ajax({
        url: "/globalCumulativeCureMortality",
        success: function (data) {
            ec_globalCumulativeCureMortality_Option.xAxis[0].data = data.day
            ec_globalCumulativeCureMortality_Option.series[0].data = data.healRate
            ec_globalCumulativeCureMortality_Option.series[1].data = data.deadRate
            ec_globalCumulativeCureMortality.setOption(ec_globalCumulativeCureMortality_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}


function worldMapNoChina() {
    $.ajax({
        url: "/worldMapNoChina",
        success: function (data) {
            ec_worldMapNoChina_Option.series[0].data = data.nowConfirm
            ec_worldMapNoChina_Option.series[1].data = data.confirm
            ec_worldMapNoChina_Option.series[2].data = data.heal
            ec_worldMapNoChina_Option.series[3].data = data.dead
            ec_worldMapNoChina.setOption(ec_worldMapNoChina_Option)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}



time()
worldFourNumber()
newCasesInTheTop10CountriesWithin24Hours()
theTop10CountriesGrewFastestInSevenDays()
foreignCumulativeDiagnosisTop10Countries()
theNumberOfForeignCountriesWithConfirmedCases()
overseasCountriesWithMoreThan10000ConfirmedCases()
overseasCountriesWithMoreThan10000HaveBeenConfirmedCases()
globalCumulativeTrend()
globalCumulativeCureMortality()
worldMapNoChina()



setInterval(time, 1000000)
setInterval(worldFourNumber, 1000000)
setInterval(newCasesInTheTop10CountriesWithin24Hours, 1000000)
setInterval(theTop10CountriesGrewFastestInSevenDays, 1000000)
setInterval(foreignCumulativeDiagnosisTop10Countries, 1000000)
setInterval(theNumberOfForeignCountriesWithConfirmedCases, 1000000)
setInterval(overseasCountriesWithMoreThan10000ConfirmedCases, 1000000)
setInterval(overseasCountriesWithMoreThan10000HaveBeenConfirmedCases, 1000000)
setInterval(globalCumulativeTrend, 1000000)
setInterval(globalCumulativeCureMortality, 1000000)
setInterval(worldMapNoChina, 1000000)













