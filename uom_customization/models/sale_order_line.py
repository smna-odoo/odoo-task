# -*- coding: utf-8 -*-

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order.line'
    
    
    #-------------------------------
    # Compute method
    #-------------------------------
    
    @api.onchange('product_id')
    def set_uom(self):
        for products in self:
            for product in products.order_id.partner_id.product_line:
                if products.order_id.partner_id and products.product_id == product.product_id:
                    products.product_uom = product.uom_id
