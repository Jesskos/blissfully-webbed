
// // rsvp 

function submitRSVP(evt) {
	// submits the RSVP form 
	console.log('in function')

	//prevents default action of the form
	evt.preventDefault();
	let rsvpFormValues = $('form').serializeArray();

	// prints form values
	console.log(rsvpFormValues)

	//gets number other RSVPs from guest
	let otherRsvps = $('#other-rsvps').find(":selected").text();

	// makes a hash of all gue
	let guestInfo = {
		"first": rsvpFormValues[0]["value"],
		"last": rsvpFormValues[1]["value"],
		"email": rsvpFormValues[2]["value"],
		"phone": rsvpFormValues[3]["value"],
		"update": rsvpFormValues[4]["value"], 
		"e-update": rsvpFormValues[5]["value"],
		"rsvp": rsvpFormValues[6]["value"],
		"others": otherRsvps
	};
	
	console.log(guestInfo)
	$.post('/rsvp_response', 
		guestInfo,
		getConfirmation);

}

function getConfirmation(result) {
	console.log(result)
	alert(result["message"])
}


// function getGuestConfirmation(result) {
// 	console.log(result)
// 	if (result["num_guests"] != "0") {
// 		document.getElementById("submit-rsvp").reset();
// 		$("#self-or-guest").html("<h1>Please Enter Guest Information</h1>")
// 	} else { 
// 		$("#rsvp-space").remove() 
// 	};
// 	alert(result["message"])
// }

// function submitGuestRSVP(evt) {
// 	// submits the RSVP form 

// 	console.log('in other function')
// 	evt.preventDefault();
// 	let rsvpFormValues = $('form').serializeArray();
// 	let guestInfo = {
// 		"first": rsvpFormValues[0]["value"],
// 		"last": rsvpFormValues[1]["value"],
// 		"email": rsvpFormValues[2]["value"],
// 		"phone": rsvpFormValues[3]["value"],
// 		"rsvp": rsvpFormValues[4]["value"], 
// 		"update": rsvpFormValues[5]["value"],
// 	};
	
// 	console.log(guestInfo)
// 	$.post('/rsvp_response', 
// 		guestInfo,
// 		getGuestConfirmation);

// }


$(document).ready(function() {
	$("#submit-rsvp").on("submit", submitRSVP)
});
	




