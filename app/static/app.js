console.log("Hola a todos, soy Javascript");

function edit() {
	const spanText = document.querySelector("#taskText");
	const taskText = spanText.innerText;

	const inputText = `<input type="text" id="inputText" class="form-control d-inline" placeholder="${taskText}" value="${taskText}">`;
	const btnSave = `<a href="javascript: save();" class="btn btn-primary">guardar</a>`;
	spanText.innerHTML += inputText + btnSave;

	console.log("editando...");
}

function save() {
	const id = document.querySelector("#taskId").innerText;
	const text = document.querySelector("#inputText").value;

	const formData = new FormData();
	formData.append("text", text);
	// XHR : PUT
	fetch("/update/" + id, {
		method: "PUT",
		body: formData,
	})
		.then((response) => response.json())
		.then((data) => console.log(data));
}
