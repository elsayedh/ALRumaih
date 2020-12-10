# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


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


