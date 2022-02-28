# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class SaleOrder(models.Model):
    
    _inherit='sale.order'
    
    
    #----------------------------------
    # Fields declartion
    #----------------------------------
    
    appointment_date = fields.Datetime(string="Appointment Date")
    # commitment_date = fields.Datetime('Delivery Date', copy=False,
    #                                   states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
    #                                   help="This is the delivery date promised to the customer. "
    #                                        "If set, the delivery order will be scheduled based on "
    #                                        "this date rather than product lead times.")
    
    
    #-----------------------------------
    # Onchange Method 
    #-----------------------------------
    
    @api.onchange('appointment_date')
    def _onchange_of_appointment_date(self):
        for rec in self:
            if rec.appointment_date and rec.partner_id and rec.partner_id.days_to_deliver > 0:
                rec.commitment_date = rec.appointment_date - timedelta(days=rec.partner_id.days_to_deliver)
           
           
    #-----------------------------------
    # Compute Method 
    #-----------------------------------
    
    # @api.depends('appointment_date')
    # def _delivery_date(self):
    #     for rec in self:
    #         if rec.appointment_date and rec.partner_id and rec.partner_id.days_to_deliver > 0:
    #             rec.commitment_date = rec.appointment_date - timedelta(days=rec.partner_id.days_to_deliver)
    
    
    #-----------------------------------
    # confirm method 
    #-----------------------------------
    
    def action_confirm(self):
        res = super(SaleOrder , self).action_confirm()
        for picking in self.picking_ids :
            picking.appointment_date = self.appointment_date
        return res



