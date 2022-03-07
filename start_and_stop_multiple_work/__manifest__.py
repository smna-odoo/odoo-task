{
    #  Information
    'name': 'start_and_stop_multiple_work',
    'version': '15.0.1',
    'summary': 'Start and Stop Multiple Work',
    'description': 'Start and Stop Multiple Work',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['mrp', 'mrp_workorder'],
    'data': [
        'views/mrp_workorder.xml',
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}