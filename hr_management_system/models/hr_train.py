# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import datetime

class HRTrain(models.Model):
    _name = 'hr.train'
    _description = 'Employees Trains'
    _inherit = ['mail.thread','mail.activity.mixin']

    # dt = Department
    # emp = Employee

    name = fields.Char('Train Name')
    emp_id = fields.Many2one('hr.employee', invisible=1, copy=False, string="Employee")
    emp_job_id = fields.Many2one('hr.job', compute="_compute_employee", store=True, readonly=True, string="Job Position")
    emp_manager_id = fields.Many2one('hr.employee', compute="_compute_employee", store=True, readonly=True, string="Manager")

    doc_attachment_id09 = fields.Many2many('ir.attachment', 'doc_attach_rel09', 'doc_id09','attach_id09', string="Attachment", copy=False)

    date_from = fields.Date("Start Date", default=datetime.now())
    date_to = fields.Date("End Date")

    description = fields.Text('Description')

    state = fields.Selection([('draft','Draft'),('reject','Reject'),('approve','Approve')], default='draft')


    @api.depends('emp_id')
    def _compute_employee(self):
        for i in self.filtered('emp_id'):
            i.emp_job_id = i.emp_id.job_id
            i.emp_manager_id = i.emp_id.parent_id

    # @api.onchange('emp_id')
    # def emp_details(self):
    #     if self.emp_id.job_id:
    #         self.emp_job_id = self.emp_id.job_id
    #     else:
    #         self.emp_job_id = False
    #
    #     # if self.emp_id.parent_id:
    #     #     self.emp_manager_id = self.emp_id.parent_id
    #     # else:
    #     #     self.emp_manager_id = False



    def reject_action(self):
        return self.write({'state': 'reject'})

    def approve_action(self):
        return self.write({'state': 'approve'})

    def reset_action(self):
        return self.write({'state': 'draft'})


class HrTrainAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rel09 = fields.Many2many('hr.train', 'doc_attachment_id09', 'attach_id09', 'doc_id09',
                                        string="Attachment", invisible=1)

