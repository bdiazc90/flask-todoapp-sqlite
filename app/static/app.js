console.log("Hola a todos, soy Javascript");

const taskId = document.querySelector("#taskId").innerText;
const taskSection = document.querySelector("#task_section");
const editButton = taskSection.querySelector("a.btn");

function edit() {
	const spanText = document.querySelector("#taskText");
	const taskText = spanText.innerText;

	const inputText = `<input type="text" id="inputText" class="form-control d-inline" placeholder="${taskText}" value="${taskText}">`;
	const btnSave = `<a href="javascript: save();" class="btn btn-primary">guardar</a>`;
	taskSection.innerHTML = inputText + btnSave;
}

function save() {
	const text = document.querySelector("#inputText").value;

	const formData = new FormData();
	formData.append("text", text);
	// XHR : PUT
	fetch("/update/" + taskId, {
		method: "PUT",
		body: formData,
	})
		.then((response) => response.json())
		.then(
			(data) =>
				(taskSection.innerHTML = `
		<h1 class="display-4 mt-3">
		<span id="taskId">${data.id}</span>:
		<span id="taskText">${data.text}</span>
	</h1>
	<a class="btn btn-secondary" href="javascript: edit(this);">editar</a>`)
		);
}
