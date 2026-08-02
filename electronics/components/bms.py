from skidl import TEMPLATE, Part
from power_specs import PowerSpec, VoltageSpec, CurrentSpec, DeviceType

BMS_4S_40A = Part(
    "Bobot_Custom_Library",
    "BMS_4S_40A",
    dest=TEMPLATE,
    value="4S 40A Li-ion BMS (Common Port)",
    # Part source
    price_uah=59.0,
    buy_link="https://prom.ua/ua/p1061741339-bms-40a-168v.html",
    # Power specs
    power_specs=PowerSpec(VoltageSpec(4*3.0, 4*3.6, 4*4.2), CurrentSpec(40.0, 80.0, DeviceType.CONDUCTOR)),
    # Physical specs
    weight_g=-1,# Need to be specified
)
