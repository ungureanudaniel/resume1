// js Document

    // Created on   : 04/04/2019.
    // Theme Name   : CVR- CV-Resume Template.
    // Version      : 1.0.
    // Developed by : Jubayer al hasan. (jubayer.hasan1991@gmail.com)


(function($) {
    "use strict";


    $(document).on ('ready', function (){

        // -------------------- Navigation Scroll
        $(window).on('scroll', function (){
          var sticky = $('.theme-top-button'),
          scroll = $(window).scrollTop();
          if (scroll >= 100) sticky.addClass('fixed');
          else sticky.removeClass('fixed');

        });


        // -------------------- Remove Placeholder When Focus Or Click
        $("input,textarea").each( function(){
            $(this).data('holder',$(this).attr('placeholder'));
            $(this).on('focusin', function() {
                $(this).attr('placeholder','');
            });
            $(this).on('focusout', function() {
                $(this).attr('placeholder',$(this).data('holder'));
            });
        });



        //---------------------- Click event to scroll to top
        $('.scroll-top').on('click', function() {
          $('html, body').animate({scrollTop : 0},1500);
          return false;
        });


        // ------------------------ Aside Menu
        if($("#theme-menu-list").length) {
          $('#theme-menu-list a').on('click', function(){
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
              var target = $(this.hash);
              target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
              if (target.length) {
                $('html, body').animate({
                  scrollTop: (target.offset().top - 0)
                }, 1000, "easeOutCubic");
                return false;
              }
            }
          });


          /* scroll animate
          -------------------------------------------------------*/
          var links = $('a.scroll-target');
          links.on('click', function() {
              if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') || location.hostname == this.hostname) {
              var target = $(this.hash);
                  target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                  if (target.length) {
                  $('html,body').animate({
                      scrollTop: target.offset().top - 75,
                      }, 1000);
                      return false;
                  }
              }
          });


          // Activate scrollspy to add active class to navbar items on scroll
          $('body').scrollspy({
            target: 'body',
            offset: 20
          });
          }



        // ---------------------------- Style Switcher
        var switcher = $('.switch-menu');
        if (switcher.length) {
            $('.switch-btn button').on('click', function(){
              $('.switcher').toggleClass('switcher-show')
            });

            $('#styleOptions').styleSwitcher({
                fullPath: 'css/'
            });
          }


        // ----------------------------- Counter Function
        var timer = $('.timer');
        if(timer.length) {
            timer.appear(function () {
              timer.countTo();
          });
        }



        // ------------------------------------- Fancybox
        var fancy = $ (".fancybox");
        if(fancy.length) {
          fancy.fancybox({
            arrows: true,
            animationEffect: "zoom-in-out",
            transitionEffect: "zoom-in-out",
          });
        }


        // ----------------------- Progress Bar
        $('.progress-bar').each(function(){
            var width = $(this).data('percent');
            $(this).css({'transition': 'width 3s'});
            $(this).appear(function() {
                console.log('hello');
                $(this).css('width', width + '%');
                $(this).find('.count').countTo({
                    from: 0,
                    to: width,
                    speed: 3000,
                    refreshInterval: 50,
                });
            });
        });





        // ------------------------------ Partner Logo Footer
        var logoslider = $ (".partner-logo");
          if(logoslider.length) {
              logoslider.owlCarousel({
                loop:true,
                nav:false,
                dots:false,
                autoplay:true,
                autoplayTimeout:4000,
                autoplaySpeed:1000,
                lazyLoad:true,
                singleItem:true,
                responsive:{
                    0:{
                        items:1
                    },
                    550:{
                        items:2
                    },
                    768:{
                        items:3
                    },
                    992:{
                        items:4
                    }
                }
            });
          }


          // ------------------------------- Testimonial Slider
          // var tSlider = $ (".testimonial-slider");
          // if(tSlider.length) {
          //     tSlider.owlCarousel({
          //       loop:true,
          //       nav:false,
          //       dots:false,
          //       autoplay:true,
          //       autoplayTimeout:4000,
          //       smartSpeed:1200,
          //       autoplayHoverPause:true,
          //       lazyLoad:true,
          //       items:1
          //   });
          // }




        // --------------------------------- Contact Form
        // init the validator
        // validator files are included in the download package
        // otherwise download from http://1000hz.github.io/bootstrap-validator
        if($("#contact-form").length) {
          $('#contact-form').validator();
          // when the form is submitted
          $('#contact-form').on('submit', function (e) {
              // if the validator does not prevent form submit
              if (!e.isDefaultPrevented()) {
                  var url = "inc/contact.php";
                  // POST values in the background the the script URL
                  $.ajax({
                      type: "POST",
                      url: url,
                      data: $(this).serialize(),
                      success: function (data)
                      {
                          // data = JSON object that contact.php returns
                          // we recieve the type of the message: success x danger and apply it to the
                          var messageAlert = 'alert-' + data.type;
                          var messageText = data.message;
                          // let's compose Bootstrap alert box HTML
                          var alertBox = '<div class="alert ' + messageAlert + ' alert-dismissable"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>' + messageText + '</div>';
                          // If we have messageAlert and messageText
                          if (messageAlert && messageText) {
                              // inject the alert to .messages div in our form
                              $('#contact-form').find('.messages').html(alertBox);
                              // empty the form
                              $('#contact-form')[0].reset();
                          }
                      }
                  });
                  return false;
              }
          });
        }


        // -------------------------- Partical Bg

    });


    $(window).on ('load', function (){ // makes sure the whole site is loaded

        // -------------------- Site Preloader
        $('#loader').fadeOut(); // will first fade out the loading animation
        $('#loader-wrapper').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website.
        $('body').delay(350).css({'overflow':'visible'});


          // ------------------------------- AOS Animation
          // AOS.init({
          //   duration: 1000,
          //   mirror: true
          // });



        // ----------------------------- isotop gallery
          if ($("#isotop-gallery-wrapper").length) {
            var $grid = $('#isotop-gallery-wrapper').isotope({
              // options
              itemSelector: '.isotop-item',
              percentPosition: true,
              masonry: {
                // use element for option
                columnWidth: '.grid-sizer'
              }

            });
            // initial filtering
            $grid.isotope({filter:'.web'})
            // filter items on button click
            $('.isotop-menu-wrapper').on( 'click', 'li', function() {
              var filterValue = $(this).attr('data-filter');
              $grid.isotope({ filter: filterValue });
            });

             // change is-checked class on buttons
              $('.isotop-menu-wrapper').each( function( i, buttonGroup ) {
                var $buttonGroup = $( buttonGroup );
                $buttonGroup.on( 'click', 'li', function() {
                  $buttonGroup.find('.is-checked').removeClass('is-checked');
                  $( this ).addClass('is-checked');
                });
              });
          }




    });

})(jQuery);
