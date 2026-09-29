import json
import os

from pathlib import Path


project_dir = Path(__file__).resolve().parent.parent
netlist_path = project_dir / "verilog" / "netlist.json"

# try:
with open('verilog/netlist.json') as f:
    print(f)
    design = json.load(f)
# except FileExistsError:
#     print("File Error")
#     exit()
# except FileNotFoundError:
#     print("File not found")
#     exit()

module = design["modules"]["test_adder"]

# 1. Look at your gates (Cells)
for cell_name, cell_data in module["cells"].items():
    gate_type = cell_data["type"] # e.g., "$_NOR_"
    inputs = cell_data["connections"]["A"] # The wire ID connected to input A
    print(f"Place a {gate_type} gate for {cell_name}")

# 2. Look at your wires (Nets)
for net_name, net_data in module["netnames"].items():
    wire_bits = net_data["bits"] # Unique integer IDs representing wire segments
    print(f"Route wire {net_name} using bits {wire_bits}")