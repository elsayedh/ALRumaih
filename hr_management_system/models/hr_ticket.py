# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class HRTicket(models.Model):
    _name = 'hr.ticket'
    _description = 'Employees Tickets'
    _inherit = ['mail.thread','mail.activity.mixin']

    # dt = Department
    # emp = Employee

    name = fields.Many2one('ticket.type', string="Ticket Type")
    ticket_claim = fields.Float('Ticket Entitlement')
    emp_id = fields.Many2one('hr.employee', required=True, string="Employee")
    emp_job_id = fields.Many2one('hr.job', readonly=True, string="Job Position")

    doc_attachment_id08 = fields.Many2many('ir.attachment', 'doc_attach_rel08', 'doc_id08','attach_id08', string="Attachment", copy=False)

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


class HRTicketType(models.Model):
    _name = 'ticket.type'

    name = fields.Char("Name")


class HrTicketAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rel08 = fields.Many2many('hr.ticket', 'doc_attachment_id08', 'attach_id08', 'doc_id08',
                                        string="Attachment", invisible=1)

