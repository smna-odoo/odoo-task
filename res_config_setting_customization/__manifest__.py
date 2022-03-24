{
    #  Information
    'name': 'res_config_setting_customization',
    'version': '15.0.1',
    'summary': 'res config setting customization',
    'description': 'res config setting customization',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['sale_management'],
    'data': [
        'views/res_config_setting_view.xml',
        'views/sale_order_view.xml',
        ],

    # Other
    'installable': True,
    'auto_install': False,
}