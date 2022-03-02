# -*- coding: utf-8 -*-

from odoo import fields, models, _, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    
    _inherit = 'sale.order'
    

    #--------------------------------
    # Fields declaration
    #--------------------------------
    
    is_approval_right = fields.Boolean(compute='_compute_approval_rights')
    zero_stock_approval = fields.Boolean(string="Zero Stock Approval")
    
    
    #-------------------------------
    # confirm method
    #-------------------------------
    
    def action_confirm(self):
        for record in self:
            if record.zero_stock_approval:
                return super(SaleOrder, self).action_confirm()
            else:
                raise UserError("Please Check Zero Stock Approval field")
    
    
    #-------------------------------
    # Compute method
    #-------------------------------
    
    @api.depends('zero_stock_approval')
    def _compute_approval_rights(self):
        for order in self:
            order.is_approval_right = True if self.env.user.has_group("sales_team.group_sale_manager") else False
