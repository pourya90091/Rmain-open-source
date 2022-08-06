const inputs = document.querySelector("div.inputs");
if (inputs) {
    inputs.addEventListener("keypress", function (key_data) {
        if (key_data.key === "Enter") {
            document.querySelector("button.btn").click();
        }
    });
}
