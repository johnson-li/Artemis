/*
 * 	白名单
 */
window.PDPSList = ["PDPS000000046010", "PDPS000000058599", "PDPS000000058858", "PDPS000000043766", "PDPS000000060868", "PDPS000000057131", "PDPS000000057132", "PDPS000000057133", "PDPS000000055657", "PDPS000000055301", "PDPS000000055659", "PDPS000000055658", "PDPS000000055660", "PDPS000000055661", "PDPS000000057465", "CS_PDPS000000046010", "CS_PDPS000000060868"];
var power = {
    PDPS000000025255: ["NowDate", "name"],
    PDPS000000043763: ["name", "post"]
};
for (var listNum = 0; listNum < PDPSList.length; listNum++) {
    let newPDPS = PDPSList[listNum];
    power.newPDPS = ["NowDate", "name", "post"];
}

var startTime = Date.parse(new Date()),
    timeoutId = null;

/*
 * 	方法综合
 */
window.Tool = {
    // adsArray: new Array(),
    whiteList: window.PDPSList || [],

    getIframeDomain: function () {
        var ifDom = document.getElementsByTagName("iframe");
        if (ifDom[0]) {
            url = ifDom[0].src;
        }

        var ifdomain = url.split("/"); //以“/”进行分割
        if (ifdomain[2]) {
            ifdomain = ifdomain[2];
        } else {
            ifdomain = ""; //如果url不正确就取空
        }

        return ifdomain;
    },
    /**
     * getData    获取并返回数据
     */
    getData: function (event) {
        var oncePost = event.oncePost;
        var pdps = event.pdps || "";
        var adsIframe = Tool.getAdsDom(pdps);
        var data = {
            frequency: event.frequency
        };
        for (var i = 0, len = oncePost.length; i < len; i++) {
            var onceData = {};

            // var firstUp = oncePost[i].substring(0,1).toUpperCase() + oncePost[i].substring(1);
            // var methodName = `getIframe${firstUp}`;
            // onceData[oncePost[i]] = Tool[methodName](pdps);

            switch (oncePost[i]) {
                case "top":
                    onceData = {
                        top: Tool.getIframeTop(pdps)
                    };
                    break;
                case "left":
                    onceData = {
                        left: Tool.getIframeLeft(pdps)
                    };
                    break;
                case "width":
                    onceData = {
                        width: Tool.getIframeWidth(pdps)
                    };
                    break;
                case "height":
                    onceData = {
                        ifrHeight: Tool.getIframeHeight(pdps)
                    };
                    break;
                case "allSize":
                    onceData = Tool.getIframeAllSize(pdps);
                    break;
                default:
            }
            data = Tool.mergeObject(data, onceData);
        }

        if (adsIframe) {
            var dataStr = JSON.stringify(data);
            adsIframe.contentWindow.postMessage(dataStr, "*");
        }
    },
    mergeObject: function (beMerObj, merObj) {
        var newObj = JSON.parse(JSON.stringify(beMerObj));
        for (var x in merObj) {
            newObj[x] = merObj[x];
        }
        return newObj;
    },

    /**
     * monitorPost
     */
    getlistener: function (event) {
        if (window.addEventListener) {
            window.addEventListener("scroll", function () {
                if (timeoutId !== null) clearTimeout(timeoutId);
                var currentTime = Date.parse(new Date());
                if (currentTime - startTime < 1000) {
                    timeoutId = setTimeout(Tool.getData(event), 300);
                } else {
                    Tool.getData(event);
                    startTime = currentTime;
                }

                // Tool.getData(event);
            });

        } else if (window.attachEvent) {
            window.attachEvent("onscroll", function () {
                Tool.getData(event);
            });
        }
    },
    /**
     * @param {*} isPC 判断是PC还是wap
     */
    isPC: function () {
        var userAgentInfo = navigator.userAgent;
        var Agents = [
            "Android",
            "iPhone",
            "SymbianOS",
            "Windows Phone",
            "iPad",
            "iPod"
        ];
        var flag = true;
        for (var v = 0; v < Agents.length; v++) {
            if (userAgentInfo.indexOf(Agents[v]) > 0) {
                flag = false;
                break;
            }
        }
        return flag;
    },

    /**
     * @param {*} getAdsDom 获取iframe
     */
    getAdsDom: function (pdps) {
        // 广告dom
        var queryer = this.isPC()
            ? '[data-ad-pdps="' + pdps + '"]'
            : '[data-id="' + pdps + '"]';
        var adsDom = document.querySelector(queryer);

        if (adsDom) {
            return adsDom.getElementsByTagName("iframe")[0];
        } else {
            return "";
        }
    },

    getIframeAllSize: function (pdps) {
        var otherInfo = ["top", "left", "width", "height"];

        var data = {
            allSize: {
                windowH: Tool.getClientHeight(),
                windowW: Tool.getClientWidth()
            }
        };
        // 遍历非实时监听的数据信息
        for (var i = 0; i < otherInfo.length; i++) {
            let firstUp = otherInfo[i].substring(0, 1).toUpperCase() + otherInfo[i].substring(1);
            let methodName = `getIframe${firstUp}`;
            data.allSize[otherInfo[i]] = Tool[methodName](pdps);

            // switch (otherInfo[i]) {
            //   case "top":
            //     top = Tool.getIframeTop(pdps);
            //     break;
            //   case "left":
            //     left = Tool.getIframeLeft(pdps);
            //     break;
            //   case "width":
            //     width = Tool.getIframeWidth(pdps);
            //     break;
            //   case "height":
            //     height = Tool.getIframeHeight(pdps);
            //     break;
            //   default:
            //     break;
            // }
        }

        return data;
    },

    /**
     * @param {*} whiteList 白名单列表或白名单字符
     */
    // setWhiteList: function(whiteList) {
    //   if (whiteList instanceof Array) {
    //     this.whiteList = this.whiteList.concat(whiteList);
    //   } else if (whiteList instanceof String) {
    //     this.whiteList.push(whiteList);
    //   }
    // },

    /**
     * @param {*} name  获取权限，返回相应cookie
     * @returns
     */
    getPower: function (adsPDPS, name) {
        var newName = power[adsPDPS];
        var cookie = {};
        for (var j = 0, nameLen = name.length; j < nameLen; j++) {
            for (var i = 0, len = newName.length; i < len; i++) {
                if (name[j] == newName[i]) {
                    cookie[name[j]] = Tool.getCookie(name[j]);
                }
            }
        }
        return cookie;
    },

    /**
     * @param {*} name  获取cookie
     * @returns
     */
    getCookie: function (name) {
        var strcookie = document.cookie; //获取cookie字符串
        var arrcookie = strcookie.split("; "); //分割
        //遍历匹配
        for (var i = 0; i < arrcookie.length; i++) {
            var arr = arrcookie[i].split("=");

            if (arr[0] == name) {
                return arr[1];
            }
        }
        return "";
    },

    getReset: function (event) {
        var pdps = event.pdps;
        var queryer = this.isPC()
            ? '[data-ad-pdps="' + pdps + '"]'
            : '[data-id="' + pdps + '"]';

        var adsDom = document.querySelector(queryer);
        var adsIframe = "";
        if (adsDom) {
            adsIframe = adsDom.getElementsByTagName("iframe")[0];
        }
        if (adsIframe) {
            if (parseInt(event.oncePost.resetSizeH) > 203) {
                adsIframe.style.height = "203px";
            } else {
                adsIframe.style.height = event.oncePost.resetSizeH + "px";
            }
        }
    },
    /**
     * getDomain
     */
    getDomain: function () {
        return document.referrer || window.location.href || document.domain;
    },
    /**
     * @param {*}     建桥,并传递权限内信息
     */
    getAdsList: function () {
        if (window.addEventListener) {
            // window.addEventListener("load", function() {
            // for (var i = 0, len = Tool.whiteList.length; i < len; i++) {
            //   Tool.postData(Tool.whiteList[i]);
            // }
            // });
        } else if (window.attachEvent) {
            // window.attachEvent("onload", function() {
            //   for (var i = 0, len = Tool.whiteList.length; i < len; i++) {
            //     Tool.postData(Tool.whiteList[i]);
            //   }
            // });
        }
    },
    postData: function (adsPDPS) {
        // 默认传递给第三方的一些数据
        var obj = {
            init: {
                // cookie: Tool.getPower(adsPDPS, power[adsPDPS]),
                pdps: adsPDPS,
                referrer: Tool.getDomain()
            }
        };

        var adsIframeDom = Tool.getAdsDom(adsPDPS);
        var objStr = JSON.stringify(obj);
        var postDomain = Tool.getIframeDomain();
        if (adsIframeDom) {
            adsIframeDom.contentWindow.postMessage(objStr, "*");
        }
    },

    /**
     *    取窗口可视范围的高度
     */
    getClientHeight: function () {
        var clientHeight =
            document.body.clientHeight < document.documentElement.clientHeight
                ? document.body.clientHeight
                : document.documentElement.clientHeight;

        return clientHeight;
    },

    /**
     *    取窗口可视范围的k度
     */
    getClientWidth: function () {
        var clientWidth =
            document.body.clientWidth < document.documentElement.clientWidth
                ? document.body.clientWidth
                : document.documentElement.clientWidth;

        return clientWidth;
    },

    /**
     * 获取iframe的height
     *
     */
    getIframeHeight: function (pdps) {
        var ifrHeight;
        var queryer = this.isPC()
            ? '[data-ad-pdps="' + pdps + '"]'
            : '[data-id="' + pdps + '"]';
        var adsDom = document.querySelector(queryer);
        if (adsDom) {
            ifrHeight = adsDom.clientHeight;
        }

        return ifrHeight;
    },

    /**
     *    获取iframe的width
     */
    getIframeWidth: function (pdps) {
        var width;
        var queryer = this.isPC()
            ? '[data-ad-pdps="' + pdps + '"]'
            : '[data-id="' + pdps + '"]';
        var adsDom = document.querySelector(queryer);

        if (adsDom) {
            width = adsDom.clientWidth;
        }
        return width;
    },

    /**
     *    获取iframe的位置
     */
    getIframeTop: function (pdps) {
        if (!pdps) {
            return;
        }

        // 广告坐标
        var queryer = this.isPC()
            ? '[data-ad-pdps="' + pdps + '"]'
            : '[data-id="' + pdps + '"]';
        var adsDom = document.querySelector(queryer);

        var adsTop;
        if (adsDom) {
            adsTop = parseInt(adsDom.getBoundingClientRect().top);
        }

        return adsTop;
    },

    getIframeLeft: function (pdps) {
        if (!pdps) {
            return;
        }
        // 广告坐标

        var queryer = this.isPC()
            ? '[data-ad-pdps="' + pdps + '"]'
            : '[data-id="' + pdps + '"]';
        var adsDom = document.querySelector(queryer);

        var adsLeft;
        if (adsDom) {
            adsLeft = parseInt(adsDom.getBoundingClientRect().left);
        }
        return adsLeft;
    },

    throttle (fun, delay, maxTime) {
        var startTime = Date.parse(new Date()),
            timeoutId = null;

        return function () {
            if (timeoutId !== null) clearTimeout(timeoutId);
            debugger;
            var currentTime = Date.parse(new Date());

            if (currentTime - startTime < maxTime) {
                console.log("小于1000");
                timeoutId = setTimeout(fun, delay);
            } else {
                console.log("大于1000");
                fun;
                startTime = currentTime;
            }
        };
    }
};

/*
 * 	接收数据
 */
document.cookie = "NowDate=" + new Date();
document.cookie = "name=" + "sinaAds";
document.cookie = "post=" + "massage";
document.cookie = "page=" + "23333";

if (window.addEventListener) {
    window.addEventListener("message", function (event) {
        getMessage(event);
    });
} else if (window.attachEvent) {
    window.attachEvent("onmessage", function (event) {
        getMessage(event);
    });
}

function getMessage (event) {
    try {
        var eventData = JSON.parse(event.data);
        console.log("我们拿到的第三方传过来的数据：", eventData);

        if (eventData.frequency === "oncePost") {
            Tool.getData(eventData);
        } else if (eventData.frequency === "monitorPost") {
            Tool.getlistener(eventData);
        } else if (eventData.frequency === "resetPost") {
            Tool.getReset(eventData);
        }
    } catch (e) { }
}

/*
 *   入口
 */
Tool.getAdsList();