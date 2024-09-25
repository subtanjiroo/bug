{
    "name": "Real Estate",
    "version":"1.0",
    "website":"",
    "author":"Miracle",
    "description": """
        Real Estate module to showw
    """,

    "depends":['base','mail'],
    "data":[
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'security/model_access.xml',
        'security/ir_rule.xml',

        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tags_view.xml',
        
        'views/property_offer_view.xml',
        'views/menu_items.xml',
        #data files
        # 'data/property_type.xml',
        'data/estate.property.type.csv',
        'data/mail_template.xml',

        #report
        'report/report_template.xml',
        'report/property_report.xml',
    ],
    'demo':[
        'demo/property_tag.xml',
    ],

    # 'assets': {
    #     'web.assets_backend':[
    #         'real_estate/static/src/js/my_custom_tag.js',
    #         'real_estate/static/src/xml/my_custom_tag.xml',
    #     ]
    # },

    "installable": True,
    "application": True,
    "license": "LGPL-3"
}