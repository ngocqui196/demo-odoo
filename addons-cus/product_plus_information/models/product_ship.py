from odoo import api, fields, models, tools


class ProductShip(models.Model):
    _name = "pro.product.ship.information"
    _inherit = "pro.product.information"
    _description = "Hàng giao"

    address_ship = fields.Text(string="Địa chỉ giao hàng")