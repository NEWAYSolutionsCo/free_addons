# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hide Followers Chatter',
    'version': '13.0.1.0.0',
    'sequence': 1,
    'summary': 'Odoo Hide Followers in Chatter, , All in one Chatter, All in one Odoo Chatter, Odoo Chatter Message, Mail Activity Chatter, Followers Odoo Chatter, Followers Chatter Log, Followers Chatter Notes, Web Backend Chatter, Web Responsive Chatter, Web Chatter Sidebar, Web Sidebar Chatter',
    'description': "Remove followers section from chatter.",
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
        'views/assets.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
