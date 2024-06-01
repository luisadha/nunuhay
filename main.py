# main interactive_script for nunuhay.py

import subprocess
import sys
import nunuhay as nunu
import os
import time

def main_menu():
    print("Pilihan Menu:")
    print("1. tabel")
    print("2. csv")
    print("3. json")
    print("4. Exit")

    try:
        choice = int(input("Pilihan anda: "))
    except ValueError:
        print("Masukkan angka yang valid.")
        return True

    if choice == 1:
        print("\n")
        start = time.perf_counter()
        nunu.tabel_choice()
        finish = time.perf_counter()
        print(f"\nConversion completed in {finish - start} seconds\n")
        print("\n")
    elif choice == 2:
        print("\n")
        start = time.perf_counter()
        nunu.csv_choice()
        finish = time.perf_counter()
        print(f"\nConversion completed in {finish - start} seconds\n")
        print("\n")
    elif choice == 3:
        print("\n")
        start = time.perf_counter()
        nunu.csv_to_json(nunu.csvFilePath, nunu.jsonFilePath)
        with open(nunu.jsonFilePath, 'r') as f:
            opening_json = f.read()
            print(opening_json)
        finish = time.perf_counter()
        print(f"\nConversion completed in {finish - start} seconds\n")
        print("\n")
    elif choice == 4:
        print("Exiting...")
        return False
    else:
        print("Pilihan tidak valid.")
    
    return True

if __name__ == "__main__":
    while main_menu():
        pass
