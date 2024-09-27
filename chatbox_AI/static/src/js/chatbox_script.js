/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, xml } from "@odoo/owl";

class CustomField extends Component {
    static template = xml`
        <div id="chatbox">
            <div id="messages">
                <!-- Các tin nhắn sẽ được thêm vào đây -->
            </div>
            <textarea t-on-keydown="handleKeyDown" id="message_input" placeholder="Type your message..." t-ref="messageInput"></textarea>
            <button name="send-message" type="button" id="send_button" t-on-click="sendMessage">Send</button>
        </div>
    `;

    setup() {
        this.messages = []; // Khởi tạo biến messages
    }
    handleKeyDown(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault(); // Ngăn chặn hành động mặc định (xuống dòng)
            this.sendMessage(); // Gọi hàm gửi tin nhắn
        }
    }

    async sendMessage() {
        // Lấy phần tử textarea bằng getElementById
        const messageInput = document.getElementById('message_input');
        const message = messageInput.value; // Lấy giá trị từ textarea
        if (message) {
            try {
                const response = await this.env.services.rpc('/chat/send', { message: message });
                
                // Tạo thẻ div cho client_message
                const client_message = document.createElement('div');
                client_message.className = 'client_message'; // Thiết lập class cho thẻ div
                client_message.textContent = message; // Thêm nội dung vào thẻ div
                
                // Sử dụng getElementById để lấy thẻ messages và thêm server_message vào
                const messagesContainer = document.getElementById('messages');
                messagesContainer.appendChild(client_message); // Thêm thẻ div vào messagesContainer


                // Tạo thẻ div mới cho response.status và thêm vào messages
                const server_message = document.createElement('div');
                server_message.className = 'server_message'; // Thiết lập class cho thẻ div
                server_message.textContent = response.status; // Thêm nội dung vào thẻ div

                // Thêm server_message vào
                messagesContainer.appendChild(server_message); // Thêm thẻ div vào messagesContainer
                
                
                // Cuộn xuống để hiển thị tin nhắn mới
                messagesContainer.scrollTo(0, messagesContainer.scrollHeight);

                messageInput.value = ''; // Xóa nội dung textarea
            } catch (error) {
                console.error("Error sending message:", error);
            }
        }
    }
}

// Đăng ký component này vào registry của Odoo với một field tùy chỉnh
registry.category("fields").add("custom_char", {
    component: CustomField,
    supportedTypes: ["char"],  // Định nghĩa loại field được hỗ trợ
});
