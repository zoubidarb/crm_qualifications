# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import logging

from odoo.addons.mail.controllers.main import MailController
from odoo import http
from odoo.http import request
from datetime import datetime
_logger = logging.getLogger(__name__)


class CrmController(http.Controller):

    

    #conroller for pistes en retard
    @http.route('/crm/piste_retard/', website=True, auth='public')
    def piste_retard(self, **kw):
        Customer=request.env['crm.lead'].sudo().search([]) 
        return request.render("crm_qualifications.action_retard", {'Customer': Customer})
    
    @http.route('/crm/list_doc/', website=True, auth='public')
    def list_doc(self, **kw):
        to_day=datetime.today()
        count_=request.env['crm.lead'].sudo().search_count(
            [('date_deadline', '!=', False),('date_deadline', '<', to_day) ]
        ) 
        return request.render("crm_qualifications.crm_list_doc", {'count_pistes': count_})





