from skidl import Part, TEMPLATE

Battery_4S4P_20Ah = Part(
    "Bobot_Custom_Library",
    "Battery_4S4P_20Ah",
    dest=TEMPLATE,
    value="Battery 4S4P 20Ah",
    # Part source
    price_uah=4*4*135.0,
    buy_link="https://prom.ua/ua/m7985862593714244078-akumulyator-eve-inr.html",
    # Battery specs
    capacity_mah=4*5000,
    # Electrical specs
    v_out_range=[4*3.6, 4*4.2],
    i_max_out_amp=4*15.0,
    # Physical specs
    weight_g=4*4*69
)
