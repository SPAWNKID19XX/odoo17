from odoo import models, api, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char()
    author = fields.Char()
    pages = fields.Integer()

    rental_ids = fields.One2many(
        comodel_name='library.rental',
        inverse_name='book_id',
        string=None,
    )