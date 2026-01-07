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

# --- 1. ТВОЯ ФУНКЦИЯ ОТПРАВКИ (Вставь свой 16-значный код сюда!) ---
def send_feedback_email(user_name, rating, user_text):
    sender_email = "solodovnikov.nazarchik.s@gmail.com" 
    receiver_email = "solodovnikov.nazarchik.s@gmail.com" 
    password = "sgpw hfta ritp nswe" # Сюда 16 букв от Google
    
    msg = MIMEText(f"Имя: {user_name}\nОценка: {rating}/5\nОтзыв: {user_text}")
    msg['Subject'] = f"Zerde: Отзыв от {user_name}"
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return True
    except:
        return False

# --- 2. БЛОК РАСЧЕТОВ И СЕКРЕТНАЯ ФОРМУЛА ---
st.divider()
if st.button('Рассчитать итоги', key="final_calc_button"):
    # Секретные расчеты
    saved_liters = liters_per_min * minutes
    saved_kwh = (watt / 1000) * hours
    direct_money = daily_power + daily_water_money
    
    # Секретная формула (энергия города на перекачку воды)
    indirect_kwh = saved_liters * 0.0005
    indirect_money = indirect_kwh * 25 # Тариф Алматы
    total_result = direct_money + indirect_money
    
    st.header("📊 Итоги экономии")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Прямая выгода", f"{round(direct_money, 2)} тг")
    with col2:
        st.metric("Эко-бонус (энергия города)", f"{round(indirect_money, 4)} тг")
        
    st.success(f"🔥 Общая сумма экономии для Казахстана: {round(total_result, 2)} тенге в день!")
    st.info(f"💡 **Секретный факт:** Чтобы подать вам {saved_liters} л воды, насосы Алматы тратят {round(indirect_kwh, 4)} кВт*ч. Экономя воду, вы экономите свет всего города!")
    st.balloons()

# --- 3. КНОПКА ОТЗЫВА (ПОСЛЕ РАСЧЕТА) ---
st.write("") # Отступ
with st.expander("💬 Оставить отзыв о проекте (Назару на почту)"):
    with st.form("unique_feedback_form", clear_on_submit=True):
        f_name = st.text_input("Ваше имя")
        f_stars = st.select_slider("Оценка", options=[1, 2, 3, 4, 5], value=5)
        f_comment = st.text_area("Ваш отзыв")
        submit_feedback = st.form_submit_button("Подтвердить и отправить")

    if submit_feedback:
        if f_name and f_comment:
            if send_feedback_email(f_name, f_stars, f_comment):
                st.success("Спасибо! Отзыв улетел на почту.")
            else:
                st.error("Ошибка! Проверь пароль приложения.")

# --- 4. ЦЕЛЬ ПРОЕКТА (ЖИРНО И СО СМАЙЛИКОМ) ---
st.write("")
st.info("🎯 **ЦЕЛЬ ПРОЕКТА: Помочь жителям Алматы сократить потребление ресурсов и беречь природу нашего Казахстана!**")

def calculate_city_saving():
    # Данные для расчета (примерные для Алматы)
    num_households = 600000  # Кол-во квартир/домов
    old_lamp_watt = 100      # Обычная лампа
    led_lamp_watt = 10       # LED лампа
    hours_per_day = 5        # Сколько часов в среднем горит свет
    almaty_tariff = 28       # Средний тариф в тенге за кВт*ч (на 2026 год)
    
    # Расчет экономии в час на одну лампу (в кВт)
    saving_per_hour_kw = (old_lamp_watt - led_lamp_watt) / 1000
    
    # Экономия всего города за год (в тенге)
    city_saving_year = saving_per_hour_kw * hours_per_day * 365 * num_households * almaty_tariff
    
    # Округляем до миллиардов
    billions = city_saving_year / 1_000_000_000
    return round(billions, 2)

print(f" ⚡Если каждый алматинец заменит 1 лампу, город сэкономит {calculate_city_saving()} млрд тенге в год!")

# Итоговая плашка
total_monthly = (daily_power + daily_water_money) * 30
st.success(f"### 🗓️ Итоговая экономия за месяц: {round(total_monthly, 2)} тенге")
st.write("💡 **Совет дня:** Замените одну лампу 100Вт на LED 12Вт, и вы начнете экономить сразу!")
