// rsvp 

function rsvpRequestReceived(result) {
	alert(result)
}

function submitRSVP(evt) {
	evt.preventDefault();
	console.log(evt)
	let otherRsvps = $('#other-rsvps').find(":selected").text();
	formValues = $('form').serializeArray()
	let guestInfo = {
		"first": formValues[0]["value"],
		"last": formValues[1]["value"],
		"rsvp": formValues[2]["value"],
		"phone": formValues[3]["value"],
		"email": formValues[4]["value"], 
		"others": otherRsvps
	}


	console.log(guestInfo)

	$.post("/rsvp_response",
		guestInfo, 
		rsvpRequestReceived);
}

	

$(".rsvp-form").on("submit", submitRSVP)