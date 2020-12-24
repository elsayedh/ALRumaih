# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class HRApplicant(models.Model):
    _inherit = 'hr.applicant'


    def write(self, vals):
        # user_id change: update date_open

        if 'stage_id' in vals:
            new_stage = self.env['hr.recruitment.stage'].browse(vals['stage_id'])
            if new_stage.name == "Contract Proposal" or new_stage.name == "اقتراح العقد":
                mail_content = _(
                    "  Hello  " + str(self.partner_name) + ",<br>This is our job offer for you:  <br>" + str(self.description)
                    + "<br>And Our Salary Is: " + str(self.salary_proposed))

                main_content = {
                    'subject': _('Our Job Offer'),
                    'author_id': self.env.user.partner_id.id,
                    'body_html': mail_content,
                    'email_to': self.email_from,
                }
                self.env['mail.mail'].create(main_content).send()


        if vals.get('user_id'):
            vals['date_open'] = fields.Datetime.now()
        if vals.get('email_from'):
            vals['email_from'] = vals['email_from'].strip()
        # stage_id: track last stage before update
        if 'stage_id' in vals:
            vals['date_last_stage_update'] = fields.Datetime.now()
            if 'kanban_state' not in vals:
                vals['kanban_state'] = 'normal'
            for applicant in self:
                vals['last_stage_id'] = applicant.stage_id.id
                res = super(HRApplicant, self).write(vals)
        else:
            res = super(HRApplicant, self).write(vals)

        return res
