from datetime import datetime
from odoo import models, api, fields


class CarDriver(models.Model):
    _name = 'car.driver'
    _description = 'Car Driver'

    name = fields.Char('Driver Name', required=True)
    phone_number = fields.Char('Phone Number', required=True)
    license_number = fields.Char(string="License Number", required=True)
    trip_ids = fields.One2many(
        comodel_name="car.trip",
        inverse_name="driver_id",
        string="Trips"
    )

    def show_trips_list(self):
        driver_id = self.id
        driver_trip_ids = self.env['car.trip'].search([('driver_id', '=', driver_id)])
        print(driver_trip_ids)
        for trip in driver_trip_ids:
            print(trip.id, trip.car_id, trip.distance_km, trip.duration_hours)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Trips',
            'view_mode': 'tree,form',
            'res_model': 'car.trip',
            'domain': [('driver_id', '=', driver_id)],
            'context': {'default_driver_id': driver_id},
            'target': 'new',
        }
