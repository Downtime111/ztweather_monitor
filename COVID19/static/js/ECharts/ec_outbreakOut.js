var ec_outbreakOut = echarts.init(document.getElementById('outbreakOut'), "macarons");
var ec_outbreakOut_option = {
    title: {
        text: "今日疫情热搜",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left'
    },
    tooltip: {
        show: false
    },
    grid: {
        left: '4%',
        right: '6%',
        bottom: '8%',
        top: 50,
        containLabel: true
    },
    series: [{
        type: 'wordCloud',
        gridSize: 1,
        sizeRange: [30, 80],
        rotationRange: [-45, 0, 45, 90],
        textStyle: {
            normal: {
                color: function () {
                    return 'rgb(' +
                        Math.round(Math.random() * 255) +
                        ', ' + Math.round(Math.random() * 255) +
                        ', ' + Math.round(Math.random() * 255) + ')'
                }
            }
        },
        right: null,
        bottom: null,
        data: []
    }]
}

ec_outbreakOut.setOption(ec_outbreakOut_option);
