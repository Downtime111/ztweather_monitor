var ec_chinaMap = echarts.init(document.getElementById('chinaMap'), "roma");
var ec_chinaMap_option = {
    title: {
        text: '新型冠状病毒肺炎全国分布图',
        subtext: '点击省份可查看各省内数据',
        left: 'center',
        textStyle: {
            color: '#000',
            fontSize: 22
        },
        subtextStyle: {
            fontSize: 16
        }
    },
    tooltip: {
        formatter: function (params) {
            return params.seriesName + '<br />' + params.name + '：' + params.value
        }
    },
    legend: {
        data: ['今天新增确诊', '当前确诊', '累计确诊', "累计治愈", "累计死亡"],
        left: 20,
        top: 80,
        selected: {'今天新增确诊': false, '当前确诊': false, '累计确诊': true, '累计治愈': false, '累计死亡': false},
        selectedMode: "single",
        textStyle: {
            color: '#000',
            fontSize: 18
        }
    },
    visualMap: {
        show: true,
        x: '50px',
        y: 'bottom',
        textStyle: {
            fontSize: 18,
        },
        splitList: [{start: 0, end: 0},
            {start: 1, end: 9},
            {start: 10, end: 99},
            {start: 100, end: 999},
            {start: 1000, end: 9999},
            {start: 10000}],
        color: ['#70161D', '#CB2A2F', '#E55A4E', '#F59E83', '#FDEBCF', '#DCE2EB']
    },
    series: [{
        name: "今天新增确诊",
        type: 'map',
        roam: false,
        zoom: 1.2,

        mapType: 'china',
        label: {
            normal: {
                show: true,
                fontSize: 14,
            },
            emphasis: {
                show: true,
                fontSize: 14,
            }
        },
        data: []
    }, {
        name: "当前确诊",
        type: 'map',
        roam: false,
        mapType: 'china',
        zoom: 1.2,
        label: {
            normal: {
                show: true,
                fontSize: 14,
            },
            emphasis: {
                show: true,
                fontSize: 14,
            }
        },
        data: []
    }, {
        name: "累计确诊",
        type: 'map',
        roam: false,
        mapType: 'china',
        zoom: 1.2,
        label: {
            normal: {
                show: true,
                fontSize: 14,
            },
            emphasis: {
                show: true,
                fontSize: 14,
            }
        },
        data: []
    }, {
        name: "累计治愈",
        type: 'map',
        mapType: 'china',
        zoom: 1.2,
        roam: false,
        label: {
            normal: {
                show: true,
                fontSize: 14,
            },
            emphasis: {
                show: true,
                fontSize: 14,
            }
        },
        data: []
    }, {
        name: "累计死亡",
        type: 'map',
        mapType: 'china',
        zoom: 1.2,
        roam: false,
        label: {
            normal: {
                show: true,
                fontSize: 14,
            },
            emphasis: {
                show: true,
                fontSize: 14,
            }
        },
        data: []
    }]
};
ec_chinaMap.setOption(ec_chinaMap_option)
var chinaProvinceMap;
function showCity(city) {
    chinaProvinceMap = echarts.init(document.getElementById('chinaProvinceMap'), "roma");
    chinaProvinceMap_option1 = {
        title: {
            text: city + '疫情分布图',
            subtext: '点击提示返回到国家地图',
            left: 'center',
            top: '30',
            textStyle: {
                color: '#000',
                fontSize: 18
            }
        },
        tooltip: {
            formatter: function (params) {
                return params.seriesName + '<br />' + params.name + '：' + params.value
            }
        },
        legend: {
            data: ['今天新增确诊', '当前确诊', '累计确诊', "累计治愈", "累计死亡"],
            left: 40,
            selected: {'今天新增确诊': false, '当前确诊': false, '累计确诊': true, '累计治愈': false, '累计死亡': false},
            selectedMode: "single",
            textStyle: {
                color: '#000',
                fontSize: 18
            }
        },
        visualMap: {
            textStyle: {
                fontSize: 16,
            },
            splitList: [{start: 0, end: 0},
                {start: 1, end: 9},
                {start: 10, end: 99},
                {start: 100, end: 999},
                {start: 1000, end: 9999},
                {start: 10000}],
            color: ['#70161D', '#CB2A2F', '#E55A4E', '#F59E83', '#FDEBCF', '#DCE2EB'],
            left: 'left',
            top: 'bottom',
            show: true
        },
        geo: {
            map: 'city',
            roam: false,
            zoom: 1.23,
            label: {
                normal: {
                    show: true,
                    fontSize: '10',
                    color: 'rgba(0,0,0,0.7)'
                }
            }
        },
        series: [{
            name: "今天新增确诊",
            type: 'map',
            roam: false,
            zoom: 1.2,
            label: {
                normal: {
                    show: true,
                    fontSize: 14,
                },
                emphasis: {
                    show: true,
                    fontSize: 14,
                }
            },
            mapType: city,
            data: []
        }, {
            name: "当前确诊",
            type: 'map',
            roam: false,
            mapType: city,
            zoom: 1.2,
            label: {
                normal: {
                    show: true,
                    fontSize: 14,
                },
                emphasis: {
                    show: true,
                    fontSize: 14,
                }
            },
            data: []
        }, {
            name: "累计确诊",
            type: 'map',
            roam: false,
            mapType: city,
            zoom: 1.2,
            label: {
                normal: {
                    show: true,
                    fontSize: 14,
                },
                emphasis: {
                    show: true,
                    fontSize: 14,
                }
            },
            data: []
        }, {
            name: "累计治愈",
            type: 'map',
            mapType: city,
            zoom: 1.2,
            label: {
                normal: {
                    show: true,
                    fontSize: 14,
                },
                emphasis: {
                    show: true,
                    fontSize: 14,
                }
            },
            roam: false,

            data: []
        }, {
            name: "累计死亡",
            type: 'map',
            mapType: city,
            zoom: 1.2,
            label: {
                normal: {
                    show: true,
                    fontSize: 14,
                },
                emphasis: {
                    show: true,
                    fontSize: 14,
                }
            },
            roam: false,
            data: []
        }]
    };
    $.ajax({
        url: "/chinaProvinceMap",
        success: function (data) {
            chinaProvinceMap_option1.series[0].data = data.confirmToday;
            chinaProvinceMap_option1.series[1].data = data.nowConfirmTotal;
            chinaProvinceMap_option1.series[2].data = data.confirmTotal;
            chinaProvinceMap_option1.series[3].data = data.healTotal;
            chinaProvinceMap_option1.series[4].data = data.deadTotal;
            chinaProvinceMap.setOption(chinaProvinceMap_option1)
        },
        error: function (xhr, type, errorThrown) {

        }
    })
}
var spantest = document.getElementById('test');
spantest.style.display = "none";
ec_chinaMap.on('click', function (param) {
    ec_chinaMap.clear();
    document.getElementById('chinaMap').style.display = "none";
    spantest.style.display = "";
    city = param.name;
    showCity(city)
});
$(function () {
    $('#test').bind("click", function () {
        chinaProvinceMap = echarts.init(document.getElementById('chinaProvinceMap')).clear();
        document.getElementById('chinaMap').style.display = "";
        spantest.style.display = "none";
        $.ajax({
            url: "/chinaMap",
            success: function (data) {
                ec_chinaMap_option.series[0].data = data.confirmToday;
                ec_chinaMap_option.series[1].data = data.nowConfirmTotal;
                ec_chinaMap_option.series[2].data = data.confirmTotal;
                ec_chinaMap_option.series[3].data = data.healTotal;
                ec_chinaMap_option.series[4].data = data.deadTotal;
                ec_chinaMap.setOption(ec_chinaMap_option)
            },
            error: function (xhr, type, errorThrown) {

            }
        })
    });
})


