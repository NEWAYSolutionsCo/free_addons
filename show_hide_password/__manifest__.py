# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Show/Hide Password',
    'version': '13.0.1.0.0',
    'sequence': 1,
    'summary': """
        Show/Hide Password in login screen, View Password Login Page, Show Password Login Page, Hide Password Login Page, Web Responsive login, Odoo Web Login Page, Web backend login, Odoo login,
        Show/Hide Password in sign in screen, View Password SignIn Page, Show Password SignUp Page, Hide Password SignIn Page, Web Responsive SignIn, Odoo Web SignIn Page, Web backend SignIn, Odoo SignUp Page, Odoo SignIn Page
    """,
    'description': "You can show and hide your password in login screen.",
    'author': 'NEWAY Solutions',
    'maintainer': 'NEWAY Solutions',
    'price': '0.0',
    'currency': 'USD',
    'website': 'https://neway-solutions.com',
    'license': 'LGPL-3',
    'images': [
        'static/description/screenshot.png'    
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
