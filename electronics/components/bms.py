from skidl import TEMPLATE, Part

BMS_4S_40A = Part(
    "Bobot_Custom_Library",
    "BMS_4S_40A",
    dest=TEMPLATE,
    value="4S 40A Li-ion BMS (Common Port)",
    # Part source
    price_uah=59.0,
    buy_link="https://prom.ua/ua/p1061741339-bms-40a-168v.html",
    # Electrical specs
    v_charge_max=16.8,
    i_max_out_amp=40.0,
    balancing_current_ma=100,
    # Physical specs
    weight_g=-1,# Need to be specified
)
