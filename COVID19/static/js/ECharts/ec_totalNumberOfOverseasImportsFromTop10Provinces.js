var ec_totalNumberOfOverseasImportsFromTop10Provinces = echarts.init(document.getElementById('totalNumberOfOverseasImportsFromTop10Provinces'), "infographic");
var ec_totalNumberOfOverseasImportsFromTop10Provinces_Option = {
    title: {
        text: "累计境外输入top10省份(南丁格尔玫瑰图)",
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
        top: '30%',
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
        center: ['50%', '50%'],
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
                        "#a71a4f", "#c71b1b", "#ce4018", "#e7741b", "#da9c2d", "#bbd337", "#67b52d", "#48af54", "#48a698", "#57868c"
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

ec_totalNumberOfOverseasImportsFromTop10Provinces.setOption(ec_totalNumberOfOverseasImportsFromTop10Provinces_Option)
