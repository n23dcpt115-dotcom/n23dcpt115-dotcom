# Lab 08 – Testing ATM

## 1. Unit Test
- Hàm `verify_pin`: test PIN đúng, PIN sai.
- Hàm `withdraw`: test rút tiền thành công, không đủ tiền, số tiền không hợp lệ.
- Kết quả: tất cả pass ✅

## 2. Integration Test (Selenium)
- Login thành công với `admin/1234`.
- Login sai với password sai.
- Login với input rỗng.
- Kết quả: pass ✅

## 3. Ảnh minh họa
- ![unit-test](screenshots/unit-test.png)
- ![login-test](screenshots/login-test.png)

## 4. Kết luận
- Thực hành Unit test và Integration test thành công.
- Đảm bảo ATM module hoạt động đúng với yêu cầu.
