{
    #  Information
    'name': 'excel_report',
    'version': '15.0.1',
    'summary': 'excel report',
    'description': 'excel report',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['account_accountant'],
    'data': [
        'report/report.xml',
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}