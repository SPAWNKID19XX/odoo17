from odoo import models, api, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char()
    author = fields.Char()
    pages = fields.Integer()
    short_name = fields.Char(
        compute='_compute_short_name',
        store=True,
    )
    rental_ids = fields.One2many(
        comodel_name='library.rental',
        inverse_name='book_id',
        string=None,
    )

    @api.depends('name')
    def _compute_short_name(self):
        print(self)
        if self.name:
            if len(self.name) > 10:
                self.short_name = self.name[:10]
            else:
                self.short_name = self.name

    def show_rentals_list(self):
        book_id = self.id
        # print('Smart button For book', book_id)
        book_rental_ids = self.env['library.rental'].search([('book_id', '=', book_id)])
        # print(book_rental_ids)
        # for rental_id in book_rental_ids:
        #     print(rental_id.id, rental_id.customer_name)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Rentals',
            'view_mode': 'tree,form',
            'res_model': 'library.rental',
            'domain': [('book_id', '=', book_id)],
            'context': {'default_book_id': book_id},
            'target': 'new',
        }
