from odoo import api, fields, models
from odoo.exceptions import UserError


class Product(models.Model):
    _name = "pro.product.information"
    _description = "My product"

    name = fields.Char('Product Name', required=True)
    description = fields.Text('Product Description')
    amount = fields.Integer('Product Amount', default=1)
    price = fields.Float(compute="_compute_price", string="Price Product (VND)")
    made_in = fields.Char(string='Made In (Country)')
    tax = fields.Float(string="Thuế", default=1)
    import_price = fields.Float(string="Giá nhập")
    company_id = fields.Many2one('company.information', string='Công ty')
    subject_list = fields.Many2many("subject.information", "relation_subject_product", "product_id", "subject_id",
                                    string="bảng quan hệ sản phầm và người dùng")

    address = fields.Text(related="company_id.address", string="Địa chỉ công ty")

    @api.depends("import_price", "made_in", "tax")
    def _compute_price(self):
        for pro in self:
            if pro.made_in != "Việt Nam":
                pro.price = pro.import_price + (pro.import_price * pro.tax / 100)
            else:
                pro.price = pro.import_price

    def write(self, values):
        if not self.subject_list:
            raise UserError("Bạn cần chọn người sử dụng")


class SubjectInformation(models.Model):
    _name = "subject.information"
    _description = "Subject Information"

    user_name = fields.Char(string='Tên người dùng')
    birth = fields.Date(string="Ngày sinh")
