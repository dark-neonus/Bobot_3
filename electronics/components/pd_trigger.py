from skidl import TEMPLATE, Part
from power_specs import PowerSpec, VoltageSpec, CurrentSpec, DeviceType

PD_Trigger_20V = Part(
    "Bobot_Custom_Library",
    "PD_Trigger_20V",
    dest=TEMPLATE,
    value="USB-C PD 20V Decoy Trigger",
    # Part source
    price_uah=28.0,
    buy_link="https://prom.ua/ua/p2510013050-trigger-usb-plata.html",
    # Electrical specs
    power_specs=PowerSpec(VoltageSpec(5.0, 20.0), CurrentSpec(3.0, 5.0, DeviceType.CONDUCTOR)),
    v_in_range=(5.0, 20.0),
    v_out=20.0,
    i_max_out_amp=5.0,
    # Physical specs
    weight_g=-1,# Need to be specified
)
