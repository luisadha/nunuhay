#!/data/data/com.termux/files/usr/bin/bash

# bash ./install.sh

set -xv
NUNUHAY_ROOT="${0%/*}"

mkdir -p /data/data/com.termux/files/home/.shortcuts
chmod 700 -R /data/data/com.termux/files/home/.shortcuts

install -m 755 "$NUNUHAY_ROOT/.shortcuts/Jalankan_server" "/data/data/com.termux/files/home/.shortcuts"
install -m 755 "$NUNUHAY_ROOT/.shortcuts/Ubah_data_barang" "/data/data/com.termux/files/home/.shortcuts"
install -m 755 "$NUNUHAY_ROOT/nunuhay" "/data/data/com.termux/files/usr/bin"
install -m 755 "$NUNUHAY_ROOT/libnunuhay.py" "/data/data/com.termux/files/usr/bin"

