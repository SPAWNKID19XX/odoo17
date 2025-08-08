from datetime import datetime
from odoo.exceptions import ValidationError
from odoo import models, api, fields


class CarFleet(models.Model):
    _name = 'car.fleet'
    _description = 'Car Fleet'
    _rec_name = 'license_plate'

    _sql_constraints = [
        (
            'license_plate',
            'UNIQUE(license_plate)',
            'Licence_plate is unique value'
        )
    ]

    name = fields.Char(string='Fleet Name', required=True)
    license_plate = fields.Char()
    made_year = fields.Integer()
    driver_id = fields.Many2one('car.driver', string='Driver')
    feature_ids = fields.Many2many(
        comodel_name='car.feature',
        string='Features',
    )

    car_age = fields.Integer(
        string='Car Age',
        compute='_compute_car_age',
        store=True,
    )

    trip_ids = fields.One2many(
        comodel_name="car.trip",
        inverse_name="car_id",
        string="Trips"
    )

    @api.depends('made_year')
    def _compute_car_age(self):
        this_year = datetime.today().year
        for record in self:
            if record.made_year and record.made_year < this_year:
                record.car_age = this_year - record.made_year
            else:
                record.car_age = 0

    @api.constrains('made_year')
    def _validate_made_year(self):
        current_year = datetime.today().year
        for record in self:
            if record.made_year and record.made_year > current_year:
                raise ValidationError("Year Made cannot be in the future.")

    def show_trips_list(self):
        car_id = self.id
        # print('Smart button For book', book_id)
        car_trip_ids = self.env['car.trip'].search([('car_id', '=', car_id)])
        # print(car_trip_ids)
        # for trip in car_trip_ids:
        #     print(trip.id, trip.car_id, trip.distance_km, trip.duration_hours )
        return {
            'type': 'ir.actions.act_window',
            'name': 'Trips',
            'view_mode': 'tree,form',
            'res_model': 'car.trip',
            'domain': [('car_id', '=', car_id)],
            'context': {'default_book_id': car_id},
            'target': 'new',
        }
