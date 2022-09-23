# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customize Title Header',
    'version': '15.0.1.0.0',
    'sequence': 1,
    'summary': 'Custom shortcut title, Odoo Favicon Title, Odoo Title and Favicon, Odoo Backend Title Favicon, Odoo Web Favicon Title, Odoo Web Title, Odoo Customize Title Header, Odoo Browser Header, Odoo Header Favicon, Odoo Header Title, Remove Odoo Favicon Header, Remove Odoo Title, Remove Favicon Header',
    'description': "Choose your own Title to display on the browser header.",
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
        'web.assets_backend_prod_only': [
            'customize_title_header/static/src/js/favicon.js',
        ],
    },
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'qweb': [
        
    ],
}
