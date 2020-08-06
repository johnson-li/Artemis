!function(e,t){"object"==typeof exports&&"object"==typeof module?module.exports=t():"function"==typeof define&&define.amd?define("wafer-menu",[],t):"object"==typeof exports?exports["wafer-menu"]=t():(e.wafer=e.wafer||{},e.wafer.wafers=e.wafer.wafers||{},e.wafer.wafers["wafer-menu"]=t())}("undefined"!=typeof self?self:this,function(){return function(e){function t(o){if(n[o])return n[o].exports;var r=n[o]={i:o,l:!1,exports:{}};return e[o].call(r.exports,r,r.exports,t),r.l=!0,r.exports}var n={};return t.m=e,t.c=n,t.d=function(e,n,o){t.o(e,n)||Object.defineProperty(e,n,{configurable:!1,enumerable:!0,get:o})},t.n=function(e){var n=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(n,"a",n),n},t.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},t.p="https://s.yimg.com/aaq/wf/",t(t.s="./src/entry.js")}({"./src/entry.js":function(e,t,n){"use strict";function o(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function r(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function a(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}function i(e,t){if(!(e instanceof t))throw new TypeError("Cannot call a class as a function")}function s(e,t){if(!e)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!t||"object"!=typeof t&&"function"!=typeof t?e:t}function c(e,t){if("function"!=typeof t&&null!==t)throw new TypeError("Super expression must either be null or a function, not "+typeof t);e.prototype=Object.create(t&&t.prototype,{constructor:{value:e,enumerable:!1,writable:!0,configurable:!0}}),t&&(Object.setPrototypeOf?Object.setPrototypeOf(e,t):e.__proto__=t)}Object.defineProperty(t,"__esModule",{value:!0});var l=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(e[o]=n[o])}return e},u=function(){function e(e,t){for(var n=0;n<t.length;n++){var o=t[n];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(e,o.key,o)}}return function(t,n,o){return n&&e(t.prototype,n),o&&e(t,o),t}}(),f=window.wafer,p=f.constants,v=f.WaferBaseClass,m=f.utils,y=m.convertNodeListToArray,h=p.ATTR_PREFIX,b=["menuClick","toggleMenu"],d=[],w=function(e){function t(e){var n=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{};n.selector;o(this,t);var a=r(this,(t.__proto__||Object.getPrototypeOf(t)).call(this,e,{},{STATE_ATTRS:d})),i=y(e.getElementsByClassName("menu-options"))[0],s=y(e.getElementsByClassName("menu-toggle"))[0],c=i.getAttribute(h+"menu-active-class")||"menu-active";return a._util=l({},a._util,{activeClass:c,elem:e,optionsElem:i,toggleElem:s}),b.forEach(function(e){a[e]=a[e].bind(a)}),a.addEventListeners(),a._state=l({},a._state,{active:i.classList.contains(c)}),a}return a(t,e),u(t,[{key:"menuClick",value:function(e){var t=this._util,n=t.activeClass,o=t.optionsElem,r=e.target;y(o.getElementsByClassName("menu-item-active")).forEach(function(e){e.classList.remove("menu-item-active")}),this.didComplete(null,r.getAttribute("data-value")||r.value.toLowerCase()),this._state.active=!1,r.classList.add("menu-item-active"),o.classList.remove(n)}},{key:"toggleMenu",value:function(){var e=this._util,t=e.activeClass,n=e.optionsElem;this._state.active?(this._state.active=!1,n.classList.remove(t)):(this._state.active=!0,n.classList.add(t))}},{key:"handleClickOutside",value:function(e){if(this._state.active){var t=e.waferComposedMap,n=this._util,o=n.activeClass,r=n.optionsElem,a=n.toggleElem;t().get(r)||t().get(a)||(this._state.active=!1,r.classList.remove(o))}}}]),t}(v);w.events={click:[["menu-item","menuClick"],["menu-toggle","toggleMenu"]]};var g=w,_=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var o in n)Object.prototype.hasOwnProperty.call(n,o)&&(e[o]=n[o])}return e},O=window.wafer.controllers.WaferBaseController,j=function(e){function t(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},n=e.containerClass,o=void 0===n?null:n,r=e.root,a=void 0===r?document:r,c=e.selector;i(this,t);var l=s(this,(t.__proto__||Object.getPrototypeOf(t)).call(this,{root:a,selector:c,WaferClass:g}));return l._options=_({},l._options,{props:{},container:!!o&&a.getElementsByClassName(o)}),l.sync(),l}return c(t,e),t}(O),C=j;t.default=new C({selector:"wafer-menu"})}})});