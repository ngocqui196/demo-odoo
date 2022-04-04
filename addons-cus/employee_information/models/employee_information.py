from odoo import models, fields, api


class EmployeeInformation(models.Model):
    _name = 'employee.information'
    _description = 'Nhân viên'

    full_name = fields.Char(string="Tên đầy đủ", required=True)
    birth = fields.Integer(string="Ngày sinh", required=1)
    gender = fields.Selection([('male', 'Male'), ('female', "Female")])
    address = fields.Text(string="Địa chỉ")
