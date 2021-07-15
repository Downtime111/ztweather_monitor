var ec_newCasesInTheTop10CountriesWithin24Hours = echarts.init(document.getElementById('newCasesInTheTop10CountriesWithin24Hours'), "infographic");
var ec_newCasesInTheTop10CountriesWithin24Hours_Option = {
    title: {
        text: "24小时内新增确诊病例top10国家",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left'
    },
    legend: {
        data: [],
        right: 0,
        orient: 'vertical',
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
        radius: '65%',
        center: ['50%', '50%'],
        selectedMode: 'single',
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
                        "#a71a4f", "#c71b1b", "#ce4018", "#e7741b", "#da9c2d", "#bbd337", "#67b52d", "#48af54", "#48a698", "#57868c"
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

ec_newCasesInTheTop10CountriesWithin24Hours.setOption(ec_newCasesInTheTop10CountriesWithin24Hours_Option)
