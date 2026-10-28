{
    'name': 'PDF Restrict Edit',
    'version': '16.0.1.0.0',
    'category': 'Technical',
    'summary': 'Protect PDF reports from editing (no password on open)',
    'depends': ['base'],
    'author': 'Servertronix',
    'website': 'https://github.com/yogannnn',
    'data': [
        'security/ir.model.access.csv',
        'views/pdf_settings_view.xml',
    ],
    'images': [
        'static/description/screenshot.png',
        'static/description/icon.png',
    ],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
    'price': 39.00,
    'currency': 'EUR',
}
