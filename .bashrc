if $(declare -a nunuhay); then 
alias nunuhay='source ~/.profile && nunuhay ${nunuhay[@]} && php -S localhost:8000 -t ~/storage/shared/htdocs/'
fi
