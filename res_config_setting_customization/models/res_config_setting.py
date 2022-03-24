# -*- coding: utf-8 -*-

from odoo import fields, models

class ResConfig(models.TransientModel):
    _inherit = 'res.config.settings'
    
    
    #-------------------------------
    # field declaration
    #-------------------------------
    
    is_salesperson = fields.Boolean(string="Sales Person", config_parameter="res_config_setting_customization.is_salesperson")
    sales_person = fields.Many2one('res.users', config_parameter="res_config_setting_customization.sales_person")
