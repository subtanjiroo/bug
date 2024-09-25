odoo.define('my_chatbox_module.chatbox_script', function (require) {
    'use strict';

    $(document).ready(function () {
        const chatInput = $('#chat_input');
        const sendButton = $('#send_button');
        const messages = $('#messages');

        // Send button click event
        sendButton.on('click', function () {
            const messageText = chatInput.val().trim();
            if (messageText !== "") {
                // Append message to the chat
                const messageDiv = $('<div>').text(messageText).addClass('message');
                messages.append(messageDiv);

                // Clear input
                chatInput.val('');
            }
        });

        // Handle Enter key press
        chatInput.on('keypress', function (e) {
            if (e.which === 13) { // Enter key
                sendButton.click();
            }
        });
    });
});
