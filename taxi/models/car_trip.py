from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CarTrip(models.Model):
    _name = 'car.trip'
    _description = 'Car Trip'
    _rec_name = 'car_id'

    car_id = fields.Many2one('car.fleet', 'Car', required=True)
    driver_id = fields.Many2one('car.driver', 'driver', required=True)
    start_time = fields.Datetime('Start Time', required=True)
    end_time = fields.Datetime('End Time', required=True)
    distance_km = fields.Float('Distance (km)', required=True)
    duration_hours = fields.Float(
        'Duration (hours)',
        compute='_compute_duration_hours'
    )

    @api.depends('start_time', 'end_time')
    def _compute_duration_hours(self):
        for trip in self:
            if trip.start_time and trip.end_time:
                trip.duration_hours = (trip.end_time - trip.start_time).total_seconds() / 3600
            else:
                trip.duration_hours = 0.0


    @api.constrains('start_time', 'end_time')
    def _validate_duration_hours(self):
        for trip in self:
            if (trip.start_time and trip.end_time) and (trip.duration_hours < 0.0):
                raise ValidationError(
                    'Duration hours cannot be negative.'
                )

