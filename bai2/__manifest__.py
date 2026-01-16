{
    'name': "Bài 2",
    'summary': "Đáp án bài 2",
    'description': "yêu cầu đơn hàng, chi tiết đơn hàng",
    'author': "Đoàn Công Huy",
    'version': "1.0",
    'category': "Bài tập",
    'depends': ['purchase', 'hr', 'product', 'uom'],
    'data':
        [
            'security/request_purchase_security.xml',
            'security/ir.model.access.csv',
            'data/ir_sequence_data.xml',
            'views/request_purchase_views.xml',
            'views/cancel_reason_wizard_view.xml',
        ],
    'license': 'LGPL-3',
}
