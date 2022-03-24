{
    #  Information
    'name': 'sale_order_search_panel',
    'version': '15.0.1',
    'summary': 'sale_order_search_panel',
    'description': 'sale_order_search_panel',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['sale_management', 'muk_web_searchpanel'],
    'data': [
        'views/sale_oreder_search_panel_view.xml'
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}