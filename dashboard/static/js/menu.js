document.getElementById('change-image-btn').addEventListener('click', function() {
    document.getElementById('menuImage').click();
});

document.getElementById('menuImage').addEventListener('change', function(event) {
    var file = event.target.files[0];
    if (file) {
        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('menu-image-preview').src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});