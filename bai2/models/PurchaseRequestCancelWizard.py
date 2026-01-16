from odoo import models, fields
class PurchaseRequestCancelWizard(models.TransientModel):
    _name="purchase.request.cancel.wizard"
    _description="Lý do từ chối"

    reason = fields.Text(string="Nhập lí do", required=True)
    request_id = fields.Many2one('purchase.request', string='Phiếu yêu cầu')
      
    def action_confirm_cancel(self):
        if self.request_id:
            self.request_id.write({
                'state': 'cancel',
                'cancel_reason': self.reason,
                'date_approve': fields.Datetime.now(),
                'approver_id': self.env.user.id
            })
        return {'type': 'ir.actions.act_window_close'}


