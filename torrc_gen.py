# Get input from user
filename = input("File in which save torrc: ")
instances_count = int(input("Number of Tor instances to spawn: "))
starting_port = int(input("First port (usually 9050): "))

ports = ""
control_ports = ""

for instance in range(instances_count):
    ports += f"SOCKSPort 0.0.0.0:{starting_port}\n"
    control_ports += f"ControlPort {starting_port+1}\n"

    starting_port += 10

print(ports, control_ports, sep="\n")
with open(filename, "x") as f:
    f.write(ports)
    f.write(control_ports)

