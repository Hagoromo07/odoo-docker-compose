# -*- coding: utf-8 -*-
from odoo.http import request
from odoo.addons.website_crm.controllers.main import WebsiteForm

class WebsiteForm(WebsiteForm):
   
    def insert_record(self, request, model, values, custom, meta=None):
        if model.model == 'crm.lead':
            values['team_id'] = request.env.ref('numigi_test_crm_manda_julien.crm_team_sales').id

        return super(WebsiteForm, self).insert_record(request, model, values, custom, meta=meta)
    