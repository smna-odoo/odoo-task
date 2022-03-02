# -*- coding: utf-8 -*-

from odoo import models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    #-------------------------------
    # method declaration
    #-------------------------------
    
    def action_confirm(self):
        if self.amount_total > self.partner_id.customer_credit_limit:
            raise UserError("Your credit is {}".format(self.partner_id.customer_credit_limit))
        return super(SaleOrder, self).action_confirm()

    def _create_invoices(self, grouped=False, final=False):
        if self.amount_total > self.partner_id.customer_credit_limit:
            raise UserError("Your credit is {}".format(self.partner_id.customer_credit_limit))
        return super(SaleOrder, self)._create_invoices(grouped, final)
    
    
