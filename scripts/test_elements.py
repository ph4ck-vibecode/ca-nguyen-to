#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kiểm thử tự động cho mô hình "Cá Nguyên Tố".
Dùng trước & sau mỗi lần chỉnh sửa file HTML để chắc chắn không làm vỡ dữ liệu.

Cách chạy (tại thư mục gốc dự án):
    python3 scripts/test_elements.py

Trả về mã thoát 0 nếu mọi kiểm định ĐẠT — mỗi điểm phải ÉP "cá không dư / thiếu nguyên tố nào".
"""
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "element-fish.html"
problems = []
passed = []


def check(name, ok, detail=""):
    (passed if ok else problems).append(f"{'✔' if ok else '✘'} {name}" + (f" — {detail}" if detail else ""))


def main():
    src = SRC.read_text(encoding="utf-8")

    # ── 1. Dữ liệu 118 nguyên tố ──────────────────────────────────────────────
    m = re.search(r"const EL = \[(.*?)\n\];", src, re.S)
    check("Có mảng dữ liệu const EL", bool(m))
    if not m:
        return finish()

    entries = re.findall(r'\["(\w{1,3})","([^"]+)","([^"]+)"\]', m.group(1))
    symbols = [e[0] for e in entries]

    check("Đủ 118 nguyên tố", len(entries) == 118, f"thấy {len(entries)}")
    check("Không có ký hiệu trùng lặp", len(set(symbols)) == len(symbols))
    check("Không có tên trùng lặp", len({e[1] for e in entries}) == len(entries))

    # ký hiệu phải bắt đầu bằng chữ in hoa
    check("Mọi ký hiệu đúng quy cách", all(re.fullmatch(r"[A-Z][a-z]?", s) for s in symbols))

    # ── 2. Mỗi nguyên tố phải được xếp vào một ô (không thiếu, không dư) ──
    mz = re.search(r"const ZONES = \[[\s\S]*?\n \]\}\n\];", src)
    check("Có ma trận toạ độ ZONES", bool(mz))
    if mz:
        placed = re.findall(r'"([A-Z][a-z]?)"', mz.group(0))
        missing = sorted(set(symbols) - set(placed))
        surfaced = sorted(set(placed) - set(symbols))
        check("Mỗi nguyên tố xuất hiện đúng 1 lần trên hình",
              not missing and not surfaced and len(placed) == 118,
              f"thiếu={missing or '∅'} lạ={surfaced or '∅'} count={len(placed)}")

        # ── 3. Kiểm tra cấu trúc vùng cơ thể ──
        rows = re.findall(r'\{key:"body-r([1-4])", type:"body", y:(\d+), cards:\[(.*?)\]\}', mz.group(0))
        check("Thân chính có đủ 4 hàng × 12 ô", len(rows) == 4 and all(len(r[2].split(",")) == 12 for r in rows),
              "hàng: " + ", ".join(f"{r[0]}→y{r[1]}" for r in rows) if rows else "")

    # ── 4.Không sót dữ liệu tooltip / vùng (META) ──
    check("Có bảng mô tả vùng META", 'const META = {' in src and "Đuôi Quạt" in src)

    # ── 5. Dự án tiếng Việt ──
    check('Khai báo lang="vi"', 'lang="vi"' in src or 'lang="vi"' in src)
    check("Không sót dòng UI tiếng Anh gốc",
          not re.search(r"(Hover any element|Series Marker|Build Stats|click the marker again)", src))

    return finish()


def finish():
    print("\n════════ KIỂM THỬ CÁ NGUYÊN TỐ ════════")
    for p in passed:
        print("  " + p)
    if problems:
        print("\n  ── LỖI CẦN SỬA ──")
        for p in problems:
            print("  " + p)
        print(f"\nKết quả: {len(passed)} đạt / {len(problems)} LỖI ❌\n")
        sys.exit(1)
    print(f"\nKết quả: {len(passed)} đạt / 0 lỗi ✅ Ổn định, cứ vậy commit!\n")
    sys.exit(0)


if __name__ == "__main__":
    main()
