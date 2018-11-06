// rsvp 
function submitRSVP(evt) {
	evt.preventDefault();
	console.log(evt)
}


$(".rsvp-form").on("submit", submitRSVP)