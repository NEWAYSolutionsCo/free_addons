# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Fixed Header Kanban View',
    'version': '15.0.1.0.0',
    'sequence': 1,
    'summary': 'Set Fix Header Kanban, Set Permanent Header Kanban, Web Sticky Header Kanban, Freeze Header Kanban, Set Fix Header, Set Permanent Header, Web Sticky Header, Freeze Header, Set Fix Header in Kanban, Set Permanent Header in Kanban, Web Sticky Header in Kanban, Freeze Header in Kanban, Set Fix Kanban Header, Set Permanent Kanban Header, Web Sticky Kanban Header, Freeze Kanban Header, All in one Fix Header, All in one Permanent Header, All in one Web Sticky Header, All in one Freeze Header',
    'description': "Fixed Header Kanban View is very useful for displaying kanban headers within Odoo.",
    'author': 'NEWAY Solutions',
    'maintainer': 'NEWAY Solutions',
    'price': '0.0',
    'currency': 'USD',
    'website': 'https://neway-solutions.com',
    'license': 'LGPL-3',
    'images': [
        'static/description/screenshot.gif'    
    ],
    'depends': [
        'web'
    ],
    'data': [
        
    ],
    'assets': {
        'web.assets_backend': [
            'fixed_header_kanban/static/src/scss/kanban.scss',
        ],
    },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
