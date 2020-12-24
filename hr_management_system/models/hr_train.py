# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class HRTrain(models.Model):
    _name = 'hr.train'
    _description = 'Employees Trains'
    _inherit = ['mail.thread','mail.activity.mixin']

    # dt = Department
    # emp = Employee

    emp_ref = fields.Many2one('hr.employee', related='emp_id', invisible=1, copy=False)

    name = fields.Char('Train Name')
    emp_id = fields.Many2one('hr.employee', required=True, string="Employee")
    emp_job_id = fields.Many2one('hr.job', readonly=True, string="Job Position")
    emp_manager_id = fields.Many2one('hr.employee', readonly=True, string="Manager")
    date_from = fields.Date("Start Date", default=datetime.now())
    date_to = fields.Date("End Date")

    description = fields.Text('Description')

    state = fields.Selection([('draft','Draft'),('reject','Reject'),('approve','Approve')], default='draft')

    @api.onchange('emp_id')
    def emp_details(self):
        if self.emp_id.job_id:
            self.emp_job_id = self.emp_id.job_id
        else:
            self.emp_job_id = False

        if self.emp_id.parent_id:
            self.emp_manager_id = self.emp_id.parent_id
        else:
            self.emp_manager_id = False



    def reject_action(self):
        return self.write({'state': 'reject'})

    def approve_action(self):
        return self.write({'state': 'approve'})

    def reset_action(self):
        return self.write({'state': 'draft'})