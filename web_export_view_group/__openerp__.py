# -*- coding: utf-8 -*-
# Copyright 2016 Ecosoft Co. Ltd.
#
# This module is for limiting the access for "Excel Export Button". To assign the uesr to a new group named Excel Expor
# the user has access to this button to export needed information
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Limit Excel Button CFT",
    "version": "8.0.0.1.0",
    "author": "Ecosoft Co. Ltd.",
    "license": "AGPL-3",
    "description": """
    """,
    "category": "Base",
    "depends": [
        'web_export_view',
    ],
    "data": [
        'security/security_export.xml'
    ],
    "js": [
    ],
    "css": [
    ],
    "auto_install": False,
    "installable": True,
    "external_dependencies": {
        'python': [],
    },
}
