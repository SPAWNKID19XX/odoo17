# -*- coding: utf-8 -*-
# from odoo import http


# class Taxi(http.Controller):
#     @http.route('/taxi/taxi', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/taxi/taxi/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('taxi.listing', {
#             'root': '/taxi/taxi',
#             'objects': http.request.env['taxi.taxi'].search([]),
#         })

#     @http.route('/taxi/taxi/objects/<model("taxi.taxi"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('taxi.object', {
#             'object': obj
#         })

