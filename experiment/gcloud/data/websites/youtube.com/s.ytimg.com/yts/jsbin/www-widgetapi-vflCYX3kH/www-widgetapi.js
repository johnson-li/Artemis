(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var r;function aa(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}}
var ba="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};
function ca(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("Cannot find global object");}
var da=ca(this);function t(a,b){if(b)a:{for(var c=da,d=a.split("."),e=0;e<d.length-1;e++){var f=d[e];if(!(f in c))break a;c=c[f]}d=d[d.length-1];e=c[d];f=b(e);f!=e&&null!=f&&ba(c,d,{configurable:!0,writable:!0,value:f})}}
t("Symbol",function(a){function b(e){if(this instanceof b)throw new TypeError("Symbol is not a constructor");return new c("jscomp_symbol_"+(e||"")+"_"+d++,e)}
function c(e,f){this.f=e;ba(this,"description",{configurable:!0,writable:!0,value:f})}
if(a)return a;c.prototype.toString=function(){return this.f};
var d=0;return b});
t("Symbol.iterator",function(a){if(a)return a;a=Symbol("Symbol.iterator");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=da[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&ba(d.prototype,a,{configurable:!0,writable:!0,value:function(){return ea(aa(this))}})}return a});
function ea(a){a={next:a};a[Symbol.iterator]=function(){return this};
return a}
function u(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:aa(a)}}
function fa(a){for(var b,c=[];!(b=a.next()).done;)c.push(b.value);return c}
var ha="function"==typeof Object.create?Object.create:function(a){function b(){}
b.prototype=a;return new b},ia;
if("function"==typeof Object.setPrototypeOf)ia=Object.setPrototypeOf;else{var ja;a:{var ka={a:!0},la={};try{la.__proto__=ka;ja=la.a;break a}catch(a){}ja=!1}ia=ja?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError(a+" is not extensible");return a}:null}var ma=ia;
function na(a,b){a.prototype=ha(b.prototype);a.prototype.constructor=a;if(ma)ma(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.D=b.prototype}
function oa(){this.m=!1;this.i=null;this.g=void 0;this.f=1;this.j=this.l=0;this.A=this.h=null}
function qa(a){if(a.m)throw new TypeError("Generator is already running");a.m=!0}
oa.prototype.s=function(a){this.g=a};
function ra(a,b){a.h={da:b,S:!0};a.f=a.l||a.j}
oa.prototype["return"]=function(a){this.h={"return":a};this.f=this.j};
function x(a,b,c){a.f=c;return{value:b}}
oa.prototype.v=function(a){this.f=a};
function sa(a){a.l=2;a.j=3}
function ta(a){a.l=0;a.h=null}
function ua(a){a.A=[a.h];a.l=0;a.j=0}
function va(a){var b=a.A.splice(0)[0];(b=a.h=a.h||b)?b.S?a.f=a.l||a.j:void 0!=b.v&&a.j<b.v?(a.f=b.v,a.h=null):a.f=a.j:a.f=0}
function wa(a){this.f=new oa;this.g=a}
function xa(a,b){qa(a.f);var c=a.f.i;if(c)return ya(a,"return"in c?c["return"]:function(d){return{value:d,done:!0}},b,a.f["return"]);
a.f["return"](b);return za(a)}
function ya(a,b,c,d){try{var e=b.call(a.f.i,c);if(!(e instanceof Object))throw new TypeError("Iterator result "+e+" is not an object");if(!e.done)return a.f.m=!1,e;var f=e.value}catch(g){return a.f.i=null,ra(a.f,g),za(a)}a.f.i=null;d.call(a.f,f);return za(a)}
function za(a){for(;a.f.f;)try{var b=a.g(a.f);if(b)return a.f.m=!1,{value:b.value,done:!1}}catch(c){a.f.g=void 0,ra(a.f,c)}a.f.m=!1;if(a.f.h){b=a.f.h;a.f.h=null;if(b.S)throw b.da;return{value:b["return"],done:!0}}return{value:void 0,done:!0}}
function Aa(a){this.next=function(b){qa(a.f);a.f.i?b=ya(a,a.f.i.next,b,a.f.s):(a.f.s(b),b=za(a));return b};
this["throw"]=function(b){qa(a.f);a.f.i?b=ya(a,a.f.i["throw"],b,a.f.s):(ra(a.f,b),b=za(a));return b};
this["return"]=function(b){return xa(a,b)};
this[Symbol.iterator]=function(){return this}}
function y(a,b){var c=new Aa(new wa(b));ma&&a.prototype&&ma(c,a.prototype);return c}
function Ba(a,b,c){if(null==a)throw new TypeError("The 'this' value for String.prototype."+c+" must not be null or undefined");if(b instanceof RegExp)throw new TypeError("First argument to String.prototype."+c+" must not be a regular expression");return a+""}
t("String.prototype.endsWith",function(a){return a?a:function(b,c){var d=Ba(this,b,"endsWith");b+="";void 0===c&&(c=d.length);for(var e=Math.max(0,Math.min(c|0,d.length)),f=b.length;0<f&&0<e;)if(d[--e]!=b[--f])return!1;return 0>=f}});
t("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=Ba(this,b,"startsWith");b+="";for(var e=d.length,f=b.length,g=Math.max(0,Math.min(c|0,d.length)),h=0;h<f&&g<e;)if(d[g++]!=b[h++])return!1;return h>=f}});
function z(a,b){return Object.prototype.hasOwnProperty.call(a,b)}
var Ca="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)z(d,e)&&(a[e]=d[e])}return a};
t("Object.assign",function(a){return a||Ca});
t("Object.setPrototypeOf",function(a){return a||ma});
t("Promise",function(a){function b(g){this.g=0;this.h=void 0;this.f=[];var h=this.i();try{g(h.resolve,h.reject)}catch(k){h.reject(k)}}
function c(){this.f=null}
function d(g){return g instanceof b?g:new b(function(h){h(g)})}
if(a)return a;c.prototype.g=function(g){if(null==this.f){this.f=[];var h=this;this.h(function(){h.j()})}this.f.push(g)};
var e=da.setTimeout;c.prototype.h=function(g){e(g,0)};
c.prototype.j=function(){for(;this.f&&this.f.length;){var g=this.f;this.f=[];for(var h=0;h<g.length;++h){var k=g[h];g[h]=null;try{k()}catch(l){this.i(l)}}}this.f=null};
c.prototype.i=function(g){this.h(function(){throw g;})};
b.prototype.i=function(){function g(l){return function(m){k||(k=!0,l.call(h,m))}}
var h=this,k=!1;return{resolve:g(this.F),reject:g(this.j)}};
b.prototype.F=function(g){if(g===this)this.j(new TypeError("A Promise cannot resolve to itself"));else if(g instanceof b)this.ma(g);else{a:switch(typeof g){case "object":var h=null!=g;break a;case "function":h=!0;break a;default:h=!1}h?this.A(g):this.l(g)}};
b.prototype.A=function(g){var h=void 0;try{h=g.then}catch(k){this.j(k);return}"function"==typeof h?this.ba(h,g):this.l(g)};
b.prototype.j=function(g){this.m(2,g)};
b.prototype.l=function(g){this.m(1,g)};
b.prototype.m=function(g,h){if(0!=this.g)throw Error("Cannot settle("+g+", "+h+"): Promise already settled in state"+this.g);this.g=g;this.h=h;this.s()};
b.prototype.s=function(){if(null!=this.f){for(var g=0;g<this.f.length;++g)f.g(this.f[g]);this.f=null}};
var f=new c;b.prototype.ma=function(g){var h=this.i();g.G(h.resolve,h.reject)};
b.prototype.ba=function(g,h){var k=this.i();try{g.call(h,k.resolve,k.reject)}catch(l){k.reject(l)}};
b.prototype.then=function(g,h){function k(q,p){return"function"==typeof q?function(v){try{l(q(v))}catch(w){m(w)}}:p}
var l,m,n=new b(function(q,p){l=q;m=p});
this.G(k(g,l),k(h,m));return n};
b.prototype["catch"]=function(g){return this.then(void 0,g)};
b.prototype.G=function(g,h){function k(){switch(l.g){case 1:g(l.h);break;case 2:h(l.h);break;default:throw Error("Unexpected state: "+l.g);}}
var l=this;null==this.f?f.g(k):this.f.push(k)};
b.resolve=d;b.reject=function(g){return new b(function(h,k){k(g)})};
b.race=function(g){return new b(function(h,k){for(var l=u(g),m=l.next();!m.done;m=l.next())d(m.value).G(h,k)})};
b.all=function(g){var h=u(g),k=h.next();return k.done?d([]):new b(function(l,m){function n(v){return function(w){q[v]=w;p--;0==p&&l(q)}}
var q=[],p=0;do q.push(void 0),p++,d(k.value).G(n(q.length-1),m),k=h.next();while(!k.done)})};
return b});
t("WeakMap",function(a){function b(k){this.f=(h+=Math.random()+1).toString();if(k){k=u(k);for(var l;!(l=k.next()).done;)l=l.value,this.set(l[0],l[1])}}
function c(){}
function d(k){var l=typeof k;return"object"===l&&null!==k||"function"===l}
function e(k){if(!z(k,g)){var l=new c;ba(k,g,{value:l})}}
function f(k){var l=Object[k];l&&(Object[k]=function(m){if(m instanceof c)return m;Object.isExtensible(m)&&e(m);return l(m)})}
if(function(){if(!a||!Object.seal)return!1;try{var k=Object.seal({}),l=Object.seal({}),m=new a([[k,2],[l,3]]);if(2!=m.get(k)||3!=m.get(l))return!1;m["delete"](k);m.set(l,4);return!m.has(k)&&4==m.get(l)}catch(n){return!1}}())return a;
var g="$jscomp_hidden_"+Math.random();f("freeze");f("preventExtensions");f("seal");var h=0;b.prototype.set=function(k,l){if(!d(k))throw Error("Invalid WeakMap key");e(k);if(!z(k,g))throw Error("WeakMap key fail: "+k);k[g][this.f]=l;return this};
b.prototype.get=function(k){return d(k)&&z(k,g)?k[g][this.f]:void 0};
b.prototype.has=function(k){return d(k)&&z(k,g)&&z(k[g],this.f)};
b.prototype["delete"]=function(k){return d(k)&&z(k,g)&&z(k[g],this.f)?delete k[g][this.f]:!1};
return b});
t("Map",function(a){function b(){var h={};return h.previous=h.next=h.head=h}
function c(h,k){var l=h.f;return ea(function(){if(l){for(;l.head!=h.f;)l=l.previous;for(;l.next!=l.head;)return l=l.next,{done:!1,value:k(l)};l=null}return{done:!0,value:void 0}})}
function d(h,k){var l=k&&typeof k;"object"==l||"function"==l?f.has(k)?l=f.get(k):(l=""+ ++g,f.set(k,l)):l="p_"+k;var m=h.g[l];if(m&&z(h.g,l))for(var n=0;n<m.length;n++){var q=m[n];if(k!==k&&q.key!==q.key||k===q.key)return{id:l,list:m,index:n,o:q}}return{id:l,list:m,index:-1,o:void 0}}
function e(h){this.g={};this.f=b();this.size=0;if(h){h=u(h);for(var k;!(k=h.next()).done;)k=k.value,this.set(k[0],k[1])}}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),k=new a(u([[h,"s"]]));if("s"!=k.get(h)||1!=k.size||k.get({x:4})||k.set({x:4},"t")!=k||2!=k.size)return!1;var l=k.entries(),m=l.next();if(m.done||m.value[0]!=h||"s"!=m.value[1])return!1;m=l.next();return m.done||4!=m.value[0].x||"t"!=m.value[1]||!l.next().done?!1:!0}catch(n){return!1}}())return a;
var f=new WeakMap;e.prototype.set=function(h,k){h=0===h?0:h;var l=d(this,h);l.list||(l.list=this.g[l.id]=[]);l.o?l.o.value=k:(l.o={next:this.f,previous:this.f.previous,head:this.f,key:h,value:k},l.list.push(l.o),this.f.previous.next=l.o,this.f.previous=l.o,this.size++);return this};
e.prototype["delete"]=function(h){h=d(this,h);return h.o&&h.list?(h.list.splice(h.index,1),h.list.length||delete this.g[h.id],h.o.previous.next=h.o.next,h.o.next.previous=h.o.previous,h.o.head=null,this.size--,!0):!1};
e.prototype.clear=function(){this.g={};this.f=this.f.previous=b();this.size=0};
e.prototype.has=function(h){return!!d(this,h).o};
e.prototype.get=function(h){return(h=d(this,h).o)&&h.value};
e.prototype.entries=function(){return c(this,function(h){return[h.key,h.value]})};
e.prototype.keys=function(){return c(this,function(h){return h.key})};
e.prototype.values=function(){return c(this,function(h){return h.value})};
e.prototype.forEach=function(h,k){for(var l=this.entries(),m;!(m=l.next()).done;)m=m.value,h.call(k,m[1],m[0],this)};
e.prototype[Symbol.iterator]=e.prototype.entries;var g=0;return e});
t("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)z(b,d)&&c.push([d,b[d]]);return c}});
t("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==Ba(this,b,"includes").indexOf(b,c||0)}});
t("Set",function(a){function b(c){this.f=new Map;if(c){c=u(c);for(var d;!(d=c.next()).done;)this.add(d.value)}this.size=this.f.size}
if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var c=Object.seal({x:4}),d=new a(u([c]));if(!d.has(c)||1!=d.size||d.add(c)!=d||1!=d.size||d.add({x:4})!=d||2!=d.size)return!1;var e=d.entries(),f=e.next();if(f.done||f.value[0]!=c||f.value[1]!=c)return!1;f=e.next();return f.done||f.value[0]==c||4!=f.value[0].x||f.value[1]!=f.value[0]?!1:e.next().done}catch(g){return!1}}())return a;
b.prototype.add=function(c){c=0===c?0:c;this.f.set(c,c);this.size=this.f.size;return this};
b.prototype["delete"]=function(c){c=this.f["delete"](c);this.size=this.f.size;return c};
b.prototype.clear=function(){this.f.clear();this.size=0};
b.prototype.has=function(c){return this.f.has(c)};
b.prototype.entries=function(){return this.f.entries()};
b.prototype.values=function(){return this.f.values()};
b.prototype.keys=b.prototype.values;b.prototype[Symbol.iterator]=b.prototype.values;b.prototype.forEach=function(c,d){var e=this;this.f.forEach(function(f){return c.call(d,f,f,e)})};
return b});
var A=this||self;function B(a,b){for(var c=a.split("."),d=b||A,e=0;e<c.length;e++)if(d=d[c[e]],null==d)return null;return d}
function Da(){}
function Ea(a){var b=typeof a;return"object"!=b?b:a?Array.isArray(a)?"array":b:"null"}
function Fa(a){var b=Ea(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function Ga(a){return"function"==Ea(a)}
function Ha(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function Ia(a){return Object.prototype.hasOwnProperty.call(a,Ja)&&a[Ja]||(a[Ja]=++Ka)}
var Ja="closure_uid_"+(1E9*Math.random()>>>0),Ka=0;function La(a,b,c){return a.call.apply(a.bind,arguments)}
function Ma(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}}
function D(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?D=La:D=Ma;return D.apply(null,arguments)}
var E=Date.now;function F(a,b){var c=a.split("."),d=A;c[0]in d||"undefined"==typeof d.execScript||d.execScript("var "+c[0]);for(var e;c.length&&(e=c.shift());)c.length||void 0===b?d[e]&&d[e]!==Object.prototype[e]?d=d[e]:d=d[e]={}:d[e]=b}
function G(a,b){function c(){}
c.prototype=b.prototype;a.D=b.prototype;a.prototype=new c;a.prototype.constructor=a}
function Na(a){return a}
;function Oa(a){if(Error.captureStackTrace)Error.captureStackTrace(this,Oa);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
G(Oa,Error);Oa.prototype.name="CustomError";var Pa=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);
for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},H=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},Qa=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;
H(a,function(e,f){d=b.call(void 0,d,e,f,a)});
return d};
function Ra(a,b){a:{var c=a.length;for(var d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:"string"===typeof a?a.charAt(c):a[c]}
function Sa(a){return Array.prototype.concat.apply([],arguments)}
function Ua(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function Va(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(Fa(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
;function Wa(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;function Xa(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function Ya(a){var b=I,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function Za(a,b){for(var c in a)if(!(c in b)||a[c]!==b[c])return!1;for(var d in b)if(!(d in a))return!1;return!0}
function $a(a){var b=Ea(a);if("object"==b||"array"==b){if(Ga(a.clone))return a.clone();b="array"==b?[]:{};for(var c in a)b[c]=$a(a[c]);return b}return a}
var ab="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function bb(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<ab.length;f++)c=ab[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var cb;function db(){if(void 0===cb){var a=null,b=A.trustedTypes;if(b&&b.createPolicy){try{a=b.createPolicy("goog#html",{createHTML:Na,createScript:Na,createScriptURL:Na})}catch(c){A.console&&A.console.error(c.message)}cb=a}else cb=a}return cb}
;function eb(a,b){this.g=a===fb&&b||"";this.f=gb}
function hb(a){return a instanceof eb&&a.constructor===eb&&a.f===gb?a.g:"type_error:Const"}
var gb={},fb={};var ib=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]},jb=/&/g,kb=/</g,lb=/>/g,mb=/"/g,nb=/'/g,ob=/\x00/g,pb=/[\x00&<>"']/;var qb;a:{var rb=A.navigator;if(rb){var sb=rb.userAgent;if(sb){qb=sb;break a}}qb=""}function J(a){return-1!=qb.indexOf(a)}
;function tb(){}
;var ub=J("Opera"),vb=J("Trident")||J("MSIE"),wb=J("Edge"),xb=J("Gecko")&&!(-1!=qb.toLowerCase().indexOf("webkit")&&!J("Edge"))&&!(J("Trident")||J("MSIE"))&&!J("Edge"),yb=-1!=qb.toLowerCase().indexOf("webkit")&&!J("Edge");function zb(){var a=A.document;return a?a.documentMode:void 0}
var Ab;a:{var Bb="",Cb=function(){var a=qb;if(xb)return/rv:([^\);]+)(\)|;)/.exec(a);if(wb)return/Edge\/([\d\.]+)/.exec(a);if(vb)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(yb)return/WebKit\/(\S+)/.exec(a);if(ub)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
Cb&&(Bb=Cb?Cb[1]:"");if(vb){var Db=zb();if(null!=Db&&Db>parseFloat(Bb)){Ab=String(Db);break a}}Ab=Bb}var Eb=Ab,Fb;if(A.document&&vb){var Gb=zb();Fb=Gb?Gb:parseInt(Eb,10)||void 0}else Fb=void 0;var Hb=Fb;var Ib={},Jb=null;var K=window;function Kb(a){var b=B("window.location.href");null==a&&(a='Unknown Error of type "null/undefined"');if("string"===typeof a)return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};var c=!1;try{var d=a.lineNumber||a.line||"Not available"}catch(f){d="Not available",c=!0}try{var e=a.fileName||a.filename||a.sourceURL||A.$googDebugFname||b}catch(f){e="Not available",c=!0}return!c&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name?a:(b=a.message,null==b&&(a.constructor&&
a.constructor instanceof Function?(a.constructor.name?b=a.constructor.name:(b=a.constructor,Lb[b]?b=Lb[b]:(b=String(b),Lb[b]||(c=/function\s+([^\(]+)/m.exec(b),Lb[b]=c?c[1]:"[Anonymous]"),b=Lb[b])),b='Unknown Error of type "'+b+'"'):b="Unknown Error of unknown type"),{message:b,name:a.name||"UnknownError",lineNumber:d,fileName:e,stack:a.stack||"Not available"})}
var Lb={};function Mb(a){this.f=a||{cookie:""}}
r=Mb.prototype;r.isEnabled=function(){return navigator.cookieEnabled};
r.set=function(a,b,c){var d=!1;if("object"===typeof c){var e=c.Ha;d=c.secure||!1;var f=c.domain||void 0;var g=c.path||void 0;var h=c.T}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');void 0===h&&(h=-1);c=f?";domain="+f:"";g=g?";path="+g:"";d=d?";secure":"";h=0>h?"":0==h?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(E()+1E3*h)).toUTCString();this.f.cookie=a+"="+b+c+g+h+d+(null!=e?";samesite="+e:"")};
r.get=function(a,b){for(var c=a+"=",d=(this.f.cookie||"").split(";"),e=0,f;e<d.length;e++){f=ib(d[e]);if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
r.remove=function(a,b,c){var d=void 0!==this.get(a);this.set(a,"",{T:0,path:b,domain:c});return d};
r.isEmpty=function(){return!this.f.cookie};
r.clear=function(){for(var a=(this.f.cookie||"").split(";"),b=[],c=[],d,e,f=0;f<a.length;f++)e=ib(a[f]),d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var Nb=new Mb("undefined"==typeof document?null:document);function Ob(a,b){this.width=a;this.height=b}
r=Ob.prototype;r.clone=function(){return new Ob(this.width,this.height)};
r.aspectRatio=function(){return this.width/this.height};
r.isEmpty=function(){return!(this.width*this.height)};
r.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
r.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
r.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Pb(){var a=document;var b="IFRAME";"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());return a.createElement(b)}
function Qb(a,b){for(var c=0;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;var Rb=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^\\/?#]*)@)?([^\\/?#]*?)(?::([0-9]+))?(?=[\\/?#]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function L(a){return a.match(Rb)}
function Sb(a){return a?decodeURI(a):a}
function Tb(a){var b=L(a);a=b[1];var c=b[2],d=b[3];b=b[4];var e="";a&&(e+=a+":");d&&(e+="//",c&&(e+=c+"@"),e+=d,b&&(e+=":"+b));return e}
function Ub(a,b,c){if(Array.isArray(b))for(var d=0;d<b.length;d++)Ub(a,String(b[d]),c);else null!=b&&c.push(a+(""===b?"":"="+encodeURIComponent(String(b))))}
function Vb(a){var b=[],c;for(c in a)Ub(c,a[c],b);return b.join("&")}
var Wb=/#|$/;function Xb(a){var b=Yb;if(b)for(var c in b)Object.prototype.hasOwnProperty.call(b,c)&&a.call(void 0,b[c],c,b)}
function Zb(){var a=[];Xb(function(b){a.push(b)});
return a}
var Yb={na:"allow-forms",oa:"allow-modals",pa:"allow-orientation-lock",qa:"allow-pointer-lock",ra:"allow-popups",sa:"allow-popups-to-escape-sandbox",ta:"allow-presentation",ua:"allow-same-origin",va:"allow-scripts",wa:"allow-top-navigation",xa:"allow-top-navigation-by-user-activation"},$b=Wa(function(){return Zb()});
function ac(){var a=Pb(),b={};H($b(),function(c){a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
;function bc(){this.h=this.h;this.i=this.i}
bc.prototype.h=!1;bc.prototype.dispose=function(){this.h||(this.h=!0,this.J())};
bc.prototype.J=function(){if(this.i)for(;this.i.length;)this.i.shift()()};function M(a,b){var c=void 0;return new (c||(c=Promise))(function(d,e){function f(k){try{h(b.next(k))}catch(l){e(l)}}
function g(k){try{h(b["throw"](k))}catch(l){e(l)}}
function h(k){k.done?d(k.value):(new c(function(l){l(k.value)})).then(f,g)}
h((b=b.apply(a,void 0)).next())})}
;var cc=hb(new eb(fb,"//fonts.googleapis.com/css")),dc=db();dc&&dc.createScriptURL(cc);var ec=(new Date).getTime();function fc(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));a=a.substring(0,a.indexOf("://"));if("http"!==a&&"https"!==a&&"chrome-extension"!==a&&"file"!==a&&"android-app"!==a&&"chrome-search"!==a&&"chrome-untrusted"!==a&&"chrome"!==a&&"app"!==a)throw Error("Invalid URI scheme in origin: "+a);c="";
var d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1);b=b.substring(0,d);if("http"===a&&"80"!==e||"https"===a&&"443"!==e)c=":"+e}return a+"://"+b+c}
;function gc(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;m=l=0}
function b(n){for(var q=g,p=0;64>p;p+=4)q[p/4]=n[p]<<24|n[p+1]<<16|n[p+2]<<8|n[p+3];for(p=16;80>p;p++)n=q[p-3]^q[p-8]^q[p-14]^q[p-16],q[p]=(n<<1|n>>>31)&4294967295;n=e[0];var v=e[1],w=e[2],C=e[3],R=e[4];for(p=0;80>p;p++){if(40>p)if(20>p){var pa=C^v&(w^C);var Ta=1518500249}else pa=v^w^C,Ta=1859775393;else 60>p?(pa=v&w|C&(v|w),Ta=2400959708):(pa=v^w^C,Ta=3395469782);pa=((n<<5|n>>>27)&4294967295)+pa+R+Ta+q[p]&4294967295;R=C;C=w;w=(v<<30|v>>>2)&4294967295;v=n;n=pa}e[0]=e[0]+n&4294967295;e[1]=e[1]+v&4294967295;
e[2]=e[2]+w&4294967295;e[3]=e[3]+C&4294967295;e[4]=e[4]+R&4294967295}
function c(n,q){if("string"===typeof n){n=unescape(encodeURIComponent(n));for(var p=[],v=0,w=n.length;v<w;++v)p.push(n.charCodeAt(v));n=p}q||(q=n.length);p=0;if(0==l)for(;p+64<q;)b(n.slice(p,p+64)),p+=64,m+=64;for(;p<q;)if(f[l++]=n[p++],m++,64==l)for(l=0,b(f);p+64<q;)b(n.slice(p,p+64)),p+=64,m+=64}
function d(){var n=[],q=8*m;56>l?c(h,56-l):c(h,64-(l-56));for(var p=63;56<=p;p--)f[p]=q&255,q>>>=8;b(f);for(p=q=0;5>p;p++)for(var v=24;0<=v;v-=8)n[q++]=e[p]>>v&255;return n}
for(var e=[],f=[],g=[],h=[128],k=1;64>k;++k)h[k]=0;var l,m;a();return{reset:a,update:c,digest:d,ca:function(){for(var n=d(),q="",p=0;p<n.length;p++)q+="0123456789ABCDEF".charAt(Math.floor(n[p]/16))+"0123456789ABCDEF".charAt(n[p]%16);return q}}}
;function hc(a,b,c){var d=[],e=[];if(1==(Array.isArray(c)?2:1))return e=[b,a],H(d,function(h){e.push(h)}),ic(e.join(" "));
var f=[],g=[];H(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];H(d,function(h){e.push(h)});
a=ic(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function ic(a){var b=gc();b.update(a);return b.ca().toLowerCase()}
;function jc(a){var b=fc(String(A.location.href)),c;(c=A.__SAPISID||A.__APISID||A.__OVERRIDE_SID)?c=!0:(c=new Mb(document),c=c.get("SAPISID")||c.get("APISID")||c.get("__Secure-3PAPISID")||c.get("SID"),c=!!c);if(c&&(c=(b=0==b.indexOf("https:")||0==b.indexOf("chrome-extension:"))?A.__SAPISID:A.__APISID,c||(c=new Mb(document),c=c.get(b?"SAPISID":"APISID")||c.get("__Secure-3PAPISID")),c)){b=b?"SAPISIDHASH":"APISIDHASH";var d=String(A.location.href);return d&&c&&b?[b,hc(fc(d),c,a||null)].join(" "):null}return null}
;function kc(){this.g=[];this.f=-1}
kc.prototype.set=function(a,b){b=void 0===b?!0:b;0<=a&&52>a&&0===a%1&&this.g[a]!=b&&(this.g[a]=b,this.f=-1)};
kc.prototype.get=function(a){return!!this.g[a]};
function lc(a){-1==a.f&&(a.f=Qa(a.g,function(b,c,d){return c?b+Math.pow(2,d):b},0));
return a.f}
;function mc(a,b){this.h=a;this.i=b;this.g=0;this.f=null}
mc.prototype.get=function(){if(0<this.g){this.g--;var a=this.f;this.f=a.next;a.next=null}else a=this.h();return a};
function nc(a,b){a.i(b);100>a.g&&(a.g++,b.next=a.f,a.f=b)}
;function oc(a){A.setTimeout(function(){throw a;},0)}
var pc;function qc(){var a=A.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!J("Presto")&&(a=function(){var e=Pb();e.style.display="none";document.documentElement.appendChild(e);var f=e.contentWindow;e=f.document;e.open();e.close();var g="callImmediate"+Math.random(),h="file:"==f.location.protocol?"*":f.location.protocol+"//"+f.location.host;e=D(function(k){if(("*"==h||k.origin==h)&&k.data==g)this.port1.onmessage()},this);
f.addEventListener("message",e,!1);this.port1={};this.port2={postMessage:function(){f.postMessage(g,h)}}});
if("undefined"!==typeof a&&!J("Trident")&&!J("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(void 0!==c.next){c=c.next;var e=c.P;c.P=null;e()}};
return function(e){d.next={P:e};d=d.next;b.port2.postMessage(0)}}return function(e){A.setTimeout(e,0)}}
;function rc(){this.g=this.f=null}
var tc=new mc(function(){return new sc},function(a){a.reset()});
rc.prototype.add=function(a,b){var c=tc.get();c.set(a,b);this.g?this.g.next=c:this.f=c;this.g=c};
rc.prototype.remove=function(){var a=null;this.f&&(a=this.f,this.f=this.f.next,this.f||(this.g=null),a.next=null);return a};
function sc(){this.next=this.scope=this.f=null}
sc.prototype.set=function(a,b){this.f=a;this.scope=b;this.next=null};
sc.prototype.reset=function(){this.next=this.scope=this.f=null};function uc(a,b){vc||wc();xc||(vc(),xc=!0);yc.add(a,b)}
var vc;function wc(){if(A.Promise&&A.Promise.resolve){var a=A.Promise.resolve(void 0);vc=function(){a.then(zc)}}else vc=function(){var b=zc;
!Ga(A.setImmediate)||A.Window&&A.Window.prototype&&!J("Edge")&&A.Window.prototype.setImmediate==A.setImmediate?(pc||(pc=qc()),pc(b)):A.setImmediate(b)}}
var xc=!1,yc=new rc;function zc(){for(var a;a=yc.remove();){try{a.f.call(a.scope)}catch(b){oc(b)}nc(tc,a)}xc=!1}
;function Ac(){this.g=-1}
;function Bc(){this.g=64;this.f=[];this.l=[];this.m=[];this.i=[];this.i[0]=128;for(var a=1;a<this.g;++a)this.i[a]=0;this.j=this.h=0;this.reset()}
G(Bc,Ac);Bc.prototype.reset=function(){this.f[0]=1732584193;this.f[1]=4023233417;this.f[2]=2562383102;this.f[3]=271733878;this.f[4]=3285377520;this.j=this.h=0};
function Cc(a,b,c){c||(c=0);var d=a.m;if("string"===typeof b)for(var e=0;16>e;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;16>e;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(e=16;80>e;e++){var f=d[e-3]^d[e-8]^d[e-14]^d[e-16];d[e]=(f<<1|f>>>31)&4294967295}b=a.f[0];c=a.f[1];var g=a.f[2],h=a.f[3],k=a.f[4];for(e=0;80>e;e++){if(40>e)if(20>e){f=h^c&(g^h);var l=1518500249}else f=c^g^h,l=1859775393;else 60>e?(f=c&g|h&(c|g),l=2400959708):
(f=c^g^h,l=3395469782);f=(b<<5|b>>>27)+f+k+l+d[e]&4294967295;k=h;h=g;g=(c<<30|c>>>2)&4294967295;c=b;b=f}a.f[0]=a.f[0]+b&4294967295;a.f[1]=a.f[1]+c&4294967295;a.f[2]=a.f[2]+g&4294967295;a.f[3]=a.f[3]+h&4294967295;a.f[4]=a.f[4]+k&4294967295}
Bc.prototype.update=function(a,b){if(null!=a){void 0===b&&(b=a.length);for(var c=b-this.g,d=0,e=this.l,f=this.h;d<b;){if(0==f)for(;d<=c;)Cc(this,a,d),d+=this.g;if("string"===typeof a)for(;d<b;){if(e[f]=a.charCodeAt(d),++f,++d,f==this.g){Cc(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.g){Cc(this,e);f=0;break}}this.h=f;this.j+=b}};
Bc.prototype.digest=function(){var a=[],b=8*this.j;56>this.h?this.update(this.i,56-this.h):this.update(this.i,this.g-(this.h-56));for(var c=this.g-1;56<=c;c--)this.l[c]=b&255,b/=256;Cc(this,this.l);for(c=b=0;5>c;c++)for(var d=24;0<=d;d-=8)a[b]=this.f[c]>>d&255,++b;return a};var Dc="StopIteration"in A?A.StopIteration:{message:"StopIteration",stack:""};function Ec(){}
Ec.prototype.next=function(){throw Dc;};
Ec.prototype.B=function(){return this};
function Fc(a){if(a instanceof Ec)return a;if("function"==typeof a.B)return a.B(!1);if(Fa(a)){var b=0,c=new Ec;c.next=function(){for(;;){if(b>=a.length)throw Dc;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function Gc(a,b){if(Fa(a))try{H(a,b,void 0)}catch(c){if(c!==Dc)throw c;}else{a=Fc(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==Dc)throw c;}}}
function Hc(a){if(Fa(a))return Ua(a);a=Fc(a);var b=[];Gc(a,function(c){b.push(c)});
return b}
;function Ic(a,b){this.h={};this.f=[];this.i=this.g=0;var c=arguments.length;if(1<c){if(c%2)throw Error("Uneven number of arguments");for(var d=0;d<c;d+=2)this.set(arguments[d],arguments[d+1])}else if(a)if(a instanceof Ic)for(c=Jc(a),d=0;d<c.length;d++)this.set(c[d],a.get(c[d]));else for(d in a)this.set(d,a[d])}
function Jc(a){Kc(a);return a.f.concat()}
r=Ic.prototype;r.equals=function(a,b){if(this===a)return!0;if(this.g!=a.g)return!1;var c=b||Lc;Kc(this);for(var d,e=0;d=this.f[e];e++)if(!c(this.get(d),a.get(d)))return!1;return!0};
function Lc(a,b){return a===b}
r.isEmpty=function(){return 0==this.g};
r.clear=function(){this.h={};this.i=this.g=this.f.length=0};
r.remove=function(a){return Object.prototype.hasOwnProperty.call(this.h,a)?(delete this.h[a],this.g--,this.i++,this.f.length>2*this.g&&Kc(this),!0):!1};
function Kc(a){if(a.g!=a.f.length){for(var b=0,c=0;b<a.f.length;){var d=a.f[b];Object.prototype.hasOwnProperty.call(a.h,d)&&(a.f[c++]=d);b++}a.f.length=c}if(a.g!=a.f.length){var e={};for(c=b=0;b<a.f.length;)d=a.f[b],Object.prototype.hasOwnProperty.call(e,d)||(a.f[c++]=d,e[d]=1),b++;a.f.length=c}}
r.get=function(a,b){return Object.prototype.hasOwnProperty.call(this.h,a)?this.h[a]:b};
r.set=function(a,b){Object.prototype.hasOwnProperty.call(this.h,a)||(this.g++,this.f.push(a),this.i++);this.h[a]=b};
r.forEach=function(a,b){for(var c=Jc(this),d=0;d<c.length;d++){var e=c[d],f=this.get(e);a.call(b,f,e,this)}};
r.clone=function(){return new Ic(this)};
r.B=function(a){Kc(this);var b=0,c=this.i,d=this,e=new Ec;e.next=function(){if(c!=d.i)throw Error("The map has changed since the iterator was created");if(b>=d.f.length)throw Dc;var f=d.f[b++];return a?f:d.h[f]};
return e};var Mc=A.JSON.stringify;function N(a){this.f=0;this.m=void 0;this.i=this.g=this.h=null;this.j=this.l=!1;if(a!=Da)try{var b=this;a.call(void 0,function(c){Nc(b,2,c)},function(c){Nc(b,3,c)})}catch(c){Nc(this,3,c)}}
function Oc(){this.next=this.context=this.onRejected=this.g=this.f=null;this.h=!1}
Oc.prototype.reset=function(){this.context=this.onRejected=this.g=this.f=null;this.h=!1};
var Pc=new mc(function(){return new Oc},function(a){a.reset()});
function Qc(a,b,c){var d=Pc.get();d.g=a;d.onRejected=b;d.context=c;return d}
function Rc(){var a=Sc;if(a instanceof N)return a;var b=new N(Da);Nc(b,2,a);return b}
N.prototype.then=function(a,b,c){return Tc(this,Ga(a)?a:null,Ga(b)?b:null,c)};
N.prototype.$goog_Thenable=!0;N.prototype.cancel=function(a){if(0==this.f){var b=new Uc(a);uc(function(){Vc(this,b)},this)}};
function Vc(a,b){if(0==a.f)if(a.h){var c=a.h;if(c.g){for(var d=0,e=null,f=null,g=c.g;g&&(g.h||(d++,g.f==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.f&&1==d?Vc(c,b):(f?(d=f,d.next==c.i&&(c.i=d),d.next=d.next.next):Wc(c),Xc(c,e,3,b)))}a.h=null}else Nc(a,3,b)}
function Yc(a,b){a.g||2!=a.f&&3!=a.f||Zc(a);a.i?a.i.next=b:a.g=b;a.i=b}
function Tc(a,b,c,d){var e=Qc(null,null,null);e.f=new N(function(f,g){e.g=b?function(h){try{var k=b.call(d,h);f(k)}catch(l){g(l)}}:f;
e.onRejected=c?function(h){try{var k=c.call(d,h);void 0===k&&h instanceof Uc?g(h):f(k)}catch(l){g(l)}}:g});
e.f.h=a;Yc(a,e);return e.f}
N.prototype.A=function(a){this.f=0;Nc(this,2,a)};
N.prototype.F=function(a){this.f=0;Nc(this,3,a)};
function Nc(a,b,c){if(0==a.f){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.f=1;a:{var d=c,e=a.A,f=a.F;if(d instanceof N){Yc(d,Qc(e||Da,f||null,a));var g=!0}else{if(d)try{var h=!!d.$goog_Thenable}catch(l){h=!1}else h=!1;if(h)d.then(e,f,a),g=!0;else{if(Ha(d))try{var k=d.then;if(Ga(k)){$c(d,k,e,f,a);g=!0;break a}}catch(l){f.call(a,l);g=!0;break a}g=!1}}}g||(a.m=c,a.f=b,a.h=null,Zc(a),3!=b||c instanceof Uc||ad(a,c))}}
function $c(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
var h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function Zc(a){a.l||(a.l=!0,uc(a.s,a))}
function Wc(a){var b=null;a.g&&(b=a.g,a.g=b.next,b.next=null);a.g||(a.i=null);return b}
N.prototype.s=function(){for(var a;a=Wc(this);)Xc(this,a,this.f,this.m);this.l=!1};
function Xc(a,b,c,d){if(3==c&&b.onRejected&&!b.h)for(;a&&a.j;a=a.h)a.j=!1;if(b.f)b.f.h=null,bd(b,c,d);else try{b.h?b.g.call(b.context):bd(b,c,d)}catch(e){cd.call(null,e)}nc(Pc,b)}
function bd(a,b,c){2==b?a.g.call(a.context,c):a.onRejected&&a.onRejected.call(a.context,c)}
function ad(a,b){a.j=!0;uc(function(){a.j&&cd.call(null,b)})}
var cd=oc;function Uc(a){Oa.call(this,a)}
G(Uc,Oa);Uc.prototype.name="cancel";function O(a){bc.call(this);this.m=1;this.j=[];this.l=0;this.f=[];this.g={};this.s=!!a}
G(O,bc);r=O.prototype;r.subscribe=function(a,b,c){var d=this.g[a];d||(d=this.g[a]=[]);var e=this.m;this.f[e]=a;this.f[e+1]=b;this.f[e+2]=c;this.m=e+3;d.push(e);return e};
function dd(a,b,c){var d=ed;if(a=d.g[a]){var e=d.f;(a=Ra(a,function(f){return e[f+1]==b&&e[f+2]==c}))&&d.I(a)}}
r.I=function(a){var b=this.f[a];if(b){var c=this.g[b];if(0!=this.l)this.j.push(a),this.f[a+1]=Da;else{if(c){var d=Pa(c,a);0<=d&&Array.prototype.splice.call(c,d,1)}delete this.f[a];delete this.f[a+1];delete this.f[a+2]}}return!!b};
r.M=function(a,b){var c=this.g[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.s)for(e=0;e<c.length;e++){var g=c[e];fd(this.f[g+1],this.f[g+2],d)}else{this.l++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.f[g+1].apply(this.f[g+2],d)}finally{if(this.l--,0<this.j.length&&0==this.l)for(;c=this.j.pop();)this.I(c)}}return 0!=e}return!1};
function fd(a,b,c){uc(function(){a.apply(b,c)})}
r.clear=function(a){if(a){var b=this.g[a];b&&(H(b,this.I,this),delete this.g[a])}else this.f.length=0,this.g={}};
r.J=function(){O.D.J.call(this);this.clear();this.j.length=0};function gd(a){this.f=a}
gd.prototype.set=function(a,b){void 0===b?this.f.remove(a):this.f.set(a,Mc(b))};
gd.prototype.get=function(a){try{var b=this.f.get(a)}catch(c){return}if(null!==b)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
gd.prototype.remove=function(a){this.f.remove(a)};function hd(a){this.f=a}
G(hd,gd);function id(a){this.data=a}
function jd(a){return void 0===a||a instanceof id?a:new id(a)}
hd.prototype.set=function(a,b){hd.D.set.call(this,a,jd(b))};
hd.prototype.g=function(a){a=hd.D.get.call(this,a);if(void 0===a||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
hd.prototype.get=function(a){if(a=this.g(a)){if(a=a.data,void 0===a)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function kd(a){this.f=a}
G(kd,hd);kd.prototype.set=function(a,b,c){if(b=jd(b)){if(c){if(c<E()){kd.prototype.remove.call(this,a);return}b.expiration=c}b.creation=E()}kd.D.set.call(this,a,b)};
kd.prototype.g=function(a){var b=kd.D.g.call(this,a);if(b){var c=b.creation,d=b.expiration;if(d&&d<E()||c&&c>E())kd.prototype.remove.call(this,a);else return b}};function ld(){}
;function md(){}
G(md,ld);md.prototype.clear=function(){var a=Hc(this.B(!0)),b=this;H(a,function(c){b.remove(c)})};function nd(a){this.f=a}
G(nd,md);r=nd.prototype;r.isAvailable=function(){if(!this.f)return!1;try{return this.f.setItem("__sak","1"),this.f.removeItem("__sak"),!0}catch(a){return!1}};
r.set=function(a,b){try{this.f.setItem(a,b)}catch(c){if(0==this.f.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
r.get=function(a){a=this.f.getItem(a);if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
r.remove=function(a){this.f.removeItem(a)};
r.B=function(a){var b=0,c=this.f,d=new Ec;d.next=function(){if(b>=c.length)throw Dc;var e=c.key(b++);if(a)return e;e=c.getItem(e);if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
r.clear=function(){this.f.clear()};
r.key=function(a){return this.f.key(a)};function od(){var a=null;try{a=window.localStorage||null}catch(b){}this.f=a}
G(od,nd);function pd(a,b){this.g=a;this.f=null;var c;if(c=vb)c=!(9<=Number(Hb));if(c){qd||(qd=new Ic);this.f=qd.get(a);this.f||(b?this.f=document.getElementById(b):(this.f=document.createElement("userdata"),this.f.addBehavior("#default#userData"),document.body.appendChild(this.f)),qd.set(a,this.f));try{this.f.load(this.g)}catch(d){this.f=null}}}
G(pd,md);var rd={".":".2E","!":".21","~":".7E","*":".2A","'":".27","(":".28",")":".29","%":"."},qd=null;function sd(a){return"_"+encodeURIComponent(a).replace(/[.!~*'()%]/g,function(b){return rd[b]})}
r=pd.prototype;r.isAvailable=function(){return!!this.f};
r.set=function(a,b){this.f.setAttribute(sd(a),b);td(this)};
r.get=function(a){a=this.f.getAttribute(sd(a));if("string"!==typeof a&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
r.remove=function(a){this.f.removeAttribute(sd(a));td(this)};
r.B=function(a){var b=0,c=this.f.XMLDocument.documentElement.attributes,d=new Ec;d.next=function(){if(b>=c.length)throw Dc;var e=c[b++];if(a)return decodeURIComponent(e.nodeName.replace(/\./g,"%")).substr(1);e=e.nodeValue;if("string"!==typeof e)throw"Storage mechanism: Invalid value was encountered";return e};
return d};
r.clear=function(){for(var a=this.f.XMLDocument.documentElement,b=a.attributes.length;0<b;b--)a.removeAttribute(a.attributes[b-1].nodeName);td(this)};
function td(a){try{a.f.save(a.g)}catch(b){throw"Storage mechanism: Quota exceeded";}}
;function ud(a,b){this.g=a;this.f=b+"::"}
G(ud,md);ud.prototype.set=function(a,b){this.g.set(this.f+a,b)};
ud.prototype.get=function(a){return this.g.get(this.f+a)};
ud.prototype.remove=function(a){this.g.remove(this.f+a)};
ud.prototype.B=function(a){var b=this.g.B(!0),c=this,d=new Ec;d.next=function(){for(var e=b.next();e.substr(0,c.f.length)!=c.f;)e=b.next();return a?e.substr(c.f.length):c.g.get(e)};
return d};var vd=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};F("yt.config_",vd);function wd(a){var b=arguments;1<b.length?vd[b[0]]=b[1]:1===b.length&&Object.assign(vd,b[0])}
function P(a,b){return a in vd?vd[a]:b}
;var xd=[];function yd(a){xd.forEach(function(b){return b(a)})}
function zd(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Ad(b),yd(b)}}:a}
function Ad(a){var b=B("yt.logging.errors.log");b?b(a,"ERROR",void 0,void 0,void 0):(b=P("ERRORS",[]),b.push([a,"ERROR",void 0,void 0,void 0]),wd("ERRORS",b))}
function Bd(a){var b=B("yt.logging.errors.log");b?b(a,"WARNING",void 0,void 0,void 0):(b=P("ERRORS",[]),b.push([a,"WARNING",void 0,void 0,void 0]),wd("ERRORS",b))}
;var Cd=0;F("ytDomDomGetNextId",B("ytDomDomGetNextId")||function(){return++Cd});var Dd={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};
function Ed(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(var b in a)b in Dd||(this[b]=a[b]);var c=a.target||a.srcElement;c&&3==c.nodeType&&(c=c.parentNode);this.target=c;var d=a.relatedTarget;if(d)try{d=d.nodeName?d:null}catch(e){d=null}else"mouseover"==
this.type?d=a.fromElement:"mouseout"==this.type&&(d=a.toElement);this.relatedTarget=d;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey}}catch(e){}}
Ed.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
Ed.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
Ed.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};var I=A.ytEventsEventsListeners||{};F("ytEventsEventsListeners",I);var Fd=A.ytEventsEventsCounter||{count:0};F("ytEventsEventsCounter",Fd);
function Gd(a,b,c,d){d=void 0===d?{}:d;a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return Ya(function(e){var f="boolean"===typeof e[4]&&e[4]==!!d,g=Ha(e[4])&&Ha(d)&&Za(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
function Hd(a){a&&("string"==typeof a&&(a=[a]),H(a,function(b){if(b in I){var c=I[b],d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?Id()||"boolean"===typeof c?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent("on"+e,f);delete I[b]}}))}
var Id=Wa(function(){var a=!1;try{var b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(c){}return a});
function Jd(a,b,c){var d=void 0===d?{}:d;if(a&&(a.addEventListener||a.attachEvent)){var e=Gd(a,b,c,d);if(!e){e=++Fd.count+"";var f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document);var g=f?function(h){h=new Ed(h);if(!Qb(h.relatedTarget,function(k){return k==a}))return h.currentTarget=a,h.type=b,c.call(a,h)}:function(h){h=new Ed(h);
h.currentTarget=a;return c.call(a,h)};
g=zd(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),Id()||"boolean"===typeof d?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent("on"+b,g);I[e]=[a,b,c,g,d]}}}
;function Kd(a,b){Ga(a)&&(a=zd(a));return window.setTimeout(a,b)}
function Ld(a){Ga(a)&&(a=zd(a));return window.setInterval(a,250)}
;function Md(a){var b=[];Xa(a,function(c,d){var e=encodeURIComponent(String(d)),f;Array.isArray(c)?f=c:f=[c];H(f,function(g){""==g?b.push(e):b.push(e+"="+encodeURIComponent(String(g)))})});
return b.join("&")}
function Nd(a){"?"==a.charAt(0)&&(a=a.substr(1));a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length)try{var f=decodeURIComponent((e[0]||"").replace(/\+/g," ")),g=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?Array.isArray(b[f])?Va(b[f],g):b[f]=[b[f],g]:b[f]=g}catch(k){if("q"!=e[0]){var h=Error("Error decoding URL component");h.params={key:e[0],value:e[1]};Ad(h)}}}return b}
function Od(a,b){return Pd(a,b||{},!0)}
function Pd(a,b,c){var d=a.split("#",2);a=d[0];d=1<d.length?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=Nd(e[1]||"");for(var f in b)!c&&null!==e&&f in e||(e[f]=b[f]);b=a;a=Vb(e);a?(c=b.indexOf("#"),0>c&&(c=b.length),f=b.indexOf("?"),0>f||f>c?(f=c,e=""):e=b.substring(f+1,c),b=[b.substr(0,f),e,b.substr(c)],c=b[1],b[1]=a?c?c+"&"+a:a:c,a=b[0]+(b[1]?"?"+b[1]:"")+b[2]):a=b;return a+d}
;var Qd={};function Rd(a){return Qd[a]||(Qd[a]=String(a).replace(/\-([a-z])/g,function(b,c){return c.toUpperCase()}))}
;var Sd={},Td=[],ed=new O,Ud={};function Vd(){for(var a=u(Td),b=a.next();!b.done;b=a.next())b=b.value,b()}
function Wd(a,b){var c;"yt:"==a.tagName.toLowerCase().substr(0,3)?c=a.getAttribute(b):c=a?a.dataset?a.dataset[Rd(b)]:a.getAttribute("data-"+b):null;return c}
function Xd(a,b){ed.M.apply(ed,arguments)}
;function Yd(a){this.g=a||{};this.h=this.f=!1;a=document.getElementById("www-widgetapi-script");if(this.f=!!("https:"==document.location.protocol||a&&0==a.src.indexOf("https:"))){a=[this.g,window.YTConfig||{}];for(var b=0;b<a.length;b++)a[b].host&&(a[b].host=a[b].host.replace("http://","https://"))}}
function Q(a,b){for(var c=[a.g,window.YTConfig||{}],d=0;d<c.length;d++){var e=c[d][b];if(void 0!=e)return e}return null}
function Zd(a,b,c){$d||($d={},Jd(window,"message",D(a.i,a)));$d[c]=b}
Yd.prototype.i=function(a){if(a.origin==Q(this,"host")||a.origin==Q(this,"host").replace(/^http:/,"https:")){try{var b=JSON.parse(a.data)}catch(c){return}this.h=!0;this.f||0!=a.origin.indexOf("https:")||(this.f=!0);if(a=$d[b.id])a.s=!0,a.s&&(H(a.m,a.O,a),a.m.length=0),a.Z(b)}};
var $d=null;function S(a){a=ae(a);return"string"===typeof a&&"false"===a?!1:!!a}
function be(a,b){var c=ae(a);return void 0===c&&void 0!==b?b:Number(c||0)}
function ae(a){var b=P("EXPERIMENTS_FORCED_FLAGS",{});return void 0!==b[a]?b[a]:P("EXPERIMENT_FLAGS",{})[a]}
;function ce(){}
function de(a,b){return ee(a,0,b)}
;function fe(){}
na(fe,ce);function ee(a,b,c){isNaN(c)&&(c=void 0);var d=B("yt.scheduler.instance.addJob");return d?d(a,b,c):void 0===c?(a(),NaN):Kd(a,c||0)}
fe.prototype.start=function(){var a=B("yt.scheduler.instance.start");a&&a()};
fe.f=void 0;fe.g=function(){fe.f||(fe.f=new fe)};
fe.g();var ge=A.ytPubsubPubsubInstance||new O;O.prototype.subscribe=O.prototype.subscribe;O.prototype.unsubscribeByKey=O.prototype.I;O.prototype.publish=O.prototype.M;O.prototype.clear=O.prototype.clear;F("ytPubsubPubsubInstance",ge);F("ytPubsubPubsubSubscribedKeys",A.ytPubsubPubsubSubscribedKeys||{});F("ytPubsubPubsubTopicToKeys",A.ytPubsubPubsubTopicToKeys||{});F("ytPubsubPubsubIsSynchronous",A.ytPubsubPubsubIsSynchronous||{});var T=window,U=T.ytcsi&&T.ytcsi.now?T.ytcsi.now:T.performance&&T.performance.timing&&T.performance.now&&T.performance.timing.navigationStart?function(){return T.performance.timing.navigationStart+T.performance.now()}:function(){return(new Date).getTime()};var he=be("initial_gel_batch_timeout",1E3),ie=Math.pow(2,16)-1,je=null,ke=0,le=void 0,me=0,ne=0,oe=0,pe=!0,qe=A.ytLoggingTransportLogPayloadsQueue_||{};F("ytLoggingTransportLogPayloadsQueue_",qe);var re=A.ytLoggingTransportGELQueue_||new Map;F("ytLoggingTransportGELQueue_",re);var se=A.ytLoggingTransportTokensToCttTargetIds_||{};F("ytLoggingTransportTokensToCttTargetIds_",se);
function te(){window.clearTimeout(me);window.clearTimeout(ne);ne=0;le&&le.isReady()?(ue(re),"log_event"in qe&&ue(Object.entries(qe.log_event)),re.clear(),delete qe.log_event):ve()}
function ve(){S("web_gel_timeout_cap")&&!ne&&(ne=Kd(te,6E4));window.clearTimeout(me);var a=P("LOGGING_BATCH_TIMEOUT",be("web_gel_debounce_ms",1E4));S("shorten_initial_gel_batch_timeout")&&pe&&(a=he);me=Kd(te,a)}
function ue(a){var b=le,c=Math.round(U());a=u(a);for(var d=a.next();!d.done;d=a.next()){var e=u(d.value);d=e.next().value;var f=e.next().value;e=$a({context:we(b.f||xe())});e.events=f;(f=se[d])&&ye(e,d,f);delete se[d];ze(e,c);Ae(b,"log_event",e,{retry:!0,onSuccess:function(){ke=Math.round(U()-c)}});
pe=!1}}
function ze(a,b){a.requestTimeMs=String(b);S("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);var c=P("EVENT_ID",void 0);if(c){var d=P("BATCH_CLIENT_COUNTER",void 0)||0;!d&&S("web_client_counter_random_seed")&&(d=Math.floor(Math.random()*ie/2));d++;d>ie&&(d=1);wd("BATCH_CLIENT_COUNTER",d);c={serializedEventId:c,clientCounter:String(d)};a.serializedClientEventId=c;je&&ke&&S("log_gel_rtt_web")&&(a.previousBatchInfo={serializedClientEventId:je,roundtripMs:String(ke)});je=c;ke=0}}
function ye(a,b,c){if(c.videoId)var d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
;var Be=A.ytLoggingGelSequenceIdObj_||{};F("ytLoggingGelSequenceIdObj_",Be);function Ce(a){var b=De;a=void 0===a?B("yt.ads.biscotti.lastId_")||"":a;b=Object.assign(Ee(b),Fe(b));b.ca_type="image";a&&(b.bid=a);return b}
function Ee(a){var b={};b.dt=ec;b.flash="0";a:{try{var c=a.f.top.location.href}catch(f){a=2;break a}a=c?c===a.g.location.href?0:1:2}b=(b.frm=a,b);b.u_tz=-(new Date).getTimezoneOffset();var d=void 0===d?K:d;try{var e=d.history.length}catch(f){e=0}b.u_his=e;b.u_java=!!K.navigator&&"unknown"!==typeof K.navigator.javaEnabled&&!!K.navigator.javaEnabled&&K.navigator.javaEnabled();K.screen&&(b.u_h=K.screen.height,b.u_w=K.screen.width,b.u_ah=K.screen.availHeight,b.u_aw=K.screen.availWidth,b.u_cd=K.screen.colorDepth);
K.navigator&&K.navigator.plugins&&(b.u_nplug=K.navigator.plugins.length);K.navigator&&K.navigator.mimeTypes&&(b.u_nmime=K.navigator.mimeTypes.length);return b}
function Fe(a){var b=a.f;try{var c=b.screenX;var d=b.screenY}catch(n){}try{var e=b.outerWidth;var f=b.outerHeight}catch(n){}try{var g=b.innerWidth;var h=b.innerHeight}catch(n){}b=[b.screenLeft,b.screenTop,c,d,b.screen?b.screen.availWidth:void 0,b.screen?b.screen.availTop:void 0,e,f,g,h];c=a.f.top;try{var k=(c||window).document,l="CSS1Compat"==k.compatMode?k.documentElement:k.body;var m=(new Ob(l.clientWidth,l.clientHeight)).round()}catch(n){m=new Ob(-12245933,-12245933)}k=m;m={};l=new kc;A.SVGElement&&
A.document.createElementNS&&l.set(0);c=ac();c["allow-top-navigation-by-user-activation"]&&l.set(1);c["allow-popups-to-escape-sandbox"]&&l.set(2);A.crypto&&A.crypto.subtle&&l.set(3);A.TextDecoder&&A.TextEncoder&&l.set(4);l=lc(l);m.bc=l;m.bih=k.height;m.biw=k.width;m.brdim=b.join();a=a.g;return m.vis={visible:1,hidden:2,prerender:3,preview:4,unloaded:5}[a.visibilityState||a.webkitVisibilityState||a.mozVisibilityState||""]||0,m.wgl=!!K.WebGLRenderingContext,m}
var De=new function(){var a=window.document;this.f=window;this.g=a};
F("yt.ads_.signals_.getAdSignalsString",function(a){return Md(Ce(a))});E();var Ge=void 0!==XMLHttpRequest?function(){return new XMLHttpRequest}:void 0!==ActiveXObject?function(){return new ActiveXObject("Microsoft.XMLHTTP")}:null;
function He(){if(!Ge)return null;var a=Ge();return"open"in a?a:null}
;var Ie={Authorization:"AUTHORIZATION","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"},Je="app debugcss debugjs expflag force_ad_params force_viral_ad_response_params forced_experiments innertube_snapshots innertube_goldens internalcountrycode internalipoverride absolute_experiments conditional_experiments sbb sr_bns_address".split(" "),
Ke=!1;
function Le(a,b){b=void 0===b?{}:b;if(!c)var c=window.location.href;var d=L(a)[1]||null,e=Sb(L(a)[3]||null);d&&e?(d=c,c=L(a),d=L(d),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?Sb(L(c)[3]||null)==e&&(Number(L(c)[4]||null)||null)==(Number(L(a)[4]||null)||null):!0;d=S("web_ajax_ignore_global_headers_if_set");for(var f in Ie)e=P(Ie[f]),!e||!c&&!Me(a,f)||d&&void 0!==b[f]||(b[f]=e);if(c||Me(a,"X-YouTube-Utc-Offset"))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());(c||Me(a,"X-YouTube-Time-Zone"))&&(f=
"undefined"!=typeof Intl?(new Intl.DateTimeFormat).resolvedOptions().timeZone:null)&&(b["X-YouTube-Time-Zone"]=f);if(c||Me(a,"X-YouTube-Ad-Signals"))b["X-YouTube-Ad-Signals"]=Md(Ce(void 0));return b}
function Ne(a){var b=window.location.search,c=Sb(L(a)[3]||null),d=Sb(L(a)[5]||null);d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;var e=Nd(b),f={};H(Je,function(g){e[g]&&(f[g]=e[g])});
return Pd(a,f||{},!1)}
function Me(a,b){var c=P("CORS_HEADER_WHITELIST")||{},d=Sb(L(a)[3]||null);return d?(c=c[d])?0<=Pa(c,b):!1:!0}
function Oe(a,b){if(window.fetch&&"XML"!=b.format){var c={method:b.method||"GET",credentials:"same-origin"};b.headers&&(c.headers=b.headers);a=Pe(a,b);var d=Qe(a,b);d&&(c.body=d);b.withCredentials&&(c.credentials="include");var e=!1,f;fetch(a,c).then(function(g){if(!e){e=!0;f&&window.clearTimeout(f);var h=g.ok,k=function(l){l=l||{};var m=b.context||A;h?b.onSuccess&&b.onSuccess.call(m,l,g):b.onError&&b.onError.call(m,l,g);b.K&&b.K.call(m,l,g)};
"JSON"==(b.format||"JSON")&&(h||400<=g.status&&500>g.status)?g.json().then(k,function(){k(null)}):k(null)}});
b.W&&0<b.timeout&&(f=Kd(function(){e||(e=!0,window.clearTimeout(f),b.W.call(b.context||A))},b.timeout))}else Re(a,b)}
function Re(a,b){var c=b.format||"JSON";a=Pe(a,b);var d=Qe(a,b),e=!1,f=Se(a,function(k){if(!e){e=!0;h&&window.clearTimeout(h);a:switch(k&&"status"in k?k.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:var l=!0;break a;default:l=!1}var m=null,n=400<=k.status&&500>k.status,q=500<=k.status&&600>k.status;if(l||n||q)m=Te(a,c,k,b.Ba);if(l)a:if(k&&204==k.status)l=!0;else{switch(c){case "XML":l=0==parseInt(m&&m.return_code,10);break a;case "RAW":l=!0;break a}l=!!m}m=m||
{};n=b.context||A;l?b.onSuccess&&b.onSuccess.call(n,k,m):b.onError&&b.onError.call(n,k,m);b.K&&b.K.call(n,k,m)}},b.method,d,b.headers,b.responseType,b.withCredentials);
if(b.H&&0<b.timeout){var g=b.H;var h=Kd(function(){e||(e=!0,f.abort(),window.clearTimeout(h),g.call(b.context||A,f))},b.timeout)}}
function Pe(a,b){b.Fa&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var c=P("XSRF_FIELD_NAME",void 0),d=b.la;d&&(d[c]&&delete d[c],a=Od(a,d));return a}
function Qe(a,b){var c=P("XSRF_FIELD_NAME",void 0),d=P("XSRF_TOKEN",void 0),e=b.postBody||"",f=b.u,g=P("XSRF_FIELD_NAME",void 0),h;b.headers&&(h=b.headers["Content-Type"]);b.Ea||Sb(L(a)[3]||null)&&!b.withCredentials&&Sb(L(a)[3]||null)!=document.location.hostname||"POST"!=b.method||h&&"application/x-www-form-urlencoded"!=h||b.u&&b.u[g]||(f||(f={}),f[c]=d);f&&"string"===typeof e&&(e=Nd(e),bb(e,f),e=b.Y&&"JSON"==b.Y?JSON.stringify(e):Vb(e));if(!(c=e)&&(c=f)){a:{for(var k in f){f=!1;break a}f=!0}c=!f}!Ke&&
c&&"POST"!=b.method&&(Ke=!0,Ad(Error("AJAX request with postData should use POST")));return e}
function Te(a,b,c,d){var e=null;switch(b){case "JSON":try{var f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,Bd(d),g;}a=c.getResponseHeader("Content-Type")||"";f&&0<=a.indexOf("json")&&(e=JSON.parse(f));break;case "XML":if(a=(a=c.responseXML)?Ue(a):null)e={},H(a.getElementsByTagName("*"),function(g){e[g.tagName]=Ve(g)})}d&&We(e);
return e}
function We(a){if(Ha(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d=a[b],e=new eb(fb,"HTML that is escaped and sanitized server-side and passed through yt.net.ajax");hb(e);hb(e);e=new tb;var f=db();f&&f.createHTML(d);a[c]=e}else We(a[b])}}
function Ue(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Ve(a){var b="";H(a.childNodes,function(c){b+=c.nodeValue});
return b}
function Se(a,b,c,d,e,f,g){function h(){4==(k&&"readyState"in k?k.readyState:0)&&b&&zd(b)(k)}
c=void 0===c?"GET":c;d=void 0===d?"":d;var k=He();if(!k)return null;"onloadend"in k?k.addEventListener("loadend",h,!1):k.onreadystatechange=h;S("debug_forward_web_query_parameters")&&(a=Ne(a));k.open(c,a,!0);f&&(k.responseType=f);g&&(k.withCredentials=!0);c="POST"==c&&(void 0===window.FormData||!(d instanceof FormData));if(e=Le(a,e))for(var l in e)k.setRequestHeader(l,e[l]),"content-type"==l.toLowerCase()&&(c=!1);c&&k.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k.send(d);
return k}
;function Xe(){for(var a={},b=u(Object.entries(Nd(P("DEVICE","")))),c=b.next();!c.done;c=b.next()){var d=u(c.value);c=d.next().value;d=d.next().value;"cbrand"===c?a.deviceMake=d:"cmodel"===c?a.deviceModel=d:"cbr"===c?a.browserName=d:"cbrver"===c?a.browserVersion=d:"cos"===c?a.osName=d:"cosver"===c?a.osVersion=d:"cplatform"===c&&(a.platform=d)}return a}
;function Ye(){return"INNERTUBE_API_KEY"in vd&&"INNERTUBE_API_VERSION"in vd}
function xe(){return{innertubeApiKey:P("INNERTUBE_API_KEY",void 0),innertubeApiVersion:P("INNERTUBE_API_VERSION",void 0),ea:P("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),fa:P("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:P("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0),ha:P("INNERTUBE_CONTEXT_HL",void 0),ga:P("INNERTUBE_CONTEXT_GL",void 0),ia:P("INNERTUBE_HOST_OVERRIDE",void 0)||"",ja:!!P("INNERTUBE_USE_THIRD_PARTY_AUTH",!1)}}
function we(a){a={client:{hl:a.ha,gl:a.ga,clientName:a.fa,clientVersion:a.innertubeContextClientVersion,configInfo:a.ea}};var b=window.devicePixelRatio;b&&1!=b&&(a.client.screenDensityFloat=String(b));b=P("EXPERIMENTS_TOKEN","");""!==b&&(a.client.experimentsToken=b);b=[];var c=P("EXPERIMENTS_FORCED_FLAGS",{});for(d in c)b.push({key:d,value:String(c[d])});var d=P("EXPERIMENT_FLAGS",{});for(var e in d)e.startsWith("force_")&&void 0===c[e]&&b.push({key:e,value:String(d[e])});0<b.length&&(a.request={internalExperimentFlags:b});
P("DELEGATED_SESSION_ID")&&!S("pageid_as_header_web")&&(a.user={onBehalfOfUser:P("DELEGATED_SESSION_ID")});a.client=Object.assign(a.client,Xe());return a}
function Ze(a,b,c){c=void 0===c?{}:c;var d={"X-Goog-Visitor-Id":c.visitorData||P("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;(b=c.za||P("AUTHORIZATION"))||(a?b="Bearer "+B("gapi.auth.getToken")().ya:b=jc([]));b&&(d.Authorization=b,d["X-Goog-AuthUser"]=P("SESSION_INDEX",0),S("pageid_as_header_web")&&(d["X-Goog-PageId"]=P("DELEGATED_SESSION_ID")));return d}
function $e(a){a=Object.assign({},a);delete a.Authorization;var b=jc();if(b){var c=new Bc;c.update(P("INNERTUBE_API_KEY",void 0));c.update(b);b=c.digest();c=3;Fa(b);void 0===c&&(c=0);if(!Jb){Jb={};for(var d="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),e=["+/=","+/","-_=","-_.","-_"],f=0;5>f;f++){var g=d.concat(e[f].split(""));Ib[f]=g;for(var h=0;h<g.length;h++){var k=g[h];void 0===Jb[k]&&(Jb[k]=h)}}}c=Ib[c];d=[];for(e=0;e<b.length;e+=3){var l=b[e],m=(f=e+1<b.length)?
b[e+1]:0;k=(g=e+2<b.length)?b[e+2]:0;h=l>>2;l=(l&3)<<4|m>>4;m=(m&15)<<2|k>>6;k&=63;g||(k=64,f||(m=64));d.push(c[h],c[l],c[m]||"",c[k]||"")}a.hash=d.join("")}return a}
;function af(){var a=new od;(a=a.isAvailable()?new ud(a,"yt.innertube"):null)||(a=new pd("yt.innertube"),a=a.isAvailable()?a:null);this.f=a?new kd(a):null;this.g=document.domain||window.location.hostname}
af.prototype.set=function(a,b,c,d){c=c||31104E3;this.remove(a);if(this.f)try{this.f.set(a,b,E()+1E3*c);return}catch(f){}var e="";if(d)try{e=escape(Mc(b))}catch(f){return}else e=escape(b);b=this.g;Nb.set(""+a,e,{T:c,path:"/",domain:void 0===b?"youtube.com":b,secure:!1})};
af.prototype.get=function(a,b){var c=void 0,d=!this.f;if(!d)try{c=this.f.get(a)}catch(e){d=!0}if(d&&(c=Nb.get(""+a,void 0))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),c=void 0}return c};
af.prototype.remove=function(a){this.f&&this.f.remove(a);var b=this.g;Nb.remove(""+a,"/",void 0===b?"youtube.com":b)};var bf=new af;function cf(a,b,c,d){if(d)return null;d=bf.get("nextId",!0)||1;var e=bf.get("requests",!0)||{};e[d]={method:a,request:b,authState:$e(c),requestTime:Math.round(U())};bf.set("nextId",d+1,86400,!0);bf.set("requests",e,86400,!0);return d}
function df(a){var b=bf.get("requests",!0)||{};delete b[a];bf.set("requests",b,86400,!0)}
function ef(a){var b=bf.get("requests",!0);if(b){for(var c in b){var d=b[c];if(!(6E4>Math.round(U())-d.requestTime)){var e=d.authState,f=$e(Ze(!1));Za(e,f)&&(e=d.request,"requestTimeMs"in e&&(e.requestTimeMs=Math.round(U())),Ae(a,d.method,e,{}));delete b[c]}}bf.set("requests",b,86400,!0)}}
;function V(a){return new N(function(b,c){function d(){c(a.error);f()}
function e(){b(a.result);f()}
function f(){a.removeEventListener("success",e);a.removeEventListener("error",d)}
a.addEventListener("success",e);a.addEventListener("error",d)})}
;function ff(a){this.f=a}
r=ff.prototype;r.add=function(a,b,c){return W(X(this,[a],"readwrite"),a).add(b,c)};
r.clear=function(a){return W(X(this,[a],"readwrite"),a).clear()};
r.close=function(){this.f.close()};
r.count=function(a,b){return W(X(this,[a]),a).count(b)};
r["delete"]=function(a,b){return W(X(this,[a],"readwrite"),a)["delete"](b)};
r.get=function(a,b){return W(X(this,[a]),a).get(b)};
r.getName=function(){return this.f.name};
function X(a,b,c){a=a.f.transaction(b,c);return new gf(a)}
function hf(a){this.f=a}
r=hf.prototype;r.add=function(a,b){return V(this.f.add(a,b))};
r.clear=function(){return V(this.f.clear()).then(function(){})};
r.count=function(a){return V(this.f.count(a))};
r["delete"]=function(a){return V(this.f["delete"](a))};
r.get=function(a){return V(this.f.get(a))};
r.index=function(a){return new jf(this.f.index(a))};
r.getName=function(){return this.f.name};
function kf(){var a=Error.call(this,"Transaction was aborted");this.message=a.message;"stack"in a&&(this.stack=a.stack);Object.setPrototypeOf(this,kf.prototype)}
na(kf,Error);function gf(a){var b=this;this.f=a;this.g=new Map;this.done=new N(function(c,d){b.f.addEventListener("complete",function(){c()});
b.f.addEventListener("error",function(){d(b.f.error)});
b.f.addEventListener("abort",function(){d(new kf)})})}
gf.prototype.abort=function(){this.f.abort();return this.done};
function W(a,b){var c=a.f.objectStore(b),d=a.g.get(c);d||(d=new hf(c),a.g.set(c,d));return d}
function jf(a){this.f=a}
jf.prototype.count=function(a){return V(this.f.count(a))};
jf.prototype.get=function(a){return V(this.f.get(a))};
function lf(a,b){var c=a.f.openCursor(b,"prev");return V(c).then(function(d){return null===d?null:new mf(c,d)})}
function mf(a,b){this.request=a;this.f=b}
mf.prototype["delete"]=function(){return V(this.f["delete"]()).then(function(){})};
mf.prototype.update=function(a){return V(this.f.update(a))};function nf(a,b,c){function d(){l||(l=new ff(e.result));return l}
c=void 0===c?{}:c;var e=void 0!==b?self.indexedDB.open(a,b):self.indexedDB.open(a);a=c;var f=a.Aa,g=a.blocking,h=a.Ia,k=a.upgrade,l;k&&e.addEventListener("upgradeneeded",function(m){if(null===m.newVersion)throw Error("Invariant: newVersion on IDBVersionChangeEvent is null");if(null===e.transaction)throw Error("Invariant: transaction on IDBOpenDBRequest is null");var n=d(),q=new gf(e.transaction);k(n,m.oldVersion,m.newVersion,q)});
f&&e.addEventListener("blocked",function(){f()});
return V(e).then(function(m){g&&m.addEventListener("versionchange",function(){g()});
h&&m.addEventListener("close",function(){h()});
return d()})}
;var Sc,of=["getAll","getAllKeys","getKey","openKeyCursor"],pf=["getAll","getAllKeys","getKey","openKeyCursor"];
function qf(){return M(this,function b(){var c,d,e,f,g,h,k,l;return y(b,function(m){switch(m.f){case 1:if(!self.indexedDB)return m["return"](!1);c=u(of);for(d=c.next();!d.done;d=c.next())if(e=d.value,!IDBObjectStore.prototype[e])return m["return"](!1);f=u(pf);for(d=f.next();!d.done;d=f.next())if(g=d.value,!IDBIndex.prototype[g])return m["return"](!1);if(!IDBObjectStore.prototype.getKey)return m["return"](!1);sa(m);l=!1;return x(m,nf("yt-idb-test-do-not-use",void 0,{blocking:function(){l=!0;h&&(h.close(),
h=void 0)}}),5);
case 5:return h=m.g,x(m,nf("yt-idb-test-do-not-use",h.f.version+1),6);case 6:return k=m.g,k.close(),k=void 0,m["return"](l);case 3:ua(m);if(h)try{h.close()}catch(n){}if(k)try{k.close()}catch(n){}va(m);break;case 2:return ta(m),m["return"](!1)}})})}
function rf(){return void 0!==Sc?Rc():new N(function(a){qf().then(function(b){Sc=b;a(b)})})}
;var sf;function tf(){return M(this,function b(){return y(b,function(c){if(!sf)try{sf=nf("LogsDataBase",1,{upgrade:function(d,e){if(1>e){var f=d.f.createObjectStore("LogsRequestsStore",{keyPath:"id",autoIncrement:!0});(new hf(f)).f.createIndex("newRequest",["status","timestamp"],{unique:!1})}}})}catch(d){"VersionError"===d&&Ad(d),sf=nf("LogsDataBase",1)}return c["return"](sf)})})}
function uf(a){return M(this,function c(){var d,e,f,g;return y(c,function(h){if(1==h.f)return x(h,tf(),2);if(3!=h.f)return d=h.g,e=W(X(d,["LogsRequestsStore"],"readwrite"),"LogsRequestsStore"),f=Object.assign(Object.assign({},a),{options:JSON.parse(JSON.stringify(a.options))}),x(h,e.add(f),3);g=h.g;return h["return"](g)})})}
function vf(){return M(this,function b(){var c,d,e,f,g,h,k;return y(b,function(l){switch(l.f){case 1:return c=["NEW",0],d=["NEW",U()],e=IDBKeyRange.bound(c,d),x(l,tf(),2);case 2:return f=l.g,g=X(f,["LogsRequestsStore"],"readwrite"),x(l,lf(W(g,"LogsRequestsStore").index("newRequest"),e),3);case 3:h=l.g;k=void 0;if(null===h||void 0===h||!h.f.value){l.v(4);break}k=h.f.value;k.status="QUEUED";return x(l,h.update(k),4);case 4:return l["return"](k)}})})}
function wf(a){return M(this,function c(){var d,e,f;return y(c,function(g){switch(g.f){case 1:return x(g,tf(),2);case 2:return d=g.g,e=W(X(d,["LogsRequestsStore"],"readwrite"),"LogsRequestsStore"),x(g,e.get(a),3);case 3:return f=g.g,f.status="QUEUED",x(g,V(e.f.put(f,void 0)),4);case 4:return g["return"](f)}})})}
function xf(a){return M(this,function c(){var d,e,f;return y(c,function(g){switch(g.f){case 1:return x(g,tf(),2);case 2:return d=g.g,e=W(X(d,["LogsRequestsStore"],"readwrite"),"LogsRequestsStore"),x(g,e.get(a),3);case 3:return f=g.g,f.status="NEW",f.N+=1,x(g,V(e.f.put(f,void 0)),4);case 4:return g["return"](f)}})})}
function yf(){return M(this,function b(){var c,d;return y(b,function(e){if(1==e.f)return x(e,tf(),2);if(3!=e.f)return c=e.g,x(e,c.count("LogsRequestsStore"),3);d=e.g;return e["return"](!d)})})}
function zf(a){return M(this,function c(){var d;return y(c,function(e){if(1==e.f)return x(e,tf(),2);d=e.g;return e["return"](d["delete"]("LogsRequestsStore",a))})})}
;var Af=be("network_polling_interval",3E4);function Bf(){this.i=0;this.f=window.navigator.onLine;Cf(this);Df(this)}
function Ef(){Bf.instance||(Bf.instance=new Bf);return Bf.instance}
function Ff(a){var b=Gf,c=Hf;a.i||If(a);(new N(function(d){a.h=d})).then(function(){b();
c&&(a.g=c)})}
function Df(a){window.addEventListener("online",function(){a.f=!0;a.h&&a.h()})}
function Cf(a){window.addEventListener("offline",function(){a.f=!1;a.g&&a.g()})}
function If(a){a.i=de(function(){window.navigator.onLine?(!1===a.f&&Ad(Error("NetworkStatusManager missed online event.")),a.f=!0,a.h&&a.h()):(!0===a.f&&Ad(Error("NetworkStatusManager missed offline event.")),a.f=!1,a.g&&a.g());If(a)},Af)}
;var Jf=be("networkless_throttle_timeout")||100,Kf=be("networkless_retry_attempts")||1,Lf=0;function Mf(a,b){rf().then(function(c){if(c&&!S("networkless_bypass_write")){var d={url:a,options:b,timestamp:U(),status:"NEW",N:0};uf(d).then(function(e){d.id=e;e=Ef();e.f?Nf(d):Ff(e)})["catch"](function(){Nf(d);
Ad(Error("Networkless Logging: Log request setting to indexedDB failed."))})}else Re(a,b)})}
function Gf(){Lf||(Lf=ee(function(){Nf();Lf=0;Gf()},1,Jf))}
function Hf(){var a=Lf;if(!isNaN(a)){var b=B("yt.scheduler.instance.cancelJob");b?b(a):window.clearTimeout(a)}Lf=0}
function Nf(a){M(this,function c(){var d=this,e,f,g,h;return y(c,function(k){switch(k.f){case 1:e=d;if(!a)return x(k,vf(),6);if(!a.id){k.v(3);break}return x(k,wf(a.id),5);case 5:a=k.g;k.v(3);break;case 6:if(a=k.g){k.v(3);break}return x(k,yf(),8);case 8:return(f=k.g)&&Hf(),k["return"]();case 3:if(Of(a))g=a.options.onError?a.options.onError:function(){},h=a.options.onSuccess?a.options.onSuccess:function(){},a.options.onError=function(l,m){return M(e,function q(){return y(q,function(p){if(1==p.f)return a&&
a.id?a.N<Kf?x(p,xf(a.id),6):x(p,zf(a.id),2):p.v(2);
2!=p.f&&(Lf||Ff(Ef()),g(l,m));g(l,m);p.f=0})})},a.options.onSuccess=function(l,m){return M(e,function q(){return y(q,function(p){if(1==p.f)return a&&a.id?x(p,zf(a.id),2):p.v(2);
h(l,m);p.f=0})})},Re(a.url,a.options);
else if(Bd(Error("Networkless Logging: Stored logs request expired age limit")),a.id)return x(k,zf(a.id),0);k.v(0)}})})}
function Of(a){a=a.timestamp;return 2592E6<=U()-a?!1:!0}
;function Pf(a,b){for(var c=[],d=1;d<arguments.length;++d)c[d-1]=arguments[d];d=Error.call(this,a);this.message=d.message;"stack"in d&&(this.stack=d.stack);this.args=[].concat(c instanceof Array?c:fa(u(c)))}
na(Pf,Error);function Qf(a){var b=this;this.f=null;a?this.f=a:Ye()&&(this.f=xe());de(function(){ef(b)},5E3)}
Qf.prototype.isReady=function(){!this.f&&Ye()&&(this.f=xe());return!!this.f};
function Ae(a,b,c,d){!P("VISITOR_DATA")&&"visitor_id"!==b&&.01>Math.random()&&Bd(new Pf("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady())throw b=new Pf("innertube xhrclient not ready",b,c,d),Ad(b),b.f=0,b;var e={headers:{"Content-Type":"application/json"},method:"POST",u:c,Y:"JSON",H:function(){d.H()},
W:d.H,onSuccess:function(q,p){if(d.onSuccess)d.onSuccess(p)},
V:function(q){if(d.onSuccess)d.onSuccess(q)},
onError:function(q,p){if(d.onError)d.onError(p)},
Ga:function(q){if(d.onError)d.onError(q)},
timeout:d.timeout,withCredentials:!0},f="",g=a.f.ia;g&&(f=g);g=a.f.ja||!1;var h=Ze(g,f,d);Object.assign(e.headers,h);e.headers.Authorization&&!f&&(e.headers["x-origin"]=window.location.origin);var k=Od(""+f+("/youtubei/"+a.f.innertubeApiVersion+"/"+b),{alt:"json",key:a.f.innertubeApiKey}),l;if(d.retry&&S("retry_web_logging_batches")&&"www.youtube-nocookie.com"!=f&&(l=cf(b,c,h,g))){var m=e.onSuccess,n=e.V;e.onSuccess=function(q,p){df(l);m(q,p)};
c.V=function(q,p){df(l);n(q,p)}}try{S("use_fetch_for_op_xhr")?Oe(k,e):S("networkless_logging")&&d.retry?(e.method="POST",Mf(k,e)):(e.method="POST",e.u||(e.u={}),Re(k,e))}catch(q){if("InvalidAccessError"==q.name)l&&(df(l),l=0),Bd(Error("An extension is blocking network request."));
else throw q;}l&&de(function(){ef(a)},5E3)}
;var Rf=[{U:function(a){return"Cannot read property '"+a.key+"'"},
L:{TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,
groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]}],Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}]}},{U:function(a){return"Cannot call '"+a.key+"'"},
L:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,
groups:["key"]}]}}];var Sf=new Set,Tf=0,Uf=void 0;function Vf(a,b,c,d){c+="."+a;a=String(JSON.stringify(b)).substr(0,500);d[c]=a;return c.length+a.length}
;function Y(a,b,c){this.l=this.f=this.g=null;this.j=Ia(this);this.h=0;this.s=!1;this.m=[];this.i=null;this.A=c;this.F={};c=document;if(a="string"===typeof a?c.getElementById(a):a)if(c="iframe"==a.tagName.toLowerCase(),b.host||(b.host=c?Tb(a.src):"https://www.youtube.com"),this.g=new Yd(b),c||(b=Wf(this,a),this.l=a,(c=a.parentNode)&&c.replaceChild(b,a),a=b),this.f=a,this.f.id||(this.f.id="widget"+Ia(this.f)),Sd[this.f.id]=this,window.postMessage){this.i=new O;Xf(this);b=Q(this.g,"events");for(var d in b)b.hasOwnProperty(d)&&
this.addEventListener(d,b[d]);for(var e in Ud)Yf(this,e)}}
r=Y.prototype;r.setSize=function(a,b){this.f.width=a;this.f.height=b;return this};
r.ka=function(){return this.f};
r.Z=function(a){Zf(this,a.event,a)};
r.addEventListener=function(a,b){var c=b;"string"==typeof b&&(c=function(){window[b].apply(window,arguments)});
if(!c)return this;this.i.subscribe(a,c);$f(this,a);return this};
function Yf(a,b){var c=b.split(".");if(2==c.length){var d=c[1];a.A==c[0]&&$f(a,d)}}
r.destroy=function(){this.f.id&&(Sd[this.f.id]=null);var a=this.i;a&&"function"==typeof a.dispose&&a.dispose();if(this.l){a=this.f;var b=a.parentNode;b&&b.replaceChild(this.l,a)}else(a=this.f)&&a.parentNode&&a.parentNode.removeChild(a);$d&&($d[this.j]=null);this.g=null;a=this.f;for(var c in I)I[c][0]==a&&Hd(c);this.l=this.f=null};
r.R=function(){return{}};
function ag(a,b,c){c=c||[];c=Array.prototype.slice.call(c);b={event:"command",func:b,args:c};a.s?a.O(b):a.m.push(b)}
function Zf(a,b,c){a.i.h||(c={target:a,data:c},a.i.M(b,c),Xd(a.A+"."+b,c))}
function Wf(a,b){for(var c=document.createElement("iframe"),d=b.attributes,e=0,f=d.length;e<f;e++){var g=d[e].value;null!=g&&""!=g&&"null"!=g&&c.setAttribute(d[e].name,g)}c.setAttribute("frameBorder",0);c.setAttribute("allowfullscreen",1);c.setAttribute("allow","accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture");c.setAttribute("title","YouTube "+Q(a.g,"title"));(d=Q(a.g,"width"))&&c.setAttribute("width",d);(d=Q(a.g,"height"))&&c.setAttribute("height",d);var h=a.R();h.enablejsapi=
window.postMessage?1:0;window.location.host&&(h.origin=window.location.protocol+"//"+window.location.host);h.widgetid=a.j;window.location.href&&H(["debugjs","debugcss"],function(k){var l=window.location.href;var m=l.search(Wb);b:{var n=0;for(var q=k.length;0<=(n=l.indexOf(k,n))&&n<m;){var p=l.charCodeAt(n-1);if(38==p||63==p)if(p=l.charCodeAt(n+q),!p||61==p||38==p||35==p)break b;n+=q+1}n=-1}if(0>n)l=null;else{q=l.indexOf("&",n);if(0>q||q>m)q=m;n+=k.length+1;l=decodeURIComponent(l.substr(n,q-n).replace(/\+/g,
" "))}null!==l&&(h[k]=l)});
c.src=Q(a.g,"host")+("/embed/"+Q(a.g,"videoId"))+"?"+Vb(h);return c}
r.X=function(){this.f&&this.f.contentWindow?this.O({event:"listening"}):window.clearInterval(this.h)};
function Xf(a){Zd(a.g,a,a.j);a.h=Ld(D(a.X,a));Jd(a.f,"load",D(function(){window.clearInterval(this.h);this.h=Ld(D(this.X,this))},a))}
function $f(a,b){a.F[b]||(a.F[b]=!0,ag(a,"addEventListener",[b]))}
r.O=function(a){a.id=this.j;a.channel="widget";a=Mc(a);var b=this.g;var c=Tb(this.f.src||"");b=0==c.indexOf("https:")?[c]:b.f?[c.replace("http:","https:")]:b.h?[c]:[c,c.replace("http:","https:")];if(this.f.contentWindow)for(c=0;c<b.length;c++)try{this.f.contentWindow.postMessage(a,b[c])}catch(R){if(R.name&&"SyntaxError"==R.name){if(!(R.message&&0<R.message.indexOf("target origin ''"))){var d=void 0,e=void 0,f=R;e=void 0===e?{}:e;e.name=P("INNERTUBE_CONTEXT_CLIENT_NAME",1);e.version=P("INNERTUBE_CONTEXT_CLIENT_VERSION",
void 0);var g=e||{};e="WARNING";e=void 0===e?"ERROR":e;d=void 0===d?!1:d;if(f){if(S("console_log_js_exceptions")){var h=f,k=[];k.push("Name: "+h.name);k.push("Message: "+h.message);h.hasOwnProperty("params")&&k.push("Error Params: "+JSON.stringify(h.params));k.push("File name: "+h.fileName);k.push("Stacktrace: "+h.stack);window.console.log(k.join("\n"),h)}if((window&&window.yterr||d)&&!(5<=Tf)&&0!==f.f){var l=void 0,m=Kb(f);d=m.message||"Unknown Error";h=m.name||"UnknownError";k=m.lineNumber||"Not available";
var n=m.fileName||"Not available";m=m.stack||f.g||"Not available";if(f.hasOwnProperty("args")&&f.args&&f.args.length){var q=0;for(l=0;l<f.args.length;l++){var p=f.args[l],v="params."+l;q+=v.length;if(p)if(Array.isArray(p))for(var w=g,C=0;C<p.length&&!(p[C]&&(q+=Vf(C,p[C],v,w),500<q));C++);else if("object"===typeof p)for(w in w=void 0,C=g,p){if(p[w]&&(q+=Vf(w,p[w],v,C),500<q))break}else g[v]=String(JSON.stringify(p)).substring(0,500),q+=g[v].length;else g[v]=String(JSON.stringify(p)).substring(0,500),
q+=g[v].length;if(500<=q)break}}else if(f.hasOwnProperty("params")&&f.params)if(p=f.params,"object"===typeof f.params)for(l in v=0,p){if(p[l]&&(q="params."+l,w=String(JSON.stringify(p[l])).substr(0,500),g[q]=w,v+=q.length+w.length,500<v))break}else g.params=String(JSON.stringify(p)).substr(0,500);g={message:d,name:h,lineNumber:k,fileName:n,stack:m,params:g};f=Number(f.columnNumber);isNaN(f)||(g.lineNumber=g.lineNumber+":"+f);f=g;void 0===Uf&&(Uf=Math.random()<be("log_js_error_clusters"));if(!0===
Uf)a:for(h=u(Rf),g=h.next();!g.done;g=h.next())if(g=g.value,g.L[f.name])for(k=u(g.L[f.name]),d=k.next();!d.done;d=k.next())if(n=d.value,d=f.message.match(n.regexp)){f.params["error.original"]=d[0];h=n.groups;k={};for(n=0;n<h.length;n++)k[h[n]]=d[n+1],f.params["error."+h[n]]=d[n+1];f.message=g.U(k);break a}window.yterr&&"function"===typeof window.yterr&&window.yterr(f);if(!(Sf.has(f.message)||0<=f.stack.indexOf("/YouTubeCenter.js")||0<=f.stack.indexOf("/mytube.js"))){if(S("kevlar_gel_error_routing")){g=
void 0;h=e;n=f;k={stackTrace:n.stack};n.fileName&&(k.filename=n.fileName);d=n.lineNumber&&n.lineNumber.split?n.lineNumber.split(":"):[];0!==d.length&&(1!==d.length||isNaN(Number(d[0]))?2!==d.length||isNaN(Number(d[0]))||isNaN(Number(d[1]))||(k.lineNumber=Number(d[0]),k.columnNumber=Number(d[1])):k.lineNumber=Number(d[0]));d={level:"ERROR_LEVEL_UNKNOWN",message:n.message};"ERROR"===h?d.level="ERROR_LEVEL_ERROR":"WARNING"===h&&(d.level="ERROR_LEVEL_WARNNING");h={isObfuscated:!0,browserStackInfo:k};
k={pageUrl:window.location.href,kvPairs:[]};if(n=n.params)for(m=u(Object.keys(n)),l=m.next();!l.done;l=m.next())l=l.value,k.kvPairs.push({key:"client."+l,value:String(n[l])});k={errorMetadata:k,stackTrace:h,logMessage:d};g=void 0===g?{}:g;d=Qf;P("ytLoggingEventsDefaultDisabled",!1)&&Qf==Qf&&(d=null);g=void 0===g?{}:g;h={};h.eventTimeMs=Math.round(g.timestamp||U());h.clientError=k;k=String;g.timestamp?n=-1:(n=B("_lact",window),null==n?n=-1:n=Math.max(E()-n,0));h.context={lastActivityMs:k(n)};S("log_sequence_info_on_gel_web")&&
g.aa&&(k=h.context,n=g.aa,Be[n]=n in Be?Be[n]+1:0,k.sequence={index:Be[n],groupKey:n},g.Da&&delete Be[g.aa]);g=g.Ca;k="";g&&(k=g,n={},k.videoId?n.videoId=k.videoId:k.playlistId&&(n.playlistId=k.playlistId),se[g.token]=n,k=g.token);g=re.get(k)||[];re.set(k,g);g.push(h);d&&(le=new d);d=be("web_logging_max_batch")||100;h=U();g.length>=d?te():10<=h-oe&&(ve(),oe=h);te()}d=f;g=d.params||{};e={la:{a:"logerror",t:"jserror",type:d.name,msg:d.message.substr(0,250),line:d.lineNumber,level:e,"client.name":g.name},
u:{url:P("PAGE_NAME",window.location.href),file:d.fileName},method:"POST"};g.version&&(e["client.version"]=g.version);if(e.u){d.stack&&(e.u.stack=d.stack);d=u(Object.keys(g));for(h=d.next();!h.done;h=d.next())h=h.value,e.u["client."+h]=g[h];if(g=P("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(d=u(Object.keys(g)),h=d.next();!h.done;h=d.next())h=h.value,e.u[h]=g[h];g=P("SERVER_NAME",void 0);d=P("SERVER_VERSION",void 0);g&&d&&(e.u["server.name"]=g,e.u["server.version"]=d)}Re(P("ECATCHER_REPORT_HOST",
"")+"/error_204",e);Sf.add(f.message);Tf++}}}}}else throw R;}else console&&console.warn&&console.warn("The YouTube player is not attached to the DOM. API calls should be made after the onReady event. See more: https://developers.google.com/youtube/iframe_api_reference#Events")};function bg(a){return(0===a.search("cue")||0===a.search("load"))&&"loadModule"!==a}
function cg(a){return 0===a.search("get")||0===a.search("is")}
;function Z(a,b){if(!a)throw Error("YouTube player element ID required.");var c={title:"video player",videoId:"",width:640,height:360};if(b)for(var d in b)c[d]=b[d];Y.call(this,a,c,"player");this.C={};this.playerInfo={}}
na(Z,Y);r=Z.prototype;r.R=function(){var a=Q(this.g,"playerVars");if(a){var b={},c;for(c in a)b[c]=a[c];a=b}else a={};window!=window.top&&document.referrer&&(a.widget_referrer=document.referrer.substring(0,256));if(c=Q(this.g,"embedConfig")){if(Ha(c))try{c=JSON.stringify(c)}catch(d){console.error("Invalid embed config JSON",d)}a.embed_config=c}return a};
r.Z=function(a){var b=a.event;a=a.info;switch(b){case "apiInfoDelivery":if(Ha(a))for(var c in a)this.C[c]=a[c];break;case "infoDelivery":dg(this,a);break;case "initialDelivery":window.clearInterval(this.h);this.playerInfo={};this.C={};eg(this,a.apiInterface);dg(this,a);break;default:Zf(this,b,a)}};
function dg(a,b){if(Ha(b))for(var c in b)a.playerInfo[c]=b[c]}
function eg(a,b){H(b,function(c){this[c]||("getCurrentTime"==c?this[c]=function(){var d=this.playerInfo.currentTime;if(1==this.playerInfo.playerState){var e=(E()/1E3-this.playerInfo.currentTimeLastUpdated_)*this.playerInfo.playbackRate;0<e&&(d+=Math.min(e,1))}return d}:bg(c)?this[c]=function(){this.playerInfo={};
this.C={};ag(this,c,arguments);return this}:cg(c)?this[c]=function(){var d=0;
0===c.search("get")?d=3:0===c.search("is")&&(d=2);return this.playerInfo[c.charAt(d).toLowerCase()+c.substr(d+1)]}:this[c]=function(){ag(this,c,arguments);
return this})},a)}
r.getVideoEmbedCode=function(){var a=parseInt(Q(this.g,"width"),10),b=parseInt(Q(this.g,"height"),10),c=Q(this.g,"host")+("/embed/"+Q(this.g,"videoId"));pb.test(c)&&(-1!=c.indexOf("&")&&(c=c.replace(jb,"&amp;")),-1!=c.indexOf("<")&&(c=c.replace(kb,"&lt;")),-1!=c.indexOf(">")&&(c=c.replace(lb,"&gt;")),-1!=c.indexOf('"')&&(c=c.replace(mb,"&quot;")),-1!=c.indexOf("'")&&(c=c.replace(nb,"&#39;")),-1!=c.indexOf("\x00")&&(c=c.replace(ob,"&#0;")));return'<iframe width="'+a+'" height="'+b+'" src="'+c+'" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'};
r.getOptions=function(a){return this.C.namespaces?a?this.C[a].options||[]:this.C.namespaces||[]:[]};
r.getOption=function(a,b){if(this.C.namespaces&&a&&b)return this.C[a][b]};
function fg(a){if("iframe"!=a.tagName.toLowerCase()){var b=Wd(a,"videoid");b&&(b={videoId:b,width:Wd(a,"width"),height:Wd(a,"height")},new Z(a,b))}}
;F("YT.PlayerState.UNSTARTED",-1);F("YT.PlayerState.ENDED",0);F("YT.PlayerState.PLAYING",1);F("YT.PlayerState.PAUSED",2);F("YT.PlayerState.BUFFERING",3);F("YT.PlayerState.CUED",5);F("YT.get",function(a){return Sd[a]});
F("YT.scan",Vd);F("YT.subscribe",function(a,b,c){ed.subscribe(a,b,c);Ud[a]=!0;for(var d in Sd)Yf(Sd[d],a)});
F("YT.unsubscribe",function(a,b,c){dd(a,b,c)});
F("YT.Player",Z);Y.prototype.destroy=Y.prototype.destroy;Y.prototype.setSize=Y.prototype.setSize;Y.prototype.getIframe=Y.prototype.ka;Y.prototype.addEventListener=Y.prototype.addEventListener;Z.prototype.getVideoEmbedCode=Z.prototype.getVideoEmbedCode;Z.prototype.getOptions=Z.prototype.getOptions;Z.prototype.getOption=Z.prototype.getOption;
Td.push(function(a){var b=a;b||(b=document);a=Ua(b.getElementsByTagName("yt:player"));var c=b||document;if(c.querySelectorAll&&c.querySelector)b=c.querySelectorAll(".yt-player");else{var d;c=document;b=b||c;if(b.querySelectorAll&&b.querySelector)b=b.querySelectorAll(".yt-player");else if(b.getElementsByClassName){var e=b.getElementsByClassName("yt-player");b=e}else{e=b.getElementsByTagName("*");var f={};for(c=d=0;b=e[c];c++){var g=b.className,h;if(h="function"==typeof g.split)h=0<=Pa(g.split(/\s+/),
"yt-player");h&&(f[d++]=b)}f.length=d;b=f}}b=Ua(b);H(Sa(a,b),fg)});
"undefined"!=typeof YTConfig&&YTConfig.parsetags&&"onload"!=YTConfig.parsetags||Vd();var gg=A.onYTReady;gg&&gg();var hg=A.onYouTubeIframeAPIReady;hg&&hg();var ig=A.onYouTubePlayerAPIReady;ig&&ig();}).call(this);
