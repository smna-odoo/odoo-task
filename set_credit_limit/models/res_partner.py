# -*- coding: utf-8 -*-

from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    
    #--------------------------------
    # Fields declaration
    #--------------------------------
    
    customer_credit_limit = fields.Integer(string='Credit Limit')
