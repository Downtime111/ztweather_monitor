var ec_cumulativeNumberOfConfirmedCasesInAllProvinces = echarts.init(document.getElementById('cumulativeNumberOfConfirmedCasesInAllProvinces'), "infographic");
var ec_cumulativeNumberOfConfirmedCasesInAllProvinces_Option = {
    title: {
        text: "各省份级累计确诊(南丁格尔玫瑰图)",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left'
    },
    legend: {
        data: [],
        orient: 'vertical',
        right: 0,
        top: '10%',
        textStyle: {
            color: '#000',
            fontSize: 16
        }
    },
    toolbox: {
        show: true,
        feature: {
            saveAsImage: {}
        }
    },
    tooltip: {
        trigger: 'item',
        formatter: '{b} : {c} ({d}%)'
    },
    grid: {
        bottom: '8%',
        top: 50,
        containLabel: true
    },
    series: [{
        type: 'pie',
        radius: [5, '75%'],
        center: ['40%', '50%'],
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
                        '#cf208f', '#ea257e', '#eb2462', '#ee3131',
                        '#f1562f', "#e7741b", '#f67932', '#f89230',
                        '#e2a924', '#faeb23', '#e8e517', '#c9db33',
                        '#9fcb3d', '#6bbe45', "#67b52d", "#53b440",
                        '#37b64b', '#3db979', '#11adcf', '#1f9bca',
                        '#1d8fc6', "#48a698", "#57868c", "#57868c",
                        '#2d6da4', '#26539e', '#2a3780', '#423787',
                        '#69398d', '#7d3a93', '#913986', "#a71a4f",
                        "#bc1540", "#c71b1b"
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

ec_cumulativeNumberOfConfirmedCasesInAllProvinces.setOption(ec_cumulativeNumberOfConfirmedCasesInAllProvinces_Option)
