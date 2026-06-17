from odoo import models, fields  # type: ignore[import]


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string="Student Name", required=True)
    age = fields.Integer(string="Age")
    email = fields.Char(string="Email")