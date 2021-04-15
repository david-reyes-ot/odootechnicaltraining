# -*- coding: utf-8 -*-

from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    is_session_product = fields.Boolean(string = "Use as session product",
                                        help = "Check this box to use this as a product for the session fee",
                                        default = False)
    