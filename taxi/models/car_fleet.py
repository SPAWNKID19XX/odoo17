from datetime import datetime
from odoo.exceptions import ValidationError
from odoo import models, api, fields

class CarFleet(models.Model):
    _name = 'car.fleet'
    _description = 'Car Fleet'
    _rec_name = 'license_plate'

    _sql_constraints = [
        (
            'license_plate',
            'UNIQUE(license_plate)',
            'Licence_plate is unique value'
        )
    ]

    name = fields.Char(string='Fleet Name', required=True)
    license_plate = fields.Char()
    made_year = fields.Integer()
    driver_id = fields.Many2one('car.driver', string='Driver')
    feature_ids = fields.Many2many(
        comodel_name='car.feature',
        string='Features',
    )
    car_age = fields.Integer(
        string='Car Age',
        compute='_compute_car_age',
        store=True,
    )

    @api.depends('made_year')
    def _compute_car_age(self):
        this_year = datetime.today().year
        for record in self:
            if record.made_year and record.made_year < this_year:
                record.car_age = this_year - record.made_year
            else:
                record.car_age = 0

    @api.constrains('made_year')
    def _validate_made_year(self):
        current_year = datetime.today().year
        for record in self:
            if record.made_year and record.made_year > current_year:
                raise ValidationError("Year Made cannot be in the future.")



    #TODO smart button show_trips