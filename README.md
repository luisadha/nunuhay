# nunuhay
## Config
```bash
if $(declare -a nunuhay); then
   alias nunuhay='source ~/.profile && nunuhay ${nunuhay[@]} && php -S localhost:8000 -t /sdcard/htdocs/'
fi
```

## Usage
```bash
$ nunuhay
```
