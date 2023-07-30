# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Show/Hide Password',
    'version': '15.0.1.0.0',
    'sequence': 1,
    'summary': """
        Show/Hide Password in login screen, View Password Login Page, Show Password Login Page, Hide Password Login Page, 
        Web Responsive login, Odoo Web Login Page, Web backend login, Odoo login, Web Odoo Login Page Odoo Page Login,
        Web Responsive SignIn, Odoo Web SignIn Page, Web backend SignIn, Odoo SignUp Page, Odoo SignIn Page,
        Odoo login Odoo, Sign-up Odoo, SignUp Form Login, Odoo SignIn screen, Web Responsive SignIn, Odoo Web SignIn Page, 
        Web backend SignIn, Toggle Password SignUp Page, Odoo SignIn Page, Odoo Authentication Screen, Customize Login Page,
        Show/Hide Password in sign in screen, View Password SignIn Page, Show Password SignUp Page, Hide Password SignIn Page
    """,
    'description': "You can show and hide your password in login screen.",
    'author': 'Innoway',
    'maintainer': 'Innoway',
    'price': '0.0',
    'currency': 'USD',
    'website': 'https://innoway-solutions.com',
    'license': 'LGPL-3',
    'images': [
        'static/description/wallpaper.png'   
    ],
    'depends': [
        'web'
    ],
    'data': [
        'views/login_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'show_hide_password/static/src/scss/login.scss',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
