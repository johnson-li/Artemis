"use strict";!function(){var n,r,e,i,a,o,d="header-mail-button",c="header-mail-panel",u="header-notification-button",s="header-notification-panel",l=".headertdv2wafer";function f(e,t){if(e){var n={id:e.id},i=e.getAttribute(t||"data-ylk");return i&&(n=i.split(";").reduce(function(e,t){var n=t.split(":");return 2===n.length&&(e[n[0]]=n[1]),e},n)),n}}function v(){return e=e||(n.YAHOO&&n.YAHOO.i13n&&n.YAHOO.i13n.rapidInstance||n.rapidInstance)}function m(){var e,t,n;return i||(t=(f(e=r&&r.querySelector(l),"data-i13n")||{}).sec||"hd",n=e&&f(e),i=Object.assign({},{sec:t},n)),i}function E(e){var t,n,i,a=v();a&&(n=(t=r.getElementById(e))&&t.querySelectorAll("a,button"),i=Object.assign({},m(),{_links:[]}),n&&(n.forEach(function(e){var t=f(e);t&&t.slk&&i._links.push(t)}),a.beaconLinkViews&&a.beaconLinkViews([i])))}function p(e,t){var n=v(),i=t&&Object.assign({},m(),f(t),{itc:2});t&&i&&n&&n.beaconClick(i.sec||"hd",i.slk||e,t.getAttribute("data-rapid_p"),i)}function t(e){var t,n=e&&e.target;n&&n.getAttribute&&((t=n.getAttribute("id"))===d?(p("mail",a||r.getElementById(d)),E(c)):t===u&&(p("notifications",o||r.getElementById(u)),E(s)))}function g(){(a=r.getElementById(d))&&a.addEventListener("mouseenter",t),(o=r.getElementById(u))&&o.addEventListener("mouseenter",t);var e=r.getElementById("dialogue-open-locker");e&&e.addEventListener("click",b)}function b(){var e,t=r.body;"undefined"!=typeof CustomEvent?t.dispatchEvent(new CustomEvent("show-locker")):((e=document.createEvent("Event")).initEvent("show-locker",!0,!0),t.dispatchEvent(e))}function h(e,t){n=e,r=t}"undefined"!=typeof module?(module.exports.defineGlobals=h,module.exports.initEventHandlers=g,module.exports.handleHeaderMenuHover=t):window&&document&&(h(window,document),n.wafer&&n.wafer.ready(g))}();