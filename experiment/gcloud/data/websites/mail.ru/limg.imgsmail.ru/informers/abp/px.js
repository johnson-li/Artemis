(function (abp) {
	abp = abp || false;
	// with fallback for IE
	var script = document.currentScript || getCurrentScript(/^https:\/\/limg\.imgsmail\.ru\/informers\/abp\/px\.js/)

	if (script) {
		var query = script.src.replace(/^[^\?]+\??/, '').split('&');
		var params = {};
		
		for (var i = 0; i < query.length; i++) {
			var param = query[i].split('=');
			params[param[0]] = param[1];
		}

		if (params['ch'] == 1) {
			abp = true;
		} else if (params['ch'] == 2) {
			abp = abp && false;
		}
	}

	window.abp = abp;

	function getCurrentScript(srcPattern) {
		var scripts = document.getElementsByTagName('script');
		var matched;

		for (var i = 0; i < scripts.length; i++) {
			var script = scripts[i];

			if (script.src && srcPattern.test(script.src)) {
				matched = script;
			}
		}

		return matched
	}
})(window.abp)
