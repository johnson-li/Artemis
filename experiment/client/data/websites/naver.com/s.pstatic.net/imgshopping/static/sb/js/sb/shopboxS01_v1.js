/**
 * 네이버 쇼핑박스. (구버전 : shopboxR0005_v2.js)
 */
(function(global, $) {
	'use strict';

	var sbData = global.sbData = {};
	sbData.version = '1.0';

	// 타입 구분
	sbData.typeProduct = 'product';
	sbData.typeMall = 'mall';
	sbData.typeMen = 'men';

	sbData.parentHeightControl = function() {
		if(typeof window.parent.adjustShopcastHeight !== "undefined") {
			window.parent.adjustShopcastHeight(window.document.body.offsetHeight);
		}
	};

	/**
	 * html 데이터 가져오기.
	 * @param url
	 * @param params
	 * @param targetElemId
	 */
	sbData.getCnts = function(url, params, targetElemId, callback) {
		params.bucket = bucket;

		$.ajax( {
			url: url,
			data: params,
			method: 'GET',
			dataType: 'html',
			cache: false,
			async :	true,
			timeout: 10000
		} )
			.done(function(data, textStatus, jqXHR) {
				try {
					if (jqXHR.status === 200 && data !== null && data !== '') {
						$('#' + targetElemId).html(data);
						sbData.parentHeightControl();

						if(callback && typeof callback === "function") {
							callback();
						}
					}
				} catch (e) {
					console.log(e);
				}
			})
			.fail(function(jqXHR, textStatus, errorThrown) {
				console.log(errorThrown);
			})
			.always(function() {
			});
	};

	// 탭메뉴명 구하기
	sbData.getTabName = function (typeName) {
		return 'tab_' + typeName;
	};

	// 탭메뉴 클릭시
	sbData.clickTab = function (typeName, targetElemId) {

		$("#" + this.getTabName(this.typeProduct) + " a:first-child").removeAttr('aria-selected');
		$('#' + this.getTabName(this.typeMall) + ' a:first-child').removeAttr('aria-selected');
		$('#' + this.getTabName(this.typeMen) + ' a:first-child').removeAttr('aria-selected');
		$('#' + this.getTabName(typeName) + ' a:first-child').attr('aria-selected', true);

		this.getCnts(tabTitle[typeName],{}, targetElemId);
	};

	// [이전] 클릭시
	sbData.prev = function(typeName, targetElemId, curOrder, exposePage, bannerCurOrder, bannerExposePage, callback) {

		this.getCnts(tabTitle[typeName],{type:'prev', order:curOrder, exposePage:exposePage, bannerType:'prev', bannerOrder:bannerCurOrder, bannerExposePage:bannerExposePage}, targetElemId, callback);
	};

	// [다음] 클릭시
	sbData.next = function(typeName, targetElemId, curOrder, exposePage, bannerCurOrder, bannerExposePage, callback) {

		this.getCnts(tabTitle[typeName],{type:'next', order:curOrder, exposePage:exposePage, bannerType:'next', bannerOrder:bannerCurOrder, bannerExposePage:bannerExposePage}, targetElemId, callback);
	};

	// 배너 롤링 아이콘 클릭시
	sbData.nextBanner = function(typeName, targetElemId, bannerCurOrder, bannerExposePage, callback) {

		this.getCnts(tabTitle[typeName], {bannerType:'next', bannerOrder:bannerCurOrder, bannerExposePage:bannerExposePage}, targetElemId, callback);
	};

	// input value 구하기
	sbData.val = function(elemId) {
		return $('#' + elemId).val();
	};

	sbData.focus = function(divId) {
		return function() {
			document.getElementById(divId).focus();
		}
	};


	var main = global.main = {}; // 메인에서 넘겨줄 함수 정의

	main.next = function() {
		var mainNextEl = document.getElementsByClassName('main_next');
		if(mainNextEl && mainNextEl.length > 0) {
			for (var i = 0; i < mainNextEl.length; i++) {
				mainNextEl[i].onclick();
			}
		}
	}
	


}(this, jQuery));


/**
 * 쇼핑박스 초기화
 *  - 쇼핑박스 초기 실행시 초기화할 동작,함수를 지정
 */

(function($) {

	$( document ).ready(function() {

		$('#' + sbData.getTabName(sbData.typeProduct)+ ' > a').on( 'click', function() {
			sbData.clickTab(sbData.typeProduct,'contents');
			return false;
		});

		$('#' + sbData.getTabName(sbData.typeMall) + ' > a').on( 'click', function() {
			sbData.clickTab(sbData.typeMall,'contents');
			return false;
		});

		$('#' + sbData.getTabName(sbData.typeMen) + ' > a').on( 'click', function() {
			sbData.clickTab(sbData.typeMen,'contents');
			return false;
		});

		sbData.parentHeightControl();
	});

	nclk_evt = 1;
	nsc = "navertop.v4";
	nclk_do();

}(jQuery));

