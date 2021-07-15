var ec_eachProvinceComparesYesterdayData = echarts.init(document.getElementById('eachProvinceComparesYesterdayData'), "westeros");
var ec_eachProvinceComparesYesterdayData_Option = {
    title: {
        text: "各省份较昨日趋势(按照连续无新增确诊天数排序)",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left'
    },
    legend: {
        data: ["较昨日现有确诊", "较昨日新增确诊", "较昨日新增治愈", "较昨日新增死亡", "连续无确诊天数"],
        left: 'center',
        top: 40,
        textStyle: {
            color: '#000',
            fontSize: 16
        }
    },
    toolbox: {
        show: true,
        feature: {
            magicType: {type: ['line', 'bar', 'stack']},
            restore: {},
            saveAsImage: {}
        }
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
        top: 120,
        containLabel: true
    },
    xAxis: [{
        type: 'category',
        splitLine: {
            show: true
        },
        data: [],
        axisLabel: {
            show: true,
            fontSize: 16
        }
    }],
    yAxis: [{
        type: 'value',
        name: '人',
        axisLabel: {
            show: true,
            fontSize: 16
        }
    }, {
        type: 'value',
        name: '天',
        axisLabel: {
            show: true,
            fontSize: 16
        }

    }],
    series: [{
        name: "较昨日现有确诊",
        type: 'bar',
        data: []
    }, {
        name: "较昨日新增确诊",
        type: 'bar',
        data: []
    }, {
        name: "较昨日新增治愈",
        type: 'bar',
        data: []
    }, {
        name: "较昨日新增死亡",
        type: 'bar',
        data: []
    }, {
        name: "连续无确诊天数",
        type: 'line',
        yAxisIndex: 1,
        data: []
    }]
};

ec_eachProvinceComparesYesterdayData.setOption(ec_eachProvinceComparesYesterdayData_Option)
