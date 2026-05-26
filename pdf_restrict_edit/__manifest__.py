{
    'name': 'PDF Restrict Edit',
    'version': '16.0.1.0.0',
    'category': 'Technical',
    'summary': 'Protect PDF reports from editing (no password on open)',
    'depends': ['base'],
    'author': 'Servertronix',      # ← ваше имя или название компании
    'website': 'https://github.com/yogannnn',  # ← опциональная ссылка на профиль/сайт
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
