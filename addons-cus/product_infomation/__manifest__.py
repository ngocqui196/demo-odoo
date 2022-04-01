{
    'name': 'Product',
    'version': '1.2',
    'summary': 'Phần mềm quản lý sản phẩm',
    'sequence': 16,
    'description': """
    App quản lý sản phẩm
    """,
    'category': '',
    'author': '',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        'base',
    ],
    'data': [
        'views/product_information_views.xml',
        'views/subject_information.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}