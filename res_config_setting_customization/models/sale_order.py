# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    #-------------------------------
    # field declaration
    #-------------------------------
    
    my_name = fields.Char(string='Name', default="smit nagar")
    is_boolean = fields.Boolean(compute='_compute_name')
    
    
    #-------------------------------
    # method declaration
    #-------------------------------
    
    @api.depends('my_name')
    def _compute_name(self):
        for rec in self:
            rec.is_boolean = self.env['ir.config_parameter'].sudo().get_param('res_config_setting_customization.is_salesperson')
    
    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        salesman_name = self.env['ir.config_parameter'].sudo().get_param('res_config_setting_customization.sales_person')
        if salesman_name:
            res.user_id = salesman_name
        return res
        