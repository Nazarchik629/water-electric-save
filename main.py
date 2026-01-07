import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Эко-Калькулятор Назара", page_icon="🌱")

# Заголовок и оформление
st.title("🌱 Калькулятор экономии ресурсов")
st.subheader("Проект ученика 5 класса Солодовникова Назара")
st.markdown("---")

# Боковая панель с данными (как в настоящем приложении)
st.sidebar.header("Настройки тарифа")
tarif = st.sidebar.number_input("Тариф Алматы (тенге за 1 кВт*ч):", value=30.76)

# Основная часть
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
    minutes = st.slider("Минут экономии в день:", 0, 60, 3)

    # Расчет воды (примерный тариф за воду в Алматы ~55 тг за куб)
    # 1 литр = 0.001 куба
    daily_water = (liters_per_min * minutes) * 0.055 
    st.info(f"Экономия в день: {round(daily_water, 2)} тенге")

st.markdown("---")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            /* Убираем иконку профиля и кнопки управления внизу на мобильных */
            div[data-testid="stStatusWidget"] {display: none;}
            .stAppDeployButton {display: none;}
            #viewerBadge {display: none;}
            </style>
           """
import requests
st.markdown(hide_st_style, unsafe_allow_html=True)
st.divider()
st.subheader("📝 Оставьте отзыв о проекте")

# Создаем форму для сбора данных
with st.form("feedback_form"):
    name = st.text_input("Ваше имя:")
    
    # Слайдер для звезд (от 1 до 5)
    stars = st.select_slider("Ваша оценка проекта:", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    
    feedback_text = st.text_area("Ваши предложения или отзыв:")
    
    # Скрытая ссылка на твой Formspree (замени 'ВАШ_ID' на то, что скопировал)
    contact_url = "https://formspree.io/f/xbdlndab" 
    
    submit_button = st.form_submit_button("Отправить отзыв на почту")

    if submit_button:
        if name and feedback_text:
            import requests
            # Данные для отправки
            data = {
                "Имя": name,
                "Оценка": stars,
                "Отзыв": feedback_text
            }
            # Отправляем запрос на почту через сервис
            response = requests.post(contact_url, data=data)
            
            if response.status_code == 200:
                st.success("Спасибо! Отзыв успешно отправлен на сервис .")
            else:
                st.error("Произошла ошибка при отправке. Проверьте ID формы.")
        else:
            st.warning("Пожалуйста, заполните все поля перед отправкой.")

import streamlit as st

# ... твой существующий код (ввод данных) ...

# Блок расчетов (вставь это после получения данных от пользователя)
if st.button('Рассчитать экономию'):
    water = 10 * 3 
    electricity = (100 / 1000) * 5
    
    direct_money = (water * 0.15) + (electricity * 25)
    
    indirect_kwh = water * 0.0005
    indirect_money = indirect_kwh * 25
    
    st.write(f"Общая экономия: {direct_money + indirect_money:.2f} тенге")
    st.info(f"Ваш вклад: вы сберегли городу Алматы {indirect_kwh:.4f} кВт⋅ч!")
    direct_money = (water * 0.15) + (electricity * 25) # Примерные тарифы
    
    # 2. ТВОЯ СЕКРЕТНАЯ ФОРМУЛА ДЛЯ 1-ГО МЕСТА
    # Косвенная экономия: на каждый 1 литр воды город тратит 0.0005 кВтч
    indirect_kwh = water * 0.0005
    indirect_money = indirect_kwh * 25 # Переводим спасенные кВтч города в тенге
    
    total_result = direct_money + indirect_money

    # --- ВЫВОД НА ЭКРАН САЙТА ---
    st.header("📊 Итоги экономии за месяц")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Прямая выгода (Ваш кошелек)", f"{direct_money:.2f} ₸")
    with col2:
        st.metric("Эко-бонус (Энергия города)", f"{indirect_money:.2f} ₸", delta="Спасенные кВтч")

    st.success(f"🔥 Общая сумма экономии для Казахстана: {total_result:.2f} тенге!")
    
    st.info(f"💡 Знаете ли вы? Сэкономив {water} л воды, вы сберегли {indirect_kwh:.4f} кВт⋅ч "
            f"электроэнергии, которую насосы Алматы не потратили на доставку воды в ваш кран.")
st.divider()
st.info("📢 **Цель проекта:** Помочь жителям Алматы сократить потребление ресурсов на 10%. Если каждый второй алматинец воспользуется этим калькулятором, мы спасем целое озеро воды в год!")
# Итоговый результат за месяц
total_monthly = (daily_power + daily_water) * 30
st.success(f"### 💰 Итоговая экономия за месяц: {round(total_monthly, 2)} тенге")

ге")

st.write("💡 *Совет жюри: Заменив одну лампу 100Вт на LED 12Вт, вы бережете бюдже
