# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from datetime import datetime
from odoo import  fields, models



class Partner(models.Model):
    _description = "Lead/partner"
    _inherit = "res.partner"

    lead_ids = fields.One2many('crm.lead', 'partner_id', string='Leads',
        domain=[('type', '=', 'lead'),('date_deadline', '>', datetime.today())])
    
    