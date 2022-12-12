# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _


class HREmployee(models.Model):
    _inherit = "hr.employee"

    is_saudi = fields.Boolean(string='Is Saudi?', compute='_is_from_saudi')
    arabic_name = fields.Char(string='Arabic Name')
    identification_id = fields.Char(string='ID/ Iqama number', groups="hr.group_hr_user", tracking=True)

    def _is_from_saudi(self):
        for employee in self:
            if employee.country_id and employee.country_id.code == 'SA':
                employee.is_saudi = True
            else:
                employee.is_saudi = False