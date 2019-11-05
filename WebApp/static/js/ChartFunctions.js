//这是世界的根源 所有动态消息都在这里拿
setInterval(function () {

    //取所有的json数据
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


    //热门话题显示到网页
    update_mel(melData);
    var melHT = $('#melHotTopic').text("Here are the Hot Topics of Melbourne:" + '\n' + "1." + melData.webTopic[0] + '\n' + "2." + melData.webTopic[1] + '\n' + "3." + melData.webTopic[2] + '\n' + "4." + melData.webTopic[3] + '\n' + "5." + melData.webTopic[4]);
    melHT.html(melHT.html().replace(/\n/g, '<br/>'));

    update_syd(sydData);
    var sydHT = $('#sydHotTopic').text("Here are the Hot Topics of Sydney:" + '\n' + "1." + sydData.webTopic[0] + '\n' + "2." + sydData.webTopic[1] + '\n' + "3." + sydData.webTopic[2] + '\n' + "4." + sydData.webTopic[3] + '\n' + "5." + sydData.webTopic[4]);
    sydHT.html(sydHT.html().replace(/\n/g, '<br/>'));

    update_ade(adeData);
    var adeHT = $('#adeHotTopic').text("Here are the Hot Topics of Adelaide:" + '\n' + "1." + adeData.webTopic[0] + '\n' + "2." + adeData.webTopic[1] + '\n' + "3." + adeData.webTopic[2] + '\n' + "4." + adeData.webTopic[3] + '\n' + "5." + adeData.webTopic[4]);
    adeHT.html(adeHT.html().replace(/\n/g, '<br/>'));

    update_bri(briData);
    var briHT = $('#briHotTopic').text("Here are the Hot Topics of Brisbane:" + '\n' + "1." + briData.webTopic[0] + '\n' + "2." + briData.webTopic[1] + '\n' + "3." + briData.webTopic[2] + '\n' + "4." + briData.webTopic[3] + '\n' + "5." + briData.webTopic[4]);
    briHT.html(briHT.html().replace(/\n/g, '<br/>'));

    update_cbd(cbdData);
    var cbdHT = $('#cbdHotTopic').text("Here are the Hot Topics of CBD:" + '\n' + "1." + cbdData.webTopic[0] + '\n' + "2." + cbdData.webTopic[1] + '\n' + "3." + cbdData.webTopic[2] + '\n' + "4." + cbdData.webTopic[3] + '\n' + "5." + cbdData.webTopic[4]);
    cbdHT.html(cbdHT.html().replace(/\n/g, '<br/>'));

    update_pre(preData);
    var preHT = $('#preHotTopic').text("Here are the Hot Topics of Perston:" + '\n' + "1." + preData.webTopic[0] + '\n' + "2." + preData.webTopic[1] + '\n' + "3." + preData.webTopic[2] + '\n' + "4." + preData.webTopic[3] + '\n' + "5." + preData.webTopic[4]);
    preHT.html(preHT.html().replace(/\n/g, '<br/>'));

    update_don(donData);
    var donHT = $('#donHotTopic').text("Here are the Hot Topics of Camberwell:" + '\n' + "1." + donData.webTopic[0] + '\n' + "2." + donData.webTopic[1] + '\n' + "3." + donData.webTopic[2] + '\n' + "4." + donData.webTopic[3] + '\n' + "5." + donData.webTopic[4]);
    donHT.html(donHT.html().replace(/\n/g, '<br/>'));

    update_SY(SYData);
    var SYHT = $('#SYHotTopic').text("Here are the Hot Topics of SouthYarra:" + '\n' + "1." + SYData.webTopic[0] + '\n' + "2." + SYData.webTopic[1] + '\n' + "3." + SYData.webTopic[2] + '\n' + "4." + SYData.webTopic[3] + '\n' + "5." + SYData.webTopic[4]);
    SYHT.html(SYHT.html().replace(/\n/g, '<br/>'));

}, 20000);

//初始化数据
var melTime = ["", "", "", "", "", "", "", "", "", ""],
    sydTime = ["", "", "", "", "", "", "", "", "", ""],
    adeTime = ["", "", "", "", "", "", "", "", "", ""],
    briTime = ["", "", "", "", "", "", "", "", "", ""],
    cbdTime = ["", "", "", "", "", "", "", "", "", ""],
    preTime = ["", "", "", "", "", "", "", "", "", ""],
    donTime = ["", "", "", "", "", "", "", "", "", ""],
    SYTime = ["", "", "", "", "", "", "", "", "", ""],
    melSentiment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    sydSentiment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    adeSentiment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    briSentiment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    cbdSentiment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    preSentiment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    donSentiment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    SYSentiment = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

//新生成图表
var myMelChart = echarts.init(document.getElementById('mel'));
var mySydChart = echarts.init(document.getElementById('syd'));
var myAdeChart = echarts.init(document.getElementById('ade'));
var myBriChart = echarts.init(document.getElementById('bri'));
var myCbdChart = echarts.init(document.getElementById('cbd'));
var myPreChart = echarts.init(document.getElementById('pre'));
var myDonChart = echarts.init(document.getElementById('don'));
var mySYChart = echarts.init(document.getElementById('SY'));

