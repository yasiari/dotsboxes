/*
*
* Custom JS
*/ 

jQuery(function() {

    new Page({
    
        // METHODS

    }).Is("*", function(pagename, methods) {
    

    }) ("IndexPage", function(pagename, methods) { 
    
    
    }) ("SigninPage", function(pagename, methods) {
    
        // Backbone SigninView
        new APP.Views.SigninView();

    }) ("SignupPage", function(pagename, methods) {
    
        // Backbone SigninView
        new APP.Views.SignupView();
    });
});
