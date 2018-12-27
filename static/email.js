function getUpdate(results) {
	alert(results["message"])
}

function submitEmail(evt) {
	debugger;
	evt.preventDefault()
	let email = {"email": $('#email-text').val()}
	console.log(email)

	$.post("/submit_email", email, getUpdate)
}


$(document).ready(function() {
	$("#submitEmail").on("submit", submitEmail)
});
	
