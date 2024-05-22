// Function to remove messages after a certain period of time
function removeMessages() {
    const messages = document.querySelectorAll('.message');
    messages.forEach(function(message) {
        setTimeout(function() {
            message.remove();
        }, 5000); // Adjust the duration (in milliseconds) as needed, e.g., 5000 milliseconds = 5 seconds
    });
}

// Call the function to remove messages when the document is ready
document.addEventListener('DOMContentLoaded', function() {
    removeMessages();
});