# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _

class PurchaseOrderExtends(models.Model):
    _inherit = "purchase.order"
    po_type = fields.Selection([
        ('internal_purchase', 'Internal'),
        ('external_purchase', 'External'),
    ], string='Type', required=True, default='internal_purchase')


class ProductTemplate(models.Model):
    _inherit = "product.template"

    retail_price = fields.Float(string='Retail Price')
    discounted_sale_price_tire_2 = fields.Float(string='Discounted Sale Price Tier 2')
    wholesale_price = fields.Float(string='Wholesale Price')
    gov_price = fields.Float(string='Gov Price')
