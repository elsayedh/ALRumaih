# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class HRProtection(models.Model):
    _name = 'hr.protection'
    _description = 'Employees Protections'
    _inherit = ['mail.thread','mail.activity.mixin']

    # dt = Department
    # emp = Employee

    name = fields.Char('Protection Name')
    emp_id = fields.Many2one('hr.employee', required=True, string="Employee")
    emp_job_id = fields.Many2one('hr.job', compute="_compute_employee", store=True, readonly=True, string="Job Position")

    doc_attachment_id06 = fields.Many2many('ir.attachment', 'doc_attach_rel06', 'doc_id06','attach_id06', string="Attachment", copy=False)

    date_from = fields.Date("Start Date", default=datetime.now())
    date_to = fields.Date("End Date")

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


class HrProtectionAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rel06 = fields.Many2many('hr.protection', 'doc_attachment_id06', 'attach_id06', 'doc_id06',
                                        string="Attachment", invisible=1)

