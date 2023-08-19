// Function to display the selected image
function showPreview(event) {
    const input = event.target;
    const preview = document.getElementById("photoPreview");

    if (input.files && input.files[0]) {
        const reader = new FileReader();

        reader.onload = function (e) {
            preview.src = e.target.result;
        };

        reader.readAsDataURL(input.files[0]);
    }
}

// Attach event listener to the input element
const photoInput = document.getElementById("photoInput");
photoInput.addEventListener("change", showPreview);

// Attach event listener to the image for triggering the input click
const photoPreview = document.getElementById("photoPreview");
photoPreview.addEventListener("click", function () {
    photoInput.click();
});
