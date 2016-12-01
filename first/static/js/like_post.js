function get_count() {
    // sanity check
   
    $.ajax({
        url : "/", // the endpoint
        dataType : "json", 
         // http method
         // data sent with the post request

        // handle a successful response
        success : function(json) {
             // remove the value from the input
          
             //
        for (i in json)
        {

            $("#count-" +json[i][0]).html(json[i][1]) ;
        } 
        console.log(json[2][0]);
        console.log("#count-" +json[2][0]);
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            alert('error');
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};


function get_like(post) {
    // sanity check
   
    $.ajax({
        url : "/handle_ajax_like/", // the endpoint
        dataType : "json", 
        type : "POST", // http method
        data : { post_id : post,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
        	 // remove the value from the input
             // 
        get_color();

        console.log(json);
        console.log("success");
        /*if (json=="create")
        {
            $("#like-" +post).attr("bgcolor", "green") 
        }
         if (json=="delete")
        {
            $("#like-" +post).attr("bgcolor", "white") 
        }
            console.log(json); // log the returned json to the console

            console.log("success"); // another sanity check*/
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            alert('error');
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
function get_color(){
$.ajax({

      url: /handle_ajax_like/ ,
      dataType : "json",
      type : "GET" ,
      success: function(data) {
        var my_out="<h3 align='center'>Турниры</h3><br><table cellspacing='10' width='30%'><tr><th>Id</th><th>Название</th><th>Платформа</th>"



        $("td.cl").attr("bgcolor", "white"); 
        for ( i in data)
        {
           
           $("#like-" +data[i]).attr("bgcolor", "green") ;
            
        }
       
        
      }

    });

};
get_color();
get_count();

           var centrifuge = new Centrifuge({
                url: 'http://localhost:7000/connection',
                insecure: true
            });
            centrifuge.subscribe('like-updates', function (message) {
                get_count();
                get_color();
            });
            centrifuge.connect();