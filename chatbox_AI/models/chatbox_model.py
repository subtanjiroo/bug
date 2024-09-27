from odoo import models, fields, api
from odoo.tools.translate import _
from odoo import http
from odoo.http import request
class Chatbox(models.Model):
    _name = 'chatbox.ai'
    _description = 'Chat Message'
    name = fields.Char(string='Name')
    message = fields.Text(string='Message')

class ChatboxController(http.Controller):

    @http.route('/chat/send', type='json', auth='user')
    def send_message(self, message):
        # Xử lý message ở đây
        print("Received message:", message)  # In ra message nhận được
        return {'status': 'thành công'}  # Trả về chuỗi 'thành công'
