import ifcopenshell

# Load the provided IFC file
ifc_file_path = 'FS0912-BDP-01-ZZ-M-A-0002.ifc'  # Update with the correct path
ifc_file = ifcopenshell.open(ifc_file_path)

# Let's inspect a few IFCDOOR entities and their properties
ifc_doors = ifc_file.by_type("IFCDOOR")

# Collect relevant details from the first few doors
door_details = []
for door in ifc_doors[:5]:  # Let's inspect the first 5 doors
    door_info = {
        "Entity ID": door.id(),
        "Name": door.Name,
        "Property Sets": {}
    }
    psets = ifcopenshell.util.element.get_psets(door)
    for pset_name, pset_values in psets.items():
        door_info["Property Sets"][pset_name] = pset_values
    door_details.append(door_info)

# Print the collected details
for detail in door_details:
    print(detail)
