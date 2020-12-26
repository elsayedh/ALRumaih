# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class HRMandate(models.Model):
    _name = 'hr.mandate'
    _description = 'Employees Mandates'
    _inherit = ['mail.thread','mail.activity.mixin']

    # dt = Department
    # emp = Employee

    # emp_ref = fields.Many2one('hr.employee', related='emp_id', invisible=1, copy=False)

    name = fields.Char('Mandate Name')
    emp_id = fields.Many2one('hr.employee', required=True, string="Mandated Employee")
    emp_job_id = fields.Many2one('hr.job', readonly=True, string="Job Position")

    date_from = fields.Date("Date From", default=datetime.now())
    date_to = fields.Date("Date To")

    description = fields.Text('Description')

    state = fields.Selection([('draft','Draft'),('reject','Reject'),('approve','Approve')], default='draft')

    @api.onchange('emp_id')
    def emp_details(self):
        # Job Position
        if self.emp_id.job_id:
            self.emp_job_id = self.emp_id.job_id
        else:
            self.emp_job_id = False



    def reject_action(self):
        return self.write({'state': 'reject'})

    def approve_action(self):
        return self.write({'state': 'approve'})

    def reset_action(self):
        return self.write({'state': 'draft'})

