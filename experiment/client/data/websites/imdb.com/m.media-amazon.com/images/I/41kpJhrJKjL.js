(window.webpackJsonpBoomer=window.webpackJsonpBoomer||[]).push([["imdb.IMDbConsumerSiteFooterFeature"],{"1V0srIkwUL":function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=r("k8534MhAUt");e.socialMediaLinks={type:"social",links:{facebookLink:{link:"/whitelist-offsite?url="+encodeURIComponent("https://facebook.com/imdb")+"&page-action=fol_fb&ref=ft_fol_fb",label:"Facebook",name:"facebook",type:"external"},instagramLink:{link:"/whitelist-offsite?url="+encodeURIComponent("https://instagram.com/imdb")+"&page-action=fol_inst&ref=ft_fol_inst",label:"Instagram",name:"instagram",type:"external"},twitchLink:{link:"/whitelist-offsite?url="+encodeURIComponent("https://twitch.tv/IMDb")+"&page-action=fol_twch&ref=ft_fol_twch",label:"Twitch",name:"twitch",type:"external"},twitterLink:{link:"/whitelist-offsite?url="+encodeURIComponent("https://twitter.com/imdb")+"&page-action=fol_tw&ref=ft_fol_tw",label:"Twitter",name:"twitter",type:"external"},youtubeLink:{link:"/whitelist-offsite?url="+encodeURIComponent("https://youtube.com/imdb/")+"&page-action=fol_yt&ref=ft_fol_yt",label:"YouTube",name:"youtube",type:"external"}}},e.firstRowIMDbLinks={links:{appLink:{link:"/whitelist-offsite?url="+encodeURIComponent("https://tqp-4.tlnk.io/serve?action=click&campaign_id_android=427112&campaign_id_ios=427111&destination_id_android=464200&destination_id_ios=464199&my_campaign=mdot%20sitewide%20footer%20&my_site=m.imdb.com&publisher_id=350552&site_id_android=133429&site_id_ios=133428")+"&page-action=ft-gettheapp&ref=ft_apps",label:"Get the IMDb App",type:"launch",onScreenSize:"wide",i18nKey:"footer_firstRow_link_imdbApp"},desktopLink:{link:"http://www.imdb.com?ref_=ft_dsk",label:"View Full Site",onScreenSize:"small",i18nKey:"footer_firstRow_link_viewFullSite"},helpLink:{link:"https://help.imdb.com/imdb?ref_=ft_hlp",label:"Help",type:"launch",i18nKey:"footer_firstRow_link_help"},siteIndexLink:{link:"https://help.imdb.com/article/imdb/general-information/imdb-site-index/GNCX7BHNSPBTFALQ?ref_=ft_si#so",label:"Site Index",type:"launch",i18nKey:"footer_firstRow_link_siteIndex"},proLink:{link:"https://pro.imdb.com?ref_=ft_pro&rf=cons_tf_pro",label:"IMDbPro",type:"launch",i18nKey:"footer_firstRow_link_imdbPro"},imdbTVLink:{link:"/tv/?ref_=ft_fdv",label:"IMDb TV",enableFlagName:"showIMDbTVLink",i18nKey:"footer_firstRow_link_imdbTv"},bomojoLink:{label:"Box Office Mojo",link:"https://www.boxofficemojo.com",type:"launch",i18nKey:"footer_firstRow_link_boxOfficeMojo"},developerLink:{label:"IMDb Developer",link:"https://developer.imdb.com/?ref=ft_ds",type:"launch",i18nKey:"footer_firstRow_link_IMDbDeveloper"}}},e.secondRowIMDbLinks={links:{pressroomLink:{label:"Press Room",link:"https://www.imdb.com/pressroom/?ref_=ft_pr",i18nKey:"footer_firstRow_link_pressRoom"},advertisingLink:{label:"Advertising",link:"https://advertising.amazon.com/products/display-ads",type:"launch",i18nKey:"footer_firstRow_link_advertising"},jobsLink:{label:"Jobs",link:"https://www.amazon.jobs/en/teams/imdb?ref_=ft_jb",type:"launch",i18nKey:"footer_secondRow_link_jobs"},termsLink:{link:"/conditions?ref_=ft_cou",label:"Conditions of Use",i18nKey:"footer_secondRow_link_conditionsOfUse"},privacyLink:{link:"/privacy?ref_=ft_pvc",label:"Privacy Policy",i18nKey:"footer_secondRow_link_privacyPolicy"},interestBasedAdsLink:{label:"Interest-Based Ads",link:"/whitelist-offsite?url="+encodeURIComponent("https://www.amazon.com/b/?&node=5160028011&ref_=ft_iba")+"&page-action=ft-iba&ref=ft_iba",type:"launch",i18nKey:"footer_secondRow_link_interestBaseAds"},gdprLink:{label:n.GDPR_LINK,link:n.GDPR_LINK}}},e.ViewModelFixture={ResponsiveFooterModel:{rows:[e.socialMediaLinks,e.firstRowIMDbLinks,e.secondRowIMDbLinks],currentYear:(new Date).getFullYear(),showIMDbTVLink:!0}}},"6++5zMus17":function(t,e,r){"use strict";var n,o=this&&this.__extends||(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var r in e)e.hasOwnProperty(r)&&(t[r]=e[r])})(t,e)},function(t,e){function r(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(r.prototype=e.prototype,new r)}),i=this&&this.__assign||function(){return(i=Object.assign||function(t){for(var e,r=1,n=arguments.length;r<n;r++)for(var o in e=arguments[r])Object.prototype.hasOwnProperty.call(e,o)&&(t[o]=e[o]);return t}).apply(this,arguments)};Object.defineProperty(e,"__esModule",{value:!0});var a=r("LDoPTt+kJa"),l=r("iHhLPsdb7V"),c=r("1V0srIkwUL"),s=r("NM7kAUG+GO"),f=r("C4t8WifyLe");var u=function(t){function e(e){return t.call(this,e)||this}return o(e,t),e.prototype.render=function(){var t=this.props,e=t.ResponsiveFooterModel,r=t.ResponsiveFooterModelOverrides,n=i(i({},c.ViewModelFixture.ResponsiveFooterModel),e);return r&&f(n,r),a.createElement(l.PLAIDProvider,null,a.createElement(s.default,i({},n)))},e}(a.PureComponent);e.Root=u,e.default=u},C4t8WifyLe:function(t,e,r){(function(t,r){var n=200,o="__lodash_hash_undefined__",i=800,a=16,l=9007199254740991,c="[object Arguments]",s="[object AsyncFunction]",f="[object Function]",u="[object GeneratorFunction]",_="[object Null]",p="[object Object]",d="[object Proxy]",h="[object Undefined]",m=/^\[object .+?Constructor\]$/,v=/^(?:0|[1-9]\d*)$/,k={};k["[object Float32Array]"]=k["[object Float64Array]"]=k["[object Int8Array]"]=k["[object Int16Array]"]=k["[object Int32Array]"]=k["[object Uint8Array]"]=k["[object Uint8ClampedArray]"]=k["[object Uint16Array]"]=k["[object Uint32Array]"]=!0,k[c]=k["[object Array]"]=k["[object ArrayBuffer]"]=k["[object Boolean]"]=k["[object DataView]"]=k["[object Date]"]=k["[object Error]"]=k[f]=k["[object Map]"]=k["[object Number]"]=k[p]=k["[object RegExp]"]=k["[object Set]"]=k["[object String]"]=k["[object WeakMap]"]=!1;var b="object"==typeof t&&t&&t.Object===Object&&t,y="object"==typeof self&&self&&self.Object===Object&&self,g=b||y||Function("return this")(),w=e&&!e.nodeType&&e,C=w&&"object"==typeof r&&r&&!r.nodeType&&r,M=C&&C.exports===w,L=M&&b.process,z=function(){try{var t=C&&C.require&&C.require("util").types;return t||L&&L.binding&&L.binding("util")}catch(e){}}(),j=z&&z.isTypedArray;var O,I,A,x=Array.prototype,R=Function.prototype,V=Object.prototype,H=g["__core-js_shared__"],P=R.toString,S=V.hasOwnProperty,D=(O=/[^.]+$/.exec(H&&H.keys&&H.keys.IE_PROTO||""))?"Symbol(src)_1."+O:"",E=V.toString,N=P.call(Object),F=RegExp("^"+P.call(S).replace(/[\\^$.*+?()[\]{}|]/g,"\\$&").replace(/hasOwnProperty|(function).*?(?=\\\()| for .+?(?=\\\])/g,"$1.*?")+"$"),T=M?g.Buffer:void 0,U=g.Symbol,K=g.Uint8Array,G=T?T.allocUnsafe:void 0,B=(I=Object.getPrototypeOf,A=Object,function(t){return I(A(t))}),J=Object.create,q=V.propertyIsEnumerable,W=x.splice,X=U?U.toStringTag:void 0,$=function(){try{var t=gt(Object,"defineProperty");return t({},"",{}),t}catch(e){}}(),Y=T?T.isBuffer:void 0,Z=Math.max,Q=Date.now,tt=gt(g,"Map"),et=gt(Object,"create"),rt=function(){function t(){}return function(e){if(!Vt(e))return{};if(J)return J(e);t.prototype=e;var r=new t;return t.prototype=void 0,r}}();function nt(t){var e=-1,r=null==t?0:t.length;for(this.clear();++e<r;){var n=t[e];this.set(n[0],n[1])}}function ot(t){var e=-1,r=null==t?0:t.length;for(this.clear();++e<r;){var n=t[e];this.set(n[0],n[1])}}function it(t){var e=-1,r=null==t?0:t.length;for(this.clear();++e<r;){var n=t[e];this.set(n[0],n[1])}}function at(t){var e=this.__data__=new ot(t);this.size=e.size}function lt(t,e){var r=Ot(t),n=!r&&jt(t),o=!r&&!n&&At(t),i=!r&&!n&&!o&&Pt(t),a=r||n||o||i,l=a?function(t,e){for(var r=-1,n=Array(t);++r<t;)n[r]=e(r);return n}(t.length,String):[],c=l.length;for(var s in t)!e&&!S.call(t,s)||a&&("length"==s||o&&("offset"==s||"parent"==s)||i&&("buffer"==s||"byteLength"==s||"byteOffset"==s)||wt(s,c))||l.push(s);return l}function ct(t,e,r){(void 0===r||zt(t[e],r))&&(void 0!==r||e in t)||ut(t,e,r)}function st(t,e,r){var n=t[e];S.call(t,e)&&zt(n,r)&&(void 0!==r||e in t)||ut(t,e,r)}function ft(t,e){for(var r=t.length;r--;)if(zt(t[r][0],e))return r;return-1}function ut(t,e,r){"__proto__"==e&&$?$(t,e,{configurable:!0,enumerable:!0,value:r,writable:!0}):t[e]=r}nt.prototype.clear=function(){this.__data__=et?et(null):{},this.size=0},nt.prototype.delete=function(t){var e=this.has(t)&&delete this.__data__[t];return this.size-=e?1:0,e},nt.prototype.get=function(t){var e=this.__data__;if(et){var r=e[t];return r===o?void 0:r}return S.call(e,t)?e[t]:void 0},nt.prototype.has=function(t){var e=this.__data__;return et?void 0!==e[t]:S.call(e,t)},nt.prototype.set=function(t,e){var r=this.__data__;return this.size+=this.has(t)?0:1,r[t]=et&&void 0===e?o:e,this},ot.prototype.clear=function(){this.__data__=[],this.size=0},ot.prototype.delete=function(t){var e=this.__data__,r=ft(e,t);return!(r<0||(r==e.length-1?e.pop():W.call(e,r,1),--this.size,0))},ot.prototype.get=function(t){var e=this.__data__,r=ft(e,t);return r<0?void 0:e[r][1]},ot.prototype.has=function(t){return ft(this.__data__,t)>-1},ot.prototype.set=function(t,e){var r=this.__data__,n=ft(r,t);return n<0?(++this.size,r.push([t,e])):r[n][1]=e,this},it.prototype.clear=function(){this.size=0,this.__data__={hash:new nt,map:new(tt||ot),string:new nt}},it.prototype.delete=function(t){var e=yt(this,t).delete(t);return this.size-=e?1:0,e},it.prototype.get=function(t){return yt(this,t).get(t)},it.prototype.has=function(t){return yt(this,t).has(t)},it.prototype.set=function(t,e){var r=yt(this,t),n=r.size;return r.set(t,e),this.size+=r.size==n?0:1,this},at.prototype.clear=function(){this.__data__=new ot,this.size=0},at.prototype.delete=function(t){var e=this.__data__,r=e.delete(t);return this.size=e.size,r},at.prototype.get=function(t){return this.__data__.get(t)},at.prototype.has=function(t){return this.__data__.has(t)},at.prototype.set=function(t,e){var r=this.__data__;if(r instanceof ot){var o=r.__data__;if(!tt||o.length<n-1)return o.push([t,e]),this.size=++r.size,this;r=this.__data__=new it(o)}return r.set(t,e),this.size=r.size,this};var _t,pt=function(t,e,r){for(var n=-1,o=Object(t),i=r(t),a=i.length;a--;){var l=i[_t?a:++n];if(!1===e(o[l],l,o))break}return t};function dt(t){return null==t?void 0===t?h:_:X&&X in Object(t)?function(t){var e=S.call(t,X),r=t[X];try{t[X]=void 0;var n=!0}catch(i){}var o=E.call(t);n&&(e?t[X]=r:delete t[X]);return o}(t):function(t){return E.call(t)}(t)}function ht(t){return Ht(t)&&dt(t)==c}function mt(t){return!(!Vt(t)||function(t){return!!D&&D in t}(t))&&(xt(t)?F:m).test(function(t){if(null!=t){try{return P.call(t)}catch(e){}try{return t+""}catch(e){}}return""}(t))}function vt(t){if(!Vt(t))return function(t){var e=[];if(null!=t)for(var r in Object(t))e.push(r);return e}(t);var e=Ct(t),r=[];for(var n in t)("constructor"!=n||!e&&S.call(t,n))&&r.push(n);return r}function kt(t,e,r,n,o){t!==e&&pt(e,function(i,a){if(o||(o=new at),Vt(i))!function(t,e,r,n,o,i,a){var l=Mt(t,r),c=Mt(e,r),s=a.get(c);if(s)return void ct(t,r,s);var f=i?i(l,c,r+"",t,e,a):void 0,u=void 0===f;if(u){var _=Ot(c),d=!_&&At(c),h=!_&&!d&&Pt(c);f=c,_||d||h?Ot(l)?f=l:Ht(y=l)&&It(y)?f=function(t,e){var r=-1,n=t.length;e||(e=Array(n));for(;++r<n;)e[r]=t[r];return e}(l):d?(u=!1,f=function(t,e){if(e)return t.slice();var r=t.length,n=G?G(r):new t.constructor(r);return t.copy(n),n}(c,!0)):h?(u=!1,m=c,v=!0?(k=m.buffer,b=new k.constructor(k.byteLength),new K(b).set(new K(k)),b):m.buffer,f=new m.constructor(v,m.byteOffset,m.length)):f=[]:function(t){if(!Ht(t)||dt(t)!=p)return!1;var e=B(t);if(null===e)return!0;var r=S.call(e,"constructor")&&e.constructor;return"function"==typeof r&&r instanceof r&&P.call(r)==N}(c)||jt(c)?(f=l,jt(l)?f=function(t){return function(t,e,r,n){var o=!r;r||(r={});var i=-1,a=e.length;for(;++i<a;){var l=e[i],c=n?n(r[l],t[l],l,r,t):void 0;void 0===c&&(c=t[l]),o?ut(r,l,c):st(r,l,c)}return r}(t,St(t))}(l):Vt(l)&&!xt(l)||(f=function(t){return"function"!=typeof t.constructor||Ct(t)?{}:rt(B(t))}(c))):u=!1}var m,v,k,b;var y;u&&(a.set(c,f),o(f,c,n,i,a),a.delete(c));ct(t,r,f)}(t,e,a,r,kt,n,o);else{var l=n?n(Mt(t,a),i,a+"",t,e,o):void 0;void 0===l&&(l=i),ct(t,a,l)}},St)}function bt(t,e){return Lt(function(t,e,r){return e=Z(void 0===e?t.length-1:e,0),function(){for(var n=arguments,o=-1,i=Z(n.length-e,0),a=Array(i);++o<i;)a[o]=n[e+o];o=-1;for(var l=Array(e+1);++o<e;)l[o]=n[o];return l[e]=r(a),function(t,e,r){switch(r.length){case 0:return t.call(e);case 1:return t.call(e,r[0]);case 2:return t.call(e,r[0],r[1]);case 3:return t.call(e,r[0],r[1],r[2])}return t.apply(e,r)}(t,this,l)}}(t,e,Nt),t+"")}function yt(t,e){var r,n,o=t.__data__;return("string"==(n=typeof(r=e))||"number"==n||"symbol"==n||"boolean"==n?"__proto__"!==r:null===r)?o["string"==typeof e?"string":"hash"]:o.map}function gt(t,e){var r=function(t,e){return null==t?void 0:t[e]}(t,e);return mt(r)?r:void 0}function wt(t,e){var r=typeof t;return!!(e=null==e?l:e)&&("number"==r||"symbol"!=r&&v.test(t))&&t>-1&&t%1==0&&t<e}function Ct(t){var e=t&&t.constructor;return t===("function"==typeof e&&e.prototype||V)}function Mt(t,e){if(("constructor"!==e||"function"!=typeof t[e])&&"__proto__"!=e)return t[e]}var Lt=function(t){var e=0,r=0;return function(){var n=Q(),o=a-(n-r);if(r=n,o>0){if(++e>=i)return arguments[0]}else e=0;return t.apply(void 0,arguments)}}($?function(t,e){return $(t,"toString",{configurable:!0,enumerable:!1,value:(r=e,function(){return r}),writable:!0});var r}:Nt);function zt(t,e){return t===e||t!=t&&e!=e}var jt=ht(function(){return arguments}())?ht:function(t){return Ht(t)&&S.call(t,"callee")&&!q.call(t,"callee")},Ot=Array.isArray;function It(t){return null!=t&&Rt(t.length)&&!xt(t)}var At=Y||function(){return!1};function xt(t){if(!Vt(t))return!1;var e=dt(t);return e==f||e==u||e==s||e==d}function Rt(t){return"number"==typeof t&&t>-1&&t%1==0&&t<=l}function Vt(t){var e=typeof t;return null!=t&&("object"==e||"function"==e)}function Ht(t){return null!=t&&"object"==typeof t}var Pt=j?function(t){return function(e){return t(e)}}(j):function(t){return Ht(t)&&Rt(t.length)&&!!k[dt(t)]};function St(t){return It(t)?lt(t,!0):vt(t)}var Dt,Et=(Dt=function(t,e,r){kt(t,e,r)},bt(function(t,e){var r=-1,n=e.length,o=n>1?e[n-1]:void 0,i=n>2?e[2]:void 0;for(o=Dt.length>3&&"function"==typeof o?(n--,o):void 0,i&&function(t,e,r){if(!Vt(r))return!1;var n=typeof e;return!!("number"==n?It(r)&&wt(e,r.length):"string"==n&&e in r)&&zt(r[e],t)}(e[0],e[1],i)&&(o=n<3?void 0:o,n=1),t=Object(t);++r<n;){var a=e[r];a&&Dt(t,a,r,o)}return t}));function Nt(t){return t}r.exports=Et}).call(this,r("qv/MW4HMFk"),r("8EmIRJSvdI")(t))},"NM7kAUG+GO":function(t,e,r){"use strict";var n,o=this&&this.__extends||(n=function(t,e){return(n=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(t,e){t.__proto__=e}||function(t,e){for(var r in e)e.hasOwnProperty(r)&&(t[r]=e[r])})(t,e)},function(t,e){function r(){this.constructor=t}n(t,e),t.prototype=null===e?Object.create(e):(r.prototype=e.prototype,new r)});Object.defineProperty(e,"__esModule",{value:!0});var i=r("LDoPTt+kJa"),a=r("Kkip5aHMh7"),l=r("qDO/KKoIw4"),c=r("k8534MhAUt"),s=r("eOAkKVFSZf"),f={small:s.smallScreenOnly,wide:s.wideScreenOnly},u={social:s.socialMediaLinks},_=function(t){function e(){var e=null!==t&&t.apply(this,arguments)||this;return e.renderLink=function(t,r){if(t.enableFlagName&&void 0!==e.props[t.enableFlagName]&&!e.props[t.enableFlagName])return null;if(t.label===c.GDPR_LINK)return i.createElement(l.InlineListItem,{key:r},i.createElement("div",{id:c.TRUSTARC_CONTAINER_ID}));var n=t.link;e.props[r]&&(n=e.props[r]);var o=i.createElement(l.TextLink,{href:n,text:t.label,touchTarget:!0,inheritColor:!0,type:t.type});return t.name&&(o=i.createElement(l.IconLink,{href:n,label:t.label,name:t.name,type:t.type})),i.createElement(l.InlineListItem,{className:t.onScreenSize?f[t.onScreenSize]:void 0,key:r},o)},e.renderRow=function(t,r){var n=Object.keys(t.links);return i.createElement("div",{key:"footer-row-"+r,className:t.type?u[t.type]:void 0},i.createElement(l.InlineList,{className:s.linkListRow},n.map(function(r){return e.renderLink(t.links[r],r)})))},e}return o(e,t),e.prototype.render=function(){var t=this.props,e=t.rows,r=t.currentYear;return i.createElement(l.SetPalette,{palette:"dark"},i.createElement("footer",{className:a("imdb-footer",s.footer)},!(!e[1]||!e[1].links.appLink)&&i.createElement("div",{className:s.openAppContainer},i.createElement(l.PageContentContainer,{orientContent:"center"},i.createElement(l.ButtonLink,{className:"imdb-footer__open-in-app-button",width:"double-padding",href:e[1].links.appLink.link},e[1].links.appLink.label))),i.createElement(l.PageContentContainer,{orientContent:"center",className:s.linksContainer},i.createElement("div",{className:"imdb-footer__links"},e.map(this.renderRow)),i.createElement("div",{className:a("imdb-footer__logo",s.logo),dangerouslySetInnerHTML:{__html:c.LOGO_SVG}}),i.createElement("p",{className:a("imdb-footer__copyright",s.copyright)},"© 1990-",r," by IMDb.com, Inc."))))},e}(i.PureComponent);e.Footer=_,e.default=_},eOAkKVFSZf:function(t,e,r){t.exports={footer:"_TLXOR4lOiPIyTmiJ0dPW",openAppContainer:"ZNUbpZKH8xCwa1W-_fcXn",socialMediaLinks:"_27Hr-itnXHPpOoaB59daSz",logo:"_2xLxFM9nEN1i2gy27-iTkh",copyright:"_1qNTRY72M5RnFTeiT5Ho-6",linksContainer:"_3z5OrvzxXylpc4E_IkyaJo",linkListRow:"_1W6LtHiV5M-NUnes6xN1az",wideScreenOnly:"_3H6AMKfSRpYQwV79UPZXvX",smallScreenOnly:"_9IvGhSADepoeM_bOcxcJ"}},k8534MhAUt:function(t,e,r){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.LOGO_LABEL="IMDb, an Amazon company",e.TRUSTARC_CONTAINER_ID="teconsent",e.GDPR_LINK="gdpr",e.LOGO_SVG='<svg aria-label="'+e.LOGO_LABEL+'" title="'+e.LOGO_LABEL+'" width="160" height="18" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><defs><path d="M26.707 2.45c-3.227 2.374-7.906 3.637-11.935 3.637C9.125 6.087 4.04 4.006.193.542-.11.27.161-.101.523.109 4.675 2.517 9.81 3.968 15.111 3.968c3.577 0 7.51-.74 11.127-2.27.546-.23 1.003.358.47.752z" id="ftr__a"/><path d="M4.113 1.677C3.7 1.15 1.385 1.427.344 1.552c-.315.037-.364-.237-.08-.436C2.112-.178 5.138.196 5.49.629c.354.437-.093 3.462-1.824 4.906-.266.222-.52.104-.401-.19.39-.97 1.261-3.14.848-3.668z" id="ftr__c"/><path d="M.435 1.805V.548A.311.311 0 0 1 .755.23l5.65-.001c.181 0 .326.13.326.317v1.078c-.002.181-.154.417-.425.791L3.378 6.582c1.087-.026 2.236.137 3.224.69.222.125.282.309.3.49v1.342c0 .185-.203.398-.417.287-1.74-.908-4.047-1.008-5.97.011-.197.104-.403-.107-.403-.292V7.835c0-.204.004-.552.21-.863l3.392-4.85H.761a.314.314 0 0 1-.326-.317z" id="ftr__e"/><path d="M2.247 9.655H.528a.323.323 0 0 1-.307-.29L.222.569C.222.393.37.253.554.253h1.601a.323.323 0 0 1 .313.295v1.148h.031C2.917.586 3.703.067 4.762.067c1.075 0 1.75.518 2.23 1.629C7.41.586 8.358.067 9.369.067c.722 0 1.508.296 1.99.963.545.74.433 1.813.433 2.757l-.002 5.551a.324.324 0 0 1-.331.317H9.74a.321.321 0 0 1-.308-.316l-.001-4.663c0-.37.032-1.296-.048-1.647-.128-.593-.514-.76-1.011-.76-.418 0-.85.278-1.027.722-.177.445-.161 1.185-.161 1.685v4.662a.323.323 0 0 1-.331.317H5.137a.322.322 0 0 1-.31-.316l-.001-4.663c0-.981.16-2.424-1.059-2.424-1.236 0-1.188 1.406-1.188 2.424v4.662a.324.324 0 0 1-.332.317z" id="ftr__g"/><path d="M4.037.067c2.551 0 3.931 2.184 3.931 4.96 0 2.684-1.524 4.814-3.931 4.814C1.533 9.84.169 7.656.169 4.935.17 2.195 1.55.067 4.037.067zm.015 1.796c-1.267 0-1.347 1.721-1.347 2.795 0 1.073-.016 3.368 1.332 3.368 1.332 0 1.395-1.851 1.395-2.98 0-.74-.031-1.629-.256-2.332-.193-.61-.578-.851-1.124-.851z" id="ftr__i"/><path d="M2.206 9.655H.493a.321.321 0 0 1-.308-.316L.182.54a.325.325 0 0 1 .33-.287h1.595c.15.007.274.109.305.245v1.346h.033C2.926.641 3.6.067 4.788.067c.77 0 1.524.277 2.006 1.037.449.703.449 1.887.449 2.739v5.535a.325.325 0 0 1-.33.277H5.19a.324.324 0 0 1-.306-.277V4.602c0-.962.113-2.37-1.075-2.37-.418 0-.803.278-.995.704-.24.537-.273 1.074-.273 1.666v4.736a.328.328 0 0 1-.335.317z" id="ftr__k"/><path d="M8.314 8.295c.11.156.134.341-.006.455-.35.294-.974.834-1.318 1.139l-.004-.004a.357.357 0 0 1-.406.04c-.571-.473-.673-.692-.986-1.142-.943.958-1.611 1.246-2.834 1.246-1.447 0-2.573-.89-2.573-2.672 0-1.39.756-2.337 1.833-2.8.933-.409 2.235-.483 3.233-.595V3.74c0-.409.032-.89-.209-1.243-.21-.315-.611-.445-.965-.445-.656 0-1.238.335-1.382 1.029-.03.154-.143.307-.298.315l-1.667-.18c-.14-.032-.297-.144-.256-.358C.859.842 2.684.234 4.32.234c.837 0 1.93.222 2.59.853.836.78.755 1.818.755 2.95v2.67c0 .804.335 1.155.65 1.588zM5.253 5.706v-.37c-1.244 0-2.557.265-2.557 1.724 0 .742.386 1.244 1.045 1.244.483 0 .917-.297 1.19-.78.338-.593.322-1.15.322-1.818z" id="ftr__m"/><path d="M8.203 8.295c.11.156.135.341-.005.455-.352.294-.976.834-1.319 1.139l-.004-.004a.356.356 0 0 1-.406.04c-.571-.473-.673-.692-.985-1.142-.944.958-1.613 1.246-2.835 1.246-1.447 0-2.573-.89-2.573-2.672 0-1.39.756-2.337 1.833-2.8.933-.409 2.236-.483 3.233-.595V3.74c0-.409.032-.89-.21-1.243-.208-.315-.61-.445-.964-.445-.656 0-1.239.335-1.382 1.029-.03.154-.142.307-.298.315l-1.666-.18C.48 3.184.324 3.072.365 2.858.748.842 2.573.234 4.209.234c.836 0 1.93.222 2.59.853.835.78.755 1.818.755 2.95v2.67c0 .804.335 1.155.649 1.588zM5.142 5.706v-.37c-1.243 0-2.557.265-2.557 1.724 0 .742.386 1.244 1.045 1.244.482 0 .917-.297 1.19-.78.338-.593.322-1.15.322-1.818z" id="ftr__o"/><path d="M2.935 10.148c-.88 0-1.583-.25-2.11-.75-.527-.501-.79-1.171-.79-2.011 0-.902.322-1.622.967-2.159.644-.538 1.511-.806 2.602-.806.694 0 1.475.104 2.342.315V3.513c0-.667-.151-1.136-.455-1.408-.304-.271-.821-.407-1.553-.407-.855 0-1.691.123-2.509.37-.285.087-.464.13-.539.13-.148 0-.223-.111-.223-.334v-.5c0-.16.025-.278.075-.352C.79.938.89.87 1.039.808c.383-.173.87-.312 1.459-.417A9.997 9.997 0 0 1 4.255.234c1.177 0 2.045.244 2.602.731.557.489.836 1.233.836 2.233v6.338c0 .247-.124.37-.372.37h-.798c-.236 0-.373-.117-.41-.351l-.093-.612c-.445.383-.939.68-1.477.89-.54.21-1.076.315-1.608.315zm.446-1.39c.41 0 .836-.08 1.282-.241.447-.16.874-.395 1.283-.704v-1.89a8.408 8.408 0 0 0-1.97-.241c-1.401 0-2.1.537-2.1 1.612 0 .47.13.831.39 1.084.26.254.632.38 1.115.38z" id="ftr__q"/><path d="M.467 9.907c-.248 0-.372-.124-.372-.37V.883C.095.635.219.51.467.51h.817c.125 0 .22.026.288.075.068.05.115.142.14.277l.111.686C3 .672 4.24.234 5.541.234c.904 0 1.592.238 2.063.713.471.476.707 1.165.707 2.066v6.524c0 .246-.124.37-.372.37H6.842c-.248 0-.372-.124-.372-.37V3.625c0-.655-.133-1.137-.4-1.445-.266-.31-.684-.464-1.254-.464-.979 0-1.94.315-2.881.946v6.875c0 .246-.125.37-.372.37H.467z" id="ftr__s"/><path d="M4.641 9.859c-1.462 0-2.58-.417-3.355-1.251C.51 7.774.124 6.566.124 4.985c0-1.569.4-2.783 1.2-3.641C2.121.486 3.252.055 4.714.055c.67 0 1.326.118 1.971.353.136.05.232.111.288.185.056.074.083.198.083.37v.501c0 .248-.08.37-.241.37-.062 0-.162-.018-.297-.055a5.488 5.488 0 0 0-1.544-.222c-1.04 0-1.79.262-2.248.787-.459.526-.688 1.362-.688 2.511v.241c0 1.124.232 1.949.697 2.474.465.525 1.198.788 2.203.788a5.98 5.98 0 0 0 1.672-.26c.136-.037.23-.056.279-.056.161 0 .242.124.242.371v.5c0 .162-.025.279-.075.353-.05.074-.148.142-.297.204-.608.259-1.314.389-2.119.389z" id="ftr__u"/><path d="M4.598 10.185c-1.413 0-2.516-.438-3.31-1.316C.497 7.992.1 6.769.1 5.199c0-1.555.397-2.773 1.19-3.65C2.082.673 3.185.235 4.598.235c1.412 0 2.515.438 3.308 1.316.793.876 1.19 2.094 1.19 3.65 0 1.569-.397 2.792-1.19 3.669-.793.878-1.896 1.316-3.308 1.316zm0-1.483c1.747 0 2.62-1.167 2.62-3.502 0-2.323-.873-3.484-2.62-3.484S1.977 2.877 1.977 5.2c0 2.335.874 3.502 2.62 3.502z" id="ftr__w"/><path d="M.396 9.907c-.248 0-.371-.124-.371-.37V.883C.025.635.148.51.396.51h.818a.49.49 0 0 1 .288.075c.068.05.115.142.14.277l.111.594C2.943.64 4.102.234 5.23.234c1.152 0 1.934.438 2.342 1.315C8.798.672 10.025.234 11.25.234c.856 0 1.512.24 1.971.722.458.482.688 1.168.688 2.057v6.524c0 .246-.124.37-.372.37h-1.097c-.248 0-.371-.124-.371-.37V3.533c0-.618-.119-1.075-.354-1.372-.235-.297-.607-.445-1.115-.445-.904 0-1.815.278-2.732.834.012.087.018.18.018.278v6.709c0 .246-.124.37-.372.37H6.42c-.249 0-.372-.124-.372-.37V3.533c0-.618-.118-1.075-.353-1.372-.235-.297-.608-.445-1.115-.445-.942 0-1.847.272-2.714.815v7.006c0 .246-.125.37-.372.37H.396z" id="ftr__y"/><path d="M.617 13.724c-.248 0-.371-.124-.371-.37V.882c0-.247.123-.37.371-.37h.818c.248 0 .39.123.428.37l.093.594C2.897.648 3.944.234 5.096.234c1.203 0 2.15.435 2.845 1.307.693.87 1.04 2.053 1.04 3.548 0 1.52-.365 2.736-1.096 3.65-.731.915-1.704 1.372-2.918 1.372-1.116 0-2.076-.365-2.881-1.094v4.337c0 .246-.125.37-.372.37H.617zM4.54 8.628c1.71 0 2.566-1.149 2.566-3.447 0-1.173-.208-2.044-.624-2.612-.415-.569-1.05-.853-1.904-.853-.88 0-1.711.284-2.491.853v5.17c.805.593 1.623.889 2.453.889z" id="ftr__A"/><path d="M2.971 10.148c-.88 0-1.583-.25-2.11-.75-.526-.501-.79-1.171-.79-2.011 0-.902.322-1.622.967-2.159.644-.538 1.512-.806 2.602-.806.694 0 1.475.104 2.342.315V3.513c0-.667-.15-1.136-.455-1.408-.304-.271-.821-.407-1.552-.407-.855 0-1.692.123-2.509.37-.285.087-.465.13-.54.13-.148 0-.223-.111-.223-.334v-.5c0-.16.025-.278.075-.352.05-.074.148-.142.297-.204.384-.173.87-.312 1.46-.417A9.991 9.991 0 0 1 4.29.234c1.177 0 2.045.244 2.603.731.557.489.836 1.233.836 2.233v6.338c0 .247-.125.37-.372.37h-.799c-.236 0-.372-.117-.41-.351l-.092-.612a5.09 5.09 0 0 1-1.478.89 4.4 4.4 0 0 1-1.608.315zm.446-1.39c.41 0 .836-.08 1.283-.241.446-.16.874-.395 1.282-.704v-1.89a8.403 8.403 0 0 0-1.97-.241c-1.4 0-2.1.537-2.1 1.612 0 .47.13.831.39 1.084.26.254.632.38 1.115.38z" id="ftr__C"/><path d="M.503 9.907c-.248 0-.371-.124-.371-.37V.883C.132.635.255.51.503.51h.818a.49.49 0 0 1 .288.075c.068.05.115.142.14.277l.111.686C3.037.672 4.277.234 5.578.234c.904 0 1.592.238 2.063.713.47.476.706 1.165.706 2.066v6.524c0 .246-.123.37-.371.37H6.879c-.248 0-.372-.124-.372-.37V3.625c0-.655-.133-1.137-.4-1.445-.266-.31-.684-.464-1.254-.464-.98 0-1.94.315-2.882.946v6.875c0 .246-.124.37-.371.37H.503z" id="ftr__E"/><path d="M1.988 13.443c-.397 0-.75-.043-1.059-.13-.15-.037-.251-.1-.307-.185a.684.684 0 0 1-.084-.37v-.483c0-.234.093-.352.28-.352.06 0 .154.013.278.037.124.025.291.037.502.037.459 0 .82-.114 1.087-.343.266-.228.505-.633.716-1.213l.353-.945L.167.675C.08.465.037.316.037.23c0-.149.086-.222.26-.222h1.115c.198 0 .334.03.409.093.075.062.148.197.223.407l2.602 7.19 2.51-7.19c.074-.21.148-.345.222-.407.075-.062.211-.093.41-.093h1.04c.174 0 .261.073.261.222 0 .086-.044.235-.13.445l-4.09 10.377c-.334.853-.725 1.464-1.17 1.835-.446.37-1.017.556-1.711.556z" id="ftr__G"/></defs><g fill="none" fill-rule="evenodd"><g transform="translate(31.496 11.553)"><mask id="ftr__b" fill="currentColor"><use xlink:href="#ftr__a"/></mask><path fill="currentColor" mask="url(#ftr__b)" d="M.04 6.088h26.91V.04H.04z"/></g><g transform="translate(55.433 10.797)"><mask id="ftr__d" fill="currentColor"><use xlink:href="#ftr__c"/></mask><path fill="currentColor" mask="url(#ftr__d)" d="M.05 5.664h5.564V.222H.05z"/></g><g transform="translate(55.433 .97)"><mask id="ftr__f" fill="currentColor"><use xlink:href="#ftr__e"/></mask><path fill="currentColor" mask="url(#ftr__f)" d="M.11 9.444h6.804V.222H.111z"/></g><g transform="translate(33.008 .97)"><mask id="ftr__h" fill="currentColor"><use xlink:href="#ftr__g"/></mask><path fill="currentColor" mask="url(#ftr__h)" d="M.191 9.655h11.611V.04H.192z"/></g><g transform="translate(62.992 .97)"><mask id="ftr__j" fill="currentColor"><use xlink:href="#ftr__i"/></mask><path fill="currentColor" mask="url(#ftr__j)" d="M.141 9.867h7.831V.04H.142z"/></g><g transform="translate(72.063 .97)"><mask id="ftr__l" fill="currentColor"><use xlink:href="#ftr__k"/></mask><path fill="currentColor" mask="url(#ftr__l)" d="M.171 9.655h7.076V.04H.17z"/></g><g transform="translate(46.11 .718)"><mask id="ftr__n" fill="currentColor"><use xlink:href="#ftr__m"/></mask><path fill="currentColor" mask="url(#ftr__n)" d="M.181 10.059h8.225V.232H.18z"/></g><g transform="translate(23.685 .718)"><mask id="ftr__p" fill="currentColor"><use xlink:href="#ftr__o"/></mask><path fill="currentColor" mask="url(#ftr__p)" d="M.05 10.059h8.255V.232H.05z"/></g><g transform="translate(0 .718)"><mask id="ftr__r" fill="currentColor"><use xlink:href="#ftr__q"/></mask><path fill="currentColor" mask="url(#ftr__r)" d="M.03 10.15h7.68V.231H.03z"/></g><g transform="translate(10.33 .718)"><mask id="ftr__t" fill="currentColor"><use xlink:href="#ftr__s"/></mask><path fill="currentColor" mask="url(#ftr__t)" d="M.07 9.907h8.255V.232H.071z"/></g><g transform="translate(84.157 .97)"><mask id="ftr__v" fill="currentColor"><use xlink:href="#ftr__u"/></mask><path fill="currentColor" mask="url(#ftr__v)" d="M.11 9.867h7.046V.04H.11z"/></g><g transform="translate(92.472 .718)"><mask id="ftr__x" fill="currentColor"><use xlink:href="#ftr__w"/></mask><path fill="currentColor" mask="url(#ftr__x)" d="M.08 10.21h9.041V.232H.081z"/></g><g transform="translate(103.811 .718)"><mask id="ftr__z" fill="currentColor"><use xlink:href="#ftr__y"/></mask><path fill="currentColor" mask="url(#ftr__z)" d="M.02 9.907H13.93V.232H.02z"/></g><g transform="translate(120.189 .718)"><mask id="ftr__B" fill="currentColor"><use xlink:href="#ftr__A"/></mask><path fill="currentColor" mask="url(#ftr__B)" d="M.242 13.747H9.01V.232H.242z"/></g><g transform="translate(130.772 .718)"><mask id="ftr__D" fill="currentColor"><use xlink:href="#ftr__C"/></mask><path fill="currentColor" mask="url(#ftr__D)" d="M.06 10.15h7.68V.231H.06z"/></g><g transform="translate(141.102 .718)"><mask id="ftr__F" fill="currentColor"><use xlink:href="#ftr__E"/></mask><path fill="currentColor" mask="url(#ftr__F)" d="M.131 9.907h8.224V.232H.131z"/></g><g transform="translate(150.677 1.222)"><mask id="ftr__H" fill="currentColor"><use xlink:href="#ftr__G"/></mask><path fill="currentColor" mask="url(#ftr__H)" d="M.02 13.455h9.071V0H.021z"/></g></g></svg>'}}]);