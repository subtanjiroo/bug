from odoo import fields, models, api
from odoo.tools.translate import _

class Property(models.Model):
    _name = 'estate.property'
    _inherit = ["mail.thread",'mail.activity.mixin']
    _description = 'Estate Property'

    price = fields.Integer(string='Price')
    state = fields.Selection([
        ('news','News'),
        ('accepted','Offer Accepted'),
        ('received','Offer Received'),
        ('sold','Sold'),
        ('cancel','cancel'),
        
        ],default="news",string="State", group_expand="_expand_state")
    name = fields.Char(string="Name")
    tag_id = fields.Many2many('estate.property.tag', string="Property Tag")
    type_id=fields.Many2one('estate.property.type', string="Property Type")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date = fields.Date(string="Date")
    adate = fields.Date(string="ADate")
    expected_price = fields.Float(string="Expected Price", tracking=True)
    bed_rooms = fields.Integer(string="Bedrooms")
    living_rooms = fields.Integer(string="Living Rooms")
    garden = fields.Boolean(string="Garden", default=False)
    aaa = fields.Char(string="aaa")
    garage_area = fields.Char(string="Garage Area")
    garage = fields.Boolean(string="Garage")
    ddd = fields.Char(string="ddd")
    phone = fields.Char(string='Phone',related='buyer_id.phone')
    garden_orientation = fields.Selection(
        [("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")],
        string="Garden Orientation", default="north"
    )
    offer_id = fields.One2many('estate.property.offer','property_id',string="Offers")
    sales_id = fields.Many2one ('res.users',string="Salesman")
    buyer_id = fields.Many2one('res.partner',string="Buyer", domain=[('is_company','=',True)])
    @api.onchange('living_rooms','garden')
    def _onchange_total_area_(self):
        self.total_area = self.living_rooms + self.garden
    total_area = fields.Integer(string='Total Area')

    def  action_sold(self):
        self.state = "sold"
    def  action_cancel(self):
        self.state = "cancel"
    @api.depends('offer_id')
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_id)
    offer_count = fields.Integer(string="Offer Count", compute=_compute_offer_count)
    def action_property_view_offer(self):
        return{
            'type':'ir.actions.act_window',
            'name': f"{self.name} - Offer",
            'domain':[('property_id','=',self.id)],
            'view_mode':'tree',
            'res_model':'estate.property.offer',
            
        }
    def _expand_state(self, state, domain, order):
        return [
            key for key, dummy in type(self).state.selection
        ]
    def action_send_email(self):
        mail_template = self.env.ref('real_estate.offer_mail_template')
        mail_template.send_email(self.id, force_send=True)
            
    def _get_report_base_filename(self):
        self.ensure_one()
        return "Estate Property - %s" % self.name
    

    # def _compute_website_url(self):
    #     for rec in self:
    #         rec.website_url="/properties/%s" % rec.id

class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = 'Estate Property Type'
    name = fields.Char(string="Name", required=True)

class PropertyTags(models.Model):
    _name = "estate.property.tag"
    _description = 'Estate Property Tag'
    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color")

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def unlink(self):
        # Thực hiện hành động xóa bản ghi
        res = super(EstateProperty, self).unlink()

        # Trả về hành động điều hướng về Kanban view sau khi xóa thành công
        return {
            'type': 'ir.actions.act_window',
            'name': 'Property Kanban View',
            'res_model': 'estate.property',
            'view_mode': 'kanban',
            'target': 'current',
        }


