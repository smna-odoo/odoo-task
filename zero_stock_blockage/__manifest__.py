{
    #  Information
    'name': 'zero stock blockage',
    'version': '15.0.1',
    'summary': 'zero stock blockage',
    'description': 'zero stock blockage',
    'category': 'Sale',

    # Author
    'author': 'odoo ps',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}