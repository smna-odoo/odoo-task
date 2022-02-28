{
    #  Information
    'name': 'sale delivery date',
    'version': '15.0.1',
    'summary': 'sale delivery date',
    'description': 'sale delivery date',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['sale', 'contacts'],
    'data': [
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
        
        ],

    # Other
    'installable': True,
    'auto_install': False,
}