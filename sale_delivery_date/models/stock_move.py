# -*- coding: utf-8 -*-

# from odoo import models

# class StockMove(models.Model):
#     _inherit = 'stock.move'
    
#     def _get_new_picking_values(self):
#         vals = super(StockMove, self)._get_new_picking_values()
#         if self.sale_line_id.order_id.appointment_date:
#             vals.update({'appointment_date': self.sale_line_id.order_id.appointment_date})
#         return vals