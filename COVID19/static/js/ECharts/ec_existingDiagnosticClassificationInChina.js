var ec_existingDiagnosticClassificationInChina = echarts.init(document.getElementById('existingDiagnosticClassificationInChina'), "roma");
var ec_existingDiagnosticClassificationInChina_Option = {
    title: {
        text: "我国现存确诊分布",
        textStyle: {
            color: 'black',
            fontSize: '22'
        },
        left: 'left'
    },
    legend: {
        data: ['港澳台现存确诊', '境外输入现存确诊', '31省本土现有确诊'],
        right: 40,
        top: 50,
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
        label: {
            show: true,
            fontSize: 16
        }
    }
    ]
};

ec_existingDiagnosticClassificationInChina.setOption(ec_existingDiagnosticClassificationInChina_Option)
