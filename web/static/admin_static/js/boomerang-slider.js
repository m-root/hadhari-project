"use strict";

$(window).on('load resize', function() {
    // Boomerang slider - Based on Swiper JS
    if ($(".swiper-js-container").length > 0) {
        $('.swiper-js-container').each(function(i, swiperContainer) {

            var $swiperContainer = $(swiperContainer);
            var $swiper = $swiperContainer.find('.swiper-container');

            var swiperEffect = $swiper.data('swiper-effect');

            var slidesPerViewXs = $swiper.data('swiper-xs-items');
            var slidesPerViewSm = $swiper.data('swiper-sm-items');
            var slidesPerViewMd = $swiper.data('swiper-md-items');
            var slidesPerViewLg = $swiper.data('swiper-items');
            var spaceBetweenSlidesXs = $swiper.data('swiper-xs-space-between');
            var spaceBetweenSlidesSm = $swiper.data('swiper-sm-space-between');
            var spaceBetweenSlidesMd = $swiper.data('swiper-md-space-between');
            var spaceBetweenSlidesLg = $swiper.data('swiper-space-between');


            // Slides per view written in data attributes for adaptive resoutions
            slidesPerViewXs = !slidesPerViewXs ? slidesPerViewLg : slidesPerViewXs;
            slidesPerViewSm = !slidesPerViewSm ? slidesPerViewLg : slidesPerViewSm;
            slidesPerViewMd = !slidesPerViewMd ? slidesPerViewLg : slidesPerViewMd;
            slidesPerViewLg = !slidesPerViewLg ? 1 : slidesPerViewLg;

            // Space between slides written in data attributes for adaptive resoutions
            spaceBetweenSlidesXs = !spaceBetweenSlidesXs ? 0 : spaceBetweenSlidesXs;
            spaceBetweenSlidesSm = !spaceBetweenSlidesSm ? 0 : spaceBetweenSlidesSm;
            spaceBetweenSlidesMd = !spaceBetweenSlidesMd ? 0 : spaceBetweenSlidesMd;
            spaceBetweenSlidesLg = !spaceBetweenSlidesLg ? 0 : spaceBetweenSlidesLg;


            var animEndEv = 'webkitAnimationEnd animationend';

            var $swiper = new Swiper($swiper, {
                pagination: $swiperContainer.find('.swiper-pagination'),
                nextButton: $swiperContainer.find('.swiper-button-next'),
                prevButton: $swiperContainer.find('.swiper-button-prev'),
                slidesPerView: slidesPerViewLg,
                spaceBetween: spaceBetweenSlidesLg,
                autoplay: $swiper.data('swiper-autoplay'),
                autoHeight: $swiper.data('swiper-autoheight'),
                effect: swiperEffect,
                speed: 800,
                paginationClickable: true,
                direction: 'horizontal',
                preventClicks: true,
                preventClicksPropagation: true,
                observer: true,
                observeParents: true,
                breakpoints: {
                    460: {
                        slidesPerView: slidesPerViewXs,
                        spaceBetweenSlides: spaceBetweenSlidesXs
                    },
                    767: {
                        slidesPerView: slidesPerViewSm,
                        spaceBetweenSlides: spaceBetweenSlidesSm
                    },
                    991: {
                        slidesPerView: slidesPerViewMd,
                        spaceBetweenSlides: spaceBetweenSlidesMd
                    },
                    1100: {
                        slidesPerView: slidesPerViewLg,
                        spaceBetweenSlides: spaceBetweenSlidesLg
                    }
                },
                onInit: function(s) {

                    var currentSlide = $(s.slides[s.activeIndex]);
                    var elems = currentSlide.find(".animated");

                    elems.each(function() {
                        var $this = $(this);

                        if (!$this.hasClass('animation-ended')) {
                            var animationInType = $this.data('animation-in');
                            var animationOutType = $this.data('animation-out');
                            var animationDelay = $this.data('animation-delay');

                            setTimeout(function() {
                                $this.addClass('animation-ended ' + animationInType, 100).on(animEndEv, function() {
                                    $this.removeClass(animationInType);
                                });
                            }, animationDelay);
                        }
                    });
                },
                onSlideChangeStart: function(s) {

                    var currentSlide = $(s.slides[s.activeIndex]);
                    var elems = currentSlide.find(".animated");

                    elems.each(function() {
                        var $this = $(this);

                        if (!$this.hasClass('animation-ended')) {
                            var animationInType = $this.data('animation-in');
                            var animationOutType = $this.data('animation-out');
                            var animationDelay = $this.data('animation-delay');

                            setTimeout(function() {
                                $this.addClass('animation-ended ' + animationInType, 100).on(animEndEv, function() {
                                    $this.removeClass(animationInType);
                                });
                            }, animationDelay);
                        }
                    });
                },
                onSlideChangeEnd: function(s) {

                    var previousSlide = $(s.slides[s.previousIndex]);
                    var elems = previousSlide.find(".animated");

                    elems.each(function() {
                        var $this = $(this);
                        var animationOneTime = $this.data('animation-onetime');

                        if (!animationOneTime || animationOneTime == false) {
                            $this.removeClass('animation-ended');
                        }
                    });
                }
            });
        });
    }

    // Background image holder - Static hero with fullscreen autosize
    if ($('.background-image-holder').length) {
        $('.background-image-holder').each(function() {

            var $this = $(this);
            var holderHeight;

            if ($this.data('holder-type') == 'fullscreen') {
                if ($this.attr('data-holder-offset')) {
                    if ($this.data('holder-offset')) {
                        var offsetHeight = $('body').find($this.data('holder-offset')).height();
                        holderHeight = $(window).height() - offsetHeight;
                    }
                } else {
                    holderHeight = $(window).height();
                }
                if ($(window).width() > 991) {
                    $('.background-image-holder').css({
                        'height': holderHeight + 'px'
                    });
                } else {
                    $('.background-image-holder').css({
                        'height': 'auto'
                    });
                }
            }
        })
    }
});