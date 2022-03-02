# -*- coding: utf-8 -*-

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    
    
    #-------------------------------
    # Compute method
    #-------------------------------
    
    @api.onchange('product_id')
    def set_uom(self):
        self.ensure_one()
        for products in self.order_id.partner_id.product_line:
            if self.product_id == products.product_id:
                self.product_uom = products.uom_id
