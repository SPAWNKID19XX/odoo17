from datetime import datetime
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


    def _compute_car_age(self):
        today = datetime.today().year
        self.car_age = today - self.made_year


    #todo smart button show_trips