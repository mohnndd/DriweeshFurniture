# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _

class PurchaseOrderExtends(models.Model):
    _inherit = "purchase.order"
    po_type = fields.Selection([
        ('internal_purchase', 'Internal'),
        ('external_purchase', 'External'),
    ], string='Type', required=True, default='internal_purchase')

