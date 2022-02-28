# -*- coding: utf-8 -*-

from odoo import models, fields

class PartnerWiseUom(models.Model):
    _name = "partner.wise.uom"
    _description = "partner wise uom"
    
    
    #--------------------------------
    # Fields declaration
    #--------------------------------
    
    partner_id = fields.Many2one('res.partner' )
    product_id = fields.Many2one('product.product')
    category_id = fields.Many2one(related="product_id.uom_id.category_id")
    uom_id = fields.Many2one('uom.uom', domain="[('category_id','=', category_id)]")
