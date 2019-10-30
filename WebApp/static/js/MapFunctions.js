//设置循环，一直获取送来的refresh data
setInterval(function () {

    var melData = JSON.parse(get('http://45.113.234.34:80/refreshMel'));
    var sydData = JSON.parse(get('http://45.113.234.34:80/refreshSyd'));
    var adeData = JSON.parse(get('http://45.113.234.34:80/refreshAde'));
    var briData = JSON.parse(get('http://45.113.234.34:80/refreshBri'));
    var cbdData = JSON.parse(get('http://45.113.234.34:80/refreshCbd'));
    var preData = JSON.parse(get('http://45.113.234.34:80/refreshPre'));
    var donData = JSON.parse(get('http://45.113.234.34:80/refreshDon'));
    var SYData = JSON.parse(get('http://45.113.234.34:80/refreshSY'));

    // var melData = JSON.parse(get('http://127.0.0.1:5000/refreshMel'));
    // var sydData = JSON.parse(get('http://127.0.0.1:5000/refreshSyd'));
    // var adeData = JSON.parse(get('http://127.0.0.1:5000/refreshAde'));
    // var briData = JSON.parse(get('http://127.0.0.1:5000/refreshBri'));
    // var cbdData = JSON.parse(get('http://127.0.0.1:5000/refreshCbd'));
    // var preData = JSON.parse(get('http://127.0.0.1:5000/refreshPre'));
    // var donData = JSON.parse(get('http://127.0.0.1:5000/refreshDon'));
    // var SYData = JSON.parse(get('http://127.0.0.1:5000/refreshSY'));

    // var melData = JSON.parse(get('http://10.13.216.93:80/refreshMel'));
    // var sydData = JSON.parse(get('http://10.13.216.93:80/refreshSyd'));
    // var adeData = JSON.parse(get('http://10.13.216.93:80/refreshAde'));
    // var briData = JSON.parse(get('http://10.13.216.93:80/refreshBri'));
    // var cbdData = JSON.parse(get('http://10.13.216.93:80/refreshCbd'));
    // var preData = JSON.parse(get('http://10.13.216.93:80/refreshPre'));
    // var donData = JSON.parse(get('http://10.13.216.93:80/refreshDon'));
    // var SYData = JSON.parse(get('http://10.13.216.93:80/refreshSY'));



//地图更新功能 循环更新数据
    update_map(melData, sydData, adeData, briData);
    update_suburb(cbdData, preData, donData, SYData);

}, 20000);

//获取数据库静态各地区数据数据
var melHistoryData = JSON.parse(get('http://admin:project@45.113.234.34:5984/historytopics/80b3c10321e80413900f1e0a740e5b3b'));
var melHistoryHotTopic = $('#melHistoryHotTopic').text("1." + melHistoryData.topics[0] + '\n' + "2." + melHistoryData.topics[1] + '\n' + "3." + melHistoryData.topics[2] + '\n' + "4." + melHistoryData.topics[3] + '\n' + "5." + melHistoryData.topics[4]);
melHistoryHotTopic.html(melHistoryHotTopic.html().replace(/\n/g, '<br/>'));

var sydHistoryData = JSON.parse(get('http://admin:project@45.113.234.34:5984/historytopics/80b3c10321e80413900f1e0a740e44e5'));
var sydHistoryHotTopic = $('#sydHistoryHotTopic').text("1." + sydHistoryData.topics[0] + '\n' + "2." + sydHistoryData.topics[1] + '\n' + "3." + sydHistoryData.topics[2] + '\n' + "4." + sydHistoryData.topics[3] + '\n' + "5." + sydHistoryData.topics[4]);
sydHistoryHotTopic.html(sydHistoryHotTopic.html().replace(/\n/g, '<br/>'));

var adeHistoryData = JSON.parse(get('http://admin:project@45.113.234.34:5984/historytopics/80b3c10321e80413900f1e0a740d16a7'));
var adeHistoryHotTopic = $('#adeHistoryHotTopic').text("1." + adeHistoryData.topics[0] + '\n' + "2." + adeHistoryData.topics[1] + '\n' + "3." + adeHistoryData.topics[2] + '\n' + "4." + adeHistoryData.topics[3] + '\n' + "5." + adeHistoryData.topics[4]);
adeHistoryHotTopic.html(adeHistoryHotTopic.html().replace(/\n/g, '<br/>'));

