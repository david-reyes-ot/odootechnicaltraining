# -*- coding: utf-8 -*-

{
    "name": "Odoo Academy",
    "summary": """Academy app to manage Training""",
    "description": """
        Academy app to manage Training:
        - Courses
        - Sessions
        - Attendance
    """,
    "author": "DF",
    "website": "https://www.odoo.com",
    "category": "Training",
    "version": "0.1",
    "depends": ["base"],
    "data": [
        "views/course_views.xml",
        "views/session_views.xml",
        "views/academy_menuitems.xml",
        "security/academy_security.xml",
        "security/ir.model.access.csv"
    ],
    "demo": [
        "demo/academy_demo.xml",
    ]
}