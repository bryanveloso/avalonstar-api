// Generated by CoffeeScript 1.7.1
(function() {
  var channel, delay, poolDonating, poolHosting, poolSubscribing, pusher, running, soundSubscription, subscribed;

  delay = 5;

  running = false;

  poolDonating = 0;

  poolHosting = 0;

  poolSubscribing = 0;

  soundSubscription = new Audio('/static/audio/subscription.ogg');

  soundSubscription.volume = 0.7;

  subscribed = function(data, added) {
    if (!running) {
      running = true;
      console.log("" + data.username + " has subscribed!");
      soundSubscription.play();
      ($('.js-type')).text('Subscription');
      ($('.js-username')).text(data.username);
      ($('.js-subscribed')).addClass('visible');
      return setTimeout((function() {
        ($('.js-subscribed')).removeClass('visible');
        running = false;
        if (poolSubscribing >= 1) {
          poolSubscribing--;
          return console.log("There are " + poolSubscribing + " subs left in the pool.");
        }
      }), 7000);
    } else {
      if (!added) {
        poolSubscribing++;
        console.log("There are " + poolSubscribing + " subs left in the pool.");
      }
      return setTimeout((function() {
        console.log("Running the pool subscription for, " + data.username + ".");
        return subscribed(data, true);
      }), delay * 1000);
    }
  };

  pusher = new Pusher('207f2c96da3bdb9301f8');

  channel = pusher.subscribe('live');

  channel.bind('subscribed', function(data) {
    return subscribed(data, false);
  });

}).call(this);
