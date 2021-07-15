var ec_currentConfirmedDataInAllProvinces = echarts.init(document.getElementById('currentConfirmedDataInAllProvinces'), "roma");
var ec_currentConfirmedDataInAllProvinces_Option = {
    title: {
        text: "各省现有确诊、新增确诊、现有疑似(按现有确诊排)",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left'
    },
    legend: {
        data: ["现有确诊", "新增确诊", "现有疑似"],
        right: 50,
        top: 40,
        textStyle: {
            color: '#000',
            fontSize: 16
        }
    },
    toolbox: {
        show: true,
        feature: {
            magicType: {type: ['stack']},
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
        top: 80,
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
    }],
    series: [{
        name: "现有确诊",
        type: 'bar',
        data: []
    }, {
        name: "新增确诊",
        type: 'bar',
        data: []
    }, {
        name: "现有疑似",
        type: 'bar',
        data: []
    }]
};

ec_currentConfirmedDataInAllProvinces.setOption(ec_currentConfirmedDataInAllProvinces_Option)
