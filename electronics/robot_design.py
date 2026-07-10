from components.battery import Battery_Cell
from components.fuse import Fuse_10A
from components.motor import DC_Motor
from components.motor_driver import Motor_Driver
from skidl import Net, Group
from config_loader import load_config

def build_battery_pack(net_gnd, net_vbat_raw):
    """
    Dynamically generates and wires an SxP battery pack.

    - Organizes cells inside a 2D Python list: batteries[s_series][p_parallel]
    - Chains parallel blocks in series.
    - Exposes intermediate balance taps for BMS routing.
    """
    # 1. Pull battery configuration parameters safely from our TOML config
    bat_cfg = load_config()["battery"]

    S = bat_cfg["cells_in_series"]
    P = bat_cfg["cells_in_parallel"]

    series_nodes = [net_gnd]
    for i in range(1, S):
        series_nodes.append(Net(f"BAT_BAL_TAP_{i}"))
    series_nodes.append(net_vbat_raw)

    batteries = []

    # We group each series tier. netlistsvg renders each group as a separate physical block.
    for s in range(S):
        row = []
        # Group name format e.g., 'Series_Tier_1'
        with Group(f"Series_Tier_{s+1}"):
            for p in range(P):
                cell_ref = f"CELL_S{s+1}_P{p+1}"
                cell = Battery_Cell(ref=cell_ref)

                # Connect terminals inside the group context
                cell[1] += series_nodes[s + 1] # Positive
                cell[2] += series_nodes[s]     # Negative
                row.append(cell)
        batteries.append(row)

    # Return balance taps in case you want to route them to a BMS later
    return {
        "pos": net_vbat_raw,
        "neg": net_gnd,
        "balance_taps": series_nodes[1:-1],
        "matrix": batteries  # Returned so you can easily run tests on individual cells
    }

def build_robot_circuit():
    """Constructs the high-power dual motor drive architecture of the robot."""


    # 1. Define Global Networks
    gnd = Net("GND")
    vbat_raw = Net("VBAT_RAW")
    vbat_fused = Net("VBAT_FUSED")
    v_5v = Net("5V_LOGIC")  # 5V logic supply for BTS7960 and microcontrollers

    # 2. Build the battery pack
    batt = build_battery_pack(gnd, vbat_raw)

    drv_L = Motor_Driver(ref="MOD1")
    drv_R = Motor_Driver(ref="MOD2")

    mot_L = DC_Motor(ref="M1")
    mot_R = DC_Motor(ref="M2")

    batt["pos"] += drv_L["B+"]
    batt["neg"] += drv_L["B-"]

    batt["pos"] += drv_R["B+"]
    batt["neg"] += drv_R["B-"]

    drv_L["M+"] += mot_L["+"]
    drv_L["M-"] += mot_L["-"]
    drv_R["M+"] += mot_R["+"]
    drv_R["M-"] += mot_R["-"]