//初始化图表们----------------------------------------------------
melOption = {
    title: {
        text: 'mel emotion analysis'
    },
    tooltip: {},
    legend: {
        //对应着下面的series
        data: ['emotion','2019History']
    },
    xAxis: {
        name: 'Time',
        splitNumber: 10,
        data: []
    },
    yAxis: {
        name: 'Sentiment',
        type: 'value',
        scale: true,
        splitNumber: 10,
        max: 0.5,
        min: -0.5
    },
    series: [{
        name: 'emotion',
        type: 'line',
        data: []
    },{
            name:'2019History',
            type:'line',
            data:[0.18047673525581479,0.18047673525581479,0.18047673525581479,0.18047673525581479,0.18047673525581479,0.18047673525581479,0.18047673525581479,0.18047673525581479,0.18047673525581479,0.18047673525581479]
        }]
};

sydOption = {
    title: {
        text: 'syd emotion analysis'
    },
    tooltip: {},
    legend: {
        data: ['emotion','2019History']
    },
    xAxis: {
        name: 'Time',
        splitNumber: 10,
        data: []
    },
    yAxis: {
        name: 'Sentiment',
        type: 'value',
        scale: true,
        splitNumber: 10,
        max: 0.5,
        min: -0.5
    },
    series: [{
        name: 'emotion',
        type: 'line',
        data: []
    },{
            name:'2019History',
            type:'line',
            data:[0.21966074238856798,0.21966074238856798,0.21966074238856798,0.21966074238856798,0.21966074238856798,0.21966074238856798,0.21966074238856798,0.21966074238856798,0.21966074238856798,0.21966074238856798]
        }]
};

adeOption = {
    title: {
        text: 'ade emotion analysis'
    },
    tooltip: {},
    legend: {
        data: ['emotion','2019History']
    },
    xAxis: {
        name: 'Time',
        splitNumber: 10,
        data: []
    },
    yAxis: {
        name: 'Sentiment',
        type: 'value',
        splitNumber: 10,
        max: 0.5,
        min: -0.5
    },
    series: [{
        name: 'emotion',
        type: 'line',
        data: []
    },{
            name:'2019History',
            type:'line',
            data:[0.2678828602431957,0.2678828602431957,0.2678828602431957,0.2678828602431957,0.2678828602431957,0.2678828602431957,0.2678828602431957,0.2678828602431957,0.2678828602431957,0.2678828602431957]
        }]
};

briOption = {
    title: {
        text: 'bri emotion analysis'
    },
    tooltip: {},
    legend: {
        data: ['emotion','2019History']
    },
    xAxis: {
        name: 'Time',
        splitNumber: 10,
        data: []
    },
    yAxis: {
        name: 'Sentiment',
        type: 'value',
        splitNumber: 10,
        max: 0.5,
        min: -0.5
    },
    series: [{
        name: 'emotion',
        type: 'line',
        data: []
    },{
            name:'2019History',
            type:'line',
            data:[0.18521806371935684,0.18521806371935684,0.18521806371935684,0.18521806371935684,0.18521806371935684,0.18521806371935684,0.18521806371935684,0.18521806371935684,0.18521806371935684,0.18521806371935684]
        }]
};


cbdOption = {
    title: {
        text: 'cbd emotion analysis'
    },
    tooltip: {},
    legend: {
        data: ['emotion']
    },
    xAxis: {
        name: 'Time',
        splitNumber: 10,
        data: []
    },
    yAxis: {
        name: 'Sentiment',
        type: 'value',
        splitNumber: 10,
        max: 0.5,
        min: -0.5
    },
    series: [{
        name: 'emotion',
        type: 'line',
        data: []
    }]
};

preOption = {
    title: {
        text: 'pre emotion analysis'
    },
    tooltip: {},
    legend: {
        data: ['emotion']
    },
    xAxis: {
        name: 'Time',
        splitNumber: 10,
        data: []
    },
    yAxis: {
        name: 'Sentiment',
        type: 'value',
        splitNumber: 10,
        max: 0.5,
        min: -0.5
    },
    series: [{
        name: 'emotion',
        type: 'line',
        data: []
    }]
};

donOption = {
    title: {
        text: 'don emotion analysis'
    },
    tooltip: {},
    legend: {
        data: ['emotion']
    },
    xAxis: {
        name: 'Time',
        splitNumber: 10,
        data: []
    },
    yAxis: {
        name: 'Sentiment',
        type: 'value',
        splitNumber: 10,
        max: 0.5,
        min: -0.5
    },
    series: [{
        name: 'emotion',
        type: 'line',
        data: []
    }]
};


SYOption = {
    title: {
        text: 'SY emotion analysis'
    },
    tooltip: {},
    legend: {
        data: ['emotion']
    },
    xAxis: {
        name: 'Time',
        splitNumber: 10,
        data: []
    },
    yAxis: {
        name: 'Sentiment',
        type: 'value',
        splitNumber: 10,
        max: 0.5,
        min: -0.5
    },
    series: [{
        name: 'emotion',
        type: 'line',
        data: []
    }]
};

