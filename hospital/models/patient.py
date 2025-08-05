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

    tag_ids = fields.Many2many(
        comodel_name='hospital.patient.tag',
        relation = 'hospital_patient_hospital_patient_tag_rel',
        column1='hospital_patient_id',
        column2='hospital_patient_tag_id',
        string="Tags",
    )

    product_ids = fields.Many2many(
        comodel_name='product.product',
        string='Products',
    )

    appointments_ids = fields.One2many(
        comodel_name='hospital.appointments',
        inverse_name='user_id',
        string=None,
    )