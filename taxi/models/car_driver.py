from datetime import datetime
from odoo import models, api, fields

class CarDriver(models.Model):
    _name = 'car.driver'
    _description = 'Car Driver'

    name = fields.Char('Driver Name', required=True)
    phone_number = fields.Char('Phone Number', required=True)
    license_number = fields.Char(string="License Number", required=True)
    car_ids = fields.One2many('car.fleet', 'driver_id', string="Drivers")

    #TODO smart button Driver's trips