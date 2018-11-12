// rsvp 

function rsvpRequestReceived(result) {
	alert(result)
}

function submitRSVP(evt) {
	evt.preventDefault();
	console.log(evt)
	let formValues = $('form').serializeArray()
	let otherRsvps = $('#other-rsvps').find(":selected").text();
	let guestInfo = {
		"first": formValues[0]["value"],
		"last": formValues[1]["value"],
		"rsvp": formValues[2]["value"],
		"phone": formValues[3]["value"],
		"email": formValues[4]["value"], 
		"others": otherRsvps
	}
	let modal = document.getElementById('rsvp-modal')


	console.log(guestInfo['others'])
	if (otherRsvps != "0") {
		generateRsvp(otherRsvps)
		modal.style.display="block"
	} else { $.post("/rsvp_response",
		     guestInfo, 
		     rsvpRequestReceived);
	}

}

function closeModal(evt) {
	console.log("clicked x")
	let modal = document.getElementById('rsvp-modal');
	modal.style.display="none";
}

function generateRsvp(otherRsvps) {
	let formContent = document.getElementById('form-content');
	console.log(formContent)

}
	
$("#rsvp-button").on("click", submitRSVP)
$(".close").on("click", closeModal)

