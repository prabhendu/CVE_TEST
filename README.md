# CVE_TEST
Creating virtual environments for CVE execution using Vagrant

Current version asks user for the type of box required and list of dependencies required to run exploit.
Shell provisioning is used to install dependencies using apt-get

Usage:

python main.py exploit_list

-returns a Vagrantfile and provision.sh for VM.

-Starts VM using from script and executes binaries provided in the exploit_list on the VM

