from odoo import fields, models, api

class HospitalAppointmentLine(models.Model):
    _name = 'hospital.appointment.line'
    _description = 'Hospital Appointment Line'
    _rec_name = 'appointment_id'

    appointment_id = fields.Many2one('hospital.appointments', string='Patient')
    product_id = fields.Many2one('product.product', string='Product')
    qty = fields.Float(string='Quantity')

