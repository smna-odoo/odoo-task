# -*- coding: utf-8 -*-

from odoo import models
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit='account.move'
    
    
    #-------------------------------
    # method declaration
    #-------------------------------
    
    def action_post(self):
        if self.amount_total > self.partner_id.customer_credit_limit:
            raise UserError("Your credit is {}".format(self.partner_id.customer_credit_limit))
        return super(AccountMove, self).action_post()