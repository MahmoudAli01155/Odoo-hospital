from odoo import models ,fields

class HmsDoctors(models.Model):
    _name = "hms.doctors"

    Fname = fields.Char(string="Doctors name", required=True)
    Lname = fields.Char(string="Doctors name", required=True)
    Image = fields.Binary("Image", attachment=True, help="This field holds the image")
    department_ids = fields.Many2many(comodel_name="hms.department")