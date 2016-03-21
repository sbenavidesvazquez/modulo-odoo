#openerp del modulo
{
'name':'Openacademy',
'summary': """Manage trainings""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Las categorías se pueden utilizar para filtrar módulos en módulos listado
    # Chequea https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # para esta larga lista
    'category': 'Test',
    'version': '0.1',

    # Cualquier modulo lo necesita para trabajar correctamente
    'depends': ['base'],

    # xml que carga
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy.xml'
    ],
    # modo demostracion que carga
    'demo': [
        'demo/demo.xml',
    ]
}