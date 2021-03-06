/*
*
* Game Object new Game(area).start(player_count, )
*/
var Game = function(area, players) {

    var table;
    var turn;
    var layout;

    var playercount = parseInt(players.length);
    var Players = players;

    this.start = function(height, width){
	    
	    turn = -1; //reset turns
	    
	    var h = parseInt(height);
	    var w = parseInt(width);

	    layout = BoxLayout(w, h);


	    //calculate actual table width & height
	    var aw = 2*layout.maxX+3;
	    var ah = 2*layout.maxY+3;
	    
	    //make the table
	    table = create_table(aw, ah);
	    
	    
	    //format the table
	    var rows_dots = jQuery(""); 
	    var column_dots = jQuery("");
	    
	    //get rows
	    for(var i=0;i<ah;i=i+2){
	    	rows_dots = rows_dots.add(table_get_row(i)); 
	    }
	    //get columns
	    for(var i=0;i<aw;i=i+2){
	    	column_dots = column_dots.add(table_get_column(i));
	    }
	    
	    //get the actual dots
	    var dots = rows_dots.filter(column_dots)
	    .addClass("dot");
	    
	    //remove non-dots
	    dots.each(function(i, e){
	    	var dot = jQuery(e);
	    	if(!DotIsInLayout(dot.data("x"), dot.data("y"))){
	    		dot.addClass("undot"); 
	    	} else {
	    		return true;
	    	}
	    	return true;
	    });
	    
	    //make horizontal lines selectable
	    var rows = rows_dots.not(dots).addClass("selectablevert").filter(function(i, e){
	    	var cell = jQuery(e);
	    	if(!LineIsInLayout(cell.data("x"), cell.data("y"))){
	    		cell.removeClass("selectablevert").addClass("unselectablevert");
	    		return false;
	    	}
	    	return true;
	    });
	    
	    //make vertical lines selectable
	    var columns = column_dots.not(dots).addClass("selectablehort").filter(function(i, e){
	    	var cell = jQuery(e);
	    	if(!LineIsInLayout(cell.data("x"), cell.data("y"))){
	    		cell.removeClass("selectablehort").addClass("unselectablehort");
	    		return false;
	    	}
	    	return true;
	    });;


	    //append the table to the game area
	    jQuery(area).html("").append(table);
	    

	    //update the game
	    this.update();
    };


    this.update = function(){
        var self = this;
   
    	//remove all the old listeners etc
    	var data = table
    	.find(".selectablevert, .selectablehort")
    	.off("click")
    	.off("mouseenter mouseleave")
    	.removeAttr("style")
    	.not(".selected")
    
    	.click(function(){
    		jQuery(this).addClass("selected");
    		self.update();
    	});
    
    	var did_something = false; //Did the player gain a new box?
    	
    	//create points array for player points and populate it
    	var points = [];
    	for(var i=0;i<playercount;i++){
    		points.push(0);		
    	}
    	
    	//iterate over all the boxes in the layout and check if the yhave already been taken or if they are surrounded 
    	for(var i=0;i<=layout.maxX;i++){
    		for(var j=0;j<=layout.maxY;j++){
    			if(BoxIsInLayout(2*i+1, 2*j+1)){
    				if(!is_taken(i, j) && is_surrounded(i, j)){
                        var player = getPlayer(turn);

    					//box is suurounded but not taken
    					get_table_cell(2*i+1, 2*j+1)
    					.addClass("taken")
    					.css("background-color", player.color)
    					.data("playerId", turn);
    					did_something = true;
    				}
    				
    				if(is_taken(i, j)){
    					//count the points
    					points[
    						get_table_cell(2*i+1, 2*j+1).data("playerId")
    					]++;
    				}
    			}
    		}
    	}
    	
    	//whos next ?
    	if(!did_something){
    		turn = (turn + 1) % playercount;
    	}
    
    	//set the hover color
    	data
    	.hover(function(){

            var player = getPlayer(turn);
    		jQuery(this).css("background-color", player.color);
    	}, function(){
    		jQuery(this).removeAttr("style");
    	});
    	
    	var scoreNode = jQuery("#Scores").html("");
    
    	if(gameHasWinner(points)){
            alert("Finish Game");    
    	}
    	
    	//update the player ranking
    	var ranking = makePlayerRanking(points, playercount);
    	var taken = 0;
    

    	for(var i=0;i<ranking.length;i++){
    		for(var j=0;j<ranking[i].length;j++){
    			var player = ranking[i][j];
    			var score = points[player];
    			var color = getPlayer(player).color

    			taken += score; 

                var score_player = jQuery("<div/>", {
                
                });

    			var node = jQuery("<span>").html(getPlayer(player).username + " <b>" + score +"</b> Boxes").css("background-color", color);
    			scoreNode.append(node);

                // sort player 
    			if(player == turn){
                    node.css("font-weight", "bold");
                };
    		}
    	}
    	
        var opened_box = jQuery("<span>").text(""+taken+"/"+(layout.length)+" Boxes occupied. ");
    	scoreNode.append(opened_box);
    };
    
    /*
    	A Box layout
    */
    var BoxLayout = function(width, height){
    	var box = [];
    	for(var i=0;i<width;i++){
    		for(var j=0;j<height;j++){
    			box.push([i, j]);
    		}
    	}
    	box.maxX = width-1;
    	box.maxY = height-1;
    	return box;
    };
    
    /*
    	A Triangle layout
    */
    var TriangleLayout = function(size){
    	var box = [];
    	for(var i=0;i<=size;i++){
    		for(var j=0;j<i;j++){
    			box.push([size-i, size-j-1]);
    		}
    	}
    	box.maxX = size-1;
    	box.maxY = size-1;
    	return box;
    };
    
    /*	
    
    	Checks if a box is in the current layout
    */
    var BoxIsInLayout = function(boxX, boxY){
    	var x = (boxX-1) / 2;
    	var y = (boxY-1) / 2;
    	//return (layout.indexOf([x, y]) == -1)
    	//above line does not work because [0, 0] == [0, 0] returns false
    	for(var i=0;i<layout.length;i++){
    		if(layout[i][0] == x && layout[i][1] == y){
    			return true;
    		}
    	}
    	return false;
    };
    
    /*
    	Checks if a line is in the current layout
    */
    var LineIsInLayout = function(lineX, lineY){
    	//check if we are are adjacent to a box
    	return (
    		   BoxIsInLayout(lineX, lineY+1)
    		|| BoxIsInLayout(lineX, lineY-1)
    		|| BoxIsInLayout(lineX+1, lineY)
    		|| BoxIsInLayout(lineX-1, lineY)
    	);
    }
    
    /*
    	Checks if a dot is in the current layout
    */
    var DotIsInLayout = function(dotX, dotY){
    	//check if we have an adjacent line that ends here
    	return (
    		   LineIsInLayout(dotX, dotY+1)
    		|| LineIsInLayout(dotX, dotY-1)
    		|| LineIsInLayout(dotX+1, dotY)
    		|| LineIsInLayout(dotX-1, dotY)
    	);
    }
    
    
    /*
    	Get player ranking
    */
    var makePlayerRanking = function(player_scores){
    	//first sort the scores then get the player ids
    	var arr = [];
    	for(var i=0;i<playercount;i++){
    		arr.push([i, player_scores[i]]);
    	}
    	arr.sort(function(left, right){
    		return (left[1]>=right[1])?(-1):1;
    	});
    	var res = [];
    	var points = -1;
    	for(var i=0;i<playercount;i++){
    		var playerid = arr[i][0];
    		if(points == arr[i][1]){
    			res[res.length-1].push(arr[i][0]);
    		} else {
    			res.push([arr[i][0]]);
    		}
    
    		points = arr[i][1];
    	}
    	return res;
    };
    
    /*
    	Check if the game has a winner. 
    */
    var gameHasWinner = function(player_scores){
    	var total = 0;
    	var maxPoints = layout.length;
    	for(var i=0;i<player_scores.length;i++){
    		total += player_scores[i];
    		if(player_scores[i] > (maxPoints) / 2){
    			return true;
    		}
    	}
    	return (total == maxPoints);
    };
    
    /*
    	Checks if a square is taken
    */
    var is_taken = function(i, j){
    	return get_table_cell(2*i+1, 2*j+1).is(".taken");
    }
    
    /*
    	Checks if a square is surrounded.
    */
    var is_surrounded = function(i, j){
    	return (get_table_cell(2*i, 2*j+1).is(".selected") && 
    		get_table_cell(2*i+2, 2*j+1).is(".selected") && 
    		get_table_cell(2*i+1, 2*j).is(".selected") && 
    		get_table_cell(2*i+1, 2*j+2).is(".selected"));
    }
    
    /*
    	Get Player Colors
    */
    var getPlayer = function(i){
    	return Players[i];
    };
    
    /*
    	Create a table
    	@param	w	Table width
    	@param	h	Table height
    */
    var create_table = function(w, h){
    	var $table = jQuery("<table>");
    	var $td = jQuery("<td>");
    	var $tr = jQuery("<tr>");
    	for(var i=0;i<w;i++){
    		$tr.append($td.clone().data("x", i));
    	}
    	for(var i=0;i<h;i++){
    		var clone = $tr.clone(true);
    		clone.find("td").addBack().data("y", i);
    		$table.append(clone);
    	}
    	return $table;
    }
   

    /*
    *
    * Game box 
    * 
    *     *******
    *     *     *
    *     * box * 
    *     *     *
    *     *******
    */ 
    var get_box = function() {

        return table.find("td").filter(function() { return !this.getAttribute("class") })
    };



    /*
    	Get table cell
    */
    var get_table_cell = function(i, j){
    	return table.find("tr:nth-child("+(j+1)+") td:nth-child("+(i+1)+")");
    }
    
    /*
    	Get the ith row of a table. 
    */
    var table_get_row = function(i){
    	return table.find("tr:nth-child("+(i+1)+")").find("td");
    }
    
    /*
    	Get the nth column of a table
    */
    var table_get_column = function(i){
    	return table.find("tr td:nth-child("+(i+1)+")");
    }
    
};

