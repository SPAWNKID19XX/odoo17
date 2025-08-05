from odoo import models, fields, api


class LibraryRental(models.Model):
    _name = 'library.rental'
    _description = 'Library Rental'
    _rec_name = 'book_id'

    book_id = fields.Many2one('library.book', string='Book', ondelete="cascade")
    customer_name = fields.Char(required=True)
    rental_date = fields.Date(required=True)
    # rental_price = fields.Float()
    return_date = fields.Date(required=True)


