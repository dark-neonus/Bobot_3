from skidl import *

# Reset the circuit engine
default_circuit.reset()

# Create templates pointing directly to KiCad's official graphical symbols
q = Part(
    "Transistor_BJT",
    "Q_PNP_CBE",
    footprint="Package_TO_SOT_THT:TO-92_Inline",
    dest=TEMPLATE,
)
r = Part("Device", "R", footprint="Resistor_SMD:R_0805_2012Metric", dest=TEMPLATE)

# Create nets
gnd, vcc = Net("GND"), Net("VCC")
a, b, a_and_b = Net("A"), Net("B"), Net("A_AND_B")

# Instantiate parts
q1, q2 = q(2)
r1, r2, r3, r4, r5 = r(5, value="10K")

# Build the connections
a & r1 & q1[2, 1] & r4 & q2[2, 1] & a_and_b & r5 & gnd
b & r2 & q1[2]
q1[1] & r3 & gnd
vcc += q1[3], q2[3]

# 📄 THIS IS THE KEY: Generate a native KiCad schematic file instead of a netlist
# This will output a file named 'circuit_board.kicad_sch'
generate_schematic(file_="circuit_board.kicad_sch")
print("🎉 Clean KiCad schematic database generated!")
