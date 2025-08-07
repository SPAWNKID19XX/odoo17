from odoo import models, fields, api


class CarTrip(models.Model):
    _name = 'car.trip'
    _description = 'Car Trip'

    car_id = fields.Many2one('car.fleet', 'Car', required=True)

    driver_id = fields.Many2one('car.driver', 'driver', required=True)

    start_time = fields.Datetime('Start Time', required=True)

    end_time = fields.Datetime('Start Time', required=True)

    distance_km = fields.Float('Distance (km)', required=True)

    duration_hours = fields.Float(
        'Duration (hours)',
        compute='_compute_duration_hours'
    )

    def _compute_duration_hours(self):
        self.duration_hours = (self.end_time - self.start_time)*3600
