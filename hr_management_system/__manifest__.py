# -*- coding: utf-8 -*-
{
    'name': "HR Management System",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr','hr_recruitment'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hr_employee.xml',
        'views/hr_resignation.xml',
        'views/hr_train.xml',
        'views/hr_insurance.xml',
        'views/hr_protection.xml',
        'views/hr_membership.xml',
        'views/hr_mandate.xml',
        'views/hr_ticket.xml',
        'views/hr_assign.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
