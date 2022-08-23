# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Fixed Header Kanban View',
    'version': '15.0.1.0.0',
    'sequence': 1,
    'summary': 'Sticky Header in Kanban View.',
    'description': "Fixed Header Kanban View is very useful for displaying kanban headers within Odoo.",
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
        
    ],
    'assets': {
        'fixed_header_kanban.assets_backend': [
            'fixed_header_kanban/static/src/scss/kanban.scss',
        ],
    },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
