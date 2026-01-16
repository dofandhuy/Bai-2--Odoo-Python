from odoo import models, fields, api
class RequestPurchase(models.Model):
    _name="purchase.request"
    _description ="Đơn yêu cầu đặt hàng"
    
    name = fields.Char(string='Số phiếu', required=True, copy=False, 
                       readonly=True, default='Mới')
    
    department_id= fields.Many2one('hr.department', String='Phòng ban', required= True, ondelete = 'restrict', help="Chọn phòng ban gửi yêu cầu mua hàng",  default=lambda self: self.env.user.employee_ids.department_id , readonly=True)

    request_id= fields.Many2one('res.users', String='Người đặt', required= True, ondelete = 'restrict', default=lambda self: self.env.user, readonly=True)

    approver_id= fields.Many2one('res.users', String='Người duyệt', required=False, ondelete = 'restrict',readonly=True)

    date = fields.Date(String='Ngày đặt',readonly=True)

    is_requester = fields.Boolean(compute='_compute_is_requester')
    date_approve = fields.Datetime(String='Ngày chấp thuận',readonly=True)
    description= fields.Text(string="Mô tả")
    cancel_reason=fields.Text(string="Lí do")
    state= fields.Selection([
        ('draft', 'Dự thảo'),
        ('wait', 'Chờ duyệt'),
        ('approved', 'Đã duyệt'),
        ('cancel', 'Hủy bỏ')
    ], string='Trạng thái', default='draft', tracking=True)

    request_line_ids = fields.One2many('purchase.request.line', 'request_id', string='Chi tiết yêu cầu')


    total_qty = fields.Float(string='Tổng số lượng', compute='_compute_totals', store=True)
    total_amount = fields.Float(string='Tổng tiền', compute='_compute_totals', store=True)
    def action_confirm(self):
        for rec in self:
            rec.state = 'wait'
            rec.date= fields.Date.today()

    
    def action_return(self):
        for rec in self:
               rec.state = 'draft'

            
    def action_approve(self):
        for rec in self:
            rec.state = 'approved'
            rec.date_approve= fields.Datetime.now()
            rec.approver_id=  self.env.user.id

    def action_cancel(self):

        return {
            'name': 'Nhập lý do từ chối',
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.request.cancel.wizard',
            'view_mode': 'form',
            'target': 'new', 'context': {'default_request_id': self.id},
            }
    

    @api.model
    def create(self, vals):
        if vals.get('name', 'Mới') == 'Mới':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.request') or 'Mới'
        return super(RequestPurchase, self).create(vals)
    

    @api.depends('request_line_ids.qty', 'request_line_ids.total')
    def _compute_totals(self):
        for rec in self:
            rec.total_qty = sum(line.qty for line in rec.request_line_ids)
            rec.total_amount = sum(line.total for line in rec.request_line_ids)
            
    @api.depends('request_id')
    def _compute_is_requester(self):
        for rec in self:
            # Nếu người đang log (uid) trùng với người tạo đơn (request_id)
            if rec.request_id.id == self.env.uid:
                rec.is_requester = True
            else:
                rec.is_requester = False