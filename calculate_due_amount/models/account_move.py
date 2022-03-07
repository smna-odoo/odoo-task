# -*- coding: utf-8 -*-

from odoo import api, models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'
    
    
    #--------------------------------
    # Fields declaration
    #--------------------------------
    
    amount_paid = fields.Float(string= 'Amount paid', compute='total_paid_amount', store=True)
    
    
    #--------------------------------
    # Compute field
    #--------------------------------
    
    @api.depends('amount_total_signed', 'amount_residual_signed')
    def total_paid_amount(self):
        for amount in self:
            amount.amount_paid = abs(amount.amount_total_signed - amount.amount_residual_signed)
