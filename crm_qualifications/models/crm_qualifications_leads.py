# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from datetime import datetime
from odoo import api, models, fields


class Lead_qualif(models.Model):
    _description = "Lead/Opportunity"
    _inherit = "crm.lead"
    date_reminder = fields.Date('Reminder Date', help="Date Reminder !")
    active_reminder = fields.Boolean('Active Reminder', default=False, track_visibility=True)

    @api.model
    def delay_lead(self):
        var=datetime.now().date()
        res=self.date_deadline
        r=res - var
        p= r.days
        if  p < 0:
            return True

    def _onchange_partner_id_values(self, partner_id):
        if partner_id:
            partner = self.env['res.partner'].browse(partner_id)
            partner_name = partner.parent_id.name
            if not partner_name and partner.is_company:
                partner_name = partner.name
            
            contact_info = self.env['crm.lead'].search(
                [('partner_id', '=', partner_id), ('contact_name', '!=', False)],
                order='id desc', limit=1
            )
            company_contact = contact_info.contact_name if contact_info.contact_name else False
            company_title   = partner.title.id if contact_info.title.id == False else contact_info.title.id

            return {
                'partner_name': partner_name,
                'contact_name': partner.name if not partner.is_company else company_contact,
                'title': company_title,
                'street': partner.street,
                'street2': partner.street2,
                'city': partner.city,
                'state_id': partner.state_id.id,
                'country_id': partner.country_id.id,
                'email_from': partner.email,
                'phone': partner.phone,
                'mobile': partner.mobile,
                'zip': partner.zip,
                'function': partner.function,
                'website': partner.website,
            }
        return {}
    
    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        values = self._onchange_partner_id_values(self.partner_id.id if self.partner_id else False)
        self.update(values)
