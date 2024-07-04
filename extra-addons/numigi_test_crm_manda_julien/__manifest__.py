# -*- coding: utf-8 -*-
{
    'name': "numigi_test_crm_manda_julien",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Manda Julien",
    'website': "http://www.yourcompany.com",
    'category': 'CRM',
    'version': '0.1',
    'depends': ['crm', 'website_crm', 'sales_team'],
    'data': [
        'data/crm_team_data.xml',
        'data/res_config_settings_data.xml',
        'data/scheduled_cron_action.xml',
        'views/crm_team_view.xml',
        'views/crm_lead_view.xml',
    ],
    'demo': [],
}
