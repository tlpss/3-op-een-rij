var move_possible = true;

function fix_size(){
  
  var grid_size = Math.min($(window).height()*0.8, $(window).width());
  $(".container").css("width", 0.9*grid_size);
  $(".container").css("height", 0.9*grid_size);
}

/*sets indices of fields -> field.index() */
function set_indices() {
    console.log("hallo");
    $(".box").each( function(index) {
        set_index($(this),index);
    });
    console.log("indices set ");
    return;
}


function add_mark(field, state) {
    switch(state) {
        case 0:
            field.html('<div class=" "></div>');
            break;
        
        case 1: 
            field.html('<div class="mark_o"></div>');
            num_o++;
            break;
        
        case 2:
            field.html('<div class="mark_x"></div><div class="mark_xx"></div>');
            num_x++;
            break;
    }
    return;

}

/*this function draws the board based on a list with states */
function draw_board(board) {
    console.log("drawing board")
    num_x=0; 
    num_o=0;
    for (var index=0;index<9;index++) {
        add_mark($(".box:eq("+index+")"), board[index]);
    }
    console.log("#x,#o");
    console.log(num_x,num_o);
    return;
}


/* this function sends position of new x to server 
and updates board and states with the return*/ 
function send_to_server_index_new(jqevent) {
    var field = $(jqevent.target);
    $.getJSON("/next_move",
        JSON.stringify(field.index()),
        function(ret) {
        var val = ret["ret"];
        val=JSON.parse(val)
        var board=val["board"]
        console.log(board);
        draw_board(board);
        if(num_x==3) {
        $(".box").off();
        $(".box").click(send_to_server_index_to_remove);
        console.log(num_x);
        console.log("direct click to index remove");  
        }
    
      
    });
    return; 
}
/*this function sends position of x to server 
and updates the board and states with the return*/
function send_to_server_index_to_remove(jqevent){
    var field=$(jqevent.target);
    $.getJSON("/delete_x",
            JSON.stringify(field.index()),
            function(ret) {
            var val = ret["ret"];
            console.log(ret);
            val=JSON.parse(val)
            console.log(val);
            var board=val["board"]
            var valid=val["valid"]
            console.log(board);
            if (valid) {
                draw_board(board);
                num_x=2;
                $(".box").off(); //deletes all previous handlers ( avoids making extra action each  time)
                $(".box").click(send_to_server_index_new);
                console.log(num_x);
                console.log("direct click to index new");
                return;
            }

            })
    
}


/*gameplay*/
set_indices();
global: //used to store the number of x and o's and #games won
        var num_x=0;
        var num_o=0;
        var player_won=0;
        var CU_won=0;

$( document ).ready(function() {
  fix_size();
  console.log("direct click to index new"); //init bij adding 'X' on click
  $(".box").click(send_to_server_index_new);
});

$( window ).resize(fix_size);
