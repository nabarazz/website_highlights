# __manifest__.py

{
    "name": "Website Highlights",
    "version": "1.0",
    "category": "Website",
    "summary": "Dynamic Highlights Banner for Website",
    "description": "This module allows you to create, manage, and display dynamic scrolling highlights on your Odoo website.",
    "depends": ["website"],
    "data": [
        "views/website_highlight_views.xml",
        "views/website_templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_highlights/static/src/css/highlight_style.css",
        ],
    },
    "installable": True,
    "application": False,
}
