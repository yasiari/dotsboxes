/*
*
* Game UTILS 
*/

(function() {

    var root = this;


    /*
    *
    * New Player Object
    * 
    * @param {String} playername
    * @param {String} color
    */
    root.Player = function(playername) {
    
        this.playername = playername;
    };


    root.define_player = function(username) {
        var player = new Player(username);
        root.player = player;
    };
}).call(this);
