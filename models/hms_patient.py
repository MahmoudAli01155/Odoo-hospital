from odoo import models, fields, api,_
from odoo.fields import Text

from datetime import date


class HmsPatient(models.Model):
    _name = "hms.patient"

    Fname=fields.Char(string="First name", required=True)
    Lname = fields.Char(string="Last name", required=True)
    Bdate= fields.Date(required=True)
    Address =fields.Text(required=True)
    CRRatio =fields.Float(required=True)
    History =fields.Html()
    Boold_type =fields.Selection([('ch1','1'),('ch2','2'),('ch3','3')], string=" Boold_type")
    Pcr =fields.Boolean(required=True ,defaulte=True)
    states = fields.Selection([('1', 'Undetermined'), ('2', 'Good'), ('3', 'Fair'), ('4', 'Serious')],
                              string="Student Level", required=True)
    age = fields.Integer(readonly=True, compute='compute_age', store=True)
    Image= fields.Binary("Image", attachment=True,help="This field holds the image")
    logs = fields.Many2many('hms.logs', string="Patients Logs")
    doctors = fields.Many2many('hms.doctors', string="doctors")
    department_id=fields.Many2one(comodel_name="hms.department")

    @api.depends('Bdate')
    def compute_age(self):
        for rec in self:
            if rec.Bdate:
                today = date.today()
                rec.age = today.year - rec.Bdate.year - (
                            (today.month, today.day) < (rec.Bdate.month, rec.Bdate.day))
            else:
                rec.age = 0







    @api.onchange('states')
    def log_creation(self):
        if self.states:
            vals = {
                'description': 'states Changed to %s ' % (self.states),
                'created_by': self.fName,
            }
            log = self.env['hms.logs'].create(vals)
            self.logs += log