var briHistoryData = JSON.parse(get('http://admin:project@45.113.234.34:5984/historytopics/80b3c10321e80413900f1e0a740e1917'));
var briHistoryHotTopic = $('#briHistoryHotTopic').text("1." + briHistoryData.topics[0] + '\n' + "2." + briHistoryData.topics[1] + '\n' + "3." + briHistoryData.topics[2] + '\n' + "4." + briHistoryData.topics[3] + '\n' + "5." + briHistoryData.topics[4]);
briHistoryHotTopic.html(briHistoryHotTopic.html().replace(/\n/g, '<br/>'));

var cbdHistoryData = JSON.parse(get('http://admin:project@45.113.234.34:5984/historytopics/80b3c10321e80413900f1e0a740e4d7e'));
var cbdHistoryHotTopic = $('#cbdHistoryHotTopic').text("1." + cbdHistoryData.topics[0] + '\n' + "2." + cbdHistoryData.topics[1] + '\n' + "3." + cbdHistoryData.topics[2] + '\n' + "4." + cbdHistoryData.topics[3] + '\n' + "5." + cbdHistoryData.topics[4]);
cbdHistoryHotTopic.html(cbdHistoryHotTopic.html().replace(/\n/g, '<br/>'));

var preHistoryData = JSON.parse(get('http://admin:project@45.113.234.34:5984/historytopics/80b3c10321e80413900f1e0a740e2971'));
var preHistoryHotTopic = $('#preHistoryHotTopic').text("1." + preHistoryData.topics[0] + '\n' + "2." + preHistoryData.topics[1] + '\n' + "3." + preHistoryData.topics[2] + '\n' + "4." + preHistoryData.topics[3] + '\n' + "5." + preHistoryData.topics[4]);
preHistoryHotTopic.html(preHistoryHotTopic.html().replace(/\n/g, '<br/>'));

var donHistoryData = JSON.parse(get('http://admin:project@45.113.234.34:5984/historytopics/80b3c10321e80413900f1e0a7409a325'));
var donHistoryHotTopic = $('#donHistoryHotTopic').text("1." + donHistoryData.topics[0] + '\n' + "2." + donHistoryData.topics[1] + '\n' + "3." + donHistoryData.topics[2] + '\n' + "4." + donHistoryData.topics[3] + '\n' + "5." + donHistoryData.topics[4]);
donHistoryHotTopic.html(donHistoryHotTopic.html().replace(/\n/g, '<br/>'));

var SYHistoryData = JSON.parse(get('http://admin:project@45.113.234.34:5984/historytopics/80b3c10321e80413900f1e0a740e460c'));
var SYHistoryHotTopic = $('#SYHistoryHotTopic').text("1." + SYHistoryData.topics[0] + '\n' + "2." + SYHistoryData.topics[1] + '\n' + "3." + SYHistoryData.topics[2] + '\n' + "4." + SYHistoryData.topics[3] + '\n' + "5." + SYHistoryData.topics[4]);
SYHistoryHotTopic.html(SYHistoryHotTopic.html().replace(/\n/g, '<br/>'));

//初始化所有动态数据
var melSentiment = [0],
    sydSentiment = [0],
    adeSentiment = [0],
    briSentiment = [0],
    cbdSentiment = [0],
    preSentiment = [0],
    donSentiment = [0],
    SYSentiment = [0];

//初始化三张地图
var myMap = echarts.init(document.getElementById("sentimentMap"));
var myMelSuburb = echarts.init(document.getElementById("sentimentSuburb"));
var myAuHistory = echarts.init(document.getElementById("sentimentAuHistory"));


//第一个map 分割线-------------------------------------------------------------
$.getJSON('/static/json/australia.json', function (auJson) {
    //加载json并渲染
    echarts.registerMap('AU', auJson, {});
    //初始化的Option
    let initOption = {
        //上面的标题
        title: {
            text: 'Australia sentiment real-time',
            left: 'center',
            subtext: 'GeoData from Github, click to view',
            sublink: 'https://github.com/codeforamerica/click_that_hood/blob/master/public/data/australia.geojson'
        },
        //鼠标停留的悬浮窗
        tooltip: {
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2,
            formatter: function (params) {
                console.log(params, params.length);
                return params.seriesName + '<br/>' + params.name + ': ' + params.value;
            }
        },
        //右边的图表栏
        visualMap: {
            left: 'right',
            min: -0.5,
            max: 0.5,
            inRange: {
                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
            },
            text: ['Happy', 'Sad'], // 文本，默认为数值文本
            calculable: true
        },
        //工具栏
        toolbox: {
            show: true,
            //orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
                dataView: {
                    readOnly: false
                },
                restore: {},
                saveAsImage: {}
            }
        },
        //地图数据
        series: [
            {
                name: 'RealSentimentMap',
                type: 'map',
                roam: false,
                aspectScale: 0.85,  //地图长度比
                mapType: 'AU',
                data: [
                    {name: 'Victoria', value: []},
                    {name: 'New South Wales', value: []},
                    {name: 'Queensland', value: []},
                    {name: 'South Australia', value: []}
                ]
            }
        ]
    };
    myMap.setOption(initOption);
});

