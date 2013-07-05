(function() {

    var root = this;

    // Backbone App
    root.APP = {

        // Views Object
        Views: {}
    };

    APP.Views.SigninView = Backbone.View.extend({
        el: "#SigninPage",
        events: {
        
            "click #SigninButton": "signin"
        },
        initialize: function() { this.render(); },

        render: function() {
            this.$el.find("#id_playername").focus();
        },

        signin: function(e) {
            e.preventDefault();
            var $this = jQuery(e.currentTarget);
            var signinForm = jQuery("#SigninForm");
            
            // submit form
            signinForm.submit();
        }
    });


    APP.Views.SignupView = Backbone.View.extend({
        el: "#SignupPage",
        events: {
        
            "click #SignupButton": "signup"
        },

        initialize: function() { this.render(); },

        render: function() {
            this.$el.find("#id_playername").focus();
        },

        signup: function(e) {
            e.preventDefault();
            var $this = jQuery(e.currentTarget);
            var signupForm = jQuery("#SignupForm");
            
            // submit form
            signupForm.submit();
        }

    });
}).call(this);
