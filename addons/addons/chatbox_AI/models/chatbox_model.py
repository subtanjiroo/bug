from odoo import models, fields, api

class Chatbox(models.Model):
    _name = 'chatbox.ai'
    _description = 'Chatbox AI'

    name = fields.Char(string="Name")
    text = fields.Char(string="context")

