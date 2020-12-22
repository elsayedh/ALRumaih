# -*- coding: utf-8 -*-
# from odoo import http


# class HrContractUpdation(http.Controller):
#     @http.route('/hr_contract_updation/hr_contract_updation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_contract_updation/hr_contract_updation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_contract_updation.listing', {
#             'root': '/hr_contract_updation/hr_contract_updation',
#             'objects': http.request.env['hr_contract_updation.hr_contract_updation'].search([]),
#         })

#     @http.route('/hr_contract_updation/hr_contract_updation/objects/<model("hr_contract_updation.hr_contract_updation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_contract_updation.object', {
#             'object': obj
#         })
