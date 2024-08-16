# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install specific versions of Flask and Werkzeug to avoid compatibility issues
exec { 'install_flask_and_werkzeug':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.0.3',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
