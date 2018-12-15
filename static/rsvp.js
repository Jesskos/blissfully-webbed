// rsvp 



function submitRSVP(evt) {
	// submits the RSVP form 
	console.log('in function')
	evt.preventDefault();
	let rsvpFormValues = $('form').serializeArray();
	console.log(rsvpFormValues)
	let otherRsvps = $('#other-rsvps').find(":selected").text();
	let guestInfo = {
		"first": rsvpFormValues[0]["value"],
		"last": rsvpFormValues[1]["value"],
		"email": rsvpFormValues[2]["value"],
		"phone": rsvpFormValues[3]["value"],
		"rsvp": rsvpFormValues[4]["value"], 
		"update": rsvpFormValues[5]["value"],
		"others": otherRsvps
	};
	
	console.log(guestInfo)
	$.post('/rsvp_response', 
		guestInfo,
		getConfirmation);

}

function getConfirmation(result) {
	console.log(result)
	if (result["num_guests"] != "0") {
		document.getElementById("submit-rsvp").reset();
		$("#other-rsvps-space").remove()
		$("#self-or-guest").html("<h1>Please Enter Guest Information</h1>")
	} else { 
		$("#rsvp-space").remove() 
	};
	alert(result["message"])
}


$(document).ready(function() {
	$("#submit-rsvp").on("submit", submitRSVP)
});
	




