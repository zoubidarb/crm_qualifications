# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from datetime import datetime
from odoo import models


class Lead_qualif(models.Model):
    _description = "Lead/Opportunity"
    _inherit = "crm.lead"
    