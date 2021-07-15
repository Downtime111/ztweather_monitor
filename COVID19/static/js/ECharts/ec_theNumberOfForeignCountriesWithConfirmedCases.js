var ec_theNumberOfForeignCountriesWithConfirmedCases = echarts.init(document.getElementById('theNumberOfForeignCountriesWithConfirmedCases'), "infographic");
var ec_theNumberOfForeignCountriesWithConfirmedCases_Option = {
    title: {
        text: "海外现有确诊病例的各洲国家数量",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left'
    },
    legend: {
        data: [],
        right: 0,
        top: '25%',
        orient: 'vertical',
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
        radius: '65%',
        center: ['50%', '50%'],
        selectedMode: 'single',
        roseType: 'area',
        data: [],
        emphasis: {
            itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
        },
        itemStyle: {
            normal: {
                color: function (params) {
                    var colorList = [
                        "#a71a4f", "#d93824", "#dc9e31", "#bbd337", "#53b440", "#48a698", "#57868c"
                    ];
                    return colorList[params.dataIndex]
                },
            },
        },
        label: {
            show: true,
            fontSize: 16
        }
    }
    ]
};

ec_theNumberOfForeignCountriesWithConfirmedCases.setOption(ec_theNumberOfForeignCountriesWithConfirmedCases_Option)
