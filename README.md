# 🐟 Cá Nguyên Tố — Bảng Tuần Hoàn Hóa Học

Một trang web **một tệp duy nhất** (`index.html`): toàn bộ **118 nguyên tố hóa học** được tạc nên hình một chú cá, đúng vị trí giải phẫu:

| Vùng trên cá | Nguyên tố | Phong cách |
|---|---|---|
| 🧠 Đầu & Mõm (trái) | H–Ar (1–18) | Ô lục giác tổ ong màu bạc/xám |
| 🫁 Thân chính (giữa, 4×12) | K–Zn, Rb–Cd, Cs–Hg (kèm ô `*`), Fr–Cn (kèm ô `**`) | Xanh sáng → xám xanh → navy |
| 🐠 Vây lưng thứ nhất | Ga–Kr (31–36) | Chóp tam giác màu xanh ngọc |
| 🐠 Vây lưng thứ hai | In–Xe (49–54) | Vây nhỏ sát gốc đuôi |
| 🐠 Vây bụng trước | Tl–Rn (81–86) | Chỉ xuống dưới, màu xám |
| 🐠 Vây hậu môn | Nh–Og (113–118) | Tam giác lớn hướng xuống |
| 🌊 Đuôi quạt (phải) | La–Lu (57–71) & Ac–Lr (89–103) | Thùy trên lantan, thùy dưới actini, xoay dần tạo hình quạt |

---

## ✨ Tính năng

- **Di chuột** lên ô nguyên tố → tooltip nổi: tên đầy đủ, số hiệu nguyên tử, khối lượng nguyên tử, tên vùng.
- **Bấm** vào ô nguyên tố → bảng thông tin cơ bản khóa ở panel "Bảng tra cứu": số hiệu, chu kỳ, phân loại (s/p/d/f, kim loại kiềm, halogen…), vị trí trên mô hình.
- **Bấm** ô `*` / `**` trên thân → tô sáng cả thùy đuôi lantan / actini (bấm lần nữa để mở khóa, phím `Esc` để thoát).
- 🥚 **Trứng phục sinh:** bấm vào **mắt cá** để nó bốc chuyện!
- Bọt nước nổi lên, cá bồng lềnh, mắt tự nhìn quanh, tương thích thu nhỏ theo màn hình.

---

## 🚀 Chạy cục bộ

Không cần cài gì — chỉ mở tệp:

```bash
# Windows/macOS/Linux: nhấp đúp index.html, hoặc:
python3 -m http.server 8000     # rồi mở http://localhost:8000/
```

> Trang dùng Tailwind qua CDN khi có mạng; mọi logic dữ liệu đều chạy cục bộ.

---

## 📋 Nguyên tắc dự án (bắt buộc tuân thủ)

### 1️⃣ Kiểm thử & gỡ lỗi liên tục bằng chụp màn hình

Sau **mỗi** thay đổi, chụp lại màn hình để so sánh trực quan bản cũ/bản mới:

```bash
# Chrome/Edge headless (không cần mở cửa sổ trình duyệt):
chrome --headless=new --screenshot=shots/vuon-ket-qua.png --window-size=1440,1200 \
       "file://$(pwd)/index.html"

# Vòng lặp gợi ý: sửa → chụp → xem bảng so sánh → chốt
```

Xem nhanh các ảnh chụp đã lưu trong `shots/` để đối chiếu trực quan từng phiên bản.

### 2️⃣ Bấm để xem thông tin nguyên tố

Mọi ô nguyên tố đều bấm được và hiện thông tin cơ bản ngay trong panel bên dưới mô hình (nhắc trong code: hàm `fish.addEventListener("click", …)`).

### 3️⃣ Giao diện 100% tiếng Việt

`<html lang="vi">`, toàn bộ tooltip/mô tả/panel bằng tiếng Việt. Khi thêm nội dung mới, **văn bản hiển thị cho người dùng phải là tiếng Việt** (tên biến trong code vẫn dùng tiếng Anh được).

### 4️⃣ Dùng Git để lưu phiên bản

Commit **sau mỗi thay đổi đáng kể** để không bao giờ mất trạng thái chạy tốt:

```bash
git add -A
git commit -m "feat: mô tả ngắn gọn thay đổi"   # feat: / fix: / docs: / style: / test:
git tag v0.x.y                                  # đánh dấu phiên bản chạy tốt
```

Nếu hỏng nặng: `git checkout v0.x.y -- index.html` để quay lại bản tốt cuối.

---

## 🧪 Kiểm thử tự động (tra cứu không lỗi dữ liệu)

```bash
python3 scripts/test_elements.py
```

Kiểm 11 điều kiện: đủ 118 nguyên tố, không trùng ký hiệu/tên, mỗi nguyên tố vừa đúng 1 ô trên hình, thân chính 4×12, lang="vi", không sót chữ UI tiếng Anh. **Chỉ commit khi script báo `0 lỗi`.**

---

## 📤 Đưa lên GitHub

```bash
git init -b main                          # nếu chưa
git add -A
git commit -m "feat: cá nguyên tố bản đầu tiên"
# Tạo repo rỗng trên github.com rồi:
git remote add origin https://github.com/<tên-bạn>/ca-nguyen-to.git
git push -u origin main
```

## ▲ Triển khai lên Vercel

Đây là trang **tĩnh**, không cần build:

- **Cách 1 (Dashboard):** [vercel.com/new](https://vercel.com/new) → Import repo → Framework Preset: **Other** → Build Command: *(để trống)* → Output Directory: `./` → Deploy.
- **Cách 2 (CLI):** `npm i -g vercel && vercel --prod`

Vercel tự deploy lại mỗi lần `git push` lên `main`. Tùy đổi tên miền tại Project → Settings → Domains.

---

## 🗂️ Cấu trúc thư mục

```
.
├── index.html        # toàn bộ ứng dụng (HTML + CSS + JS)
├── scripts/
│   └── test_elements.py     # kiểm thử dữ liệu trước mỗi commit
├── shots/                   # ảnh chụp màn hình kiểm thử (bỏ qua trong Git)
├── .gitignore
└── README.md
```

## 🗺️ Ghi chú kỹ thuật

- Toạ độ từng ô nằm trong hằng số `ZONES` (canvas 1200×640, cá facing trái).
- Dữ liệu 118 nguyên tố: mảng `EL` (ký hiệu, tên, khối lượng).
- Màu phân vùng: class `.row1–.row4`, `.dorsal`, `.ventral`, `.lan`, `.act`, `.hexy` (đầu).
- Tooltip: `#tip` · Panel thông tin: `#inspector` · Trứng phục sinh: `#eye` + `#speech`.
