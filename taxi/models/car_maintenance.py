from odoo import models, fields

class CarMaintenance(models.Model):
    _name = 'car.maintenance'
    _description = 'Car Maintenance'

    car_id = fields.Many2one(
        'car.fleet',
        string="Car id",
    )

    date = fields.Date()

    description = fields.Char(string="Description")

    cost = fields.Float(string="Price")
