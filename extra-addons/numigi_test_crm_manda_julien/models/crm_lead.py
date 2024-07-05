# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, api, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    def _get_expired_opportunities(self):
        draft_stage = self.env.ref('crm.stage_lead1')
        ten_days_ago = datetime.now() - timedelta(days=10)
        return self.search([
            ('stage_id', '=', draft_stage.id),
            ('create_date', '<=', ten_days_ago),
            ('type', '=', 'opportunity'),
        ])
    
    def _send_notification(self, opportunity):
        team_members = opportunity.team_id.member_ids
        if team_members:
            message = f"""
            Hello,<br/><br/>
            Thank you for following up on this opportunity <a href="#" data-oe-model="crm.lead" data-oe-id="{opportunity.id}">{opportunity.name}</a>.<br/><br/>
            Best regards.
            """
            opportunity.message_post(
                body=message,
                subtype_id=self.env.ref('mail.mt_note').id,
                partner_ids=team_members.mapped('partner_id').ids,
            )

    @api.model
    def check_and_notify_draft_opportunities(self):
        for opportunity in self._get_expired_opportunities():
            self._send_notification(opportunity)
