!function(a){"use strict";a(".js-fullheight").css("height",a(window).height()),a(window).resize(function(){a(".js-fullheight").css("height",a(window).height())});setTimeout(function(){a("#ftco-loader").length>0&&a("#ftco-loader").removeClass("show")},1);a(window).scroll(function(){var e=a(this).scrollTop(),s=a(".ftco_navbar"),t=a(".js-scroll-wrap");e>150&&(s.hasClass("scrolled")||s.addClass("scrolled")),e<150&&s.hasClass("scrolled")&&s.removeClass("scrolled sleep"),e>30&&(s.hasClass("awake")||s.addClass("awake"),t.length>0&&t.addClass("sleep")),e<30&&(s.hasClass("awake")&&(s.removeClass("awake"),s.addClass("sleep")),t.length>0&&t.removeClass("sleep"))});a(".ftco-animate").waypoint(function(e){"down"!==e||a(this.element).hasClass("ftco-animated")||(a(this.element).addClass("item-animate"),setTimeout(function(){a("body .ftco-animate.item-animate").each(function(e){var s=a(this);setTimeout(function(){var a=s.data("animate-effect");"fadeIn"===a?s.addClass("fadeIn ftco-animated"):"fadeInLeft"===a?s.addClass("fadeInLeft ftco-animated"):"fadeInRight"===a?s.addClass("fadeInRight ftco-animated"):s.addClass("fadeInUp ftco-animated"),s.removeClass("item-animate")},50*e,"easeInOutExpo")})},100))},{offset:"95%"})}(jQuery);