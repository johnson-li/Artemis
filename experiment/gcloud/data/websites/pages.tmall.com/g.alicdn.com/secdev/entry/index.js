(function(a,e,o,t,r,i,n){if(e.__no_sec_entry){return}var m=t.userAgent;var c=n("%58%75%65%58%69");var l=c.toLowerCase();if(m.indexOf(c)>=0||r.host.indexOf(l)>=0||top!==self&&e.referrer.indexOf(l)>=0){return}var f=e.getElementsByTagName("head")[0];function s(a){var o=e.createElement("script");o.src=a;return f.appendChild(o)}var d="//g.alicdn.com";var v=self.goldlog;if(v&&v.getCdnPath){d=v.getCdnPath()}d+="/secdev/";var b=m.match(/Chrome\/(\d*)/);if(b){b=+b[1]}if(!e._sufei_data2){var h="3.9.0";var u=s(d+"sufei_data/"+h+"/index.js");u.async=e.cookie.indexOf("isg=")<0;u.id="aplus-sufei"}var g=.001;if(o()<g){e._linkstat_sample=g;s(d+"linkstat/index.js?v=1201")}a.nsrprtrt=1e-4;var p=0;if(!/Mobile/.test(m)){var _=["taobao.com","alibaba.com","alipay.com","tmall.com","lazada","aliexpress.com","1688.com","alimama.com","tb.cn","xiami.com","amap.com","cainiao.com","aliyun.com","etao.com","fliggy.com","liangxinyao.com","damai.cn","daraz.lk","tmall.hk","jiyoujia.com","taopiaopiao.com","alitrip.com","fliggy.hk","alihealth.cn","alitrip.hk","ele.me","gaode.cn","mp.dfkhgj.com","mp.bcvbw.com","m.dfkhgj.com","pailitao.com"];for(var y=0;y<_.length;y++){if(r.host&&~r.host.indexOf(_[y])){p=1;break}}}if(p){var x=["1.0.76","e",86];var j=["1.0.78","e",88];var k=1e4;var M=x;if((o()*1e4|0)<k){M=j}if(!M){return}var C=d;if(/buyertrade\.taobao\.com$/.test(r.hostname)||/refund2\.taobao\.com$|refund2\.tmall\.com$/.test(r.hostname)&&r.pathname==="/dispute/apply.htm"){C=C.replace("/secdev/","??xlly/spl/index.js,secdev/")}var w=C+"nsv/"+M[0]+"/";var E=w+"ns_"+M[1]+"_"+M[2]+"_3_f.js";var S=w+"ns_"+M[1]+"_"+M[2]+"_3_n.js";function I(){var a="function%20javaEnabled%28%29%20%7B%20%5Bnative%20code%5D%20%7D";if("WebkitAppearance"in e.documentElement.style){if(escape(t.javaEnabled.toString())===a){return true}}return false}var L=m.match(/Edge\/([\d]*)/);var A=m.match(/Safari\/([\d]*)/);var O=m.match(/Firefox\/([\d]*)/);var B=m.match(/MSIE|Trident/);if(L){s(E)}else if(b){s(E)}else if(A||O||B){s(S)}else{if(I()){s(E)}else{s(S)}}}function D(){var o=a.atob;if(!o){return}function t(a,e){var o=[];for(var t in a){o.push(t+"="+i(a[t]))}(new Image).src=e+o.join("&")}var r=0;var n="";function m(){if(++r==3){clearInterval(b)}f()}var c;var l=Math.random()*1e8|0;function f(){var a=c.getUA({MaxMTLog:500,MTInterval:7});a=l+"|"+a;var e={token:a,cna:n,ext:7};t(e,"https://fourier.taobao.com/ts?")}var d=+localStorage._xlly;if(!d&&/xlly=/.test(e.cookie)){d=+new Date;localStorage._xlly=d}if(d){var v=new Date-d;if(v>1e3*3600*24){v=0;delete localStorage._xlly}if(v<1e3*60*20){var b=setInterval(m,1e3*60);if(a.addEventListener){a.addEventListener("unload",f)}var h=e.cookie.match(/cna=([^;]+)/);if(h){n=h[1]}var u=s(o("aHR0cHM6Ly9nLmFsaWNkbi5jb20vQVdTQy9BV1NDL2F3c2MuanM="));var g=unescape("%75%61%62");u.onload=function(){a.AWSC&&AWSC.use(g,function(a,e){if(a==="loaded"){c=e}})}}}}try{D()}catch(a){}try{a.etrprtrt=.01;var T=0;var W=["login.taobao.com/member/login.jhtml","passport.alibaba.com/mini_login.htm","login.taobao.com/member/loginByIm.do","login.taobao.com/member/login_by_safe.htm","login.taobao.com/member/vst.htm","login.taobao.com/member/facebookLogin.do","buy.taobao.com/auction/buy_now.jhtml","buy.taobao.com/auction/order/confirm_order.html","buy.tmall.com/order/confirm_order.html","buyertrade.taobao.com/trade/itemlist/list_bought_items.htm","member1.taobao.com/member/fresh/account_security.htm","member1.taobao.com/member/fresh/account_management.htm","member1.taobao.com/member/fresh/weibo_bind_management.htm","member1.taobao.com/member/fresh/deliver_address.htm","liveplatform.taobao.com/live/home/live-Analysis","databot.taobao.com/tb/tblive","databot.taobao.com/tb/tblive-m"];var F=[];var N=r.host+r.pathname;if(~W.join().indexOf(N)){T=1}else if(~F.join().indexOf(N)){var R=0;if(Math.random()<R){T=1}}if(T){var U="1.61.1";var $="1.62.1";var z=1;var H=U;if(Math.random()<z){H=$}if(!H){return}var P="//g.alicdn.com/AWSC/et/"+H+"/";var Q=P+"et_f.js";var V=P+"et_n.js";if(L){s(Q)}else if(b){s(Q)}else if(A||O||B){s(V)}else{if(I()){s(Q)}else{s(V)}}}}catch(a){}})(window,document,Math.random,navigator,location,encodeURIComponent,decodeURIComponent);