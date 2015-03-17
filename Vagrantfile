# Vagrant Template used for Vagrantfile creation specific to CVE

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 80, host: 8080

  config.vm.synced_folder "/home/prabhendu/host" , "/vagrant_data"

  config.vm.provision "shell", path: "provision.sh" 
end
