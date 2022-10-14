# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hide Followers Chatter',
    'version': '15.0.1.0.0',
    'sequence': 1,
    'summary': """
        Odoo Hide Followers in Chatter, , All in one Chatter, All in one Odoo Chatter, Odoo Chatter Message, Mail Activity Chatter, 
        Web Chatter Sidebar, Web Sidebar Chatter, All in one Chatter, All in one Odoo Chatter, Odoo Chatter Message, Mail Activity Chatter, 
        Right Odoo Chatter, Show Chatter Show, Right Chatter Notes, Web Backend Chatter, Web Chatter Sidebar, Chatter Note Visibility Note, 
        Web Sidebar Chatter, Mail Messages Chatter History Chatter Messages, Chatter Activities Visibility Activities, Web Responsive Chatter,
        Inbox Chatter Inbox Mail Activity, Send Messages, Schedule Activity Schedule Activities Scheduler, Chatter Message Visibility Message,
        Chatter Messages Visibility Messages, Chatter Activity Visibility Activity, Chatter Notes Visibility Notes, Edit Messages, Log a note,
        Mail Activities Scheduler, Live Chat, Chatter Room, ChatRoom, Chatter Attachement, User Chatter Design, Toggle Chatter Toggle User Chatter, 
        Mail Chatter Email History Chatter Mail Show History, Company Chatter Comments, Chatter User Activities, Edit Notes, Chatter Followers History,
        Chatter User Mails, Chatter User Activity, Chatter User Notes, Chatter Sidebar, Hide Chatter Hide, Edit Logs, Log notes, Activity Preview,
        Disable Followers Chatter Panel Followers Disable, Followers Removed from chatter, Remove Attachements, Disable Attachement Removed,
        Followers Odoo Chatter, Followers Chatter Log, Followers Chatter Notes, Web Backend Chatter, Web Responsive Chatter, Disable Chatter Followers, 
    """,
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
        
    ],
    'assets': {
        'web.assets_backend': [
            'odoo_hide_followers/static/src/scss/form.scss',
        ],
    },
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
