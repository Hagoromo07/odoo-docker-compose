from odoo.tests.common import TransactionCase

class TestCrmTeam(TransactionCase):

    def setUp(self):
        super(TestCrmTeam, self).setUp()
        self.CrmTeam = self.env['crm.team']
        self.ResUsers = self.env['res.users']

        # Create some users
        self.user1 = self.ResUsers.create({
            'name': 'User 1',
            'login': 'user1',
            'email': 'user1@example.com',
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
        })
        self.user2 = self.ResUsers.create({
            'name': 'User 2',
            'login': 'user2',
            'email': 'user2@example.com',
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
        })

        # Create a team and add members
        self.team = self.CrmTeam.create({
            'name': 'Sales Team',
            'member_ids': [(4, self.user1.id), (4, self.user2.id)],
        })

    def test_compute_emails(self):
        self.team._compute_emails()
        expected_email_number = len(self.team.emails.split(','))
        self.assertEqual(len(self.team.member_ids), expected_email_number, "The computed emails field should have the equal length of members.")

    def test_onchange_user_id(self):
        new_user = self.ResUsers.create({
            'name': 'New User',
            'login': 'new_user',
            'email': 'new_user@example.com',
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id])],
        })

        self.team.user_id = new_user
        self.team._onchange_user_id()

        self.assertIn(new_user.id, self.team.member_ids.ids, "The new user should be added to the team's members when selected as the team user.")

        # Ensure the emails field is updated correctly
        self.team._compute_emails()
        expected_emails = len(self.team.emails.split(','))
        self.assertEqual(len(self.team.member_ids), expected_emails, "The computed emails field should be updated to include the new user.")

