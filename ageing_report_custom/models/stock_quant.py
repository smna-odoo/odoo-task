from odoo import fields, models
from datetime import datetime


class SrockQuant(models.Model):
    _inherit = 'stock.quant'
    
    ageing_date = fields.Date()
    ageing_selection = fields.Selection([
        ('0-30','0-30'),
        ('30-90','30-90'),
        ('90-120','90-120'),
        ('120-max','120-max'),
    ])
    
    def _claculate_days(self):
        for record in self:
            record.ageing_date = datetime.now()
            days = record.ageing_date - record.date
            day = days.days
            if 0 <= day <= 30:
                record.ageing_selection = '0-30'
            elif 31 <= day <= 90:
                record.ageing_selection = '30-90'
            elif 91 <= day <= 120:
                record.ageing_selection = '90-120'
            else:
                record.ageing_selection = '120-max'
