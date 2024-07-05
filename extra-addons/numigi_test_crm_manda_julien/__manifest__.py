# -*- coding: utf-8 -*-
{
    'name': "CRM Customizations",

    'summary': """
        Create an Odoo CRM module that consolidates team member emails, includes team leaders automatically, forms dedicated sales teams, 
        sends notifications for stagnant opportunities, restricts "Expected Revenue" visibility to administrators, and assigns default web leads.
    """,

    'description': """
        Develop a custom Odoo module for the CRM to add a consolidated emails field 
        for team members and automatically include the team leader among the members. 
        Create three specific sales teams, set up notifications for stagnant opportunities, 
        make the "Expected Revenue" field visible only to sales administrators, 
        and assign web-generated leads to a default sales team.
    """,

    'author': "Manda Julien",
    'website': "https://numigi.com/",
    'category': 'CRM',
    'version': '14.0.0.1',
    'depends': ['crm', 'website_crm', 'sales_team'],
    'data': [
        'data/crm_team_data.xml',
        'data/res_config_settings_data.xml',
        'data/scheduled_cron_action.xml',
        'views/crm_team_view.xml',
        'views/crm_lead_view.xml',
    ],
    'demo': [],
    'license': 'LGPL-3',
}
