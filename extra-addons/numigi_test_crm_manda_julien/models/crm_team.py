# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    emails = fields.Char(string='Emails', compute='_compute_emails')

    @api.depends('member_ids.email')
    def _compute_emails(self):
        for team in self:
            team.emails = ', '.join(member.email for member in team.member_ids)

    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id and self.user_id.id not in self.member_ids.ids:
            self.member_ids |= self.user_id
