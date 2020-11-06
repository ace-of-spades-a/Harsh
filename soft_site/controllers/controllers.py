# -*- coding: utf-8 -*-
from odoo import http

# class SoftSite(http.Controller):
#     @http.route('/soft_site/soft_site/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/soft_site/soft_site/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('soft_site.listing', {
#             'root': '/soft_site/soft_site',
#             'objects': http.request.env['soft_site.soft_site'].search([]),
#         })

#     @http.route('/soft_site/soft_site/objects/<model("soft_site.soft_site"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('soft_site.object', {
#             'object': obj
#         })