var ApplicationEmbed = ApplicationEmbed || function (w, u) {
	var wallObject = {},
		iframeModalObject = null,
		backlinkObject = null,
		iframeModalLoaded = false,
		AppPath = "https://widget.taggbox.com/widget/index.html";
	var loading = true;
	var receiveMessage = function (event) {
		var dataObject;
		if (typeof event.data == 'string') {
			try {
				dataObject = JSON.parse(event.data);
			} catch (e) {
				item = {}
				item["type"] = '';
				dataObject = item;
			}
		}
		else {
			dataObject = event.data;
		}

		switch (dataObject.type) {
			case 'getHeight':
				for (var i in wallObject) {
					if (wallObject[i].id == dataObject.data.iframe) {
						var fixedHeight = parseInt(wallObject[i].getAttribute('data-fixed-height'));
						if (fixedHeight == 1) {
							wallObject[i].parentElement.parentElement.style.height = dataObject.data.height + 'px';
							wallObject[i].style.height = dataObject.data.height + 'px';
							wallObject[i].style.minHeight = dataObject.data.height + 'px';
						}
					}
				}

				if (iframeModalObject == null)
					newModalIframe(dataObject.source);

				if (backlinkObject == null) {
					backlink = false;
					backlinkObject = document.createElement('a');
					backlinkObject.href = dataObject.data.refererlink;
					backlinkObject.text = dataObject.data.referer;
					backlinkObject.target = '_blank';
					backlinkObject.style.display = 'none';
					document.body.appendChild(backlinkObject);
				}
				break;
			case 'showPopUp':
				dataObject.data.parentWidth = window.innerWidth;
				newIframe(dataObject.data, dataObject.source);
				break;
			case 'popupPost':
				popupPost(dataObject.data);
				break;
			case 'closePopUp':
				closePopUp();
				break;
			case 'loadComplete':
				loading = dataObject.loadstatus;
				break;
			case 'scroll':
				for (var i in wallObject) {
					var fixedHeight = parseInt(wallObject[i].getAttribute('data-fixed-height'));
					var wallId = parseInt(wallObject[i].getAttribute('data-wall'));
					if (fixedHeight == 1) {
						var position = document.documentElement.scrollTop;
						if (wallId == 23725) {
							position = document.getElementsByClassName("taggbox-container")[0].closest(".content").scrollTop;
						}
						if (dataObject.data.type == 'top') {
							position = position - 120;
						}
						else {
							position = position + 120;
						}

						if (wallId == 23725) {
							document.getElementsByClassName("taggbox-container")[0].closest(".content").scrollTop = position;
						}
						else {
							document.documentElement.scrollTop = position;
						}
					}
				}
				break;
			default:
				break;
		}
	}
	var popupPost = function (data) {
		var elementExists = document.getElementById("_taggbox_modal_frame");
		if (elementExists && iframeModalObject) {
			if (iframeModalLoaded) {
				elementExists.contentWindow.postMessage(data, elementExists.src);
			}
		}
	}
	var newIframe = function (data, source) {
		var elementExists = document.getElementById("_taggbox_modal_frame");
		if (elementExists && iframeModalObject) {
			if (iframeModalLoaded) {
				elementExists.style.display = 'block';
				elementExists.contentWindow.postMessage(data, elementExists.src);

			}
			else {
				newIframe(data, source);
				return;

			}
		}
		else {
			iframeModalObject = document.createElement('iframe');
			iframeModalObject.src = 'https://widget.taggbox.com/widget-modal/index.html';
			// if (source == 'web') {
			// 	iframeModalObject.src = AppPath + 'w/endPoint/';
			// }
			iframeModalObject.id = '_taggbox_modal_frame';
			iframeModalObject.scrolling = 'no';
			iframeModalObject.frameborder = 0;
			iframeModalObject.allowtransparency = 'true';
			iframeModalObject.style.display = 'block';
			iframeModalObject.style.position = 'fixed';
			iframeModalObject.style.left = '0px';
			iframeModalObject.style.right = '0px';
			iframeModalObject.style.top = '0px';
			iframeModalObject.style.bottom = '0px';
			iframeModalObject.style.width = '100%';
			iframeModalObject.style.height = '100%';
			iframeModalObject.style.border = 'none';
			iframeModalObject.style.zIndex = '99999999';
			iframeModalObject.title = 'Taggbox widget';

			document.body.appendChild(iframeModalObject);
			iframeModalObject.onload = function () {
				iframeModalObject.contentWindow.postMessage(data, iframeModalObject.src);
			};

		}
	}
	var newModalIframe = function (source) {
		var elementExists = document.getElementById("_taggbox_modal_frame");
		if (!elementExists) {
			iframeModalObject = document.createElement('iframe');
			iframeModalObject.src = 'https://widget.taggbox.com/widget-modal/index.html';
			// if (source == 'web') {
			// 	iframeModalObject.src = AppPath + 'w/endPoint/';
			// }
			iframeModalObject.id = '_taggbox_modal_frame';
			iframeModalObject.scrolling = 'no';
			iframeModalObject.frameborder = 0;
			iframeModalObject.allowtransparency = 'true';
			iframeModalObject.style.display = 'none';
			iframeModalObject.style.position = 'fixed';
			iframeModalObject.style.left = '0px';
			iframeModalObject.style.right = '0px';
			iframeModalObject.style.top = '0px';
			iframeModalObject.style.bottom = '0px';
			iframeModalObject.style.width = '100%';
			iframeModalObject.style.height = '100%';
			iframeModalObject.style.border = 'none';
			iframeModalObject.style.zIndex = '99999999';
			iframeModalObject.title = 'Taggbox widget';
			document.body.appendChild(iframeModalObject);
			iframeModalObject.onload = function () {
				iframeModalLoaded = true;
			};
		}
	}
	var closePopUp = function () {
		document.getElementById("_taggbox_modal_frame").style.display = 'none';

	}
	return {
		init: function () {
			var count = 0;
			for (var prop in wallObject) {
				if (wallObject.hasOwnProperty(prop))
					++count;
			}
			if (count == 0) {
				window.addEventListener("message", receiveMessage, false);
			}
			var parentContainer = document.getElementsByClassName('taggbox-container');
			var container = document.getElementsByClassName('taggbox-socialwall');
			for (var i = 0; i < parentContainer.length; i++) {
				var divWidth = parentContainer[i].clientWidth;
				if (divWidth >= window.innerWidth) {
					parentContainer[i].style.width = '100%'
				}
				parentContainer[i].style.lineHeight = 'initial';
				if (container[i].getAttribute("data-wall-id") != 39221) {
					parentContainer[i].style.overflow = 'hidden';
				}
				var styleElement = document.createElement("style");
				parentContainer[i].appendChild(styleElement);
			}


			var iframe;
			for (var i = 0; i < container.length; i++) {
				iframe = container[i].getElementsByTagName("iframe");
				if (iframe.length == 0) {
					var fixedHeight = 1;
					var iframeHeight = 150;

					var containerHeight = container[i].parentElement.style.height;
					containerHeight = parseInt(containerHeight.replace(/[^\d.-]/g, ''));

					if (containerHeight > 100) {
						fixedHeight = 0;
						iframeHeight = containerHeight;
					}
					//var wallUrl = container[i].getAttribute("data-wall-id") + '/' + fixedHeight + '/' + container[i].getAttribute("data-wall-theme");
					var wallUrl = container[i].getAttribute("data-wall-id")
					//var wallType = container[i].getAttribute("data-wall-type") || 'embed';
					var frameUrl = '?webembed=1';
					var r = Math.random().toString(36).substring(7);
					var iframeElem = '<iframe src="' + AppPath + '?wall_id=' + wallUrl + '" data-fixed-height="' + fixedHeight + '" data-height="' + iframeHeight + '" data-wall="' + wallUrl + '" data-position="' + i + '" id="iframe' + r + '" style="visibility: hidden;position: absolute;margin:0;left: -999em;display: inline-block;border: none;width:100%;height:100%;" scrolling="no" frameborder="0" allowtransparency="true" title="Taggbox widget"></iframe>';
					container[i].innerHTML = iframeElem;
					container[i].style.webkitOverflowScrolling = "touch";
					try {
						/*console.log(container[i].parentElement);*/
						container[i].parentElement.style.webkitOverflowScrolling = "touch";
					} catch (err) {
						console.log('a');
					}

					iframeElem = container[i].firstChild;
					wallObject[i] = iframeElem;
					document.getElementById('iframe' + r).addEventListener("load", function () {
						var zIndex = this.getAttribute('data-position');
						var iframeId = this.getAttribute('id');
						var fixedHeight = this.getAttribute('data-fixed-height');
						var iframeHeight = this.getAttribute('data-height');

						this.style.visibility = 'visible';
						this.style.position = 'static';
						var parentContainerHeight = parentContainer[zIndex].offsetHeight;
						this.style.minHeight = parentContainerHeight + 'px';


						var myurl = window.location.href;
						var obj = {
							type: 'startEmbed',
							url: myurl,
							id: iframeId,
							fixedHeight: fixedHeight,
							iframeHeight: iframeHeight,
							theme: container[zIndex].getAttribute("data-wall-theme")
						};

						this.contentWindow.postMessage(obj, this.src);
						var p = document.querySelectorAll('p:empty');
						for (var t = p.length - 1; t > -1; t--) {
							p[t].parentNode.removeChild(p[t]);
						}
						setTimeout(function () {
							var contentHeight = container[zIndex].offsetHeight;
							var containerHeight = parentContainer[zIndex].clientHeight;
							if (containerHeight < contentHeight) {
								parentContainer[zIndex].onscroll = function () {
									if ((parentContainer[zIndex].scrollTop + parentContainer[zIndex].offsetHeight) >= (parseInt(contentHeight) - parseInt(300))) {
										if (loading) {
											loading = false;
											var obj = {
												type: 'loadMore'
											};
											container[zIndex].firstChild.contentWindow.postMessage(obj, container[zIndex].firstChild.src);
										}
									}
								};
							}
							else {
								window.onscroll = function () {
									var body = document.body,
										html = document.documentElement;

									var height = Math.max(body.scrollHeight, body.offsetHeight,
										html.clientHeight, html.scrollHeight, html.offsetHeight);
									if ((window.innerHeight + window.pageYOffset) >= (parseInt(height) - parseInt(50))) {
										if (loading) {
											loading = false;
											var obj = {
												type: 'loadMore'
											};
											for (var j = 0; j < container.length; j++) {
												container[j].firstChild.contentWindow.postMessage(obj, container[j].firstChild.src);
											}
										}
									}
								};

							}
						}, 5000);
					});
				}
			}

		}
	};
}(window, undefined);
ApplicationEmbed.init();