var ec_globalCumulativeTrend = echarts.init(document.getElementById('globalCumulativeTrend'), "walden");
var ec_globalCumulativeTrend_Option = {
    title: {
        text: "全球累计趋势(数据误差较大)",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left',
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            crossStyle: {
                color: '#999'
            }
        }
    },
    toolbox: {
        show: true,
        feature: {
            magicType: {type: ['line', 'bar']},
            restore: {},
            saveAsImage: {}
        }
    },
    legend: {
        data: ['现有确诊', '累计治愈', '累计死亡', '当日新增确诊'],
        left: "right",
        top: 30,
        textStyle: {
            color: '#000',
            fontSize: 16
        }
    },
    dataZoom: [{
        type: 'inside',
        start: 0,
        end: 100
    }, {
        start: 0,
        end: 100,
        handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
        handleSize: '80%',
        handleStyle: {
            color: '#fff',
            shadowBlur: 3,
            shadowColor: 'rgba(0, 0, 0, 0.6)',
            shadowOffsetX: 2,
            shadowOffsetY: 2
        }
    }],
    grid: {
        left: '4%',
        right: '6%',
        bottom: '8%',
        top: 100,
        containLabel: true
    },
    xAxis: [{
        type: 'category',
        data: []
    }],
    yAxis: [{
        type: 'value',
        axisLabel: {
            show: true,
            color: 'black',
            fontSize: 16,
            formatter: function (value) {
                if (value >= 1000) {
                    value = value / 1000 + 'k';
                }
                return value;
            }
        },
        axisLine: {
            show: true
        },
        splitLine: {
            show: true,
            lineStyle: {
                color: '#D8D8D8',
                width: 1,
                type: 'solid',
            }
        }
    }],
    series: [{
        name: "现有确诊",
        type: 'line',
        smooth: true,
        showAllSymbol: false,
        data: []
    }, {
        name: "累计治愈",
        type: 'line',
        smooth: true,
        showAllSymbol: false,
        data: []
    }, {
        name: "累计死亡",
        type: 'line',
        smooth: true,
        showAllSymbol: false,
        data: []
    }, {
        name: "当日新增确诊",
        type: 'line',
        smooth: true,
        showAllSymbol: false,
        data: []
    }]
};

ec_globalCumulativeTrend.setOption(ec_globalCumulativeTrend_Option)
