{
    'name': 'Chatbox AI',
    'version': '1.0',
    'depends': ['base','web'],
    'data': [
        'security/ir.model.access.csv',
        
        'views/chatbox_view.xml',
        'views/menu_items.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'chatbox_AI/static/src/js/chatbox_script.js',
            'chatbox_AI/static/src/css/chatbox_style.css',
        ],
    },
    'installable': True,
    'application': True,
    "license": "LGPL-3"
}
