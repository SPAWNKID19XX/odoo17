from odoo import models, fields, api


class PatientTag(models.Model):
    _name = 'hospital.patient.tag'
    _inherit = ['mail.thread']
    _description = 'Hospital patient tag'

    name = fields.Char(
        string='Name',
        required=True,
        tracking=True
    )


