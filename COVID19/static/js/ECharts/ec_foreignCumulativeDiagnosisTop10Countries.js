var ec_foreignCumulativeDiagnosisTop10Countries = echarts.init(document.getElementById('foreignCumulativeDiagnosisTop10Countries'), "roma");
var ec_foreignCumulativeDiagnosisTop10Countries_Option = {
    title: {
        text: "海外累计确诊人数top10国家的确诊、治愈、死亡",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left'
    },
    legend: {
        data: ['现有确诊', '累计确诊', '累计治愈', '累计死亡'],
        right: 40,
        top: 40,
        orient: 'vertical',
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
        top: 50,
        containLabel: true
    },
    xAxis: [{
        type: 'value',
        splitLine: {
            show: true
        },
        axisLabel: {
            show: true,
            fontSize: 16
        }
    }],
    yAxis: [{
        type: 'category',
        data: [],
        axisLabel: {
            show: true,
            fontSize: 16
        }
    }],
    series: [{
        name: "现有确诊",
        type: 'bar',
        data: [],
        animationDelay: function (idx) {
            return idx * 10 + 100;
        }
    }, {
        name: "累计确诊",
        type: 'bar',
        data: [],
        animationDelay: function (idx) {
            return idx * 10;
        }
    }, {
        name: "累计治愈",
        type: 'bar',
        data: [],
        animationDelay: function (idx) {
            return idx * 10 + 200;
        }
    }, {
        name: "累计死亡",
        type: 'bar',
        data: [],
        animationDelay: function (idx) {
            return idx * 10 + 300;
        }
    }],
    animationEasing: 'elasticOut',
    animationDelayUpdate: function (idx) {
        return idx * 5;
    }
};

ec_foreignCumulativeDiagnosisTop10Countries.setOption(ec_foreignCumulativeDiagnosisTop10Countries_Option)
