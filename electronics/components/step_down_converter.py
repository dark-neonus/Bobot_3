from skidl import TEMPLATE, Part
from power_specs import PowerSpec, VoltageSpec, CurrentSpec, DeviceType

Step_Down_XL4015_CCCV = Part(
    "Bobot_Custom_Library",
    "XL4015_CCCV_Module",
    dest=TEMPLATE,
    value="XL4015 5A CC/CV Buck Converter with Display",
    # Part source
    price_uah=249.99,
    buy_link="https://prom.ua/ua/p554802084-cccv-stabilizator-ponizhayuschij.html",
    # Electrical specs
    power_specs=PowerSpec(VoltageSpec(8.0, 14.6, 35.0), CurrentSpec(3.0, 5.0, DeviceType.CONDUCTOR)),

    v_in_range=[8.0, 35.0],
    v_out_range=[1.25, 32.0],
    i_max_out_amp=5.0, # Note: Needs radiator above 3A
    # efficiency_percent=95,
    # Physical specs
    weight_g=-1,# Need to be specified
)

Mini560_PRO_3V3 = Part(
    "Bobot_Custom_Library",
    "Mini560_PRO_3V3",
    dest=TEMPLATE,
    value="Mini560 Step Down 3.3V",
    # Part source
    price_uah=57.0,
    buy_link="https://prom.ua/ua/p2854711672-mini560-pro-stabilizator.html",
    # Electrical specs
    v_in_range=[7.0, 20.0],
    v_out_range=[3.3, 3.3],
    i_max_out_amp=4.0, # Note: Needs radiator above 3A
    # Physical specs
    weight_g=6,
)

Mini560_PRO_5V = Part(
    "Bobot_Custom_Library",
    "Mini560_PRO_5V",
    dest=TEMPLATE,
    value="Mini560 Step Down 5V",
    # Part source
    price_uah=54,
    buy_link="https://prom.ua/ua/p2692837436-plata-ponizhayuschego-stabilizatora.html",

    # Electrical specs
    v_in_range=[7.0, 32.0],
    v_out_range=[5.0, 5.0],
    i_max_out_amp=4.0, # Note: Needs radiator above 3A
    # Physical specs
    weight_g=6,
)
