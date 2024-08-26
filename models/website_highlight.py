# models/website_highlight.py

from odoo import models, fields


class WebsiteHighlight(models.Model):
    _name = "website.highlight"
    _description = "Website Highlights"

    name = fields.Char(string="Title", required=True)
    message = fields.Text(string="Message", required=True)
    active = fields.Boolean(string="Active", default=True)
