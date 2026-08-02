from skidl import TEMPLATE, Part
from skidl import PowerSpec, VoltageSpec, CurrentSpec, DeviceType


def _create_fuse_template(value: str, current_limit: float):
    """Helper function to create a SKiDL template Part for fuses."""
    return Part(
        "Device",
        "Fuse",
        dest=TEMPLATE,
        value=value,
        # Part source
        price_uah=0.00,
        buy_link="-1",
        footprint="Fuse:Fuse_Blade_Mini_SMD",
        # Electrical specs
        power_specs=PowerSpec(VoltageSpec(0.0, 32.0), CurrentSpec(float(current_limit*0.9), float(current_limit), DeviceType.CONDUCTOR)),
        # Physical specs
        weight_g=-1,
    )

Fuse_5A_Automotive = _create_fuse_template("Fuse 5A Automotive", 5.0)
Fuse_10A_Automotive = _create_fuse_template("Fuse 10A Automotive", 10.0)
Fuse_30A_Automotive = _create_fuse_template("Fuse 30A Automotive", 30.0)

Fuse_2A_Fast = _create_fuse_template("Fuse 2A Fast", 2.0)
Fuse_3A_Fast = _create_fuse_template("Fuse 3A Fast", 3.0)
