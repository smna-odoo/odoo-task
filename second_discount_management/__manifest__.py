
{
    #  Information
    'name': 'second_discount_management',
    'version': '15.0.1',
    'summary': 'Second Discount Management',
    'description': 'Second Discount Management',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_view.xml',
        'views/account_move.xml',
        'report/sale_order_template.xml',
        'report/account_move_template.xml',
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}