(window.webpackJsonpBoomer=window.webpackJsonpBoomer||[]).push([["imdb.IMDbBornTodayReactFeature"],{"BxGsT30+X2":function(e,t,n){"use strict";var r,o=this&&this.__extends||(r=function(e,t){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)t.hasOwnProperty(n)&&(e[n]=t[n])})(e,t)},function(e,t){function n(){this.constructor=e}r(e,t),e.prototype=null===t?Object.create(t):(n.prototype=t.prototype,new n)}),a=this&&this.__assign||function(){return(a=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var o in t=arguments[n])Object.prototype.hasOwnProperty.call(t,o)&&(e[o]=t[o]);return e}).apply(this,arguments)};Object.defineProperty(t,"__esModule",{value:!0});var i=n("LDoPTt+kJa"),s=n("Kkip5aHMh7"),c=n("h/dxICHpUb"),u=function(e){function t(t){var n=e.call(this,t)||this;return n.state={screenActive:!1,screenHover:!1},n}return o(t,e),t.prototype.render=function(){var e=this.props,t=e.children,n=e.href,r=e.ariaLabel,o=e.onMouseEnter,u=e.onMouseLeave,p=e.onMouseUp,l=e.onMouseDown,d=e.className;if(n&&!r)throw new Error("[Poster] ariaLabel required with href or onClick.");var h={"aria-label":r,onMouseEnter:o,onMouseLeave:u,onMouseUp:p,onMouseDown:l},m=s(c.container,d);return i.createElement("a",a({},h,{href:n,className:m}),t)},t}(i.PureComponent);t.AvatarCard=u},"E/oSZ6rMwx":function(e,t,n){e.exports={bornTodayContainer:"GX_cJ1DtvzFPiQCG4OHMy"}},Lw7FWlTZyw:function(e,t,n){e.exports={nameBornTodayAge:"_3zWyfts9_Qplx2r_tY5AGa","nameBornTodayAge--base":"_31A0X25xnlEAxI-wN-YSfd","nameBornTodayAge--baseAlt":"_1ROQqY_cW0o6VJsw1JwZVy",nameBornTodayName:"_3_yKeOPAgerCkgLh61Pm3k","nameBornTodayName--base":"_2u3gusGlVTu2EYdNag1Ohj","nameBornTodayName--baseAlt":"_2yQH9pjsTBDMwOZF8jLOak"}},NAm5GQf5qy:function(e,t,n){"use strict";var r,o=this&&this.__extends||(r=function(e,t){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)t.hasOwnProperty(n)&&(e[n]=t[n])})(e,t)},function(e,t){function n(){this.constructor=e}r(e,t),e.prototype=null===t?Object.create(t):(n.prototype=t.prototype,new n)});Object.defineProperty(t,"__esModule",{value:!0});var a=n("LDoPTt+kJa"),i=n("l42YtCfhhb"),s=n("ekp6onNDDg"),c=n("o6AyrkJl3Q"),u=n("qDO/KKoIw4"),p=n("8yJgKchHYK"),l=n("OR60K5WmHO"),d=n("Kkip5aHMh7"),h=n("E/oSZ6rMwx"),m={};var f=function(e){function t(t){var n=e.call(this,t)||this;return n.depthQueue=[],n.sendDepthMetrics=i(n.sendDepthMetrics,5e3),n}return o(t,e),t.prototype.render=function(){var e=this,t=this.props,n=t.seeAllLink,r=t.date,o=t.namesBornToday,i={label:l.UIStrings.get("SEE_ALL"),href:n},s=o.map(function(t,n){return a.createElement(u.SubGrid.Item,{span:2,key:n},a.createElement(c.NameBornToday,{name:t.name,age:t.age,namePageLink:t.namePageLink,plaidImageModel:t.plaidImageModel,onFirstVisibile:function(){n>6&&e.onFirstVisibile(n)}}))});return a.createElement("div",{className:d.default(h.bornTodayContainer,"born-today")},a.createElement(p.default,{title:l.UIStrings.get("BORN_TODAY"),description:l.UIStrings.get("PEOPLE_BORN_ON")+" "+r,seeAllInfo:i}),a.createElement(u.Shoveler,{wraps:!1},s))},t.prototype.onFirstVisibile=function(e){this.depthQueue.push(e),this.sendDepthMetrics()},t.prototype.sendDepthMetrics=function(){var e=Math.max.apply(Math,this.depthQueue),n={ref_:t.REF_TAG,pageAction:"depth-"+e,pt:t.METRICS_CONTEXT.PAGE_TYPE,spt:t.METRICS_CONTEXT.SUB_PAGE_TYPE,ht:t.METRICS_CONTEXT.HIT_TYPE};s.default({method:"POST",url:t.METRICS_URL,headers:{"Content-type":"application/x-www-form-urlencoded"},data:this.encodeParameters(n)}).catch(function(e){console.error("Failed to submit scroll depth metric.",e)}),this.depthQueue.splice(0,this.depthQueue.length)},t.prototype.encodeParameters=function(e){return void 0===e&&(e={}),Object.keys(e).map(function(t){return encodeURIComponent(t)+"="+encodeURIComponent(e[t])}).join("&")},t.defaultProps={seeAllLink:m.seeAllLink,namesBornToday:m.namesBornToday,date:m.date},t.METRICS_URL="/tr/",t.REF_TAG="hm_brn",t.METRICS_CONTEXT={PAGE_ACTION:"depth-",PAGE_TYPE:"home",SUB_PAGE_TYPE:"main",HIT_TYPE:"actionOnly"},t}(a.PureComponent);t.BornToday=f,t.default=f},OR60K5WmHO:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),t.UIStrings=new Map([["BORN_TODAY","Born today"],["PEOPLE_BORN_ON","People born on"],["SEE_ALL","See All"]])},"h/dxICHpUb":function(e,t,n){e.exports={container:"_1V2Ido0XiDBXxrqIpbSWzO"}},o6AyrkJl3Q:function(e,t,n){"use strict";var r,o=this&&this.__extends||(r=function(e,t){return(r=Object.setPrototypeOf||{__proto__:[]}instanceof Array&&function(e,t){e.__proto__=t}||function(e,t){for(var n in t)t.hasOwnProperty(n)&&(e[n]=t[n])})(e,t)},function(e,t){function n(){this.constructor=e}r(e,t),e.prototype=null===t?Object.create(t):(n.prototype=t.prototype,new n)}),a=this&&this.__assign||function(){return(a=Object.assign||function(e){for(var t,n=1,r=arguments.length;n<r;n++)for(var o in t=arguments[n])Object.prototype.hasOwnProperty.call(t,o)&&(e[o]=t[o]);return e}).apply(this,arguments)};Object.defineProperty(t,"__esModule",{value:!0});var i=n("qDO/KKoIw4"),s=n("tzxR7eFjx8"),c=n("LDoPTt+kJa"),u=n("BxGsT30+X2"),p=n("Kkip5aHMh7"),l=n("xGQypn1iJY"),d=n("Lw7FWlTZyw"),h=function(e){function t(t){var n=e.call(this,t)||this;return n.state={screenActive:!1,screenHover:!1},n}return o(t,e),t.prototype.render=function(){var e=this,t=this.props,n=t.name,r=t.age,o=t.namePageLink,h=t.plaidImageModel,m=t.className,f={url:h.url,caption:h.caption,maxWidth:h.maxWidth,maxHeight:h.maxHeight},_={onMouseEnter:function(){return e.setState({screenHover:!0})},onMouseLeave:function(){return e.setState({screenHover:!1,screenActive:!1})},onMouseDown:function(){return e.setState({screenActive:!0})},onMouseUp:function(){return e.setState({screenActive:!1})}};return c.createElement(s.ThemeContext.Consumer,null,function(t){var s="nameBornTodayAge--"+t.palette.baseColor,h="nameBornTodayName--"+t.palette.baseColor,y=p(d[s],d.nameBornTodayAge),v=p(d[h],d.nameBornTodayName),T=e.state.screenHover?"ipc-lockup-overlay--hover":"",E=e.state.screenActive?"ipc-lockup-overlay--active":"",O=p(T,E),b=c.createElement(c.Fragment,null,c.createElement(i.Avatar,{dynamicWidth:!0},c.createElement(i.Avatar.Image,{imageModel:f}),c.createElement(i.Avatar.Overlay,{className:O})),c.createElement("div",{className:v},n),c.createElement("div",{className:y},r));if(e.props.onFirstVisibile){var A=e.props.onFirstVisibile;return c.createElement(u.AvatarCard,a({},_,{className:m,href:o,ariaLabel:f.caption}),c.createElement(l.InView,{triggerOnce:!0,onChange:function(e){e&&A()}},b))}return c.createElement(u.AvatarCard,a({},_,{className:m,href:o,ariaLabel:f.caption}),b)})},t}(c.PureComponent);t.NameBornToday=h,t.default=h}}]);