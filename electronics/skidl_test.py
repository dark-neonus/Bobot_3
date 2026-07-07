from skidl.pyspice import *

# 1. Define your circuit networks
vcc = Net("VCC")
a, b, a_and_b = Net("A"), Net("B"), Net("A_AND_B")

# 2. Instantiate your components
q1 = Q(ref="Q1")
q2 = Q(ref="Q2")

r1 = R(ref="R1", value="10k")
r2 = R(ref="R2", value="10k")
r3 = R(ref="R3", value="10k")
r4 = R(ref="R4", value="10k")
r5 = R(ref="R5", value="10k")

# 3. Map the network topology
a & r1 & q1["b"]
b & r2 & q1["b"]
vcc & r3 & q1["c"] & r4 & q2["b"]
vcc & r5 & q2["c"] & a_and_b
gnd += q1["e"], q2["e"]

# 4. Export clean SPICE Netlist string
print("\n--- GENERATED SPICE NETLIST ---")
print(generate_netlist())

# 5. 🎨 VISUALIZATION BUG FIX / ENHANCEMENT
# Generate a schematic graph representation entirely without KiCad.
# This outputs 'pyspice.dot' and compiles it into 'pyspice.png'
print("\n--- GENERATING ELECTRICAL SCHEME GRAPH ---")
default_circuit.generate_graph(file_="circuit_graph.dot")
