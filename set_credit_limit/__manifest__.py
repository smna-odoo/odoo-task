{
    #  Information
    'name': 'set_credit_limit',
    'version': '15.0.1',
    'summary': 'Set Credit Limit',
    'description': 'Set Credit Limit',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['contacts','account','sale_management'],
    'data': [
        'views/res_partner.xml',
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}