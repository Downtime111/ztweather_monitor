var ec_overseasCountriesWithMoreThan10000ConfirmedCases = echarts.init(document.getElementById('overseasCountriesWithMoreThan10000ConfirmedCases'), "infographic");
var ec_overseasCountriesWithMoreThan10000ConfirmedCases_Option = {
    title: {
        text: "海外累计确诊超过10000的国家(南丁格尔玫瑰图)",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left'
    },
    legend: {
        data: [],
        orient: 'vertical',
        right: 10,
        top: '25%',
        textStyle: {
            color: '#000',
            fontSize: 16
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b} : {c} ({d}%)'
    },
    toolbox: {
        show: true,
        feature: {
            saveAsImage: {}
        }
    },
    grid: {
        left: '4%',
        right: '6%',
        bottom: '8%',
        top: 50,
        containLabel: true
    },
    series: [{
        type: 'pie',
        radius: [5, '80%'],
        center: ['45%', '50%'],
        selectedMode: 'single',
        roseType: 'area',
        data: [],
        label: {
            show: true,
            fontSize: 16
        },
        itemStyle: {
            normal: {
                color: function (params) {
                    var colorList = [
                        "#a71a4f", "#bc1540", "#c71b1b", "#d93824", "#ce4018", "#d15122", "#e7741b", "#e58b3d", "#e59524", "#dc9e31", "#da9c2d", "#d2b130", "#bbd337", "#8cc13f", "#67b52d", "#53b440", "#48af54", "#479c7f", "#48a698", "#57868c"
                    ];
                    return colorList[params.dataIndex]
                },
            },
        },
        emphasis: {
            itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
        }
    }
    ]
};

ec_overseasCountriesWithMoreThan10000ConfirmedCases.setOption(ec_overseasCountriesWithMoreThan10000ConfirmedCases_Option)
