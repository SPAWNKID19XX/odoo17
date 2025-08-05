from odoo import models, fields, api

class LibraryRental(models.Model):
    _name = 'library.rental'
    _description = 'Library Rental'
    _rec_name = 'book_id'

    book_id = fields.Many2one('library.book', string='Book' )
    customer_name = fields.Char()
    rental_date = fields.Date()
    # rental_price = fields.Float()
    return_date = fields.Date()