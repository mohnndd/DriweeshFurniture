# See LICENSE file for full copyright and licensing details.

{
    # Module information
    "name": "POS Multi Branch",
    "version": "15.0.1.1",
    "license": "LGPL-3",
    "category": "Extra Tools",
    "sequence": "1",
    "summary": """Multiple Branch Management for Point of Sale""",
    # Author
    "author": "Intuz",
    "website": "https://www.intuz.com",
    # Dependencies
    "depends": ["point_of_sale", "base"],
    # Views
    "data": [
        "security/multi_branch_security.xml",
        "security/ir.model.access.csv",
        "views/multi_branch_view.xml",
        "views/res_users_view.xml",
        "views/pos_view.xml",
    ],
    # Odoo App Store Specific
    "images": [],
    # Technical
    "installable": True,
    "application": True,
    "auto_install": False,
}