//第二个map 分割线-------------------------------------------------------------
$.getJSON('/static/json/melbourne.json', function (melJson) {
    echarts.registerMap('MEL', melJson, {});
    let initOption = {
        //上面的标题
        title: {
            text: 'Melbourne Suburb sentiment real-time',
            left: 'center',
            subtext: 'GeoData from Github, click to view',
            sublink: 'https://github.com/codeforamerica/click_that_hood/blob/master/public/data/melbourne.geojson'
        },
        tooltip: {
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2,
            formatter: function (params) {
                console.log(params, params.length);
                return params.seriesName + '<br/>' + params.name + ': ' + params.value;
            }
        },
        //右边的图表栏
        visualMap: {
            min: -0.5,
            max: 0.5,
            splitNumber: 5,
            color: ['#d94e5d', '#eac736', '#50a3ba'],
            text: ['Happy', 'sad'],
            textStyle: {
                color: '#000000'
            }
        },
        toolbox: {
            show: true,
            //orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
                dataView: {
                    readOnly: false
                },
                restore: {},
                saveAsImage: {}
            }
        },
        series: [
            {
                name: 'RealSentimentSuburb',
                type: 'map',
                roam: false,
                aspectScale: 0.85,  //地图长度比
                mapType: 'MEL',
                data: [
                    {name: 'Melbourne (3000)', value: []},
                    {name: 'Preston', value: []},
                    {name: 'Camberwell', value: []},
                    {name: 'South Yarra', value: []}
                ]
            }
        ]
    };
    myMelSuburb.setOption(initOption);
});

//第一个update 分割线-------------------------------------------------------------
function update_map(melData, sydData, adeData, briData) {
    // 隐藏加载动画
    myMap.hideLoading();

    // 准备数据
    melSentiment.push(parseFloat(melData.webSentiment));
    sydSentiment.push(parseFloat(sydData.webSentiment));
    adeSentiment.push(parseFloat(adeData.webSentiment));
    briSentiment.push(parseFloat(briData.webSentiment));
    if(melSentiment.length >= 2){
        melSentiment.shift();
    }
    if(sydSentiment.length >= 2){
        sydSentiment.shift();
    }
    if(adeSentiment.length >= 2){
        adeSentiment.shift();
    }
    if(briSentiment.length >= 2){
        briSentiment.shift();
    }
    //新的数据放进来
    let updateMapOption = {
        series: [
            {
                name: 'RealSentimentMap',
                type: 'map',
                roam: false,
                aspectScale: 0.85,  //地图长度比
                mapType: 'AU',
                data: [
                    {name: 'Victoria', value: melSentiment},
                    {name: 'New South Wales', value: sydSentiment},
                    {name: 'Queensland', value: adeSentiment},
                    {name: 'South Australia', value: briSentiment}
                ]
            }
        ]
    };
    // 填入数据
    myMap.setOption(updateMapOption);
}

//第二个update 分割线-------------------------------------------------------------
function update_suburb(cbdData, preData, donData, SYData) {
    //res是json格式的response对象

    // 隐藏加载动画
    myMelSuburb.hideLoading();

    // 准备数据
    cbdSentiment.push(parseFloat(cbdData.webSentiment));
    preSentiment.push(parseFloat(preData.webSentiment));
    donSentiment.push(parseFloat(donData.webSentiment));
    SYSentiment.push(parseFloat(SYData.webSentiment));
    if(cbdSentiment.length >= 2){
        cbdSentiment.shift();
    }
    if(preSentiment.length >= 2){
        preSentiment.shift();
    }
    if(donSentiment.length >= 2){
        donSentiment.shift();
    }
    if(SYSentiment.length >= 2){
        SYSentiment.shift();
    }

    let updateMapOption = {
        series: [
            {
                name: 'RealSentimentSuburb',
                type: 'map',
                roam: false,
                aspectScale: 0.85,  //地图长度比
                mapType: 'MEL',
                data: [
                    {name: 'Melbourne (3000)', value: cbdSentiment},
                    {name: 'Preston', value: preSentiment},
                    {name: 'Camberwell', value: donSentiment},
                    {name: 'South Yarra', value: SYSentiment}
                ]
            }
        ]
    };
    // 填入数据
    myMelSuburb.setOption(updateMapOption);
}

