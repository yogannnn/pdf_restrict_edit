{
    'name': 'PDF Restrict Edit',
    'version': '16.0.1.0.0',
    'category': 'Technical',
    'summary': 'Protect PDF reports from editing (no password on open)',
    'depends': ['base'],
    'price': 9.99,
    'currency': 'EUR',
    'author': 'Servertronix',      # ← ваше имя или название компании
    'data': [
        'security/ir.model.access.csv',
        'views/pdf_settings_view.xml',
    ],
    # КЛЮЧ images должен быть на этом уровне
    'images': [
        'static/description/screenshot.png',
        'static/description/icon.png', # Это иконка
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
