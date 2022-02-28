{
    #  Information
    'name': 'Partner_wise_product',
    'version': '15.0.1',
    'summary': 'Partner wise product',
    'description': 'Partner wise product',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['contacts', 'sale_management'],
    'data': [
        'views/res_partner_view.xml',
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}