$(document).ready(function () {
    var offset_top = $('.inner-item-detail').last().offset().top
    url = window.location.href
    url = url.split('/')
    url = url[url.length - 2]
    var load_enabled = true
    $(window).scroll(function () {
        if ($(window).scrollTop() > offset_top && load_enabled) {
            load_enabled = false
            var data = $('.inner-item-detail').last().data('item')
            $.ajax({
				url: '/load_content/'+url+'/',
				data: {'item': data},
				type: 'POST',
				success: function(html) {
                    try {
                        $(html).appendTo($(".inner-content .container")).hide().fadeIn(500)
                        $('.inner-item-detail').last().find('[data-lightbox]').lightBox();
                        if ($(window).width() < 768) {
                            $('.inner-item-detail').last().find('.inner-item__images').owlCarousel({
                                singleItem: true,
                                navigationText : ["<div class='button-prev'><img src='/static/img/arr-prev.png'/></div>", "<div class='button-next'><img src='/static/img/arr-next.png'/></div>"]
                            })
                        }
                        try {
                            $('.inner-images-type3').each(function() {
                                $(this).children('.inner-image__wrap:first').after($(this).children('.inner-image-left').first())
                                $(this).children('.inner-image__wrap:first').after($(this).children('.inner-image-right').first())
                                $(this).children('.inner-image-right:first').after($(this).children('.inner-image-left').last())
                            })
                        } catch(err) {
                            console.log(err)
                        }
				    }
				    catch (err) {
				        console.log('last')
                    }
				    offset_top = $('.inner-item-detail').last().offset().top
                    setTimeout(function () {
                       load_enabled = true
                    }, 500)
				},
				error: function() {
					console.log('an error has been occured...')
				}
			})
        }
    })
})