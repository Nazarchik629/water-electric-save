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

# Данные для расчета
tariff_almaty = 28.0  # Тенге за 1 кВт*ч
households_almaty = 600000  # Примерное кол-во домохозяйств в Алматы

def calculate_savings(power_old, power_new, hours_per_day, days):
    # 1. Считаем экономию для одного пользователя (в тенге)
    watt_saved = power_old - power_new
    kwh_saved = (watt_saved * hours_per_day * days) / 1000
    money_saved = kwh_saved * tariff_almaty
    
    # 2. Считаем масштаб для ГОРОДА (если каждый заменит 1 лампу на 1 год)
    # 0.09 кВт (разница между 100Вт и 10Вт) * 5 часов * 365 дней * тариф * кол-во домов
    city_savings_year = (0.09 * 5 * 365 * tariff_almaty * households_almaty)
    city_billions = round(city_savings_year / 1_000_000_000, 1)
    
    return round(money_saved, 2), city_billions

# Пример использования:
old_w = 100  # Ватт старая лампа
new_w = 12   # Ватт LED лампа
h = 5        # Часов в день
d = 30       # Дней (месяц)

user_result, city_result = calculate_savings(old_w, new_w, h, d)


print(f"✅ Итоговая экономия за месяц: {user_result} тенге")
print("-" * 30)
print(f"🏛️ ПОЛЬЗА ДЛЯ ГОСУДАРСТВА:")
print(f"Если каждый алматинец заменит всего 1 лампу,")
print(f"наш любимый город сэкономит {city_result} МИЛЛИАРДА тенге в год!")

# Итоговая плашка
total_monthly = (daily_power + daily_water_money) * 30
st.success(f"### 🗓️ Итоговая экономия за месяц: {round(total_monthly, 2)} тенге")
st.write("💡 **Совет дня:** Замените одну лампу 100Вт на LED 12Вт, и вы начнете экономить сразу!")
