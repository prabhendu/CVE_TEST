# CVE_TEST
Creating virtual environments for CVE execution using Vagrant

Current version asks user for the type of box required and list of dependencies required to run exploit.
Shell provisioning is used to install dependencies using apt-get

#Usage
python main.py <exploit> 
-returns a Vagrantfile and provision.sh for VM.
-"vagrant up" required to start VM
