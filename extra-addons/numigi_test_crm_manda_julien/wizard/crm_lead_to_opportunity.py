
from odoo import models, api

class Lead2Opportunity(models.TransientModel):
    _inherit = 'crm.lead2opportunity.partner'

    @api.depends('user_id')
    def _compute_team_id(self):
        origin_lead = self.env['crm.lead'].browse(self._context.get('active_id'))
        if not origin_lead.team_id:
            return super(Lead2Opportunity, self)._compute_team_id()

        team_id = origin_lead.team_id.id
        for convert in self:
            convert.team_id = team_id
