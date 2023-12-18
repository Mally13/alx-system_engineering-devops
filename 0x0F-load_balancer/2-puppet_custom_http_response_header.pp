# Define variables
$directory = '/etc/nginx/html'
$file_404 = '/etc/nginx/html/404.html'
$file_index = '/etc/nginx/html/index.html'

# Update package lists
package { 'nginx':
  ensure => 'latest',
}

# Ensure nginx service is running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Print hostname
notify { $::hostname: }

# Create directory if it doesn't exist
file { $directory:
  ensure => 'directory',
}

# Create index.html file if it doesn't exist
file { $file_index:
  ensure  => 'file',
  content => 'Hello World!',
}

# Create 404.html file if it doesn't exist
file { $file_404:
  ensure  => 'file',
  content => "Ceci n'est pas une page",
}

# Configure nginx default site
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {
	listen 80;
	listen [::]:80 default_server;
	root   /etc/nginx/html;
	index  index.html index.htm;
	add_header X-Served-By ${hostname} always;

	location /redirect_me {
	    return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}
	error_page 404 /404.html;
	location /404 {
	  root /etc/nginx/html;
	  internal;
	}
}",
  require => [Package['nginx'], File[$directory], File[$file_index], File[$file_404]],
}

# Restart nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
  subscribe => [Package['nginx'], File[$directory], File[$file_index], File[$file_404]],
}

