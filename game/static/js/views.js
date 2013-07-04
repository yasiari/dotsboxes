(function() {

    var root = this;

    // Backbone App
    root.APP = {

        // Views Object
        Views: {}
    };

    APP.Views.LoginView = Backbone.View.extend({
        el: "#LoginPage",
        events: {
        
            "click #LoginButton": "login"
        },
        initialize: function() { this.render(); },

        render: function() {
            this.$el.find("#id_playername").focus();
        },

        login: function(e) {
            e.preventDefault();
            var $this = jQuery(e.currentTarget);
            var loginForm = jQuery("#LoginForm");
            
            // submit form
            loginForm.submit();
        }
    });


    APP.Views.RegisterView = Backbone.View.extend({
        el: "#RegisterPage",
        events: {
        
            "click #RegisterButton": "register"
        },

        initialize: function() { this.render(); },

        render: function() {
            this.$el.find("#id_playername").focus();
        },

        register: function(e) {
            e.preventDefault();
            var $this = jQuery(e.currentTarget);
            var registerForm = jQuery("#RegisterForm");
            
            // submit form
            registerForm.submit();
        }

    });
}).call(this);
