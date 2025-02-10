# -*- coding: utf-8 -*-
{
    'name': "videoclub",

    'summary': """
        Videoclub, alquiler de películas.""",

    'description': """
        Alquiler de películas mayoritariamente de terror, acción y comedia.
    """,

    'author': "Jesus Olmos Soler",
    'website': "http://ead.murciaeduca.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
