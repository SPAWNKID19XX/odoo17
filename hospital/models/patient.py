from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread']
    _description = 'Hospital patient data'





    name = fields.Char(
        string="Name",
        required=True,
        tracking=True
    )

    birthday = fields.Datetime(
        string="Birthday",
    )

    gender = fields.Selection(
        string="Gender",
        selection=[
            ('male', 'Male'),
            ('female', 'Female'),
        ]
    )