{
    'name': 'Student Management Aman',
    'version': '19.0.1.0.0',
    'category': 'Education',
    'summary': 'Manage student records',
    'description': """
Student Management Module
=========================
A simple module to manage students.
    """,
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
}