{
    #  Information
    'name': 'calculate_due_amount',
    'version': '15.0.1',
    'summary': 'Calculate Due Amount',
    'description': 'Calculate Due Amount',
    'category': 'Sale',

    # Author
    'author': 'Odoo PS',
    'website': 'https://www.odoo.com',

    # Dependency
    'depends': ['account_accountant'],
    'data': [
        'views/account_move_view.xml'
        ],

    # Other
    'installable':True,
    'auto_install':False,
    'application':True,
}