# -*- coding: utf-8 -*-

from odoo import models, fields

class ResPartner(models.Model):
    
    _inherit = 'res.partner'
    
    
    #----------------------------------
    # Fields declartion
    #----------------------------------
    
    days_to_deliver = fields.Integer(string="Days to Deliver", default=7)