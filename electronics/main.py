import os

from robot_design import build_robot_circuit
from skidl import generate_schematic, generate_netlist, generate_svg, lib_search_paths, KICAD

os.environ["PATH"] += os.pathsep + os.path.abspath(
    os.path.join(os.getcwd(), "node_modules", ".bin")
)

# 1. ⚙️ CONFIGURATION: Set library priority
lib_search_paths[KICAD] = ["./symbols", "/usr/share/kicad/symbols"]


def run_tests():
    # Clear memory for a fresh build
    default_circuit.reset()

    # Build the logic topology from design.py
    build_robot_circuit()

    total_cost = 0.0

    # Iterate through every instantiated part to extract our custom wrapper fields
    for part in default_circuit.parts:
        price_str = getattr(part, "price_uah", 0.0)
        total_cost += float(price_str)

        # print(f"[{part.ref}] {part.name} - {part.value}")
        # print(f"    ├─ Link:  {getattr(part, 'buy_link', 'N/A')}")
        # print(f"    └─ Price: {getattr(part, 'price', 'N/A')}")

    print("---------------------------------------------")
    print(f"💰 TOTAL ESTIMATED COST: ${total_cost:.2f}")
    print("=============================================\n")

    generate_netlist(file_="main.net")
    generate_svg(file_="main")

if __name__ == "__main__":
    run_tests()
