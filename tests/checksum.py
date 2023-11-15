import yaml
import subprocess

with open("../base/config.yml", 'r') as file:
    data = yaml.safe_load(file)

CORRECT_CHECKSUM = data['base']['checksum']

OPE_BOOK_REG = data['ope']['book_registry']

OPE_BOOK_IMAGE = data['ope']['book_user'] + '/' + data['ope']['book']

OPE_BETA_TAG = "beta-ope"

ARGS = "find / -not \( -path /proc -prune \) -not \( -path /sys -prune \) -type f -exec stat -c '%n %a' {} + | LC_ALL=C sort | sha256sum | cut -c 1-64"

DARGS = "-u 0"

#CHECKSUM = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.DEVNULL)

RUN_DOCKER = "docker run -i --rm %s %s %s %s %s" % (DARGS, OPE_BOOK_REG, OPE_BOOK_IMAGE, OPE_BETA_TAG, ARGS)

print(RUN_DOCKER)

CHECKSUM = subprocess.check_output(RUN_DOCKER, shell=True, stderr=subprocess.DEVNULL).decode('utf-8')

#	@-docker run -i --rm $(DARGS) $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG) $(ARGS)

if CHECKSUM == CORRECT_CHECKSUM:
	print("Checksum Test Passed")
	print("Expected: ", CORRECT_CHECKSUM)
	print("Got: ", CHECKSUM)	
else:
	print("Checksum Test Failed")
	print("Expected: ", CORRECT_CHECKSUM)
	print("Got: ", CHECKSUM)
	exit(1)
