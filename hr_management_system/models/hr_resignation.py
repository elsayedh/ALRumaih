# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class HRResignation(models.Model):
    _name = 'hr.resignation'
    _description = 'Employees Resignations'
    _inherit = ['mail.thread','mail.activity.mixin']

    # dt = Department
    # emp = Employee

    name = fields.Char('Resignation Name')
    emp_id = fields.Many2one('hr.employee', required=True, string="Employee")
    emp_job_id = fields.Many2one('hr.job', compute="_compute_employee", store=True, readonly=True, string="Job Position")
    emp_manager_id = fields.Many2one('hr.employee', compute="_compute_employee", store=True, readonly=True, string="Manager")

    emp_dt_id = fields.Many2one('hr.department', compute="_compute_employee", store=True, readonly=True, string="Department")
    emp_dt_manager_id = fields.Many2one('hr.employee', compute="_compute_employee", store=True, readonly=True, string="Department Manager")
    date_from = fields.Date("Date From", default=datetime.now())
    date_to = fields.Date("Date To")

    description = fields.Text('Description')

    state = fields.Selection([('draft','Draft'),('reject','Reject'),('approve','Approve')], default='draft')


    @api.depends('emp_id')
    def _compute_employee(self):
        for i in self.filtered('emp_id'):
            i.emp_job_id = i.emp_id.job_id
            i.emp_manager_id = i.emp_id.parent_id
            i.emp_dt_id = i.emp_id.department_id
            i.emp_dt_manager_id = i.emp_id.department_id.manager_id



    def reject_action(self):
        return self.write({'state': 'reject'})

    def approve_action(self):
        return self.write({'state': 'approve'})

    def reset_action(self):
        return self.write({'state': 'draft'})

