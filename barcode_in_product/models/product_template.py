# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductBarcode(models.Model):
    _inherit = 'product.template'
    
    
    #--------------------------------
    # Fields declaration
    #--------------------------------
    
    barcode_number = fields.Char(string='Barcode Number')
    
        