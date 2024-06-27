# nunuhay
# The correct path
* /data/data/com.termux/files/usr/bin/nunuhay
*  /data/data/com.termux/files/usr/bin/libnunuhay.py
*  
# Usage
## 1. Termux
### place this into .bashrc
```bash
if $(declare -a nunuhay); then
   alias nunuhay='source ~/.profile && nunuhay ${nunuhay[@]} && php -S localhost:8000 -t /sdcard/htdocs/'
fi
```
### place this into .profile
```bash
export nunuhay=( 10 5 4 0)
```
###  then run
```bash
$ nunuhay
```

## 2. Termux widget

Choose 

1. Ubah_data_barang

2. Jalankan_server

