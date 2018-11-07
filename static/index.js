// rsvp 
function submitRSVP(evt) {
	evt.preventDefault();
	console.log(evt)


	formValues = $('form').serializeArray()
	let guestInfo = {
		"first": formValues[0]["value"],
		"last": formValues[1]["value"],
		"rsvp": formValues[2]["value"],
		"phone": formValues[3]["value"],
		"email": formValues[4]["value"]
	}

	let otherRsvps = $('#other-rsvps').find(":selected").text();

	console.log(otherRsvps);
	console.log(guestInfo)
}


$(".rsvp-form").on("submit", submitRSVP)