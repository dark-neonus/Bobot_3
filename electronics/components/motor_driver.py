from skidl import TEMPLATE, Part

Motor_Driver = Part(
    "Bobot_Custom_Library",
    "BTS7960_Module_IBT2M",
    dest=TEMPLATE,
    value="BTS7960 43A Driver Module",
    # Part source
    price_uah="231.8",
    buy_link="https://prom.ua/ua/p1530387483-bts7960-drajver-kollektornogo.html",
    # Driver specs
    v_in_range=[6.0, 27.0],
    i_max_in_amp=43.0,
    # Physical specs
    weight_g=80,
)
