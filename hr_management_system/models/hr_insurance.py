# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class HRInsurance(models.Model):
    _name = 'hr.insurance'
    _description = 'Employees insurances'
    _inherit = ['mail.thread','mail.activity.mixin']

    # dt = Department
    # emp = Employee

    emp_ref = fields.Many2one('hr.employee', related='emp_id', invisible=1, copy=False)

    name = fields.Char('Insurance Name')
    emp_id = fields.Many2one('hr.employee', required=True, string="Employee")

    date_from = fields.Date("Start Date", default=datetime.now())
    date_to = fields.Date("End Date")

    categ_id = fields.Many2one('insurance.category', string="Category")

    description = fields.Text('Description')

    state = fields.Selection([('draft','Draft'),('reject','Reject'),('approve','Approve')], default='draft')



    def reject_action(self):
        return self.write({'state': 'reject'})

    def approve_action(self):
        return self.write({'state': 'approve'})

    def reset_action(self):
        return self.write({'state': 'draft'})

class HRInsuranceCategoery(models.Model):
    _name = 'insurance.category'

    name = fields.Char('Name')