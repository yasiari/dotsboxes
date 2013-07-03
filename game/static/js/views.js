(function() {

    var root = this;

    // Backbone App
    root.APP = {

        // Views Object
        Views: {}
    };

    APP.Views.LoginView = Backbone.View.extend({
        el: "#LoginPage",
        events: function() {},
        initialize: function() { this.render(); },

        render: function() {
            this.$el.find("#id_playername").focus();
        }
    });


    APP.Views.RegisterView = Backbone.View.extend({
        el: "#RegisterPage",
        events: function() {},
        initialize: function() { this.render(); },

        render: function() {
            this.$el.find("#id_playername").focus();
        }
    });
}).call(this);
