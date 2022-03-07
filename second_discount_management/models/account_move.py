# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move.line'
    
    second_discount = fields.Float(string='2nd Disc. %', store=True)

    @api.onchange('quantity', 'discount', 'price_unit', 'tax_ids', 'second_discount')
    def _onchange_price_subtotal(self):
        rc = super(AccountMove, self)._onchange_price_subtotal()
        for rec in self:
            if rec.second_discount:
                rec.price_subtotal = rec.price_subtotal - ((rec.second_discount*rec.price_subtotal)/100)
        return rc

    
    # def _get_price_total_and_subtotal(self, price_unit=None, quantity=None, discount=None, currency=None, product=None, partner=None, taxes=None, move_type=None, second_discount=None):
    #     self.ensure_one()
    #     return self._get_price_total_and_subtotal_model(
    #         price_unit=price_unit or self.price_unit,
    #         quantity=quantity or self.quantity,
    #         discount=discount or self.discount,
    #         currency=currency or self.currency_id,
    #         product=product or self.product_id,
    #         partner=partner or self.partner_id,
    #         taxes=taxes or self.tax_ids,
    #         move_type=move_type or self.move_id.move_type,
    #         second_discount= second_discount or self.second_discount
    #     )

    # @api.model
    # def _get_price_total_and_subtotal_model(self, price_unit, quantity, discount, currency, product, partner, taxes, move_type, second_discount):
    #     ''' This method is used to compute 'price_total' & 'price_subtotal'.

    #     :param price_unit:  The current price unit.
    #     :param quantity:    The current quantity.
    #     :param discount:    The current discount.
    #     :param currency:    The line's currency.
    #     :param product:     The line's product.
    #     :param partner:     The line's partner.
    #     :param taxes:       The applied taxes.
    #     :param move_type:   The type of the move.
    #     :return:            A dictionary containing 'price_subtotal' & 'price_total'.
    #     '''
    #     res = {}

    #     # Compute 'price_subtotal'.
    #     line_discount_price_unit = price_unit * (1 - (discount / 100.0))
    #     subtotal = quantity * line_discount_price_unit  - second_discount

    #     # Compute 'price_total'.
    #     if taxes:
    #         force_sign = -1 if move_type in ('out_invoice', 'in_refund', 'out_receipt') else 1
    #         taxes_res = taxes._origin.with_context(force_sign=force_sign).compute_all(line_discount_price_unit,
    #             quantity=quantity, currency=currency, product=product, partner=partner, is_refund=move_type in ('out_refund', 'in_refund'))
    #         res['price_subtotal'] = taxes_res['total_excluded']
    #         res['price_total'] = taxes_res['total_included']
    #     else:
    #         res['price_total'] = res['price_subtotal'] = subtotal
    #     #In case of multi currency, round before it's use for computing debit credit
    #     if currency:
    #         res = {k: currency.round(v) for k, v in res.items()}
    #     return res
    
    # def _get_price_total_and_subtotal_model(self, price_unit, quantity, discount, currency, product, partner, taxes, move_type):
    #     res = super(AccountMove, self)._get_price_total_and_subtotal_model(price_unit, quantity, discount, currency, product, partner, taxes, move_type)
    #     if self.second_discount:
    #         res['price_subtotal'] - ((res['price_subtotal'] *self.second_discount) / 100)
    #     return res
