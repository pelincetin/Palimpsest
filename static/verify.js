var verified = function(actual_id, status, message){
    var data = {"Id": actual_id, "Status": status, "Message": message}
    $.ajax({
        type: "POST",
        url: "verified",
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
		var str = this.id
		var actual_id = str.slice(0, 1);
		var status = str.slice(1,2)
		console.log(actual_id)
		console.log(status)
		var message = $('#mes').val()
		verified(actual_id, status, message)
	});


});