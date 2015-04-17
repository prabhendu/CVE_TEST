# Main program ource
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
	print 'please enter absolute exploit list file name'
	print 'usage : python main.py <filename> \nExiting'
	sys.exit(1)

print 'Arguments are :'
for list in sys.argv:
	print list

boxname = raw_input('Please enter the name of box :')
syncfolder = raw_input('Please enter absolute host shared folder name :')
memory = raw_input('Please enter the memory required :')
shared_dir = '/vagrant_data'  #local shared dir

# Copying exploit program 
print('Copying exploit program in local directory')
exploit_file = open(sys.argv[1],'r')
i=1
for line in exploit_file:
	shutil.copy2(line.replace("\n",""),syncfolder+'/exploit'+str(i)+'.c')
	i=i+1

call(["rm","-f","Vagrantfile"])
print('Initializing Vagrant\n')
#Modifying Vagrantfile starts
vagrant_template = open(syncfolder+'/Vagrantfile','r') #common template
vagrant_file = open(os.getcwd()+'/Vagrantfile','w') #final actual file

replacements = {'BOX_NAME':boxname , 'HOST_SHARED_DIR':syncfolder , 'GUEST_MOUNT_DIR':shared_dir , 'MEMORY':memory}

for line in vagrant_template:
	for src,dest in replacements.iteritems():
		line = line.replace(src , dest)
	vagrant_file.write(line)

vagrant_template.close()
vagrant_file.close()
#Modifying Vagrantfile ends  

#puppet modules to be installed
#ensure that puppet is installed on Host
puppet_mod_install = open ('puppet.sh','w')

kernel_deb_dir=raw_input('enter the location of new kernel source(deb files) you want to build:\n ')
puppet_mod_install.write('cp ' + kernel_deb_dir + '/* ' + syncfolder +'\n')

puppet_list = raw_input('Please enter the puppet modules you want in order\n')
for module in puppet_list.split():
        puppet_mod_install.write('puppet module install --force --modulepath ' + os.getcwd() + '/puppet/modules ' + module + '\n' )
puppet_mod_install.close()
#Download puppet modules
os.chmod("./puppet.sh",0755)
call("./puppet.sh",shell=True)

#Creating provisioning file
package_list=raw_input('Please enter list of inorder packages you want in VM: ')
prov_file = open(os.getcwd()+'/provision.sh','w')
prov_file.write('#!/usr/bin/env bash\n')
prov_file.write('#update the server\n')
prov_file.write('sudo apt-get update \n')
prov_file.write('sudo apt-get -y upgrade \n')
prov_file.write('sudo apt-get -y install dkms build-essential linux-headers-generic vim gcc\n')

for package in package_list.split():
	prov_file.write('sudo apt-get install -y ' + package + '\n')

#Coying all files from shared directory.Kernel rebuild destroys shared directory
prov_file.write('sudo mkdir /temp')
prov_file.write('sudo cp ' + shared_dir +'/* /temp \n' )
if kernel_deb_dir != '':
	prov_file.write('sudo dpkg -i *.deb\n')

prov_file.close();

#Creating default.pp with required classes
print 'Please ensure default.pp is correct'
