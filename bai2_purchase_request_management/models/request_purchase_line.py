from odoo import models, fields, api
class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Chi tiết yêu cầu mua hàng'


    request_id = fields.Many2one(
        'purchase.request', 
        string='Yêu cầu gốc', 
        ondelete='cascade', 
        index=True
    )

    product_id = fields.Many2one('product.template', string='Sản phẩm', required=True)
    uom_id = fields.Many2one('uom.uom', string='Đơn vị tính')
    
    qty = fields.Float(string='Số lượng đề xuất', default=1.0)
    qty_approve = fields.Float(string='Số lượng phê duyệt')
    
    total = fields.Float(
        string='Thành tiền', 
        compute='_compute_line_total', 
        store=True
    )

    @api.depends('qty', 'product_id.list_price')
    def _compute_line_total(self):
        for line in self:
            line.total = line.qty*(line.product_id.list_price or 0.0)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.uom_id = self.product_id.uom_id