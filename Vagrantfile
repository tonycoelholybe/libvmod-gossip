# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<SCRIPT
  # General packages.
  apt-get update -q
  apt-get install -qq unzip apt-transport-https \
    autotools-dev automake libtool python-docutils pkg-config libpcre3-dev \
    libeditline-dev libedit-dev make dpkg-dev git libjemalloc-dev \
    libncurses-dev python-sphinx graphviz

  # Varnish Cache.
  sudo -u vagrant bash -c '\
    git clone https://github.com/varnishcache/varnish-cache.git /tmp/varnish; \
    cd /tmp/varnish; \
    ./autogen.sh; \
    ./configure; \
    make; \
    sudo make PREFIX="/usr/local" install; \
    sudo ldconfig'

  # VMOD.
  sudo -u vagrant bash -c '\
    cd /vagrant; \
    ./autogen.sh; \
    ./configure; \
    make'
SCRIPT

Vagrant.configure('2') do |config|
  config.vm.hostname = 'dev'
  config.vm.network :public_network
  config.vm.synced_folder '.', '/vagrant', :nfs => false
  config.vm.provider :virtualbox do |vb|
    vb.memory = 1024
    vb.cpus = 1
    vb.linked_clone = Gem::Version.new(Vagrant::VERSION) >= Gem::Version.new('1.8.0')
    vb.customize [
      'modifyvm', :id,
      '--natdnshostresolver1', 'on',
      '--natdnsproxy1', 'on',
      '--accelerate3d', 'off',
      '--audio', 'none',
      '--paravirtprovider', 'Default',
    ]
  end

  config.vm.define :master do |machine|
    machine.vm.box = 'ubuntu/xenial64'
    machine.vm.box_version = '=20180315.0.0'
    machine.vm.box_check_update = true
    machine.vm.provision :shell, :privileged => true, :keep_color => false, :inline => $script
    machine.vm.provider :virtualbox do |vb|
      vb.customize [
        'modifyvm', :id,
        '--name', 'libvmod-gossip (Varnish master)',
      ]
    end
  end
end