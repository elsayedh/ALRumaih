# -*- coding: utf-8 -*-

from datetime import timedelta, datetime, date

from odoo import api, fields, models, _


class ContractDocuments(models.Model):
    _inherit = 'hr.contract'


    def _document_count(self):
        for each in self:
            document_ids = self.env['hr.contract.document'].sudo().search([('contract_ref', '=', each.id)])
            each.document_count = len(document_ids)

    def document_view(self):
        self.ensure_one()
        domain = [
            ('contract_ref', '=', self.id)]
        return {
            'name': _('Documents'),
            'domain': domain,
            'res_model': 'hr.contract.document',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Click to Create for New Documents
                        </p>'''),
            'limit': 80,
            'context': "{'default_contract_ref': %s}" % self.id
        }

    document_count = fields.Integer(compute='_document_count', string='# Documents')


class HrContractDocument(models.Model):
    _name = 'hr.contract.document'
    _description = 'HR Employee Documents'

    def mail_reminder(self):
        """Sending document expiry notification to employees."""

        groups = self.env['res.groups'].search([('id', '=', '13')])

        print(groups)

        now = datetime.now() + timedelta(days=1)
        # date_now = now.date()
        date_now = fields.Date.today()
        match = self.search([])
        for i in match:
            if i.expiry_date:
                if i.notification_type == 'single':
                    exp_date = fields.Date.from_string(i.expiry_date)
                    print('exp_date :',exp_date)
                    # if date_now == exp_date:
                    if date_now == i.expiry_date:

                        mail_content = "  Hello  " + i.contract_ref.employee_id.name + ",<br>Your Document " + i.name + " is going to expire on " + \
                                       str(i.expiry_date) + ". Please renew it before expiry date"
                        main_content = {
                            'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                            'author_id': self.env.user.partner_id.id,
                            'body_html': mail_content,
                            'email_to': i.contract_ref.employee_id.work_email,
                        }
                        self.env['mail.mail'].create(main_content).send()
                elif i.notification_type == 'multi':
                    exp_date = fields.Date.from_string(i.expiry_date) - timedelta(days=i.before_days)
                    if date_now == exp_date or date_now == i.expiry_date: #on Expire date and few days(As it set) before expire date
                        print('mail send started before few')
                        mail_content = "  Hello  " + i.contract_ref.employee_id.name + ",<br>Your Document " + i.name + \
                                       " is going to expire on " + str(i.expiry_date) + \
                                       ". Please renew it before expiry date"
                        main_content = {
                            'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                            'author_id': self.env.user.partner_id.id,
                            'body_html': mail_content,
                            'email_to': i.contract_ref.employee_id.work_email,
                        }
                        self.env['mail.mail'].create(main_content).send()
                elif i.notification_type == 'everyday':
                    exp_date = fields.Date.from_string(i.expiry_date) - timedelta(days=i.before_days)
                    # if date_now >= exp_date and date_now == i.expiry_date:
                    if date_now >= exp_date or date_now == i.expiry_date:

                        print('Everyday till START sending')

                        mail_content = "  Hello  " + i.contract_ref.employee_id.name + ",<br>Your Document " + i.name + \
                                       " is going to expire on " + str(i.expiry_date) + \
                                       ". Please renew it before expiry date"
                        main_content = {
                            'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                            'author_id': self.env.user.partner_id.id,
                            'body_html': mail_content,
                            'email_to': i.contract_ref.employee_id.work_email,
                        }
                        self.env['mail.mail'].create(main_content).send()
                elif i.notification_type == 'everyday_after':
                    exp_date = fields.Date.from_string(i.expiry_date) + timedelta(days=i.before_days)
                    # if date_now == exp_date and date_now == i.expiry_date:
                    if date_now <= exp_date or date_now == i.expiry_date:

                        print('Every day after START sending')
                        mail_content = "  Hello  " + i.contract_ref.employee_id.name + ",<br>Your Document " + i.name + \
                                       " is expired on " + str(i.expiry_date) + \
                                       ". Please renew it "
                        main_content = {
                            'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                            'author_id': self.env.user.partner_id.id,
                            'body_html': mail_content,
                            'email_to': i.contract_ref.employee_id.work_email,
                        }
                        self.env['mail.mail'].create(main_content).send()
                else:
                    exp_date = fields.Date.from_string(i.expiry_date) - timedelta(days=7)
                    # if date_now >= exp_date:
                    if date_now == exp_date:
                        mail_content = "  Hello  " + i.contract_ref.employee_id.name + ",<br>Your Document " + i.name + \
                                       " is going to expire on " + \
                                       str(i.expiry_date) + ". Please renew it before expiry date"
                        main_content = {
                            'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                            'author_id': self.env.user.partner_id.id,
                            'body_html': mail_content,
                            'email_to': i.contract_ref.employee_id.work_email,
                        }
                        self.env['mail.mail'].create(main_content).send()

    @api.constrains('expiry_date')
    def check_expr_date(self):
        for each in self:
            if each.expiry_date:
                exp_date = fields.Date.from_string(each.expiry_date)
                if exp_date < date.today():
                    raise Warning('Your Document Is Expired.')

    name = fields.Char(string='Document Number', required=True, copy=False, help='You can give your'
                                                                                 'Document number.')
    description = fields.Text(string='Description', copy=False, help="Description")
    expiry_date = fields.Date(string='Expiry Date', copy=False, help="Date of expiry")
    contract_ref = fields.Many2one('hr.contract', invisible=1, copy=False, string="Contract")
    doc_attachment_id01 = fields.Many2many('ir.attachment', 'doc_attach_rel01', 'doc_id01', 'attach_id01', string="Attachment",
                                         help='You can attach the copy of your document', copy=False)
    issue_date = fields.Date(string='Issue Date', default=fields.datetime.now(), help="Date of issue", copy=False)
    before_days = fields.Integer(string="Days", help="How many number of days before to get the notification email")
    notification_type = fields.Selection([
        ('single', 'Notification on expiry date'),
        ('multi', 'Notification before few days'),
        ('everyday', 'Everyday till expiry date'),
        ('everyday_after', 'Notification on and after expiry')
    ], string='Notification Type',
        help="""
        Notification on expiry date: You will get notification only on expiry date.
        Notification before few days: You will get notification in 2 days.On expiry date and number of days before date.
        Everyday till expiry date: You will get notification from number of days till the expiry date of the document.
        Notification on and after expiry: You will get notification on the expiry date and continues upto Days.
        If you did't select any then you will get notification before 7 days of document expiry.""")


class HrEmployeeContractAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rel01 = fields.Many2many('hr.contract.document', 'doc_attachment_id01', 'attach_id01', 'doc_id01',
                                      string="Attachment", invisible=1)

