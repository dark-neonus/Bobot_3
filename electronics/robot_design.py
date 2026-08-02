from components.battery import Battery_4S4P_20Ah
from components.fuse import Fuse_5A_Automotive, Fuse_10A_Automotive, Fuse_30A_Automotive, Fuse_2A_Fast
from components.motor import DC_Motor
from components.motor_driver import Motor_Driver
from components.bms import BMS_4S_40A
from components.pd_trigger import PD_Trigger_20V
from components.step_down_converter import Step_Down_XL4015_CCCV
from skidl import Net, Group
from config_loader import load_config

# def build_battery_pack(net_gnd, net_vbat_raw):
#     """
#     Generates a 4S battery pack using 4 abstract 1S4P battery modules connected in series.

#     - Each block represents 4 cells in parallel (1S4P, 20Ah total).
#     - Chains 4 series blocks sequentially.
#     - Exposes intermediate balance taps for BMS routing.
#     """
#     bat_cfg = load_config().get("battery", {})
#     S = bat_cfg.get("cells_in_series", 4)

#     # Prepare node list: [GND, TAP_1, TAP_2, TAP_3, VBAT_RAW]
#     series_nodes = [net_gnd]
#     for i in range(1, S):
#         series_nodes.append(Net(f"BAT_BAL_TAP_{i}"))
#     series_nodes.append(net_vbat_raw)

#     series_blocks = []

#     # Build 4 series tiers consisting of one 1S4P block each
#     for s in range(S):
#         with Group(f"Series_Tier_{s+1}"):
#             block_ref = f"BAT_1S4P_S{s+1}"
#             cell_block = Battery_1S4P_20Ah(ref=block_ref)

#             # Wire positive and negative terminals to series nodes
#             cell_block[1] += series_nodes[s + 1]  # Positive
#             cell_block[2] += series_nodes[s]      # Negative

#             series_blocks.append(cell_block)

#     return {
#         "pos": net_vbat_raw,
#         "neg": net_gnd,
#         "balance_taps": series_nodes[1:-1],
#         "blocks": series_blocks
#     }

def build_robot_circuit():
    """Constructs the high-power dual motor drive architecture of the robot."""

    # 1. Define Global Networks
    vbat_raw = Net("VBAT_RAW")
    vbat_fused = Net("VBAT_FUSED")

    # sys_gnd = Net("SYS_GND")
    gnd = Net("GND")
    sys_pwr = Net("SYS_16V_PWR")

    # Domain C: USB CHARGING (20V)
    usb_vbus = Net("20V_USB_VBUS")
    usb_gnd = Net("USB_GND")

    v_5v = Net("5V_LOGIC")  # 5V logic supply for BTS7960 and microcontrollers

    # 2. Build the battery pack (4 x 1S4P blocks)
    # batt = build_battery_pack(gnd, vbat_raw)

    # batt = build_battery_pack(gnd, vbat_raw)
    batt = Battery_4S4P_20Ah()
    batt["16.8V"] += vbat_raw

    main_batt_fuse = Fuse_30A_Automotive()
    main_batt_fuse[1] += vbat_raw
    main_batt_fuse[2] += vbat_fused

    driver_L = Motor_Driver(ref="MOD1")
    driver_R = Motor_Driver(ref="MOD2")

    motor_FR = DC_Motor(ref="M1")
    motor_FL = DC_Motor(ref="M2")
    motor_BR = DC_Motor(ref="M3")
    motor_BL = DC_Motor(ref="M4")


    bms = BMS_4S_40A(ref="BMS")
    pd_trigger = PD_Trigger_20V(ref="PD_TRIGGER")
    step_down = Step_Down_XL4015_CCCV(ref="STEP_DOWN")

    bms["B+"] += vbat_fused
    bms["B-"] += batt["0V"]

    # Connect the balance wires exactly to the intermediate nodes (3 taps for 4S)
    bms["B1"] += batt["4.2V"]
    bms["B2"] += batt["8.4V"]
    bms["B3"] += batt["12.6V"]

    # The BMS acts as the gateway. P+ and P- become our new master power rails!
    bms["P+"] += sys_pwr
    bms["P-"] += gnd

    # USB Input
    pd_trigger["USB_IN"] += usb_vbus
    pd_trigger["GND_IN"] += usb_gnd

    # Step Down From USB to BMS
    step_down["IN+"] += pd_trigger["VBUS"]
    step_down["IN-"] += pd_trigger["GND"]
    step_down["OUT+"] += bms["P+"]
    step_down["OUT-"] += bms["P-"]

    driver_L["GND"] += gnd
    driver_R["GND"] += gnd

    driver_L_fuse = Fuse_10A_Automotive()
    driver_R_fuse = Fuse_10A_Automotive()

    driver_L_fuse[1] += sys_pwr
    driver_R_fuse[1] += sys_pwr

    driver_L["B+"] += driver_L_fuse
    driver_L["B-"] += gnd
    driver_R["B+"] += driver_R_fuse
    driver_R["B-"] += gnd

    driver_L["M+"] += motor_FL["+"]
    driver_L["M-"] += motor_FL["-"]
    driver_L["M+"] += motor_BL["+"]
    driver_L["M-"] += motor_BL["-"]
    driver_R["M+"] += motor_BR["+"]
    driver_R["M-"] += motor_BR["-"]
    driver_R["M+"] += motor_FR["+"]
    driver_R["M-"] += motor_FR["-"]
