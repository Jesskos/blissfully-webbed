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
	let modalContent = document.getElementById('model-content');
	let newForm = '<form action="/rsvp_response" class="rsvp-form" method="post">
	First Name: <input type="text" name="fname" id="first-name" required> 
  	Last Name: <input type="text" name="lname" id="last-name" required>
    Attending? 
    <input type="radio" name="rsvp" value="yes"> Yes
    <input type="radio" name="rsvp" value="no"> No 
     Phone number? <input type="text" name="phone" placeholder="optional"> 
     What is your email address? <input type="text" name="email" placeholder="optional"> <br>
     </form>'
     modalContent.innerHTML = newForm
}
	
$("#rsvp-button").on("click", submitRSVP)
$(".close").on("click", closeModal)

