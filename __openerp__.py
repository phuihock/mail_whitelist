# -*- coding: utf-8 -*-
{
    'name': 'Mail Whitelist',
    'summary': 'Model whitelist',
    'version': '0.1',
    'category': 'Extra Tools',
    'description': """
Mail Whitelist
====================
This module allows user to selectively enable tracking of ``mail.thread``
subclasses. By installing this module, all ``mail.thread`` subclasses will
skip creation of ``mail.message`` unless whitelisted.

Note that this module does not remove openchatter widget from model forms. To
remove the widget, you need to modify the form accordingly.
""",
    'author': 'CODEKAKI SYSTEMS (R49045/14)',
    'website': 'http://codekaki.com',
    'depends': ['mail'],
    'data': [
        'mail_whitelist_view.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
