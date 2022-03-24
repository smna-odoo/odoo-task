{
    #  Information
    'name': 'ageing_report_custom',
    'version': '15.0.1',
    'summary': 'ageing report custom',
    'description': 'ageing report custom',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['stock'],
    'data': [
        'views/stock_quant_view.xml',
        'data/stock_quant_cron.xml',
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}