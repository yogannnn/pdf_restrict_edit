from odoo import fields, models, api

class PdfSettings(models.TransientModel):
    _name = 'pdf.settings'
    _description = 'PDF Protection Settings'

    password = fields.Char(string='Master Password for PDFs', help='Leave empty to generate random', password=True)
    is_password_set = fields.Boolean(string='Password is set', compute='_compute_is_password_set', readonly=True)

    def _compute_is_password_set(self):
        current_password = self.env['ir.config_parameter'].sudo().get_param('pdf_restrict_edit.owner_password', '')
        self.is_password_set = bool(current_password)

    def action_save(self):
        self.env['ir.config_parameter'].sudo().set_param('pdf_restrict_edit.owner_password', self.password or '')
        return {'type': 'ir.actions.act_window_close'}
