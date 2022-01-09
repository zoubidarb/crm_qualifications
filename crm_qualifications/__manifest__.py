# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Qualifications',
    'version': '1.0',
    'category': 'Sales',
    'sequence': 5,
    'summary': 'Track leads and close opportunities',
    'description': "",
    'website': 'https://www.odoo.com',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_qualifications_leads_views.xml',
        'wizard/create_newLead_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
