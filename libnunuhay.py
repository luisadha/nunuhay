from babel.numbers import format_currency
import sys
import pandas as pd
from tabulate import tabulate
import subprocess
import json
import time
import csv 


dasar_price = float(6000.0)
nyilang_price = float(7000.0)
mateni_price = float(8000.0)
full_price = float(21000.0)

if len(sys.argv) < 5:
    print("Argument required!")
    print("   Argumen 1 = Dasar \n   Argumen 2 = Nyilang\n   Argumen 3 Mateni\n   Argumen 4 = Full")
    sys.exit(1)


def borongan(nunuhay, dasar=None, nyilang=None, mateni=None, full=None):   
    global dasar_price, nyilang_price, mateni_price, full_price
    return {  
            "+": lambda: dasar_price * float(dasar) + nyilang_price * float(nyilang) + mateni_price * float(mateni) + full_price * float(full)
}.get(nunuhay, lambda: "Gak ngambil barang")()
global t, idr_convert
t = borongan("+", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
d = sys.argv[4]
w = format_currency(dasar_price, 'IDR', locale='id_ID')
x = format_currency(nyilang_price, 'IDR', locale='id_ID')
y = format_currency(mateni_price, 'IDR', locale='id_ID')
z = format_currency(full_price, 'IDR', locale='id_ID')
#t = borongan("+", 10, 1, 3, 6)
# 5 -  3 2 1
idr_convert = format_currency(t, 'IDR', locale='id_ID')
data = [
    ["Dasar", w, a],
    ["Nyilang", x, b],
    ["Mateni", y, c],
    ["Full", z, d]
]
headers = ["    Fase    ", "    Harga     ", "    Qty    "]
table = tabulate(data, headers=headers, tablefmt="fancy_grid")

def tabel_choice():
    print(table);
    with open('nunuhay_data.table', 'w', encoding='utf-8') as tabf:
        tabf.write(f"\n{table}")
        print(f"Total dgn. module :", idr_convert);
    
    print(f"Total dgn. manual : Rp. {t:.2f}");

def csv_choice():
    df = pd.DataFrame(data, columns=headers)
    df.to_csv('nunuhay_data.csv', index=False)
    print(df)
    print("\n")
    print(f"Total dgn. module :", idr_convert);

def json_choice():
    dr = pd.read_csv('nunuhay_data.csv')  
    json_data = dr.to_json(orient='records')
    print(json_data)
    print("\n")
    print(f"Total dgn. module :", idr_convert);

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    with open(csvFilePath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf) 

        for row in csvReader: 
            jsonArray.append(row)
  
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'nunuhay_data.csv'
jsonFilePath = r'nunuhay_data.json'

if __name__=='__main__':

    start = time.perf_counter() 
    json_choice()
    finish = time.perf_counter()
    print("\n");
    print(f"Conversion 100.000 rows completed successfully in {finish - start:0.4f} seconds")
