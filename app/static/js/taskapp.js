const taskText = document.querySelector("h1.display-4");
const btnEdit = document.querySelector("#btnEdit");

btnEdit.addEventListener("click", function () {
	console.log(taskText.innerHTML);
	const btnUpdate = document.querySelector("#btnUpdate");

	const newtask = "brunodiaz";

	const formData = new FormData();
	formData.append("text", newtask);
	fetch("/update/8", {
		method: "PUT",
		body: formData,
	})
		.then((response) => response.json())
		.then((data) => (taskText.innerHTML = data.text));
});
