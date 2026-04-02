from odoo import models, api

class VisitReport(models.AbstractModel):
    _name = 'report.custom_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['custom_crm.visit'].browse(docids)
        
        return {
            'doc_ids': docids,
            'doc_model': 'custom_crm.visit',
            'docs': docs,
        }