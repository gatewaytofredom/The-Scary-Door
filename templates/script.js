$(document).ready(function() {

	setInterval(function() {
		$.getJSON("/readpin/", function(data) {
			if (data["response"] != "not pressed") {
				$("#main").html(data["response"])
				//$("#main").css("color", data["color"])
			}
		})
	}, 500);

});
