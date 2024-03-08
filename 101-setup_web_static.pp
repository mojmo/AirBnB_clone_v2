# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { ['/data/web_static/releases/test', '/data/web_static/shared']:
  ensure => directory,
}

# Create a fake HTML file
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>
                <head>
                </head>
                <body>
                    Holberton School
                </body>
            </html>',
}

# Create or recreate the symbolic link
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
}

# Give ownership of /data folder to ubuntu user and group recursively
file { '/data':
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Update Nginx configuration
file_line { 'nginx_config':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => 'location /hbnb_static { alias /data/web_static/current/; }',
  match   => '^server {',
  after   => true,
  notify  => Service['nginx'],
}

# Restart the Nginx service to apply the new configuration
service { 'nginx':
  ensure    => running,
  enable    => true,
}
