from odoo.tests import common

class TestCrmModule(common.TransactionCase):

    def setUp(self):
        super(TestCrmModule, self).setUp()
        self.crm_team_model = self.env['crm.team']
        self.crm_lead_model = self.env['crm.lead']
        self.user_model = self.env['res.users']
        self.partner_model = self.env['res.partner']

        self.user = self.user_model.create({
            'name': 'Test User',
            'login': 'testuser',
            'email': 'testuser@example.com',
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id])]
        })
        self.team = self.crm_team_model.create({
            'name': 'Test Team',
            'user_id': self.user.id
        })

    def test_add_emails_to_team(self):
        """ Test if emails are correctly aggregated for team members """
        member1 = self.user_model.create({'name': 'Member 1', 'email': 'member1@example.com'})
        member2 = self.user_model.create({'name': 'Member 2', 'email': 'member2@example.com'})
        self.team.write({'member_ids': [(4, member1.id), (4, member2.id)]})
        self.assertEqual(self.team.emails, 'member1@example.com, member2@example.com')

    def test_team_leader_in_members(self):
        """ Test if team leader is automatically added to members """
        self.team.write({'user_id': self.user.id})
        self.assertIn(self.user, self.team.member_ids)

    def test_create_teams_from_data(self):
        """ Test if predefined teams are created """
        self.assertTrue(self.env.ref('your_module.crm_team_support'))
        self.assertTrue(self.env.ref('your_module.crm_team_sales'))
        self.assertTrue(self.env.ref('your_module.crm_team_sav'))

    def test_draft_opportunity_notification(self):
        """ Test if notification is sent for draft opportunities older than 10 days """
        opportunity = self.crm_lead_model.create({
            'name': 'Test Opportunity',
            'team_id': self.team.id,
            'create_date': fields.Datetime.now() - timedelta(days=11)
        })
        opportunity._check_draft_opportunities()
        # Assuming a mail.mail is created for the notification
        mails = self.env['mail.mail'].search([('subject', 'ilike', 'Test Opportunity')])
        self.assertTrue(mails)

    def test_expected_revenue_visibility(self):
        """ Test if expected revenue field is visible only to sales managers """
        sales_manager_group = self.env.ref('sales_team.group_sale_manager')
        self.user.write({'groups_id': [(6, 0, [sales_manager_group.id])]})
        view = self.env.ref('crm.crm_case_form_view_oppor')
        fields = view.fields_get()
        self.assertIn('expected_revenue', fields)
        self.user.write({'groups_id': [(3, sales_manager_group.id)]})
        fields = view.fields_get()
        self.assertNotIn('expected_revenue', fields)

    def test_default_team_on_webform(self):
        """ Test if default sales team is assigned on webform submission """
        form = self.env['website_form'].create({
            'model_name': 'crm.lead',
            'team_id': None,
        })
        form.create({})
        lead = self.crm_lead_model.search([], order='id desc', limit=1)
        self.assertEqual(lead.team_id, self.env.ref('your_module.crm_team_sales'))
