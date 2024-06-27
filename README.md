# nunuhay
Project sederhana tabel barang support CLI & Web

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

```bash
git clone https://github.com/luisadha/nunuhay.git
cd nunuhay
bash ./install.sh
```
Close the termux app then create an widget on Home

Choose 

1. Ubah_data_barang

2. Jalankan_server

# PHP Server using [[Zhell Server](https://github.com/Teams-of-Termux-Indonesia/ZhellServer)]

# Made with love
- python
- shell
- php
