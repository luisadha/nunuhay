NUNUHAY_ROOT="${0%/*}"

mkdir -p /data/data/com.termux/files/home/.shortcuts
chmod 700 -R /data/data/com.termux/files/home/.shortcuts
cp -f "$NUNUHAY_ROOT/.shortcuts/*" "/data/data/com.termux/files/home/.shortcuts"
install -m 755 "$NUNUHAY_ROOT/nunuhay" "/data/data/com.termux/files/usr/bin"
install -m 755 "$NUNUHAY_ROOT/libnunuhay.py" "/data/data/com.termux/files/usr/bin"

