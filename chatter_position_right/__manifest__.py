# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Chatter Position Right',
    'version': '13.0.1.0.0',
    'sequence': 1,
    'summary': 'Odoo Chatter in Position Right, All in one Chatter, All in one Odoo Chatter, Odoo Chatter Message, Mail Activity Chatter, Right Odoo Chatter, Right Chatter Log, Right Chatter Notes, Web Backend Chatter, Web Responsive Chatter, Web Chatter Sidebar, Web Sidebar Chatter',
    'description': "Change Odoo Chatter Position from bottom to right.",
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
        'views/assets.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
