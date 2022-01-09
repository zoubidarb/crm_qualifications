# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import api, fields, models


class CrmLeadNew(models.TransientModel):
    _name = 'crm.lead.new'
    _description = 'New lead'
    _inherit = ['crm.lead']
    
    @api.model
    def create(self, values):
        """
            Create a new record for a model ModelName
            @param values: provides a data for new record
    
            @return: returns a id of new record
        """

    
        result = super(CrmLeadNew, self).create(values)
        return result
    