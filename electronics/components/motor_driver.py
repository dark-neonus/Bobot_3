from skidl import TEMPLATE, Part
from power_specs import PowerSpec, VoltageSpec, CurrentSpec, DeviceType

Motor_Driver = Part(
    "Bobot_Custom_Library",
    "BTS7960_Module_IBT2M",
    dest=TEMPLATE,
    value="BTS7960 43A Driver Module",
    # Part source
    price_uah="231.8",
    buy_link="https://prom.ua/ua/p1530387483-bts7960-drajver-kollektornogo.html",
    # Electrical specs
    power_specs=PowerSpec(VoltageSpec(6.0, 14.6, 27.0), CurrentSpec(10.0, 43.0, DeviceType.CONDUCTOR)),
    # Physical specs
    weight_g=80,
)