//第三个map 分割线-------------------------------------------------------------
$.get('static/json/australia.json', function (auJson) {
    echarts.registerMap('AU', auJson, {});
    //散点数据
    var sanData = [
        {
            name: 'Melbourne',
            value: melHistoryData.avgsentiment
        },
        {
            name: 'Sydney',
            value: sydHistoryData.avgsentiment
        },
        {
            name: 'Adelaide',
            value: adeHistoryData.avgsentiment
        },
        {
            name: 'Brisbane',
            value: briHistoryData.avgsentiment
        },
        {
            name: 'CBD',
            value: cbdHistoryData.avgsentiment
        },
        {
            name: 'Preston',
            value: preHistoryData.avgsentiment
        },
        {
            name: 'Camberwell',
            value: donHistoryData.avgsentiment
        },
        {
            name: 'SouthYarra',
            value: SYHistoryData.avgsentiment
        }
    ];
    //散点坐标
    var geoCoordMap = {
        'Melbourne': [144.962536, -37.812099],
        'Sydney': [151.211582, -33.861185],
        'Adelaide': [138.599946, -34.928190],
        'Brisbane': [153.025020, -27.469802],
        'CBD': [144.962311, -37.812225],
        'Preston': [145.007579, -37.740897],
        'Camberwell': [145.070753, -37.837942],
        'SouthYarra': [144.992181, -37.839043]
    };
    //处理数据函数
    var convertData = function (data) {
        var res = [];
        for (var i = 0; i < data.length; i++) {
            var geoCoord = geoCoordMap[data[i].name];
            if (geoCoord) {
                res.push({
                    name: data[i].name,
                    value: geoCoord.concat(data[i].value)
                });
            }
        }
        return res;
    };
    //地图初始化
    let initOption = {
        backgroundColor: '#404a59',
        title: {
            text: 'Austuria 2019 History Sentiment',
            left: 'center',
            subtext: 'GeoData from Github, click to view',
            sublink: 'https://github.com/codeforamerica/click_that_hood/blob/master/public/data/australia.geojson',
            textStyle: {
                color: '#fff'
            }
        },
        tooltip: {
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2,
            formatter: function (params) {
                console.log(params, params.length);
                return '2019 Sentiment: ' + '<br/>' + params.value[2];
            }
        },
        toolbox: {
            show: true,
            //orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
                dataView: {
                    readOnly: false
                },
                saveAsImage: {}
            }
        },
        geo: {
            show: true,
            map: 'AU',
            roam: true,
            label: {
                normal: {
                    show: false
                },
                emphasis: {
                    show: false
                }
            },
            itemStyle: {
                normal: {
                    areaColor: '#323c48',
                    borderColor: '#111'
                },
                emphasis: {
                    areaColor: '#2a333d'
                }
            }
        },
        series: [
            { //散点配置
                name: 'Sentiment',
                type: 'effectScatter',
                coordinateSystem: 'geo',
                data: convertData(sanData),
                symbolSize: function (val) {
                    return val[2] * 40;
                },
                showEffectOn: 'render',
                rippleEffect: {
                    brushType: 'stroke'
                },
                hoverAnimation: true,
                label: {
                    normal: {
                        formatter: '{b}',
                        position: 'right',
                        show: false
                    },
                    emphasis: {
                        show: true
                    }
                },
                itemStyle: {
                    normal: {
                        color: 'yellow',
                        shadowBlur: 10,
                        shadowColor: '#333'
                    }
                }
            },
            { //地图配置
                name: 'HistorySentiment',
                type: 'map',
                roam: true,
                mapType: 'AU',
                geoIndex: 0,
                //长宽比
                aspectScale: 0.85,
                itemStyle: {
                    normal: {
                        label: {
                            show: true
                        }
                    },
                    emphasis: {
                        label: {
                            show: true
                        }
                    }
                },
                label: {
                    normal: {
                        show: false
                    },
                    emphasis: {
                        show: false
                    }
                },
                itemStyle: {
                    emphasis: {
                        borderColor: '#ffff',
                        borderWidth: 1
                    }
                }
            }
        ]
    };
    myAuHistory.setOption(initOption);
});


myMap.showLoading();
myMelSuburb.showLoading();

//把url转json
function get(yourUrl) {
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET", yourUrl, false);
    Httpreq.send(null);
    return Httpreq.responseText;
}
