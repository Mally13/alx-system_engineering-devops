# puppet conf to Install Nginx with the following configurations:
#+	Listens on port 80.
#+	Returns a page containing "Holberton School" when queried
#+	 at the root with a curl GET request.
# Configures /redirect_me as a "301 Moved Permanently".
# Includes a custom 404 page containing "Ceci n'est pas une page".

node 'default' {
  # Install Nginx package
  package {
	'nginx':
	  ensure => present,
	}

  # Create /etc/nginx/sites-available/default directory
  file {
	'/etc/nginx/sites-available/default':
	  ensure => directory,
	  mode   => '0755',
	  owner  => 'root',
	  group  => 'root',
	}

  # Create /etc/nginx/sites-enabled/default symlink
  file {
	'/etc/nginx/sites-enabled/default':
	  ensure => link,
	  target  => '/etc/nginx/sites-available/default',
	}

  # Configure Nginx server block
  file {
	'/etc/nginx/sites-available/default':
	  ensure => present,
	  content => <<'EOF'
	  server {
	    listen 80;
	    listen [::]:80 default_server;

	    root /var/www/html;
	    index index.html index.htm;

	    location / {
	      return 200 "Hello World!";
	    }

	    location /redirect_me {
	      return 301 https://www.example.com;
	    }

	    error_page 404 /404.html;
	    location /404 {
	      return 404 "Ceci n'\''est pas une page\n";
	    }
	  }
	EOF
  }

  # Restart Nginx service
  service {
	'nginx':
	  ensure => running,
	  enable => true,
	}
}
