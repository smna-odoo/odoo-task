# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    
    second_discount = fields.Float(string='2nd Disc. %')
    
    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'second_discount')
    def _compute_amount(self):
        rc = super(SaleOrderLine, self)._compute_amount()
        for rec in self:
            if rec.second_discount:
                rec.price_subtotal = rec.price_subtotal - ((rec.second_discount*rec.price_subtotal)/100)
        return rc
