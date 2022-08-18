# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hide Powered By Odoo',
    'version': '14.0.1.0.0',
    'sequence': 1,
    'summary': 'Hide Powered By Odoo in login screen.',
    'description': "Hide Powered By Odoo in login screen.",
    'author': 'NEWAY Solutions',
    'maintainer': 'NEWAY Solutions',
    'price': '0.0',
    'currency': 'USD',
    'website': 'https://neway-solutions.com',
    'license': 'LGPL-3',
    'images': [
        'static/description/icon.png'   
    ],
    'depends': [
        'web'
    ],
    'data': [
        'views/login_templates.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
