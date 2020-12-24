# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from dateutil.parser import parse


class HRContractInherit(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def _get_lang(self):
        return self.env['res.lang'].get_installed()

    emp_lang = fields.Selection(selection='_get_lang', string='Language')
    emp_exp = fields.Char(_('Experience'))
    emp_date_start = fields.Date(_('Work Starting Date'))
    emp_insurance_num = fields.Char(_('Medical insurance number'))
    emp_job_data = fields.Char(_('Job Data'))


    # train
    def document_view_train(self):
        self.ensure_one()
        domain = [
            ('emp_ref', '=', self.id)]

        return {
            'name': _('Trains'),
            'domain': domain,
            'res_model': 'hr.train',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Click To Create For New Records
                        </p>'''),
            'limit': 80,
            'context': "{'default_emp_ref': '%s'}" % self.id,
        }

    def _document_count_train(self):
        for each in self:
            document_ids2 = self.env['hr.train'].sudo().search([('emp_ref', '=', each.id)])
            each.document_count_train = len(document_ids2)
            # print(document_ids2.emp_id.name)
            # print(self.name)

    document_count_train = fields.Integer(compute='_document_count_train', string='# Trains')

    # insurance
    def document_view_insurance(self):
        self.ensure_one()
        domain = [
            ('emp_ref', '=', self.id)]

        return {
            'name': _('Medical Insurances'),
            'domain': domain,
            'res_model': 'hr.insurance',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Click To Create For New Records
                        </p>'''),
            'limit': 80,
            'context': "{'default_emp_ref': '%s'}" % self.id,
        }

    def _document_count_insurance(self):
        for each in self:
            document_ids2 = self.env['hr.insurance'].sudo().search([('emp_ref', '=', each.id)])
            each.document_count_insurance = len(document_ids2)
            # print(document_ids2.emp_id.name)
            # print(self.name)

    document_count_insurance = fields.Integer(compute='_document_count_insurance', string='# Medical Insurance')

    # protection
    def document_view_protection(self):
        self.ensure_one()
        domain = [
            ('emp_ref', '=', self.id)]

        return {
            'name': _('Protections'),
            'domain': domain,
            'res_model': 'hr.protection',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Click To Create For New Records
                        </p>'''),
            'limit': 80,
            'context': "{'default_emp_ref': '%s'}" % self.id,
        }

    def _document_count_protection(self):
        for each in self:
            document_ids2 = self.env['hr.protection'].sudo().search([('emp_ref', '=', each.id)])
            each.document_count_protection = len(document_ids2)
            # print(document_ids2.emp_id.name)
            # print(self.name)

    document_count_protection = fields.Integer(compute='_document_count_protection', string='# Protections')


class HRTimeOffInherit(models.Model):
    _inherit = 'hr.leave'

    # this function to solve arabic date error in TIMEOFF module
    # check git error here > https://github.com/odoo/odoo/issues/62053
    @api.model
    def get_unusual_days(self, date_from, date_to=None):
        date_from = parse(date_from).strftime('%Y-%m-%d')
        if date_to:
            date_to = parse(date_to).strftime('%Y-%m-%d')
        return super(HRTimeOffInherit, self).get_unusual_days(date_from, date_to)
