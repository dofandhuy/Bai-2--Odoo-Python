from odoo import models, fields


class PurchaseRequestCancelWizard(models.TransientModel):
    _name = "purchase.request.cancel.wizard"
    _description = "Lý do từ chối"

    reason = fields.Text(string="Nhập lí do", required=True)

    def action_confirm_cancel(self):
        request_ids = self.env.context.get('active_ids')
        requests = self.env['purchase.request'].browse(request_ids)
        for req in requests:
            if req.state != 'approved':
                req.write({
                    'state': 'cancel',
                    'cancel_reason': self.reason
                })
