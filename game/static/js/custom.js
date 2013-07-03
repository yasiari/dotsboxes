/*
*
* Custom JS
*/ 

jQuery(function() {

    new Page({
    
        // METHODS

    }).Is("*", function(pagename, methods) {
    

    }) ("IndexPage", function(pagename, methods) { 
    
    
    }) ("LoginPage", function(pagename, methods) {
    
        // Backbone LoginView
        new APP.Views.LoginView();

    }) ("RegisterPage", function(pagename, methods) {
    
     
        // Backbone LoginView
        new APP.Views.RegisterView();
    });
});
