var delete_picture = function(temp_id){
    var data = {"Id": temp_id}
    $.ajax({
        type: "POST",
        url: "delete_picture",
        dataTpe: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data),
        success: function(result){
            location.reload();
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
};

$(document).ready(function(){
	$("button").click(function() {
		console.log(this.id)
		delete_picture(this.id); // or alert($(this).attr('id'));
	});
});