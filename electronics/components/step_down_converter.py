from skidl import TEMPLATE, Part

Step_Down_XL4015_CCCV = Part(
    "Bobot_Custom_Library",
    "XL4015_CCCV_Module",
    dest=TEMPLATE,
    value="XL4015 5A CC/CV Buck Converter with Display",
    # Part source
    price_uah=264.60,
    buy_link="https://prom.ua/ua/p691700190-modul-dcdc-xl4015.html",
    # Electrical specs
    v_in_range=[8.0, 35.0],
    v_out_range=[1.25, 32.0],
    i_max_out_amp=5.0, # Note: Needs radiator above 3A
    # efficiency_percent=95,
    # Physical specs
    weight_g=-1,# Need to be specified
)
