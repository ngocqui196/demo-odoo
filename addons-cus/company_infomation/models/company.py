from odoo import fields, models


class Product(models.Model):
    _name = "company.information"
    _description = "Company"

    name = fields.Char(string="Tên công ty", required=True)
    president = fields.Char(string="Giám đốc", required=True)
    address = fields.Text(string="Địa chỉ", required=True)
