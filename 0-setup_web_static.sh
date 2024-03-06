#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install the Nginx web server software
apt-get -y update
apt-get -y install nginx

# Create necessary directories
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

# Create a fake HTML file
cat > /data/web_static/releases/test/index.html <<EOF
<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>
EOF

# Create or recreate the symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data folder to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data

# Update Nginx configuration
CONFIG_FILE="/etc/nginx/sites-available/default"
NGINX_CONFIG="location /hbnb_static {\n\talias /data/web_static/current/;\n}\n"
sed -i "/^server {/a $NGINX_CONFIG" $CONFIG_FILE

# Restart the Nginx service to apply the new configuration
service nginx restart
