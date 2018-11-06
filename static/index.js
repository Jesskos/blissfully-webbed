// rsvp 
function submitRSVP(evt) {
	evt.preventDefault();
	console.log(evt)
}


$(".saveForm").on("submit", submitRSVP)