from skidl import TEMPLATE, Part
from power_specs import PowerSpec, VoltageSpec, CurrentSpec, DeviceType

DC_Motor = Part(
    "Motor",
    "Motor_DC",
    dest=TEMPLATE,
    value="JGB37-545 (12V)",
    # Part source
    price_uah=550.0,
    buy_link="https://prom.ua/ua/p2132897073-dvigatel-jgv37-545.html",
    # Motor specs
    torque_kg_cm=5,
    no_load_rpm=330,
    load_rpm=280,
    # Electrical specs
    power_specs=PowerSpec(VoltageSpec(6.0, 12.0, 24.0), CurrentSpec(1.2, 3.8, DeviceType.CONSUMER)),
    # Physical specs
    weight_g=300,
)
