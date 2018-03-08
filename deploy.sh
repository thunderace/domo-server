#!/bin/bash
# Deploy to local

DEST_DIR="/var/www/domo-server"

echo "Deploy to localhost to $DEST_DIR"
sudo cp * $DEST_DIR/
sudo cp -r ./api $DEST_DIR/
sudo cp -r ./app $DEST_DIR/
sudo cp -r ./python $DEST_DIR/

sudo pm2 restart domo-server
