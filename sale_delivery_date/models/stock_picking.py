# # -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import timedelta


class StockPicking(models.Model):
   
    _inherit = "stock.picking"
    
    
    #----------------------------------
    # Fields declartion
    #----------------------------------
    
    appointment_date = fields.Datetime(string="Appointment Date")
    
    
    #----------------------------------
    # Onchange Method 
    #----------------------------------
    
    @api.onchange('appointment_date')
    def _onchange_of_appointment_date(self):
        for rec in self:
            if rec.appointment_date and rec.partner_id and rec.partner_id.days_to_deliver > 0:
                rec.scheduled_date = rec.appointment_date - timedelta(days=rec.partner_id.days_to_deliver)
