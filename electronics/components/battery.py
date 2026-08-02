from skidl import Part, TEMPLATE
from power_specs import PowerSpec, VoltageSpec, CurrentSpec, DeviceType

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
    # Power specs
    power_specs=PowerSpec(VoltageSpec(4*3.0, 4*3.6, 4*4.2), CurrentSpec(4*5.0, 4*15.0, DeviceType.SUPPLY)),
    # Physical specs
    weight_g=4*4*69
)
