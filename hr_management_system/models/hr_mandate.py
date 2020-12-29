# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class HRMandate(models.Model):
    _name = 'hr.mandate'
    _description = 'Employees Mandates'
    _inherit = ['mail.thread','mail.activity.mixin']

    # dt = Department
    # emp = Employee

    name = fields.Char('Mandate Name')
    emp_id = fields.Many2one('hr.employee', required=True, string="Mandated Employee")
    emp_job_id = fields.Many2one('hr.job', compute="_compute_employee", store=True, readonly=True, string="Job Position")

    doc_attachment_id04 = fields.Many2many('ir.attachment', 'doc_attach_rel04', 'doc_id04','attach_id04', string="Attachment", copy=False)

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


class HrMandateAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rel04 = fields.Many2many('hr.mandate', 'doc_attachment_id04', 'attach_id04', 'doc_id04',
                                        string="Attachment", invisible=1)

