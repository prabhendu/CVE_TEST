# Vagrant Template used for Vagrantfile creation specific to CVE

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |vb|
  	vb.memory = "1024"
  end

  config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.synced_folder "/home/prabhendu/host" , "/vagrant_data"

  config.vm.provision "shell", path: "provision.sh" 

  config.vm.provision "puppet" do |puppet|
  	puppet.manifests_path = "puppet/manifests"
	puppet.module_path = "puppet/modules"
  end
end
