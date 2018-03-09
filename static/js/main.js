$(document).ready(function() {


	//menu
	$('.burger-menu').click(function() {
		$('nav ul').fadeIn(300)
	})
	if ($(window).width() < 1060) {
		$('nav ul').click(function() {
			$(this).fadeOut(300)
		})
	}

	//replies
	$('.rep-prev').click(function() {
		var current = $('.rep-current');
		current.fadeOut(300);
		setTimeout(function() {
			if (current.prev().length != '') {
				current.prev().addClass('temp');
			} else {
				$('.replies__item:last').addClass('temp');
			}
			$('.replies__item').removeClass('rep-current');
			$('.temp').addClass('rep-current').fadeIn(300);
			$('.replies__item').removeClass('temp');
		}, 300)
	});

	$('.rep-next').click(function() {
		var current = $('.rep-current');
		current.fadeOut(300);
		setTimeout(function() {
			if (current.next().length != '') {
				current.next().addClass('temp');
			} else {
				$('.replies__item:first').addClass('temp');
			}
			$('.replies__item').removeClass('rep-current');
			$('.temp').addClass('rep-current').fadeIn(300);
			$('.replies__item').removeClass('temp');
		}, 300)
	})

	$('.replies-img-min').click(function() {
		var id = $(this).data('reply');
		$('.rep-current').fadeOut(300);
		$('.replies__item').removeClass('rep-current');
		setTimeout(function() {
			$('.replies__item').each(function() {
				if ($(this).data('reply') == id) {
					$(this).addClass('rep-current');
					$(this).fadeIn(300);
				}
			})
		}, 300)
	})


	//popup

	$('.callback').click(function() {
		$('.layer').fadeIn(300);
		$('.callback-popup').fadeIn(500);
	});
	$('.calc-button').click(function() {
		$('.layer').fadeIn(300);
		$('.calculate-popup').fadeIn(500);
	});
	$('.stuff-button').click(function() {
		$('.layer').fadeIn(300);
		$('.stuff-popup').fadeIn(500);
	});
	$('.worker-button').click(function() {
		$('.layer').fadeIn(300);
		$('.worker-popup').fadeIn(500);
	});
	$('.maket-button').click(function() {
		$('.layer').fadeIn(300);
		$('.maket-popup').fadeIn(500);
	});

	$('.layer').click(function(e) {
		if ($(this).has(e.target).length === 0){
			$(this).fadeOut(500);
			$('.popup-min').fadeOut(300);
			$('.layer > .popup-big').remove();
			$('.centered-popup').fadeOut(300)
		}
	})
	$('.close').click(function() {
		$('.layer').fadeOut(500);
		$('.popup-min').fadeOut(300);
		$('.body-wrap').removeClass('blur');
	})

	$('.kitch-item').click(function() {
		$(this).children('.popup-big').clone().appendTo('.layer')
		$('.layer').fadeIn(300);
		$('.layer > .popup-big .popup-right').owlCarousel({
			singleItem : true
		});
	})

	
	
	//inner-slider

	var itemFullWidth = 287;
	if ($(window).width() < 1060) {itemFullWidth=240}
	if ($(window).width() < 1060) {itemFullWidth=240}
	var clicked = false;

	$('.inner-item').each(function(e) {
		$(this).attr('data-number', e+1);
	});
	$('.centered-popup').each(function(e) {
		$(this).attr('data-number', e+1);
	});
	
	$('.inner-next').click(function() {
		if (!$('.inner-slider__container').is(':animated')) {
			pos = clicked ? 4 : 3
			$('.inner-item').removeClass('central')
			$('.inner-item:nth-child('+pos+')').addClass('central')
			$('.inner-slider__container').animate({
				'marginLeft': '-='+itemFullWidth
			}, 300, function() {
				if (clicked) {
					$('.inner-item:first').appendTo('.inner-slider__container');
					$('.inner-slider__container').css({'margin-left': -itemFullWidth+'px'});
				}
			})

			setTimeout(function() {

				var num = $('.inner-item:first-child').data('number');
				
							
				clicked = true;
			}, 300);			
		}
	});

	$('.inner-prev').click(function() {
		if (!$('.inner-slider__container').is(':animated')) {
			if (!clicked) {
				$('.inner-item:last').prependTo('.inner-slider__container');
				$('.inner-slider__container').css({'margin-left': -itemFullWidth+'px'});
			}
			pos = clicked ? 2 : 2
			$('.inner-item').removeClass('central')
			$('.inner-item:nth-child('+pos+')').addClass('central')

			$('.inner-slider__container').animate({
				'marginLeft': '+='+itemFullWidth
			}, 300, function() {
				$('.inner-item:last').prependTo('.inner-slider__container');
				$('.inner-slider__container').css({'margin-left': -itemFullWidth+'px'});
			})

			clicked = true;
		}
	});

	$('input[name=name]').on('keyup keypress', function(e) {
		if (e.keyCode == 8 || e.keyCode == 46) {}
			else
			{
				var letters=' zxcvbnmasdfghjklqwertyuiopQWERTYUIOPLKJHGFDSAZXCVBNMйцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ';
				return (letters.indexOf(String.fromCharCode(e.which))!=-1);
			}
		});
	$("input[name=phone]").mask("8 (999) 999-9999");


	function go(select) {
		var destination = select.offset().top;
		$('html, body').animate({ scrollTop: destination}, 500);
		return false; 
	}


	$('#a5').click(function(e) {
		e.preventDefault()
		go($('.product'))
	})
	$('#a6').click(function(e) {
		e.preventDefault()
		go($('.replies'))
	})
	$('#a7').click(function(e) {
		e.preventDefault()
		go($('.map'))
	})

	$(document).on('click', '.get-price', function() {
		var d = $(this).data('type')
		$('.popup-price form input[name=type]').val(d)
		$('.layer').fadeIn(300)
		$('.popup-price').fadeIn(500)
	})

	if ($(window).width() < 768) {
		$('.inner-item__images').owlCarousel({
			singleItem: true,
			navigationText : ["<div class='button-prev'><img src='/static/img/arr-prev.png'/></div>", "<div class='button-next'><img src='/static/img/arr-next.png'/></div>"]
		})
	}

	$('.inner-item').click(function() {
		var d = $(this).data('number')
		$('.centered-popup[data-number='+d+']').fadeIn(500)
		$('.layer').fadeIn(300)
	})


	try {
		$('.inner-images-type3').each(function() {
			$(this).children('.inner-image__wrap:first').after($(this).children('.inner-image-left').first())
			$(this).children('.inner-image__wrap:first').after($(this).children('.inner-image-right').first())
			$(this).children('.inner-image-right:first').after($(this).children('.inner-image-left').last())
		})
	} catch(err) {
		console.log(err)
	}

	$('form').submit(function(e) {
		e.preventDefault()

		var data = $(this).serialize()

		$.ajax({
			url: '/send_mail/',
			data: data,
			type: 'POST',
			success: function(data) {
				$('.layer').fadeOut(300)
				$('.popup-min').fadeOut(300)
				setTimeout(function() {
					$('.thank').fadeIn(300)
				}, 300)
			},
			error: function() {
				console.log('an error has been occured...')
			}
		})

	})


})