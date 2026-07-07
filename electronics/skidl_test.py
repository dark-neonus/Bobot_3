from skidl.pyspice import *

# 1. Define your circuit networks
# Force SKiDL to preserve the strict "0" name for SPICE solvers
gnd = Net("0", fixed_name=True)
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

# 3. Map the network topology (Standard NPN RTL Configuration)
# Inputs A and B mix into the Base of Q1
a & r1 & q1["b"]
b & r2 & q1["b"]

# Collector of Q1 pulls up to VCC via R3, and drives the Base of Q2 via R4
vcc & r3 & q1["c"] & r4 & q2["b"]

# Collector of Q2 pulls up to VCC via R5, producing the output node
vcc & r5 & q2["c"] & a_and_b

# Emitters of standard NPN BJTs connect directly to Ground
gnd += q1["e"], q2["e"]

# 4. Export clean SPICE Netlist string
print("\n--- GENERATED SPICE NETLIST ---")
print(generate_netlist())
