from odoo import models, fields, api

class CarFeature(models.Model):
    _name = 'car.feature'
    _description = 'Car Feature'

    name = fields.Char(string="Feature Name")