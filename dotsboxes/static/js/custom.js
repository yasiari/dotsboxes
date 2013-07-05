/*
*
* Custom JS
*/ 

jQuery(function() {

    new Page({
    
        // METHODS
    }).Is("*", function(pagename, methods) {

        new APP.Views.OnlinePlayersView();
    }) ("IndexPage", function(pagename, methods) { 

    }) ("SigninPage", function(pagename, methods) {
    
        new APP.Views.SigninView();
    }) ("SignupPage", function(pagename, methods) {
    
        new APP.Views.SignupView();
    }) ("PlayerEditPage", function(pagename, methods) {
    
        new APP.Views.PlayerEditView();
    });
});
