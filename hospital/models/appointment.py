from odoo import models, api, fields

class HospitalAppointments(models.Model):
    _name = 'hospital.appointments'
    _inherit = ['mail.thread']
    _description = 'Hospital patient appointments'
    _rec_name = 'user_id'

    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('ongoing', 'Ongoing'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
        ],
        default='draft',
        tracking=True
    )

    ref=fields.Char(string='Reference', readonly=True, default='New')

    user_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True,
    )

    date_appointments = fields.Date()

    notes = fields.Text(
        string='Notes',
    )


    @api.model_create_multi
    def create(self, vals):
        """Create a new record with the given values."""
        for val in vals:
            if not ('ref' in val) or 'ref' == 'New':
                val['ref'] = self.env['ir.sequence'].next_by_code('hospital.appointments')
        return super().create(vals)


    def statusbar_set_confirmed(self):
        self.state = 'confirmed'


    def statusbar_set_ongoing(self):
        self.state = 'ongoing'


    def statusbar_set_done(self):
        self.state = 'done'


    def statusbar_set_cancelled(self):
        self.state = 'cancelled'