# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customize Favicon and Title',
    'version': '14.0.1.0.0',
    'sequence': 1,
    'summary': """
        Custom shortcut title, Odoo Favicon Title, Odoo Title and Favicon, Odoo Backend Title Favicon, Odoo Web Favicon Title, 
        Odoo Web Title, Odoo Customize Title Header, Odoo Browser Header, Odoo Header Favicon, Odoo Header Title, Web Window Title, 
        Web Backend Title, Odoo Backend Header, Web Responsive Title, Remove Odoo Favicon Header, Remove Odoo Title, Hide Odoo Title,
        Customization Favicon Title Customization, Configutable Favicon Title Configutable, Configution Favicon Title Configution, 
        Web Shortcut Customization Shortcut Editable Favicon Editable Shortcut Favicon Setup Title Header Title Browser Title Navigator,
        Custom shortcut icon, Odoo Backend Shortcut Header Browser Navigator, Browser Odoo Tab, Navigator Odoo Navigator, Navigator Tab,
        Remove Favicon Header, Web Odoo Shortcut Favicon Shortcut Odoo Shortcut, Odoo Backend Favicon Odoo Backend Title Odoo Browser
    """,
    'description': "Choose your own Favicon and Title to display on the browser header.",
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
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'qweb': [
        
    ],
}
