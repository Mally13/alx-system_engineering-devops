# Create Client configuration file (w/ Puppet)

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "Host 239778-web-01\n\
                  HostName 52.87.235.104\n\
                  User mally13\n\
                  IdentityFile ~/.ssh/school\n\
                  PasswordAuthentication no\n",
  owner   => mally13,
  group   => mally13,
  mode    => '0664',
}

