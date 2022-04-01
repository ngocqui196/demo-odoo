from odoo import models, fields


class ProductPlus(models.Model):
    _name = "pro.product.information"
    _inherit = "pro.product.information"
    _description = "My product Plus"

    code_pro = fields.Char(string="Mã sản phẩm")