myMelChart.setOption(melOption);
mySydChart.setOption(sydOption);
myAdeChart.setOption(adeOption);
myBriChart.setOption(briOption);
myCbdChart.setOption(cbdOption);
myPreChart.setOption(preOption);
myDonChart.setOption(donOption);
mySYChart.setOption(SYOption);


//更新图表们----------------------------------------------------
//准备好统一的 callback 函数
function update_mel(melData) {
    //res是json格式的response对象

    // 隐藏加载动画
    myMelChart.hideLoading();

    // 准备数据
    melTime.push(melData.webTime);
    melSentiment.push(parseFloat(melData.webSentiment));
    if (melTime.length >= 10) {
        melTime.shift();
        melSentiment.shift();
    }

    updateMelOption = {
        xAxis: {
            data: melTime
        },
        series: [{
            //这个name对应着上面legend的图例示例
            name: 'emotion', // 根据名字对应到相应的系列
            data: melSentiment
        }]
    };

    // 填入数据
    myMelChart.setOption(updateMelOption);

}


function update_syd(sydData) {
    mySydChart.hideLoading();
    sydTime.push(sydData.webTime);
    sydSentiment.push(parseFloat(sydData.webSentiment));
    if (sydTime.length >= 10) {
        sydTime.shift();
        sydSentiment.shift();
    }
    updateSydOption = {
        xAxis: {
            data: sydTime
        },
        series: [{
            name: 'emotion',
            data: sydSentiment
        }]
    };
    mySydChart.setOption(updateSydOption);
}


function update_ade(adeData) {
    myAdeChart.hideLoading();
    adeTime.push(adeData.webTime);
    adeSentiment.push(parseFloat(adeData.webSentiment));
    if (adeTime.length >= 10) {
        adeTime.shift();
        adeSentiment.shift();
    }
    updateAdeOption = {
        xAxis: {
            data: adeTime
        },
        series: [{
            name: 'emotion',
            data: adeSentiment
        }]
    };
    myAdeChart.setOption(updateAdeOption);
}


function update_bri(briData) {
    myBriChart.hideLoading();
    briTime.push(briData.webTime);
    briSentiment.push(parseFloat(briData.webSentiment));
    if (briTime.length >= 10) {
        briTime.shift();
        briSentiment.shift();
    }
    updateBriOption = {
        xAxis: {
            data: briTime
        },
        series: [{
            name: 'emotion',
            data: briSentiment
        }]
    };
    myBriChart.setOption(updateBriOption);
}


function update_cbd(cbdData) {
    myCbdChart.hideLoading();
    cbdTime.push(cbdData.webTime);
    cbdSentiment.push(parseFloat(cbdData.webSentiment));
    if (cbdTime.length >= 10) {
        cbdTime.shift();
        cbdSentiment.shift();
    }
    updateCbdOption = {
        xAxis: {
            data: cbdTime
        },
        series: [{
            name: 'emotion',
            data: cbdSentiment
        }]
    };
    myCbdChart.setOption(updateCbdOption);
}


function update_pre(preData) {
    myPreChart.hideLoading();
    preTime.push(preData.webTime);
    preSentiment.push(parseFloat(preData.webSentiment));
    if (preTime.length >= 10) {
        preTime.shift();
        preSentiment.shift();
    }
    updatePreOption = {
        xAxis: {
            data: preTime
        },
        series: [{
            name: 'emotion',
            data: preSentiment
        }]
    };
    myPreChart.setOption(updatePreOption);
}


function update_don(donData) {
    myDonChart.hideLoading();
    donTime.push(donData.webTime);
    donSentiment.push(parseFloat(donData.webSentiment));
    if (donTime.length >= 10) {
        donTime.shift();
        donSentiment.shift();
    }
    updateDonOption = {
        xAxis: {
            data: donTime
        },
        series: [{
            name: 'emotion',
            data: donSentiment
        }]
    };
    myDonChart.setOption(updateDonOption);
}


function update_SY(SYData) {
    mySYChart.hideLoading();
    SYTime.push(SYData.webTime);
    SYSentiment.push(parseFloat(SYData.webSentiment));
    if (SYTime.length >= 10) {
        SYTime.shift();
        SYSentiment.shift();
    }
    updateSYOption = {
        xAxis: {
            data: SYTime
        },
        series: [{
            name: 'emotion',
            data: SYSentiment
        }]
    };
    mySYChart.setOption(updateSYOption);
}


// 首次显示加载动画
myMelChart.showLoading();
mySydChart.showLoading();
myAdeChart.showLoading();
myBriChart.showLoading();
myCbdChart.showLoading();
myPreChart.showLoading();
myDonChart.showLoading();
mySYChart.showLoading();

//处理url链接请求
function get(yourUrl) {
    var Httpreq = new XMLHttpRequest();
    Httpreq.open("GET", yourUrl, false);
    Httpreq.send(null);
    return Httpreq.responseText;
}