from datetime import datetime

from dateutil.utils import today
from odoo import models, api, fields

class CarFleet(models.Model):
    _name = 'car.fleet'
    _description = 'Car Fleet'

    name = fields.Char(string='Fleet Name', required=True)
    license_plate = fields.Char()
    made_year = fields.Integer()
    driver_id = fields.Many2one('car.driver', string='Driver', required=True)
    feature_ids = fields.Many2many(
        comodel_name='car.feature',
        string='Features',
    )
    car_age = fields.Integer(
        string='Car Age',
        compute='car_age',
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



    #todo smart button show_trips