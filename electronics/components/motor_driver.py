from skidl import TEMPLATE, Part

Motor_Driver = Part(
    "Bobot_Custom_Library",
    "BTS7960_Module_IBT2M",
    dest=TEMPLATE,
    value="BTS7960 43A Driver Module",
    # Part source
    price_uah="193.5",
    buy_link="https://prom.ua/ua/m-8558366577709891752-drajver-motorov-odnokanalnyj.html",
    # Driver specs
    v_in_range=[6.0, 27.0],
    i_max_in_amp=43.0,
)
