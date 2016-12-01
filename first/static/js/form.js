


function create_tour() {
    console.log("create post is working!") // sanity check
    $.ajax({
        url : "/handle_ajax_tour/", // the endpoint
        dataType : "json", 
        type : "POST", // http method
        data : { platform : $('#id_platform').val(),
        name : $('#id_name').val(),
        first_place_rew : $('#id_first_place_rew').val(),
        second_place_rew : $('#id_second_place_rew').val(),
        third_place_rew : $('#id_third_place_rew').val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        my_id:  $('#tour_id').val(),
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
        	if (json=="Турнир успешно создан")
        	{

        		

        	$('#id_platform').val(''),
        $('#id_name').val('')
        $('#id_first_place_rew').val('')
         $('#id_second_place_rew').val('')
        $('#id_third_place_rew').val('')
        } // remove the value from the input
        $("div.scr").html(json);
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$('#sid').on('click', function(event){

    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_tour();
});
