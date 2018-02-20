"use strict";

$(window).on("load", function() {

}), $(document).ready(function() {

    // Plugins init
    $(".scrollbar-inner")[0] && $(".scrollbar-inner").scrollbar().scrollLock();
    $('.selectpicker')[0] && $('.selectpicker').selectpicker();
    $('.textarea-autosize')[0] && autosize($('.textarea-autosize'));
    $('[data-toggle="tooltip"]').tooltip();
    $('[data-toggle="popover"]').each(function() {
        var popoverClass = $(this).data('color');
        $(this).popover({
            trigger: 'focus',
            template: '<div class="popover popover-'+popoverClass+'" role="tooltip"><div class="arrow"></div><h3 class="popover-header"></h3><div class="popover-body"></div></div>'
        })
    });
    

    // Floating label
    $('.form-control').on('focus blur', function(e) {
        $(this).parents('.form-group').toggleClass('focused', (e.type === 'focus' || this.value.length > 0));
    }).trigger('blur');
    
    // Custom input file
    $('.custom-input-file').each(function() {
        var $input = $(this),
            $label = $input.next('label'),
            labelVal = $label.html();

        $input.on('change', function(e) {
            var fileName = '';

            if (this.files && this.files.length > 1)
                fileName = (this.getAttribute('data-multiple-caption') || '').replace('{count}', this.files.length);
            else if (e.target.value)
                fileName = e.target.value.split('\\').pop();

            if (fileName)
                $label.find('span').html(fileName);
            else
                $label.html(labelVal);
        });

        // Firefox bug fix
        $input.on('focus', function() {
            $input.addClass('has-focus');
        })
        .on('blur', function() {
            $input.removeClass('has-focus');
        });
    });
    
    // NoUI Slider
    if ($(".input-slider-container")[0]) {
        $('.input-slider-container').each(function() {

            var slider = $(this).find('.input-slider');
            var sliderId = slider.attr('id');
            var minValue = slider.data('range-value-min');
            var maxValue = slider.data('range-value-max');

            var sliderValue = $(this).find('.range-slider-value');
            var sliderValueId = sliderValue.attr('id');
            var startValue = sliderValue.data('range-value-low');

            var c = document.getElementById(sliderId),
                d = document.getElementById(sliderValueId);

            noUiSlider.create(c, {
                start: [parseInt(startValue)],
                connect: [true, false],
                //step: 1000,
                range: {
                    'min': [parseInt(minValue)],
                    'max': [parseInt(maxValue)]
                }
            });

            c.noUiSlider.on('update', function(a, b) {
                d.textContent = a[b];
            });
        })

    }

    if ($("#input-slider-range")[0]) {
        var c = document.getElementById("input-slider-range"),
            d = document.getElementById("input-slider-range-value-low"),
            e = document.getElementById("input-slider-range-value-high"),
            f = [d, e];

        noUiSlider.create(c, {
            start: [parseInt(d.getAttribute('data-range-value-low')), parseInt(e.getAttribute('data-range-value-high'))],
            connect: !0,
            range: {
                min: parseInt(c.getAttribute('data-range-value-min')),
                max: parseInt(c.getAttribute('data-range-value-max'))
            }
        }), c.noUiSlider.on("update", function(a, b) {
            f[b].textContent = a[b]
        })
    }

}), 

$(document).ready(function() {
    function a(a) {
        a.requestFullscreen ? a.requestFullscreen() : a.mozRequestFullScreen ? a.mozRequestFullScreen() : a.webkitRequestFullscreen ? a.webkitRequestFullscreen() : a.msRequestFullscreen && a.msRequestFullscreen()
    }
    $("body").on("click", "[data-action]", function(b) {
        b.preventDefault();
        var c = $(this),
            d = c.data("action"),
            e = "";
        switch (d) {
            case "search-open":
                $(".search").addClass("search--toggled");
                break;
            case "search-close":
                $(".search").removeClass("search--toggled");
                break;
            case "aside-open":
                e = c.data("target"), c.addClass("toggled"), $(e).addClass("toggled"), $(".content, .header").append('<div class="body-backdrop" data-action="aside-close" data-target=' + e + " />");
                break;
            case "aside-close":
                e = c.data("target"), $('[data-action="aside-open"], ' + e).removeClass("toggled"), $(".content, .header").find(".body-backdrop").remove();
                break;
            case "fullscreen":
                a(document.documentElement);
                break;
            case "print":
                window.print();
                break;
            case "clear-localstorage":
                swal({
                    title: "Are you sure?",
                    text: "This can not be undone!",
                    type: "warning",
                    showCancelButton: !0,
                    confirmButtonColor: "#3085d6",
                    confirmButtonText: "Yes, clear it",
                    cancelButtonText: "No, cancel"
                }).then(function() {
                    localStorage.clear(), swal("Cleared!", "Local storage has been successfully cleared", "success")
                });
                break;
        }
    })
});