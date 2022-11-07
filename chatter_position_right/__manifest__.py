# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Chatter Position Right',
    'version': '16.0.1.0.0',
    'sequence': 1,
    'summary': """
        Odoo Chatter in Position Right, All in one Chatter, All in one Odoo Chatter, Odoo Chatter Message, Mail Activity Chatter, Edit Notes, 
        Right Odoo Chatter, Right Chatter Log, Right Chatter Notes, Web Backend Chatter, Web Chatter Sidebar, Chatter Note Visibility Note, 
        Web Sidebar Chatter, Mail Messages Chatter History Chatter Messages, Chatter Activities Visibility Activities, Web Responsive Chatter,
        Inbox Chatter Inbox Mail Activity, Send Messages, Schedule Activity Schedule Activities Scheduler, Chatter Message Visibility Message,
        Chatter Messages Visibility Messages, Chatter Activity Visibility Activity, Chatter Notes Visibility Notes, Edit Messages, Log a note,
        Mail Activities Scheduler, Live Chat, Chatter Room, ChatRoom, Configurable Chatter Position, Chatter Attachement, User Chatter Design,
        Configure Chatter Position Chatter Customize Position Chatter Customization, Show Chatter Show, Toggle Chatter Toggle User Chatter, 
        Mail Chatter Email History Chatter Mail Show History, Company Chatter Comments, Chatter User Activities, Disable Chatter, Chatter Panel, 
        Chatter User Mails, Chatter User Activity, Chatter User Notes, Chatter Sidebar, Hide Chatter Hide, Edit Logs, Log notes, Activity Preview
    """,
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
        
    ],
    'assets': {
        'web.assets_backend': [
            'chatter_position_right/static/src/scss/form.scss',
        ],
    },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
