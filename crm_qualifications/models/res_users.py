from datetime import datetime
from odoo import  fields, models, api, modules

class Users(models.Model):
    _inherit = "res.users"
    _description = 'Users'


    @api.model
    def systray_get_leads(self):
        model_name = "crm.lead"
        query = """SELECT m.id, count(*), act.res_model as model,
                    CASE
                        WHEN %(today)s::date - act.date_deadline::date = 0 Then 'today'
                        WHEN %(today)s::date - act.date_deadline::date > 0 Then 'overdue'
                        WHEN %(today)s::date - act.date_deadline::date < 0 Then 'planned'
                    END AS states
                FROM mail_activity AS act
                JOIN ir_model AS m ON act.res_model_id = m.id
                WHERE user_id = %(user_id)s AND m.model = %(model_name)s
                GROUP BY m.id, states, act.res_model;
                """
        self.env.cr.execute(query, {
            'today': fields.Date.context_today(self),
            'user_id': self.env.uid,
            'model_name': model_name
        })
        icon_ = modules.module.get_module_icon(self.env['crm.lead']._original_module)
        activity_data = self.env.cr.dictfetchall()
        user_activities = {}
        if(activity_data):
            user_activities = {
                'name': 'Lead',
                'model': model_name,
                'type': 'activity',
                'icon': icon_,
                'total_count': len(activity_data),
                'today_count': 0,
                'overdue_count': 0,
                'planned_count': 0
            }
        
        for activity in activity_data:
            user_activities['%s_count' % activity['states']] += activity['count']
        return [user_activities,]
