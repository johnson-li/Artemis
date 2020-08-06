jQuery(document).ready(function($){'use strict';var docCookies={getItem:function(sKey){if(!sKey){return null;}
return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*"+encodeURIComponent(sKey).replace(/[\-\.\+\*]/g,"\\$&")+"\\s*\\=\\s*([^;]*).*$)|^.*$"),"$1"))||null;},setItem:function(sKey,sValue,vEnd,sPath,sDomain,bSecure){if(!sKey||/^(?:expires|max\-age|path|domain|secure)$/i.test(sKey)){return false;}
var sExpires="";if(vEnd){switch(vEnd.constructor){case Number:sExpires=vEnd===Infinity?"; expires=Fri, 31 Dec 9999 23:59:59 GMT":"; max-age="+vEnd;break;case String:sExpires="; expires="+vEnd;break;case Date:sExpires="; expires="+vEnd.toUTCString();break;}}
if('rootDomain'===sDomain||'.rootDomain'===sDomain){sDomain=('.rootDomain'===sDomain?'.':'')+document.location.hostname.split('.').slice(-2).join('.');}
document.cookie=encodeURIComponent(sKey)+"="+encodeURIComponent(sValue)+sExpires+(sDomain?"; domain="+sDomain:"")+(sPath?"; path="+sPath:"")+(bSecure?"; secure":"");return true;},removeItem:function(sKey,sPath,sDomain){if(!this.hasItem(sKey)){return false;}
document.cookie=encodeURIComponent(sKey)+"=; expires=Thu, 01 Jan 1970 00:00:00 GMT"+(sDomain?"; domain="+sDomain:"")+(sPath?"; path="+sPath:"");return true;},hasItem:function(sKey){if(!sKey||/^(?:expires|max\-age|path|domain|secure)$/i.test(sKey)){return false;}
return(new RegExp("(?:^|;\\s*)"+encodeURIComponent(sKey).replace(/[\-\.\+\*]/g,"\\$&")+"\\s*\\=")).test(document.cookie);},keys:function(){var aKeys=document.cookie.replace(/((?:^|\s*;)[^\=]+)(?=;|$)|^\s*|\s*(?:\=[^;]*)?(?:\1|$)/g,"").split(/\s*(?:\=[^;]*)?;\s*/);for(var nLen=aKeys.length,nIdx=0;nIdx<nLen;nIdx++){aKeys[nIdx]=decodeURIComponent(aKeys[nIdx]);}
return aKeys;}};window._tkq=window._tkq||[];var DEFAULT_CSS='.a8c-cookie-banner { \
		display: block; \
		z-index: {{z-index}}; \
		position: fixed; \
		bottom: 0; \
		left: 0; \
		right: 0; \
		margin: 0; \
		padding: 16px 10px 16px 10px; \
		background-color: #f0f0f0; \
		border-top: 1px solid rgba(0, 0, 0, 0.05); \
		transform: translateY(+100%); \
		transition: transform 600ms ease-out; \
	} \
	.a8c-cookie-banner p { \
		display: inline-block; \
		color: black; \
		margin: 0 120px 0 0 ; \
		padding: 0; \
		font-family: sans-serif; \
		font-size: 12px; \
		font-weight: normal; \
		line-height: 1.25; \
	} \
	.a8c-cookie-banner a { \
		color: #0087BE; \
		font-family: sans-serif; \
		font-size: 12px; \
		font-weight: normal; \
		line-height: 1.25; \
	} \
	.a8c-cookie-banner a.a8c-cookie-banner-ok-button { \
		box-sizing: border-box; \
		display: inline-block; \
		position: absolute; \
		right: 10px; \
		top: 50%; \
		width: 110px; \
		transform: translateY(-50%); \
		border-radius: 4px; \
		border: 1px solid #e0e0e0; \
		padding: 10px; \
		background-color: white; \
		text-align: center; \
		font-family: sans-serif; \
		text-decoration: none; \
	} \
	.rtl .a8c-cookie-banner a.a8c-cookie-banner-ok-button { \
		left: 10px; \
		right: auto; \
	} \
	@media only screen and (max-width : 600px) { \
		.a8c-cookie-banner { \
			padding: 10px 10px 10px 10px; \
		} \
		.a8c-cookie-banner p { \
			margin: 0 0 10px 0; \
			text-align: justify; \
		} \
		.a8c-cookie-banner a.a8c-cookie-banner-ok-button { \
			display: block; \
			position: static; \
			transform: none; \
			min-width: 89px; \
			width: 50%; \
			margin: 0 auto; \
		} \
	}';var cb=window.a8cAnalytics={maybeShowCookieBanner:function(config,countryCode){var isGdprCountry=-1!==cb.kit.GDPR_COUNTRIES.indexOf(countryCode);var userChoice=docCookies.getItem(config.cookieName);if('yes'!==userChoice&&'no'!==userChoice){userChoice='unknown';}
var show='unknown'===userChoice&&(isGdprCountry||'unknown'===countryCode);show&=!config.skipBanner;if(show){cb.showCookieBanner(config);}else{if('no'!==userChoice){setTimeout(function(){$(document).trigger('a8c-analytics:fire-sensitive-pixels');},1);}}},showCookieBanner:function(config){$('head').append('<style type="text/css">'+DEFAULT_CSS+'</style>');var $div=$('<div/>');$div.addClass('a8c-cookie-banner custom-cookie-banner');var $p=$('<p/>');$p.html(config.text);var $a=$('<a/>',{href:'#'});$a.text(config.buttonText);$a.addClass('a8c-cookie-banner-ok-button');$div.append($p);$div.append($a);$(document.body).append($div);$('.a8c-cookie-banner').css('transform','none');$('a.a8c-cookie-banner-ok-button').on('click',function(event){event.preventDefault();$('.a8c-cookie-banner').hide();var SIX_MONTHS_MAX=6*30*24*60*60;docCookies.setItem(config.cookieName,'yes',SIX_MONTHS_MAX,'/',config.cookieDomain);$(document).trigger('a8c-analytics:fire-sensitive-pixels');window._tkq.push(['recordEvent','a8c_cookie_banner_ok',{site:document.location.host,path:document.location.pathname,}]);});var sanitized_host=document.location.host.replace(/[^a-zA-Z0-9]/g,'-');window._stq=window._stq||[];window._stq.push(['extra',{'x_cookie-banner-view':'total,'+sanitized_host}]);},initCookieBanner:function(config){config=window.a8cAnalyticsConfig.cookieBanner;DEFAULT_CSS=DEFAULT_CSS.replace(/{{z-index}}/g,config.cssZIndex);var countryCode=docCookies.getItem('country_code');if(null===countryCode){$.ajax({type:'GET',dataType:"json",cache:false,url:'https://public-api.wordpress.com/geo/',success:function(data){countryCode=data['country_short'];docCookies.setItem('country_code',countryCode,6*60*60,'/',config.cookieDomain);cb.maybeShowCookieBanner(config,countryCode);},error:function(){countryCode='unknown';docCookies.setItem('country_code',countryCode,6*60*60,'/',config.cookieDomain);cb.maybeShowCookieBanner(config,countryCode);},});}else{cb.maybeShowCookieBanner(config,countryCode);}},};window.a8cAnalytics.kit={docCookies:docCookies,GDPR_COUNTRIES:['AT','BE','BG','CY','CZ','DE','DK','EE','ES','FI','FR','GR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK','GB','CH','IS','LI','NO',],QUERY_PARAMS:['aff','affiliate','sid','cid','adgroupid','campaignid','device','fbclid','format','gclid','gclsrc','keyword','locationid','matchtype','network','ref','targetid','term','type','utm_campaign','utm_content','utm_medium','utm_source','utm_term','utm_expid',],doNotTrack:function(){return(window.doNotTrack==='1'||(window.navigator&&window.navigator.doNotTrack==='1'));},tracksAnonId:function(callback){var i=setInterval(function(){var id=docCookies.getItem('tk_ai');if(id){clearInterval(i);if('function'===typeof callback){callback(id);}}},100);},uniqueId:function(length,chars){length=Number(length||32);chars=String(chars||'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789');for(var i=0,id='';i<length;i++){id+=chars.charAt(Math.floor(Math.random()*chars.length));}
return id;},parseURL:function(url,base){if('function'!==typeof window.URL){return null;}
try{url=url?url.replace(/^\/\//,location.protocol+'//'):'';return new URL(url||document.URL,base||document.URL);}catch(error){return null;}},getQueryVar:function(name,url){var queryVars=cb.kit.getQueryVars(url);return'undefined'===typeof queryVars[name]?null:queryVars[name]||'';},getQueryVars:function(url,names){url=url||document.URL;names=names||[];var searchParams={};var tkAmpSearchParams={};if(!(url=cb.kit.parseURL(url))){return{};}
if(!url.searchParams){return{};}
if(url.searchParams.has('tk_amp')){var tkAmp=url.searchParams.get('tk_amp')||'';tkAmpSearchParams=cb.kit.parseAmpEncodedSearchParams(tkAmp);}
url.searchParams.forEach(function(value,name){searchParams[name]=value;});searchParams=$.extend({},tkAmpSearchParams,searchParams);if(names.length){for(var _name in searchParams){if(-1===names.indexOf(_name)){delete searchParams[_name];}}}
return searchParams;},addQueryVar:function(name,value,url,replaceExisting){url=url||document.URL;var originalURL=url;if(!(url=cb.kit.parseURL(url))){return originalURL;}
if(!url.searchParams){return originalURL;}
replaceExisting=undefined===replaceExisting?true:replaceExisting;if(replaceExisting||!url.searchParams.has(name)){url.searchParams.set(name,value);}
return url.toString();},linkQueryVars:function(linkers){setTimeout(cb.kit.doLinkQueryVars,0,linkers);},doLinkQueryVars:function(linkers){if('function'!==typeof window.URL){return;}
linkers=$.isArray(linkers)?linkers:[];$.each(linkers,function(_,linker){linker=$.extend({},{selectors:{'a':'href','form':'action',},includeRegExps:[],excludeRegExps:[],linkQueryVars:[],linkOtherVars:{},},linker);$.each(linker.selectors,function(selector,urlAttr){$(selector).each(function(){var include=false;var exclude=false;var $this=$(this);var tagName=$this.prop('tagName');var formMethod='FORM'===tagName?($this.attr('method')||'get').toLowerCase():'';var url=$this.attr(urlAttr)||'';var fullURL=(cb.kit.parseURL(url,document.URL)||'').toString();var matchURL=fullURL.replace(/^https?\:\/\//g,'').replace(/[\/?&=#]+$/g,'');if(0===url.indexOf('#')||!/^https?\:\/\//.test(fullURL)){return;}
if(linker.includeRegExps.length){$.each(linker.includeRegExps,function(_,regExp){if(regExp.test(matchURL)){include=true;return false;}});if(!include){return;}}
if(linker.excludeRegExps.length){$.each(linker.excludeRegExps,function(_,regExp){if(regExp.test(matchURL)){exclude=true;return false;}});if(exclude){return;}}
$.each([linker.linkQueryVars,linker.linkOtherVars],function(_,vars){$.each(vars,function(indexOrName,nameOrValue){var name,value;if('string'===typeof indexOrName){name=indexOrName,value=nameOrValue;}else{name=nameOrValue,value=cb.kit.getQueryVar(name);}
if(!name||null===value||undefined===value){return;}else if('FORM'===tagName&&'get'===formMethod){if(!$this.find(':input[name="'+cb.kit.escJQSelector(name)+'"]').length){$this.append('<input type="hidden" name="'+cb.kit.escHtml(name)+'" value="'+cb.kit.escHtml(value)+'" />');}}else{url=cb.kit.addQueryVar(name,value,url,false);}});});$this.attr(urlAttr,url);});});});},parseAmpEncodedSearchParams:function(tkAmp){tkAmp=tkAmp.split('*')
.filter(function(v){return v.length>0;})
.slice(2);if(!tkAmp.length||0!==tkAmp.length%2){return{};}
for(var searchParams={},_i=0;_i<tkAmp.length;_i+=2){searchParams[tkAmp[_i]]=cb.kit.urlSafeBase64DecodeString(tkAmp[_i+1]);}
return searchParams;},urlSafeBase64DecodeString:function(str){var decodeMap={'-':'+',_:'/','.':'=',};return atob(str.replace(/[\-_.]/g,function(c){return decodeMap[c];}));},escRegex:function(str){return str.replace(/[.*+?^${}()|[\]\\\-]/g,'\\$&');},escJQSelector:function(str){return str.replace(/[!"#$%&'()*+,.\/:;<=>?@[\\\]^`{|}~]/g,'\\\\$&');},escHtml:function(str){var entityMap={'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;',};return str.replace(/[&<>"']/g,function(char){return entityMap[char];});},currentTime:function(){return Math.round((new Date()).getTime()/1000);},ymdTime:function(ymd){return cb.kit.ymdHisTime(ymd);},ymdHisTime:function(ymdHis){var parts=ymdHis.split(' ',2);parts[0]=parts[0]||'1970-01-01';parts[1]=parts[1]||'00:00:00';return Math.round(Date.parse(parts[0]+'T'+parts[1]+'.000Z')/1000);},createScriptElement:function(url,attrs,onLoad,onError){var script=document.createElement('script');script.src=url;script.type='text/javascript';script.async=true;script.onload=onLoad;script.onerror=onError;if(attrs){$.each(attrs,function(key,val){script.setAttribute(key,val);});}
return script;},attachToBody:function(element){document.body.appendChild(element);return element;},attachScriptElement:function(url,attrs,onLoad,onError){return cb.kit.attachToBody(cb.kit.createScriptElement(url,attrs,onLoad,onError));},loadPixelImage:function(url){return $('<img>',{src:url,loading:'eager',width:1,height:1,border:0,});},appendIFrame:function(url){if($('#a8c-analytics').length===0){$('body').append('<div style="display: none;" id="a8c-analytics" />');}
var $iframe=$('<iframe/>');$iframe.attr('src',url);$iframe.attr('loading','eager');$iframe.attr('width','1');$iframe.attr('height','1');$iframe.attr('frameborder','0');$iframe.css('display','none');$('#a8c-analytics').append($iframe);return $iframe;},getLastFireTimes:function(){var times=localStorage.getItem('a8cAnalytics_lastFireTimes');try{times=times?JSON.parse(times):{};}catch(e){times={};}
return'object'===typeof times?times:{};},getLastFireTime:function(tracker){var times=cb.kit.getLastFireTimes();return'number'===typeof times[tracker]?times[tracker]:0;},isLastFireTimeStale:function(tracker,maxDiffSeconds){var time=cb.kit.getLastFireTime(tracker);var currentTime=cb.kit.currentTime();return!time||currentTime-time>(maxDiffSeconds||86400);},updateLastFireTime:function(tracker){var times=cb.kit.getLastFireTimes();times[tracker]=Math.round((new Date()).getTime()/1000);localStorage.setItem('a8cAnalytics_lastFireTimes',JSON.stringify(times));},getSSGAOptimizeVariationId:function(experimentId){var _90Days=90*24*60*60;var experiments=docCookies.getItem('_gaexp_a8c');var currentTime=cb.kit.currentTime();try{experiments=experiments?JSON.parse(experiments):{};}catch(e){experiments={};}
experiments='object'===typeof experiments?experiments:{};if(experiments[experimentId]&&experiments[experimentId].v&&(experiments[experimentId].ts||0)>=currentTime-_90Days){return experiments[experimentId].v;}},loadGoogleAnalytics:function(){(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','//www.google-analytics.com/analytics.js','ga');},loadGoogleTagManager:function(gtm_id){(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer',gtm_id);},loadFacebook:function(){!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');},loadTwitter:function(){!function(e,t,n,s,u,a){e.twq||(s=e.twq=function(){s.exe?s.exe.apply(s,arguments):s.queue.push(arguments);},s.version='1.1',s.queue=[],u=t.createElement(n),u.async=!0,u.src='//static.ads-twitter.com/uwt.js',a=t.getElementsByTagName(n)[0],a.parentNode.insertBefore(u,a))}(window,document,'script');},loadGtag:function(trackingId,options){options=typeof options!=='undefined'?options:{};if(false==='gtag'in window){cb.kit.attachScriptElement('https://www.googletagmanager.com/gtag/js?id='+trackingId,{},function(){});window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments);}
window.gtag('js',new Date());window.gtag('config',trackingId,options);}else{window.gtag('config',trackingId,options);}},loadPinterest:function(){if(!window.pintrk){cb.kit.attachScriptElement('https://s.pinimg.com/ct/core.js',{},function(){});window.pintrk=function(){window.pintrk.queue.push(Array.prototype.slice.call(arguments));};var n=window.pintrk;n.queue=[];n.version='3.0';}},loadAdRoll:function(){if(!window.__adroll_loaded){window.__adroll_loaded=true;cb.kit.attachScriptElement('https://s.adroll.com/j/roundtrip.js',{},function(){});}},loadYahooGeminiOath:function(){(function(w,d,t,r,u){w[u]=w[u]||[];w[u].push({'projectId':'10000','properties':{'pixelId':'10014088'}});var s=d.createElement(t);s.src=r;s.async=true;s.onload=s.onreadystatechange=function(){var y,rs=this.readyState,c=w[u];if(rs&&rs!="complete"&&rs!="loaded"){return}
try{y=YAHOO.ywa.I13N.fireBeacon;w[u]=[];w[u].push=function(p){y([p])};y(c)}catch(e){}};var scr=d.getElementsByTagName(t)[0],par=scr.parentNode;par.insertBefore(s,scr)})(window,document,"script","https://s.yimg.com/wi/ytc.js","dotq");window.dotq=window.dotq||[];},fireHotjar:function(hjid){(function(h,o,t,j,a,r){h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};h._hjSettings={hjid:hjid,hjsv:5};a=o.getElementsByTagName('head')[0];r=o.createElement('script');r.async=1;r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;a.appendChild(r);})(window,document,'//static.hotjar.com/c/hotjar-','.js?sv=');},fireAdWords:function(data){cb.kit.attachScriptElement('https://www.googleadservices.com/pagead/conversion_async.js',{},function(){window.google_trackConversion(data);});},loadImpactRadius:function(){(function(a,b,c,d,e,f,g){e['ire_o']=c;e[c]=e[c]||function(){(e[c].a=e[c].a||[]).push(arguments)};f=d.createElement(b);g=d.getElementsByTagName(b)[0];f.async=1;f.src=a;g.parentNode.insertBefore(f,g);})('//d.impactradius-event.com/A1450388-e24d-4d48-8f36-14ba28d599111.js','script','ire',document,window);},fireImpactRadius:function(currentUserIdHashShort,currentUserEmailHash){if(typeof window.ire!=='function'){return;}
window.ire('identify',{customerId:currentUserIdHashShort,customerEmail:currentUserEmailHash});window.ire('generateClickId',function(clickId){if('~'===clickId.charAt(0)){return;}
localStorage.setItem('irclickid',clickId);var THIRTY_DAYS_MAX=30*24*60*60;docCookies.setItem('irclickid',clickId,THIRTY_DAYS_MAX,'/','.rootDomain');});},};window.a8cAnalytics.initCookieBanner();$(document).trigger('a8c-analytics:loaded');});