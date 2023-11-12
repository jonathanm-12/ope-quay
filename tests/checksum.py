import yaml
import subprocess

with open("../base/config.yml", 'r') as file:
    data = yaml.safe_load(file)

CORRECT_CHECKSUM = data['base']['checksum']

command = "find / -not \\( -path /proc -prune \\) -not \\( -path /sys -prune \\) -type f -exec stat -c '%n %a' {} + | LC_ALL=C sorat | sha256sum | cut -c 1-64"
CHECKSUM = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.DEVNULL)

if CHECKSUM == CORRECT_CHECKSUM:
	print("Checksum Test Passed")
	print("Expected: ", CORRECT_CHECKSUM)
	print("Got: ", CHECKSUM)	
else:
	print("Checksum Test Failed")
	print("Expected: ", CORRECT_CHECKSUM)
	print("Got: ", CHECKSUM)
	exit(1)