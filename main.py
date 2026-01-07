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

import streamlit as st  # ИСПРАВЛЕНО: было impor as s
import smtplib
from email.mime.text import MIMEText

# --- ФУНКЦИЯ ОТПРАВКИ НА ПОЧТУ ---
def send_feedback_email(user_name, rating, user_text):
    sender_email = "solodovnikov.nazarchik.s@gmail.com" # Впиши свою почту
    receiver_email = "solodovnikov.nazarchik.s@gmail.com" # Сюда придет письмо
    password = "zvdy hgbv imcd fnjg" # Твой 16-значный код (который получишь в Google)

    subject = f"Zerde: Отзыв от {user_name} ({rating} звезд)"
    body = f"Имя: {user_name}\nОценка: {rating}/5\nОтзыв: {user_text}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except:
        return False

# --- ТВОЙ БЛОК РАСЧЕТОВ (исправленный) ---
st.markdown("---") # Разделительная линия
if st.button('Рассчитать итоги'): # ИСПРАВЛЕНО: было buttonutton
    # Тут твои формулы из кода
    st.write("Итоговые расчеты выполнены!")
    st.balloons()

# --- НОВЫЙ БЛОК: ОТЗЫВЫ (теперь кнопка появится!) ---
st.markdown("---")
st.header("⭐⭐⭐⭐⭐ Оставьте отзыв")

with st.form("feedback_form"):
    name = st.text_input("Ваше имя")
    stars = st.select_slider("Ваша оценка", options=[1, 2, 3, 4, 5], value=5)
    comment = st.text_area("Ваш комментарий")
    
    # Вот эта кнопка, которой у тебя не было:
    submit = st.form_submit_button("Подтвердить и отправить")

if submit:
    if name and comment:
        with st.spinner("Отправляем..."):
            if send_feedback_email(name, stars, comment):
                st.success(f"Спасибо, {name}! Отзыв отправлен Назару на почту.")
            else:
                st.error("Ошибка! Проверь настройки почты или пароль приложения.")
    else:
        st.warning("Пожалуйста, заполни все поля!")

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
