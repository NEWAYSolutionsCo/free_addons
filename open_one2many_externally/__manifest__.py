# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Open One2many in External ListView',
    'version': '15.0.1.0.0',
    'sequence': 1,
    'summary': 'External List View, External One2many List, All in one External One2many List, All in one External One2many List, Open ListView One2many, Open List View One2many, Open One2many in List, External SubList View, External Sub List, Open One2many FormView, , Open One2many Form View',
    'description': "Open One2many in External ListView to allow users to search, filter and group by.",
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

    ],
    'data': [
        
    ],
    'assets': {
        'web.assets_backend': [
            'open_one2many_externally/static/src/scss/list_view.scss',
            'open_one2many_externally/static/src/js/list_view.js',
        ],
    },
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [
        
    ],
}
