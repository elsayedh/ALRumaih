# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class HRAssign(models.Model):
    _name = 'hr.assign'
    _description = 'Employees Assigns'
    _inherit = ['mail.thread','mail.activity.mixin']

    # dt = Department
    # emp = Employee

    name = fields.Many2one('assign.type', string="Assign Type")
    emp_id = fields.Many2one('hr.employee', required=True, string="Employee")
    emp_job_id = fields.Many2one('hr.job', compute="_compute_employee", store=True, readonly=True, string="Job Position")

    doc_attachment_id02 = fields.Many2many('ir.attachment', 'doc_attach_rel02', 'doc_id02','attach_id02', string="Attachment", copy=False)


    date_from = fields.Date("Date From", default=datetime.now())
    date_to = fields.Date("Date To")

    description = fields.Text('Description')

    state = fields.Selection([('draft','Draft'),('reject','Reject'),('approve','Approve')], default='draft')

    @api.depends('emp_id')
    def _compute_employee(self):
        for i in self.filtered('emp_id'):
            i.emp_job_id = i.emp_id.job_id


    def reject_action(self):
        return self.write({'state': 'reject'})

    def approve_action(self):
        return self.write({'state': 'approve'})

    def reset_action(self):
        return self.write({'state': 'draft'})


class HRAssignType(models.Model):
    _name = 'assign.type'

    name = fields.Char("Name")

class HrAssignAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rel02 = fields.Many2many('hr.assign', 'doc_attachment_id02', 'attach_id02', 'doc_id02',
                                        string="Attachment", invisible=1)

