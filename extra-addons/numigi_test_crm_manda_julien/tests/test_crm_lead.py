from odoo.tests.common import TransactionCase
from datetime import datetime, timedelta

class TestCrmLead(TransactionCase):

    def setUp(self):
        super(TestCrmLead, self).setUp()
        self.CrmLead = self.env['crm.lead']
        self.CrmStage = self.env['crm.stage']
        self.MailMessage = self.env['mail.message']

        # Create a draft stage
        self.draft_stage = self.env.ref('crm.stage_lead1')

        # Create a team and team members
        self.team = self.env['crm.team'].create({'name': 'Sales Team'})

        self.user = self.env['res.users'].create({
            'name': 'Test User',
            'login': 'test_user',
            'email': 'test_user@example.com',
            'notification_type': 'email',
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
        })
        self.team.member_ids = [(4, self.user.id)]

        # Create an expired opportunity
        self.expired_opportunity = self.CrmLead.create({
            'name': 'Expired Opportunity',
            'stage_id': self.draft_stage.id,
            'create_date': datetime.now() - timedelta(days=11),
            'type': 'opportunity',
            'team_id': self.team.id,
        })

    def test_get_expired_opportunities(self):
        expired_opportunities = self.CrmLead._get_expired_opportunities()
        self.assertIn(self.expired_opportunity.id, expired_opportunities.ids, "The expired opportunity should be retrieved.")

    def test_send_notification(self):
        self.CrmLead._send_notification(self.expired_opportunity)
        messages = self.MailMessage.search([('model', '=', 'crm.lead'), ('res_id', '=', self.expired_opportunity.id)])
        self.assertIn(self.user.partner_id.id, messages[0].partner_ids.ids, "The notification should be sent to the team member.")
