# See LICENSE file for full copyright and licensing details.
{
    # Module information
    "name": "PO Extension",
    "version": "15.0.1.1",
    "license": "LGPL-3",
    "category": "Extra Tools",
    "sequence": "1",
    "summary": """Purchase Order Extension""",
    # Author
    "author": "Intuz",
    "website": "https://www.intuz.com",
    # Dependencies
    "depends": ["purchase", "base"],
    # Views
    "data": [
        "security/po_security.xml",
        "views/Purchase_order_views.xml",
    ],
    # Odoo App Store Specific
    "images": [],
    # Technical
    "installable": True,
    "application": True,
    "auto_install": False,
}
