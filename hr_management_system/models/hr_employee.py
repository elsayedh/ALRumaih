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
