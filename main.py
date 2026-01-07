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
st.markdown(hide_st_style, unsafe_allow_html=True)

# Расчет косвенной экономии электричества через воду
water_liters = float(input("Сколько литров воды вы сэкономили? "))
# 1 кВтч тратится на 2000 литров (0.0005 кВтч на 1 литр)
energy_indirect_saved = water_liters * 0.0005 

print(f"Сэкономив воду, вы также сберегли {energy_indirect_saved} кВт⋅ч электроэнергии на городских насосах!")

# Итоговый результат за месяц
total_monthly = (daily_power + daily_water) * 30
st.success(f"### 💰 Итоговая экономия за месяц: {round(total_monthly, 2)} тенге")

st.write("💡 *Совет жюри: Заменив одну лампу 100Вт на LED 12Вт, вы бережете бюджет!*")
