# Lab 03 – Sequence Diagram for Withdraw Money

## 1. Use Case chọn: Withdraw Money
- Actor: Customer, Bank System.
- Mô tả: Khách hàng rút tiền từ tài khoản qua ATM.

## 2. Các đối tượng trong Sequence Diagram
- **Customer**: người dùng ATM.
- **ATM UI**: giao diện nhập PIN, số tiền.
- **ATM Controller**: xử lý logic ATM.
- **Bank System**: xác thực PIN, kiểm tra số dư, trừ tiền.
- **Cash Dispenser**: phát tiền cho khách.

## 3. Luồng thông điệp chính
1. Customer nhập PIN → UI → Controller → Bank.
2. Bank xác thực thành công.
3. Customer chọn rút tiền → UI → Controller.
4. Controller gọi Bank để trừ tiền.
5. Bank xác nhận giao dịch.
6. Controller kích hoạt CashDispenser → nhả tiền.
7. UI báo thành công, transaction được ghi lại.

## 4. Diagram
- Use Case: `usecase-withdraw.png`
- Sequence Diagram: `sequence-withdraw.png`
