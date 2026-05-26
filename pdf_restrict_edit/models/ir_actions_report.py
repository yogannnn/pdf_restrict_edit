import io
import logging
import secrets
from odoo import models

_logger = logging.getLogger(__name__)

try:
    from pypdf import PdfReader, PdfWriter, PdfPermissions
except ImportError:
    try:
        from PyPDF2 import PdfReader, PdfWriter
        PdfPermissions = None
    except ImportError:
        PdfReader = PdfWriter = None
        _logger.warning("pypdf / PyPDF2 not installed. PDF protection disabled.")

class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _get_owner_password(self):
        return self.env['ir.config_parameter'].sudo().get_param('pdf_restrict_edit.owner_password', '')

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        pdf_content, content_type = super()._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
        if not PdfWriter or content_type != 'pdf':
            return pdf_content, content_type
        owner_password = self._get_owner_password()
        if not owner_password:
            owner_password = secrets.token_urlsafe(24)
            _logger.info("Generated random owner password: %s", owner_password)
        try:
            reader = PdfReader(io.BytesIO(pdf_content))
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            if PdfPermissions is not None:
                permissions = PdfPermissions.PRINT | PdfPermissions.LOW_PRINT
            else:
                permissions = 4
            writer.encrypt(user_password="", owner_password=owner_password, use_128bit=True, permissions_flag=permissions)
            output = io.BytesIO()
            writer.write(output)
            return output.getvalue(), content_type
        except Exception:
            _logger.exception("PDF encryption failed for %s", report_ref)
            return pdf_content, content_type
