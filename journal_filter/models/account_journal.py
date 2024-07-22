from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.depends('company_id', 'invoice_filter_type_domain')
    def _compute_suitable_journal_ids(self):
        for move in self:
            company_id = move.company_id.id or self.env.company.id
            domain = [('company_id', '=', company_id)]
            move.suitable_journal_ids = self.env['account.journal'].search(domain)
