# -*- coding: utf-8 -*-
{
    'name': "Hospital Management System",
    'license': 'LGPL-3',
    'summary': "Odoo Tutorial",

    'description': """
Odoo tutorial app hospital
    """,

    'author': "BorisIsac",
    'website': "###",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0.1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/menu.xml',
        'views/patient_readonly_view.xml',
        'views/patient_view.xml',
        'views/appointments_view.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

