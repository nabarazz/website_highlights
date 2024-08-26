from odoo import models, fields


class WebsiteHighlight(models.Model):
    _name = "website.highlight"
    _description = "Website Highlight"

    name = fields.Char(string="Name", required=True)
    message = fields.Text(string="Message", required=True)
    active = fields.Boolean(string="Active", default=True)
