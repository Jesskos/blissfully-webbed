// rsvp 



function submitRSVP(evt) {
	// submits the RSVP form 
	console.log('in function')
	evt.preventDefault();
	let rsvpFormValues = $('form').serializeArray();
	let otherRsvps = $('#other-rsvps').find(":selected").text();
	let guestInfo = {
		"first": rsvpFormValues[0]["value"],
		"last": rsvpFormValues[1]["value"],
		"rsvp": rsvpFormValues[2]["value"],
		"phone": rsvpFormValues[3]["value"],
		"email": rsvpFormValues[4]["value"], 
		"others": otherRsvps
	};
	
	console.log(guestInfo)
	$.post('/rsvp_response', guestInfo, getConfirmation);

}

function getConfirmation(result) {
	alert('Done!')
}


$(document).ready(function() {
	$("#submit-rsvp").on("submit", submitRSVP)
});
	




