from components.battery import Battery_4S4P_20Ah
from components.circuit_breaker import Circuit_Breaker
from components.fuse import Fuse_5A_Automotive, Fuse_10A_Automotive, Fuse_30A_Automotive, Fuse_2A_Fast
from components.motor import DC_Motor
from components.motor_driver import Motor_Driver
from components.bms import BMS_4S_40A
from components.pd_trigger import PD_Trigger_20V
from components.step_down_converter import Step_Down_XL4015_CCCV
from skidl import Net, Group
from config_loader import load_config


class RobotCircuit:
    """Class representing the high-power dual motor drive architecture of BOBOT_3."""

    def __init__(self):
        # 1. Define Shared Global Networks (Power Rails & Buses)
        self.vbat_raw = Net("VBAT_RAW")
        self.vbat_fused = Net("VBAT_FUSED")
        self.gnd = Net("GND")
        self.sys_pwr = Net("SYS_16V_PWR")

        # Domain C: USB CHARGING (20V)
        self.usb_vbus = Net("20V_USB_VBUS")
        self.usb_gnd = Net("USB_GND")

        self.v_5v = Net("5V_LOGIC")  # 5V logic supply for BTS7960 and microcontrollers

    def build_battery_subsystem(self):
        """Constructs battery pack, main fuse, BMS protection, and master power switch."""
        with Group("Battery_Subsystem"):
            self.batt = Battery_4S4P_20Ah()
            self.batt["16.8V"] += self.vbat_raw

            self.main_batt_fuse = Fuse_30A_Automotive()
            self.main_batt_fuse[1] += self.vbat_raw
            self.main_batt_fuse[2] += self.vbat_fused

            self.bms = BMS_4S_40A(ref="BMS")
            self.bms["B+"] += self.vbat_fused
            self.bms["B-"] += self.batt["0V"]

            # Connect balance wires to intermediate battery taps
            self.bms["B1"] += self.batt["4.2V"]
            self.bms["B2"] += self.batt["8.4V"]
            self.bms["B3"] += self.batt["12.6V"]

            # Ground rail gateway
            self.bms["P-"] += self.gnd

            # Master system breaker switch
            self.sys_pwr_switch = Circuit_Breaker()
            self.sys_pwr_switch[1] += self.bms["P+"]
            self.sys_pwr_switch[2] += self.sys_pwr

    def build_charging_subsystem(self):
        """Constructs USB-C PD trigger and step-down charging path."""
        with Group("Charging_Subsystem"):
            self.pd_trigger = PD_Trigger_20V(ref="PD_TRIGGER")
            self.step_down = Step_Down_XL4015_CCCV(ref="STEP_DOWN")

            # USB Input connection
            self.pd_trigger["USB_IN"] += self.usb_vbus
            self.pd_trigger["GND_IN"] += self.usb_gnd

            # Step Down connection to BMS P+ / P-
            self.step_down["IN+"] += self.pd_trigger["VBUS"]
            self.step_down["IN-"] += self.pd_trigger["GND"]
            self.step_down["OUT+"] += self.bms["P+"]
            self.step_down["OUT-"] += self.bms["P-"]

    def build_drive_subsystem(self):
        """Constructs motor drivers, fuses, and DC drive motors."""
        with Group("Drive_Subsystem"):
            self.driver_L = Motor_Driver(ref="MOD1")
            self.driver_R = Motor_Driver(ref="MOD2")

            self.motor_FR = DC_Motor(ref="M1")
            self.motor_FL = DC_Motor(ref="M2")
            self.motor_BR = DC_Motor(ref="M3")
            self.motor_BL = DC_Motor(ref="M4")

            self.driver_L_fuse = Fuse_10A_Automotive()
            self.driver_R_fuse = Fuse_10A_Automotive()

            self.driver_L_fuse[1] += self.sys_pwr
            self.driver_R_fuse[1] += self.sys_pwr

            self.driver_L["B+"] += self.driver_L_fuse
            self.driver_L["B-"] += self.gnd
            self.driver_R["B+"] += self.driver_R_fuse
            self.driver_R["B-"] += self.gnd

            self.driver_L["GND"] += self.gnd
            self.driver_R["GND"] += self.gnd

            # Motor connections
            self.driver_L["M+"] += self.motor_FL["+"]
            self.driver_L["M-"] += self.motor_FL["-"]
            self.driver_L["M+"] += self.motor_BL["+"]
            self.driver_L["M-"] += self.motor_BL["-"]

            self.driver_R["M+"] += self.motor_BR["+"]
            self.driver_R["M-"] += self.motor_BR["-"]
            self.driver_R["M+"] += self.motor_FR["+"]
            self.driver_R["M-"] += self.motor_FR["-"]

    def build(self):
        """Executes full circuit assembly."""
        self.build_battery_subsystem()
        self.build_charging_subsystem()
        self.build_drive_subsystem()
        return self


def build_robot_circuit():
    """Helper function to build circuit (retained for backward compatibility)."""
    circuit = RobotCircuit()
    circuit.build()
    return circuit
