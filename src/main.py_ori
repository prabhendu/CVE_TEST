# Main program :
# Vagrantfile creation using a generic template
# Shell provisioning method used
# Pass absolute file name of exploit program to be run as initial argument
# Asks for box to be installed, Shared directory location and list of packages to be installed on VM
# Copies exploit program into /vagrant_data directory on VM

#!/usr/bin/python

import sys
import os
import shutil
from subprocess import call

if len(sys.argv)!=2:
	print 'please enter absolute exploit file name'
	print 'usage : python main.py <filename> \nExiting'
	sys.exit(1)

print 'Arguments are :'
for list in sys.argv:
	print list

boxname = raw_input('Please enter the name of box :')
syncfolder = raw_input('Please enter absolute host shared folder name :')
shared_dir = '/vagrant_data'  #local shared dir
local_file = syncfolder +'/exploit.c' #local exploit copy name

# Copying exploit program 
print('Copying exploit program in local directory')
shutil.copy2(sys.argv[1],local_file)

call(["rm","-f","Vagrantfile"])
print('Initializing Vagrant\n')
#Modifying Vagrantfile starts
vagrant_template = open(syncfolder+'/Vagrantfile','r') #common template
vagrant_file = open(os.getcwd()+'/Vagrantfile','w') #final actual file

replacements = {'BOX_NAME':boxname , 'HOST_SHARED_DIR':syncfolder , 'GUEST_MOUNT_DIR':shared_dir}

for line in vagrant_template:
	for src,dest in replacements.iteritems():
		line = line.replace(src , dest)
	vagrant_file.write(line)

vagrant_template.close()
vagrant_file.close()
#Modifying Vagrantfile ends  

#Creating provisioning file
provision_list=raw_input('Please enter list of inorder packages you want in VM: ')
prov_file = open(os.getcwd()+'/provision.sh','w')

prov_file.write('#!/usr/bin/env bash\n')
for package in provision_list.split():
	prov_file.write('sudo apt-get install -y ' + package + '\n')
prov_file.close();
