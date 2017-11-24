# -*- mode: ruby -*-
# vi: set ft=ruby :


Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.ssh.forward_agent = true
  config.ssh.insert_key = false
  config.ssh.private_key_path =  ["~/.vagrant.d/insecure_private_key","~/.ssh/id_rsa"]

  config.vm.provision :shell, privileged: false do |s|
    ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
    s.inline = <<-SHELL
       echo #{ssh_pub_key} >> /home/$USER/.ssh/authorized_keys
       sudo bash -c "echo #{ssh_pub_key} >> /root/.ssh/authorized_keys"
    SHELL
  end

  config.vm.provision :shell, inline: <<-SHELL
  if [[ ! -f /usr/bin/python ]]; then
    apt-get update
    apt-get install -y python
  fi
  SHELL


  config.vm.provision "ansible" do |ansible|
      ansible.playbook = "/datastore/projects/3av_web/bootstrap.yml"
      ansible.config_file = "/datastore/projects/3av_web/ansible.cfg"
      ansible.inventory_path = "/datastore/projects/3av_web/inventories/dev/hosts"
      ansible.vault_password_file = "/datastore/projects/3av_web/vault_pass"
  end


  config.vm.define "web1" do |machine|
      machine.vm.hostname = "web1.local"
      machine.vm.network "private_network", ip: "192.168.34.10"
      # machine.vm.network "forwarded_port", guest: 22, host:  2221, id: 'ssh'
      machine.vm.synced_folder "www/", "/projects/web1"
  end

end
