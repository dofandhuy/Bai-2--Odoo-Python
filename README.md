Đề bài 02: Quản lý yêu cầu mua hàng
1. Module cần cài đặt: purchase,hr, product
2. Yêu cầu bài toán:
* Xây dựng bảng yêu cầu mua hàng từ các bộ phận
Model:
Purchase.request: Yêu cầu mua hàng
Department_id (m2o hr.department)
Request_id (m20 res.users)
Approver_id (m2o res.users)
Date (Date, default = today)
Date_approve
Request_line_ids (o2m purchase.request.line)
Description (Text)
State = Selection (draft,wait,approved,cancel) default draft
Total_qty (sum qty in purchase request line)
Total Amount (sum Total in purchase request line)

Purchase.request.line: Chi tiết yêu cầu mua hàng
Request_id (m2o purchase.request)
Product_id (m2o product.template)
Uom_id (m2o uom.uom)
Qty (float)
Qty_approve(float)
Total (float = qty * product_id.list_price)

Yêu cầu:
- Có menu quản lý yêu cầu mua hàng. Trên menu đó thì ch o phép thêm sửa xóa yêu cầu mua hàng.
- Chỉ cho phép xóa yêu cầu mua hàng khi ở trạng thái draft
- Ở trạng thái wait của yêu cầu mua hàng thif phép sửa số lượng phê duyệt qty_approve trong chi tiết yêu cầu mua hàng

- Chỉ được phép thêm chi tiết yêu cầu mua hàng ở trạng thái draft, các trạng thái khác thì ko được phép thêm hay xóa

- Có menu quản lý chi tiết yêu cầu mua hàng. Nhưng không được phép thêm, sửa, xóa
Yêu cầu khác:
- Các trường m2o trên view ko được phép thêm sửa
- 
Về giao diện như sau:
 


0. Nhóm quyền:
+ Quản lý 
+ Người dùng

1. Purchase request

+ Thêm trường name, name tự sinh theo cú pháp PR + 5 số tự sinh (tham khảo name trong purchase order, sequence)

+ Sắp xếp giao diện purchase request. 
status lên trên statusbar, 
+ Ở trạng thái draft có nút gửi yêu cầu (Người dùng)
+ ở trạng thái chờ phê duyệt có 3 nút: quay lại (Người dùng), phê duyệt (quản lý), từ chối (quản lý) . Khi từ chối thì nhập lý do từ chối tham khảo crm xác nhận thất bại 

+ Giao diện PR: edit trên form, required product, uom. Thay đổi nhãn cho đúng. 
+ Các trường m2o thì bỏ tạo mới và sửa
+ Ở trạng thái khác dự thảo thì không phép thêm sửa xóa chi tiết yêu cầu


+ Trường total qty, total amount tự động tính khi thêm mới purchase request line
+ Trong Purchase request line bổ sung thêm trường price_unit, khi lựa chọn sản phẩm thì tự động lấy ra đơn vị tính và lấy ra giá gần nhất có trong lịch sử bảng giá mua nhà cung cấp trong sheet mua hàng của sản phẩm 

+ MẶc định khi tạo PR yêu câu fmua hàng, thì lấy người tạo là người đang thao tác. lựa chọn phòng ban thì tự động lấy ra người phê duyệt
+ Mặc định phòng ban của người tạo

+ Trên form thông tin PR thì bắt buộc nhập các trường


+ Ở trạng thái draft thì cho phép xóa bản ghi 
+ Ở trạng thái khác thì ko cho phép xóa. Nếu xóa thì bắn ra thông báo: Bạn không được phép xóa ở trạng thái khác dự thảo


+ Ở trạng thái phê duyệt. cho phép xuất chi tiết yêu cầu mua hàng ra file excel. Template thì tự thiết kế ( SẢn phẩm gì, số lượng, đơn vị tính)

+ Phân quyền: Người dùng chỉ nhìn thấy bản ghi của người đó tạo. Người quản lý thì nhìn thấy những bản ghi của bản thân người quản lý và thêm danh sách nhân viên mà người quản lý quản lý.


