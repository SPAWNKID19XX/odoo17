from odoo import models, fields, api

class CarMaintenance(models.Model):
    _name = 'car.maintenance'
    _description = 'Car Maintenance'
    _rec_name = 'car_id_name'

    car_id = fields.Many2one(
        'car.fleet',
        string="Car id",
        required=True,
    )

    date = fields.Date(
        required=True,
    )

    description = fields.Char(string="Description")

    cost = fields.Float(
        required=True,
        tring="Price"
    )

    car_id_name = fields.Char(
        string="Car id name",
        compute='_compute_car_id_name',
        readonly=True,
        store=True,
    )

    @api.depends('car_id')
    def _compute_car_id_name(self):
        for record in self:
            if record.car_id:
                record.car_id_name = record.car_id.name  # или license_plate, если нужно
            else:
                record.car_id_name = False


