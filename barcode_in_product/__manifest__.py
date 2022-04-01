{
    #  Information
    'name': 'barcode_in_product',
    'version': '15.0.1',
    'summary': 'barcode_in_product',
    'description': 'barcode_in_product',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['stock', 'sale_management'],
    'data': [
        'views/product_template.xml',
        'report/product_template_barcode.xml',
        'report/product_template.xml',
        
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}