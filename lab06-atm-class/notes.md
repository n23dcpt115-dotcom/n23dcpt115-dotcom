# Lab 06 – ATM Class & Package Diagram

## 1. Class Diagram
- Mô tả các lớp chính trong ATM:
  - ATM: quản lý giao dịch.
  - Card: thông tin thẻ.
  - Account: tài khoản.
  - Transaction: chi tiết giao dịch.
- Quan hệ: ATM liên kết với Card, Transaction; Card liên kết Account; Account liên kết Transaction.

## 2. Package Diagram
- **UI**: giao diện người dùng (ATMForm, TransactionForm).
- **Controller**: điều khiển luồng xử lý (ATMController, TransactionController).
- **BankService**: nghiệp vụ ngân hàng (AccountService, TransactionService).
- **Hardware**: phần cứng (CardReader, CashDispenser, ReceiptPrinter).

## 3. Kết luận
- Class Diagram và Package Diagram giúp mô tả chi tiết thiết kế.
- Đảm bảo tính mở rộng, phân tách rõ ràng giữa UI, logic, và phần cứng.
