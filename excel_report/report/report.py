from odoo import models


class ExcelReport(models.AbstractModel):
    
    _name = 'report.excel_report.report_invoice_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    
    def generate_xlsx_report(self, workbook, data, lines):
        for i in lines:
            format = workbook.add_format({'font_size':16})
            sheet = workbook.add_worksheet('Testing')
            sheet.write(0, 0, 'Date', format)
            sheet.write(0, 1, i.invoice_date, format)
        