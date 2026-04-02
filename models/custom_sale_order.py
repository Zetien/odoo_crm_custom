from odoo import models, fields, api

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    zone = fields.Selection([('N','Norte'), ('C','Centro'), ('S','Sur')], string='Zona comercial')