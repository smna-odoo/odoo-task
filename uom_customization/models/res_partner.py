# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'


    #--------------------------------
    # Fields declaration
    #--------------------------------
    
    product_line = fields.One2many('partner.wise.uom', 'partner_id')
