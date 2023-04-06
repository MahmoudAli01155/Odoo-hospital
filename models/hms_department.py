from odoo import models ,fields

class HmsDepartment(models.Model):
    _name = "hms.department"

    name = fields.Char(string="Department name", required=True)
    Capacity =fields.Integer(required=True)
    Is_opened = fields.Boolean(required=True, defaulte=True)
    Patients_ids = fields.One2many(comodel_name="hms.patient", inverse_name="department_id")

