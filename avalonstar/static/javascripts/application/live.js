// Generated by CoffeeScript 1.8.0
(function() {
  $(function() {
    $.adaptiveBackground.run({
      parent: ".game"
    });
    $(".game-image img").on("ab-color-found", function(ev, payload) {
      return $(this).closest('.game').find('.game-metadata-marker').css('background-color', payload.color);
    });
    return particlesJS("particles-js", {
      particles: {
        color: "#29384D",
        shape: "circle",
        opacity: 0.5,
        size: 3,
        size_random: true,
        nb: 175,
        line_linked: {
          enable_auto: true,
          distance: 100,
          color: "#29384D",
          opacity: 0.9,
          width: 1,
          condensed_mode: {
            enable: true,
            rotateX: 600,
            rotateY: 600
          }
        },
        anim: {
          enable: true,
          speed: 1.75
        }
      },
      interactivity: {
        enable: false
      },
      retina_detect: true
    });
  });

}).call(this);
