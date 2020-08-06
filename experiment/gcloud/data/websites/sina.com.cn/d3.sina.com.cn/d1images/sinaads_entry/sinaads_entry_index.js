(function() {
    var setCookie = function (key, value, options) {
        options = options || {};

        // 璁＄畻cookie杩囨湡鏃堕棿
        var expires = options.expires;
        if ('number' === typeof options.expires) {
            expires = new Date();
            expires.setTime(expires.getTime() + options.expires);
        }
        document.cookie =
            key + "=" + value +
            (options.path ? "; path=" + options.path : "") +
            (expires ? "; expires=" + expires.toGMTString() : "") +
            (options.domain ? "; domain=" + options.domain : "") +
            (options.secure ? "; secure" : '');

    }


    var addEvent = function(obj, eventType, func) {
        if(obj.attachEvent) {
            obj.attachEvent("on" + eventType, func);
        } else {
            obj.addEventListener(eventType, func, false);
        }
    };
    /**
     * 瀹氬悜鏍囪瘑(鐐瑰嚮鍚庣涓�)
     * @param  {String} 鏂囧瓧閾剧殑瀹瑰櫒id
     * @param  {String} 鏍囪瘑鍊�
     * @param  {String} 鐐瑰嚮鐩戞祴
     */
    var sinaads_entry_fn = function(id,value,url){
        var links;
        try {
            links = document.getElementById(id).getElementsByTagName("a");
        }catch(e) {
            links = [];
        }

        for (var i = 0, len = links.length; i < len; i++) {
            //涓嶆槸鍟嗗箍鑺傜偣, 杩欓噷鏈夋椂搴忓叧绯伙紝濡傛灉骞垮憡鍏堝姞杞斤紝浼氳幏鍙栧埌骞垮憡锛屽鏋滃箍鍛婂悗鍔犺浇锛岃繖閲屽氨涓嶄細琚敞鍏�
            if ('INS' === links[i].parentNode.tagName.toUpperCase() && links[i].parentNode.className.indexOf('sinaads') !== -1) {
            } else {
                addEvent(links[i], "mousedown", function() {
                    setCookie("sinaads_entry",value,{"path":"/","domain":".sina.com.cn","expires":24*3600000});
                    //鐐瑰嚮鐩戞祴
                    if(url){
                        var _clickStat = new Image();
                        _clickStat.src = url + "&_=" + new Date().getTime() + "&url=";
                    }
                });
            }
        }

    }

    //瑕侀椈鍖哄畾鍚�
    //sinaads_entry_fn("syncad_1","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,533936,539210&cid=0,0,0&sid=540113&advid=358&camid=69129&show=ignore");
    //sinaads_entry_fn("syncad_2","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,534288,539558&cid=0,0,0&sid=540487&advid=358&camid=69129&show=ignore");
    //sinaads_entry_fn("syncad_3","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,534289,539559&cid=0,0,0&sid=540488&advid=358&camid=69129&show=ignore");
    //sinaads_entry_fn("syncad_4","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,539990,545264&cid=0,0,0&sid=546428&advid=358&camid=69129&show=ignore");
    //sinaads_entry_fn("syncad_0","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,547080,552353&cid=0,0,0&sid=553716&advid=358&camid=69129&show=ignore");
    //
    ////瑕侀椈鍖築鐗堝畾鍚�
    //sinaads_entry_fn("syncad_1_B","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,533936,539210&cid=0,0,0&sid=540113&advid=358&camid=69129&show=ignore");
    //sinaads_entry_fn("syncad_2_B","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,534288,539558&cid=0,0,0&sid=540487&advid=358&camid=69129&show=ignore");
    //sinaads_entry_fn("syncad_3_B","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,534289,539559&cid=0,0,0&sid=540488&advid=358&camid=69129&show=ignore");
    //sinaads_entry_fn("syncad_4_B","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,539990,545264&cid=0,0,0&sid=546428&advid=358&camid=69129&show=ignore");
    //sinaads_entry_fn("syncad_0_B","jnc","http://sina.allyes.com/main/adfclick?db=sina&bid=372535,547080,552353&cid=0,0,0&sid=553716&advid=358&camid=69129&show=ignore");
    //
    //
    ////璐㈢粡鏉垮潡瀹氬悜
    ////sinaads_entry_fn("blk_finance_1","abc","http://sina.allyes.com/main/adfclick?db=sina&bid=202406,581303,586578&cid=0,0,0&sid=589122&advid=358&camid=36885&show=ignore");
    ////sinaads_entry_fn("blk_finance_2","abc","http://sina.allyes.com/main/adfclick?db=sina&bid=202406,581309,586584&cid=0,0,0&sid=589128&advid=358&camid=36885&show=ignore");
    ////sinaads_entry_fn("blk_finance_3","abc","http://sina.allyes.com/main/adfclick?db=sina&bid=202406,581310,586585&cid=0,0,0&sid=589129&advid=358&camid=36885&show=ignore");
    ////鏂板鍙や簳璐￠厭(2014-09-01鑷�2014-09-30)
    //sinaads_entry_fn("blk_finance_1","gujinggongjiu");
    //sinaads_entry_fn("blk_finance_2","gujinggongjiu");
    //sinaads_entry_fn("blk_finance_3","gujinggongjiu");
})();