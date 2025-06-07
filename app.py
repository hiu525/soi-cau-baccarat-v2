import streamlit as st
import pandas as pd

# Cấu hình giao diện tối ưu cho mobile
st.set_page_config(page_title="Soi cầu Baccarat", layout="centered")

st.title("🔮 Soi cầu Baccarat thông minh")

# --- Nhập kết quả mới (chính giữa) ---
st.subheader("🎯 Nhập kết quả mới")
if "history" not in st.session_state:
    st.session_state.history = []

col1, col2 = st.columns([2, 1])
with col1:
    new_result = st.text_input("Kết quả (P/B/T):", max_chars=1)
with col2:
    if st.button("➕ Thêm"):
        if new_result.upper() in ["P", "B", "T"]:
            st.session_state.history.append(new_result.upper())
            st.success(f"✅ Đã thêm: {new_result.upper()}")
        else:
            st.error("⚠️ Chỉ nhập: P / B / T")

# --- Bộ lọc ---
st.subheader("🔎 Lọc kết quả")
filter_option = st.radio("Hiển thị:", ["Tất cả", "Chỉ P", "Chỉ B", "Chỉ T"], horizontal=True)

def filter_history(history, option):
    if option == "Tất cả":
        return history
    elif option == "Chỉ P":
        return [x for x in history if x == "P"]
    elif option == "Chỉ B":
        return [x for x in history if x == "B"]
    elif option == "Chỉ T":
        return [x for x in history if x == "T"]
    return history

filtered_history = filter_history(st.session_state.history, filter_option)

# --- Lịch sử kết quả ---
st.subheader("📜 Lịch sử")
st.markdown(f"Tổng: **{len(filtered_history)}** kết quả")
st.write("➡️ " + " - ".join(filtered_history) if filtered_history else "Chưa có kết quả")

# --- Dự đoán thông minh ---
st.subheader("🤖 Dự đoán thông minh")

def smart_predict(history):
    if len(history) < 3:
        return "Chưa đủ dữ liệu"
    recent = history[-3:]
    if recent.count("P") >= 2:
        return "🔵 Dự đoán: **B**"
    elif recent.count("B") >= 2:
        return "🔴 Dự đoán: **P**"
    else:
        return "🟡 Dự đoán: **P hoặc B**"

if st.button("📈 Dự đoán tiếp theo"):
    result = smart_predict(st.session_state.history)
    st.info(result)
else:
    st.info("⏳ Nhấn nút để dự đoán...")

# --- Ghi chú ---
st.subheader("📝 Ghi chú của bạn")
note = st.text_area("Viết ghi chú tại đây...")
if st.button("💾 Lưu ghi chú"):
    st.success("✅ Ghi chú đã lưu (tạm thời)")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 by bạn & ChatGPT – Mobile friendly UI")
