# -*- coding: utf-8 -*-
# from odoo import http


# class HrManagementSystem(http.Controller):
#     @http.route('/hr_management_system/hr_management_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_management_system/hr_management_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_management_system.listing', {
#             'root': '/hr_management_system/hr_management_system',
#             'objects': http.request.env['hr_management_system.hr_management_system'].search([]),
#         })

#     @http.route('/hr_management_system/hr_management_system/objects/<model("hr_management_system.hr_management_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_management_system.object', {
#             'object': obj
#         })
