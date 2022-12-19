#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static2z
sudo apt-get -y  update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
echo "nginx configuration"  | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown ubuntu /data/
sudo sed -i '53i \\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
/etc/init.d/nginx restart
