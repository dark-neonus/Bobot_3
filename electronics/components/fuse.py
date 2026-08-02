from skidl import TEMPLATE, Part

Fuse_5A_Automotive = None
Fuse_10A_Automotive = None
Fuse_30A_Automotive = None

automotive_fuses = [
    (Fuse_5A_Automotive, 5),
    (Fuse_10A_Automotive, 10),
    (Fuse_30A_Automotive, 30),
]

for fuse, current_limit in automotive_fuses:
    fuse = Part(
    "Device",
    "Fuse",
    dest=TEMPLATE,
    value=f"Fuse {current_limit}A Automotive Mini Blade", #
    # Part source
    price_uah=0.00,
    buy_link="-1",
    footprint="Fuse:Fuse_Blade_Mini_SMD",
    # Electrical specs
    v_in_range=[0.0, 32.0],
    i_max_in_amp=float(current_limit), # Need to be specified
    # Physical specs
    weight_g=-1,# Need to be specified
)

Fuse_2A_Fast = None

fast_fuses = [
    (Fuse_2A_Fast, 2),
]

for fuse, current_limit in fast_fuses:
    fuse = Part(
    "Device",
    "Fuse",
    dest=TEMPLATE,
    value=f"Fuse {current_limit}A Fast",
    # Part source
    price_uah=0.00,
    buy_link="-1",
    footprint="Fuse:Fuse_Blade_Mini_SMD",
    # Electrical specs
    v_in_range=[0.0, 32.0],
    i_max_in_amp=float(current_limit), # Need to be specified
    # Physical specs
    weight_g=-1,# Need to be specified
)
