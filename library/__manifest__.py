# -*- coding: utf-8 -*-
{
    'name': "library",

    'license': 'LGPL-3',

    'summary': "library books management",

    'description': """
        Management for books rent
    """,

    'author': "BorisInc...",
    'website': "https://www.linkedin.com/in/boris-isac-b11a601a6",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/library_book.xml',
        'views/library_rent.xml',

        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
