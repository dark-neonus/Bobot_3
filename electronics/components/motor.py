from skidl import TEMPLATE, Part

DC_Motor = Part(
    "Motor",
    "Motor_DC",
    ref="M",
    dest=TEMPLATE,
    value="JGB37-545 (12V)",
    # Part source
    price_uah=550.0,
    buy_link="https://prom.ua/ua/p2132897073-dvigatel-jgv37-545.html",
    # Motor specs
    torque_kg_cm=5,
    no_load_rpm=330,
    no_load_i_amp=0.2,
    load_rpm=280,
    load_i_amp=1,
    stall_i_amp=3.8,
    # Electrical specs
    v_in_range=[6.0, 24.0],
    i_max_in_amp=3.8,
    # Physical specs
    weight_g=300,
)
