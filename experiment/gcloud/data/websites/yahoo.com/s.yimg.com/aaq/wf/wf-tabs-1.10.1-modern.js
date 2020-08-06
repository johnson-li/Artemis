!function(t,e){"object"==typeof exports&&"object"==typeof module?module.exports=e():"function"==typeof define&&define.amd?define("wafer-tabs",[],e):"object"==typeof exports?exports["wafer-tabs"]=e():(t.wafer=t.wafer||{},t.wafer.wafers=t.wafer.wafers||{},t.wafer.wafers["wafer-tabs"]=e())}("undefined"!=typeof self?self:this,function(){return function(t){function e(i){if(a[i])return a[i].exports;var o=a[i]={i:i,l:!1,exports:{}};return t[i].call(o.exports,o,o.exports,e),o.l=!0,o.exports}var a={};return e.m=t,e.c=a,e.d=function(t,a,i){e.o(t,a)||Object.defineProperty(t,a,{configurable:!1,enumerable:!0,get:i})},e.n=function(t){var a=t&&t.__esModule?function(){return t.default}:function(){return t};return e.d(a,"a",a),a},e.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},e.p="https://s.yimg.com/aaq/wf/",e(e.s="./src/entry.js")}({"./src/entry.js":function(t,e,a){"use strict";function i(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function o(t,e){if(!t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!e||"object"!=typeof e&&"function"!=typeof e?t:e}function s(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function, not "+typeof e);t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,enumerable:!1,writable:!0,configurable:!0}}),e&&(Object.setPrototypeOf?Object.setPrototypeOf(t,e):t.__proto__=e)}function r(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}function n(t,e){if(!t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return!e||"object"!=typeof e&&"function"!=typeof e?t:e}function u(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function, not "+typeof e);t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,enumerable:!1,writable:!0,configurable:!0}}),e&&(Object.setPrototypeOf?Object.setPrototypeOf(t,e):t.__proto__=e)}Object.defineProperty(e,"__esModule",{value:!0});var l=function(){function t(t,e){var a=[],i=!0,o=!1,s=void 0;try{for(var r,n=t[Symbol.iterator]();!(i=(r=n.next()).done)&&(a.push(r.value),!e||a.length!==e);i=!0);}catch(t){o=!0,s=t}finally{try{!i&&n.return&&n.return()}finally{if(o)throw s}}return a}return function(e,a){if(Array.isArray(e))return e;if(Symbol.iterator in Object(e))return t(e,a);throw new TypeError("Invalid attempt to destructure non-iterable instance")}}(),c=function(){function t(t,e){for(var a=0;a<e.length;a++){var i=e[a];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(t,i.key,i)}}return function(e,a,i){return a&&t(e.prototype,a),i&&t(e,i),e}}(),h=function t(e,a,i){null===e&&(e=Function.prototype);var o=Object.getOwnPropertyDescriptor(e,a);if(void 0===o){var s=Object.getPrototypeOf(e);return null===s?void 0:t(s,a,i)}if("value"in o)return o.value;var r=o.get;if(void 0!==r)return r.call(i)},f=window.wafer,v=f.base,b=f.constants,d=f.utils,p=f.WaferBaseClass,m=d.bindEvent,y=d.clearTimeout,g=d.convertNodeListToArray,w=d.findAncestor,T=d.setTimeout,_=d.unbindEvent,E=b.ATTR_PREFIX,O=["handleTargetFocusIn","handleTargetFocusOut","handleTargetMouseLeave","handleTargetMouseOver","tabChange","tabClick","tabFocusIn","tabMouseOver"],A=function(t){function e(t){i(this,e);for(var a,s=o(this,(e.__proto__||Object.getPrototypeOf(e)).call(this,t,{},{})),r=t.getAttribute(E+"active-class")||"wafer-tab-active",n=t.getAttribute(E+"inactive-class"),u=Number(t.getAttribute(E+"scroll-restore"))||0,c=t.hasAttribute(E+"collapsable"),h=t.hasAttribute(E+"handle-hover"),f=t.hasAttribute(E+"handle-focus"),v=t.hasAttribute(E+"tabs-allowdefault"),b=t.hasAttribute(E+"disable-focus"),d=Number(t.getAttribute(E+"auto-switch"))||0,p=Number(t.getAttribute(E+"auto-switch-timeout"))||2e3,m=Number(t.getAttribute(E+"auto-switch-rotation-interval"))||0,y=Number(t.getAttribute(E+"active-index"))||(c?null:0),T=w(t,t.getAttribute(E+"boundary"))||document.body,_=t.getAttribute(E+"target"),A=[],S=0,k=t.getElementsByClassName("tab");a=k[S];++S)A.push({tabElem:a,hasTrigger:"tabActivate"===a.getAttribute(E+"trigger")});var C=g(T.getElementsByClassName(_)),x=l(C,1),j=x[0],I=j&&j.children,F=s._util={activeClass:r,autoSwitchTimeout:p,autoSwitchRotationInterval:m,boundary:T,elem:t,inactiveClass:n,isCollapsable:c,shouldAllowDefault:v,shouldAutoSwitch:d,shouldDisableFocus:b,shouldHandleFocus:f,shouldHandleHover:h,shouldScrollRestore:u,tabsElems:A,targetElem:j,targetElems:I&&g(I)};if(s._state={activeIndex:0,activeTabElem:null,tabsTopStyleInPixel:0},u&&(s._state.scrollPositions=s._state.scrollPositions||{},s._state.tabsTopStyleInPixel=parseInt(window.getComputedStyle(t).top)||0),null!==y){s._state.activeIndex=y;var P=F.tabsElems[y];P&&s.activateTab(P.tabElem,{focus:!0,skipScroll:!0})}return O.forEach(function(t){s[t]=s[t].bind(s)}),d&&s.setTimeoutForTabChange(),s.addEventListeners(),s}return s(e,t),c(e,[{key:"addEventListeners",value:function(){var t=this._util,a=t.shouldAutoSwitch,i=t.targetElem;a&&(m(i,"focusin",this.handleTargetFocusIn,{passive:!1}),m(i,"focusout",this.handleTargetFocusOut,{passive:!1}),m(i,"mouseleave",this.handleTargetMouseLeave,{passive:!1}),m(i,"mouseover",this.handleTargetMouseOver,{passive:!1})),h(e.prototype.__proto__||Object.getPrototypeOf(e.prototype),"addEventListeners",this).call(this)}},{key:"removeEventListeners",value:function(){var t=this._util,a=t.shouldAutoSwitch,i=t.targetElem;a&&(_(i,"focusin",this.handleTargetFocusIn,{passive:!1}),_(i,"focusout",this.handleTargetFocusOut,{passive:!1}),_(i,"mouseleave",this.handleTargetMouseLeave,{passive:!1}),_(i,"mouseover",this.handleTargetMouseOver,{passive:!1})),h(e.prototype.__proto__||Object.getPrototypeOf(e.prototype),"removeEventListeners",this).call(this)}},{key:"setTimeoutForTabChange",value:function(){var t=this,e=this._util.autoSwitchTimeout,a=this._util.autoSwitchRotationInterval;a&&this._util.switchTabTimeout&&(e=a),this.pauseSwitching(),this._util.switchTabTimeout=T(function(){t.switchToNextTab(),t.setTimeoutForTabChange()},e,this)}},{key:"switchToNextTab",value:function(){var t=this._util.tabsElems,e=this._state.activeIndex;e===t.length-1?this.activateTab(t[0].tabElem,{force:!0}):this.activateTab(t[e+1].tabElem,{force:!0})}},{key:"pauseSwitching",value:function(){this._util.switchTabTimeout&&y(this._util.switchTabTimeout,this)}},{key:"activateTab",value:function(t){var e=this,a=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{},i=a.force,o=void 0!==i&&i,s=a.skipScroll,r=void 0!==s&&s,n=this._state.activeTabElem;if(!o&&t===n)return void t.classList.add("active");var u=this._util,l=u.activeClass,c=u.boundary,h=u.elem,f=u.inactiveClass,b=u.shouldAutoSwitch,d=u.shouldScrollRestore,p=u.tabsElems,m=u.targetElems,y=this._state,g=y.activeIndex,w=y.tabsTopStyleInPixel;b&&this.pauseSwitching();var _=0,E=0;if(d){var O=window.pageYOffset||document.documentElement.scrollTop,A=window.pageXOffset||document.documentElement.scrollLeft,S=c.getBoundingClientRect(),k=S.top,C=S.left;_=k+O-w,E=C+A,k>w?r=!0:this._state.scrollPositions[g]={top:O,lef:A}}p.forEach(function(){var a=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},i=a.tabElem,o=a.hasTrigger,s=arguments[1],n=m&&m[s];if(i===t){if(i.classList.add("active"),i.setAttribute("aria-selected",!0),e._state.activeIndex=s,e._state.activeTabElem=i,n){if(d&&!r){var u=e._state||{},c=u.scrollPositions,b=void 0===c?{}:c,p=b[s]||{},y=p.top,g=void 0===y?_:y,w=p.left,O=void 0===w?E:w;T(function(){window.scrollTo(O,g)},2)}f&&n.classList.remove(f),n.classList.add(l),n.setAttribute("aria-hidden",!1),v.unlock(i),v.sync(n),v.syncUI(n),o&&v.trigger(i),v.emitWaferEvent("tab:selected",{elem:h,meta:{targetElem:n}})}}else v.lock(i),i.classList.remove("active"),i.setAttribute("aria-selected",!1),n&&(n.classList.remove(l),f&&n.classList.add(f),n.setAttribute("aria-hidden",!0))})}},{key:"focusActiveTab",value:function(){var t=this._util,e=t.targetElems,a=t.shouldDisableFocus,i=e&&e[this._state.activeIndex];i&&!a&&(i.setAttribute("tabIndex",-1),i.focus())}},{key:"deactivateTab",value:function(t){var e=this,a=this._util,i=a.activeClass,o=a.inactiveClass,s=a.tabsElems,r=a.targetElems;this._state.activeTabElem=null,s.some(function(){var a=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},s=a.tabElem,n=arguments[1],u=r&&r[n];if(s===t)return s.classList.remove("active"),s.setAttribute("aria-selected",!1),u&&(u.classList.remove(i),o&&u.classList.add(o),u.setAttribute("aria-hidden",!0)),e._state.activeIndex=0,!0})}},{key:"tabClick",value:function(t){!this._util.shouldAllowDefault&&t.preventDefault(),this.activateTab(t.eventTarget),this.focusActiveTab()}},{key:"handleTargetFocusIn",value:function(t){this._util.shouldAutoSwitch&&this.pauseSwitching()}},{key:"tabFocusIn",value:function(t){var e=this._util,a=e.shouldHandleFocus,i=e.focusOutTimeout;a&&(i&&y(i,this),this.activateTab(t.currentTarget))}},{key:"handleTargetFocusOut",value:function(t){this._util.shouldAutoSwitch&&this.setTimeoutForTabChange()}},{key:"focusOut",value:function(){var t=this,e=this._util.shouldHandleFocus,a=this._state.activeTabElem;a&&e&&(this._util.focusOutTimeout=T(function(){t.deactivateTab(a)},1,this))}},{key:"handleTargetMouseOver",value:function(t){this._util.shouldAutoSwitch&&this.pauseSwitching()}},{key:"tabMouseOver",value:function(t){var e=this._util,a=e.shouldAutoSwitch,i=e.shouldHandleHover;a&&this.pauseSwitching(),i&&this.activateTab(t.currentTarget)}},{key:"handleTargetMouseLeave",value:function(t){this._util.shouldAutoSwitch&&this.setTimeoutForTabChange()}},{key:"mouseover",value:function(){this._util.shouldAutoSwitch&&this.pauseSwitching()}},{key:"mouseleave",value:function(){var t=this._util,e=t.shouldAutoSwitch,a=t.shouldHandleHover,i=t.isCollapsable,o=this._state.activeTabElem;e&&this.setTimeoutForTabChange(),a&&i&&o&&this.deactivateTab(o)}},{key:"tabChange",value:function(t){t.preventDefault();var e=t.eventTarget.selectedIndex||0;this.activateTab(t.eventTarget.options[e])}},{key:"destroy",value:function(){this.pauseSwitching(),this.removeEventListeners(),h(e.prototype.__proto__||Object.getPrototypeOf(e.prototype),"destroy",this).call(this)}},{key:"config",get:function(){return{shouldAutoSwitch:this._util.shouldAutoSwitch}}}]),e}(p);A.events={change:[["tabs","tabChange"]],click:[["tab","tabClick"]],focusin:[["tab","tabFocusIn"]],focusout:[["_self","focusOut"]],mouseleave:[["_self","mouseleave"]],mouseover:[["tab","tabMouseOver"],["_self","mouseover"]]};var S=A,k=function(){function t(t,e){for(var a=0;a<e.length;a++){var i=e[a];i.enumerable=i.enumerable||!1,i.configurable=!0,"value"in i&&(i.writable=!0),Object.defineProperty(t,i.key,i)}}return function(e,a,i){return a&&t(e.prototype,a),i&&t(e,i),e}}(),C=window.wafer.controllers.WaferBaseController,x=function(t){function e(){var t=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},a=t.root,i=void 0===a?document:a,o=t.selector,s=void 0===o?".wafer-tabs":o;r(this,e);var u=n(this,(e.__proto__||Object.getPrototypeOf(e)).call(this,{root:i,selector:s,WaferClass:S}));return u.sync(),u}return u(e,t),k(e,[{key:"handleVisibilityChange",value:function(){var t=!(arguments.length>0&&void 0!==arguments[0])||arguments[0],e=this._state.elementInstances,a=!0,i=!1,o=void 0;try{for(var s,r=e.values()[Symbol.iterator]();!(a=(s=r.next()).done);a=!0){var n=s.value,u=n.instance;u.config.shouldAutoSwitch&&(t?u.setTimeoutForTabChange():u.pauseSwitching())}}catch(t){i=!0,o=t}finally{try{!a&&r.return&&r.return()}finally{if(i)throw o}}}}]),e}(C),j=x;e.default=new j({selector:".wafer-tabs"})}})});