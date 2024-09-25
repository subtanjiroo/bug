from odoo import fields, models, api
from odoo.exceptions import ValidationError
from odoo.tools.translate import _
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = 'Estate Property Offer'
    
    @api.depends('property_id','partner_id')
    def _compute_name(self):
        for rec in self:
            if rec.property_id and rec.partner_id:
                rec.name = f"{rec.property_id.name} - {rec.partner_id.name} "
            else:
                rec.name = False
    name = fields.Char(string="Description", compute=_compute_name)
    price = fields.Float(string="Price")
    status = fields.Selection(
        [("accepted", "Accepted"), ("refuse", "Refuse")],
        string="Status"
    )
    partner_id = fields.Many2one('res.partner',string="Customer")
    property_id = fields.Many2one('estate.property',string="Property")
    validity = fields.Integer(string="Validity", default=7)
    deadline = fields.Date(string="Deadline", compute='_compute_deadline', inverse="_inverse_deadline")
    
    _sql_constraints = [
        ('check_validity', 'check(validity > 0)','XXXXXXXXXXXXXXXXXXXXXX')
    ]
    @api.model
    def _set_date(self):
        return fields.Date.today()
    
    create_date = fields.Date(string="Create Date", default=_set_date)

    @api.depends('validity','create_date')
    def _compute_deadline(self):
        for rec in self:
            if rec.create_date and rec.validity:
                rec.deadline = rec.create_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False
    def _inverse_deadline(self):
        for rec in self:
            if rec.deadline and rec.create_date:
                rec.validity = (rec.deadline - rec.create_date).days
            else:
                rec.validity = False

    # @api.autovacuum
    # def _clean_offers(self):
    #     self.search([("status","=","refused")]).unlink()



    # Tạo Bản Ghi Mới
    # @api.model_create_multi
    # def create(self,vals):
    #     for rec in vals:
    #         if not rec.get('create_date'):
    #             rec['create_date'] = fields.Date.today()
    #     return super(PropertyOffer,self).create(vals)


    @api.constrains('validity')
    def _check_val(self):
            for rec in self:
                if rec.deadline <= rec.create_date:
                    raise ValidationError(_('deadline cant be before create date'))
    
    def action_accept_offer(self):
        self.status = 'accepted'     
    def action_decline_offer(self):
        self.status = 'refuse'

# sever acctions !!!
    def extend_offer_deadline(self):
        activ_ids= self._context.get('active_ids',[])
        if activ_ids:
            offer_ids = self.env['estate.property.offer'].browse(activ_ids)
            for offer in offer_ids:
                offer.validity = 10

# cron(automatic) actions
    def _extend_offer_deadline(self):
        offer_ids = self.env['estate.property.offer'].search([])
        for offer in offer_ids:
            offer.validity = offer.validity + 1