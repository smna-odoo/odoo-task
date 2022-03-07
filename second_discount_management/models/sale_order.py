from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def _create_invoices(self, grouped=False, final=False):
        res = super(SaleOrder, self)._create_invoices(grouped, final)
        for discouts in self:
            discouts.invoice_ids.invoice_line_ids.second_discount = discouts.order_line.second_discount
        return res