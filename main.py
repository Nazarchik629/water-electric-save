import streamlit as st

# 1. Настройка страницы
st.set_page_config(page_title="Эко-Калькулятор Назара", page_icon="🌱")

# 2. Скрытие лишних элементов интерфейса (CSS стили)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            div[data-testid="stStatusWidget"] {display: none;}
            .stAppDeployButton {display: none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 3. Заголовок и оформление
st.title("🌱 Калькулятор экономии ресурсов")
st.subheader("Проект ученика 5 класса Солодовникова Назара")
st.markdown("---")

# 4. Боковая панель для настроек
st.sidebar.header("Настройки тарифа")
tarif = st.sidebar.number_input("Тариф Алматы (тенге за 1 кВт*ч):", value=25.0)

# 5. Основная часть: ввод данных
col1, col2 = st.columns(2)

with col1:
    st.write("### ⚡ Электричество")
    watt = st.number_input("Мощность прибора (Ватт):", min_value=0, value=100)
    hours = st.slider("Сколько часов в день выключен?", 0, 24, 5)
    
    # Расчет электричества
    daily_power = (watt / 1000) * hours * tarif
    st.info(f"Экономия в день: {round(daily_power, 2)} тенге")

with col2:
    st.write("### 💧 Вода")
    liters_per_min = st.number_input("Расход воды (литров/мин):", min_value=0, value=10)
    minutes = st.slider("Минут экономии в день:", 0, 60, 10)
    
    # Расчет воды (примерный тариф в Алматы ~55 тг за куб, 1 литр = 0.001 куба)
    # Используем коэффициент 0.055 для литров
    daily_water_money = (liters_per_min * minutes) * 0.055
    st.info(f"Экономия в день: {round(daily_water_money, 2)} тенге")

st.markdown("---")

import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- ФУНКЦИЯ ОТПРАВКИ (скрытая логика) ---
def send_auto_email(user_name, rating, user_text):
    # НАСТРОЙКИ (заполни здесь свои данные)
    sender_email = "solodovnikov.nazarchik.s@gmail.com"
    receiver_email = "solodovnikov.nazarchik.s@gmail.com"  # Куда придет письмо
    password = "zvdy hgbv imcd fnjg" # 16-значный код от Google

    # Текст письма
    subject = f"Новый отзыв: {rating} звезд от {user_name}"
    body = f"Имя пользователя: {user_name}\nОценка: {rating}/5\nОтзыв: {user_text}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        # Подключение к серверу Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except Exception as e:
        st.error(f"Ошибка при отправке: {e}")
        return False

# --- ИНТЕРФЕЙС САЙТА ---
st.header("Оставьте отзыв о проекте")

with st.form("feedback_form", clear_on_submit=True):
    name = st.text_input("Ваше имя")
    stars = st.select_slider("Оцените проект (из 5)", options=[1, 2, 3, 4, 5], value=5)
    comment = st.text_area("Ваш отзыв")
    
    submit = st.form_submit_button("Подтвердить")

if submit:
    if name and comment:
        with st.spinner("Отправка отзыва..."):
            success = send_auto_email(name, stars, comment)
            if success:
                st.success(f"Спасибо, {name}! Ваш отзыв успешно отправлен.")
                st.balloons()
    else:
        st.warning("Пожалуйста, заполните имя и текст отзыва.")

# 6. Блок расчетов и секретная формула
if st.button('Рассчитать итоги'):
    # Экономия воды в литрах
    saved_liters = liters_per_min * minutes
    # Экономия электричества в кВт
    saved_kwh = (watt / 1000) * hours
    
    # Прямая выгода (деньги)
    direct_money = daily_power + daily_water_money
    
    # Косвенная экономия (энергия города на перекачку воды)
    # На каждый 1 литр воды город тратит примерно 0.0005 кВт*ч
    indirect_kwh = saved_liters * 0.0005
    indirect_money = indirect_kwh * tarif
    
    total_result = direct_money + indirect_money
    
    st.header("📊 Итоги экономии")
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric("Прямая выгода (Ваш кошелек)", f"{round(direct_money, 2)} тг")
    with res_col2:
        st.metric("Эко-бонус (Энергия города)", f"{round(indirect_money, 4)} тг")
        
    st.success(f"🔥 Общая сумма экономии для Казахстана: {round(total_result, 2)} тенге в день!")
    
    st.info(f"💡 Знаете ли вы? Сэкономив {saved_liters} л воды, вы сберегли {round(indirect_kwh, 4)} кВт*ч электроэнергии, которую насосы Алматы не потратили на подачу воды.")

st.divider()

# 7. Итоговый результат за месяц
st.info("**Цель проекта:** Помочь жителям Алматы сократить потребление ресурсов.")
total_monthly = (daily_power + daily_water_money) * 30
st.success(f"### 📅 Итоговая экономия за месяц: {round(total_monthly, 2)} тенге")

st.write("💡 **Совет дня:** Замените одну лампу 100Вт на LED 12Вт, и вы начнете экономить сразу!")
