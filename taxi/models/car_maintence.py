from odoo import models, fields

class CarMaintence(models.Model):
    _name = 'car.maintence'
    _description = 'Car Maintence'

    car_id = fields.Many2one(
        'car.fleet',
        string="Car id",
    )

    date = fields.Date()

    description = fields.Char(string="Description")

    cost = fields.Float(string="Price")
