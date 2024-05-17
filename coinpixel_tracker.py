from datetime import datetime
import os
from rich.table import Table
from rich.console import Console
from rich.progress import track
from rich.text import Text
import time as tidur
import csv

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("%H:%M")
date_time = now.strftime("%m/%d/%Y, %H:%M")
date_only = now.strftime("%m/%d/%Y")

console = Console()
table = Table(title="")

def get_input():
    Coin_value = int(input("Coin sekarang: "))
    Pixel_value = int(input("Pixels sekarang: "))
    cls()
    for i in track(range(20), description="Made with 💙 by JojoXIX"):
        tidur.sleep(0.05)
    cls()
    console.print("Made with 💙 by JojoXIX")
    table.add_column(":alarm_clock: " + date_time, justify="left")
    table.add_column("Nilai", justify="center")
    table.add_row("🪙 COINS saat ini", str(f"{Coin_value:,}"), style="bold #ffbf00")
    table.add_row("💲 PIXELS saat ini", str(f"{Pixel_value:,}"), style="bold #E2FE36")
    console.print(table)
    return Coin_value, Pixel_value

tableHasil = Table(title="")

def Hasil():
    input("Tekan enter untuk melakukan kalkulasi...")
    Coin_value_u, Pixel_value_u = get_input()
    cls()
    console.print("Made with 💙 by JojoXIX")
    tableHasil.add_column(":alarm_clock: " + date_time, justify="left")
    tableHasil.add_column("Nilai", justify="right")
    Coin_value_c = Coin_value_u - Coin_value
    Pixel_value_c = Pixel_value_u - Pixel_value
    tableHasil.add_row("🪙 COINS dihabiskan", str(f"{Coin_value_c:,}"), style="bold #ffbf00")
    tableHasil.add_row("💲 PIXELS dihasilkan", str("+"f"{Pixel_value_c:,}"), style="bold #E2FE36")
    coin_pixel_loss = round(Coin_value_c / Pixel_value_c)
    tableHasil.add_row("🪙 COINS per 💲 PIXELS", str(coin_pixel_loss), style="bold #E2FE36")
    console.print(tableHasil)
    console.print("Apakah ini seret?\nNggak, lu kurang bersyukur ☝️🤓", style="bold cyan")
    print("\n")

    response = input("Apakah Anda ingin menyimpan hasil ke file CSV? (Y/N) ").lower()
    if response == 'y':
        with open('hasil.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['TANGGAL', 'COIN Spent', 'PIXELS Made', 'COIN per PIXELS'])
            if f.tell() == 0:
                writer.writeheader()

        # Write data to the CSV file
        with open('hasil.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['TANGGAL', 'COIN Spent', 'PIXELS Made', 'COIN per PIXELS'])
            row = {
                'TANGGAL': date_only,
                'COIN Spent': Coin_value_c,
                'PIXELS Made': Pixel_value_c,
                'COIN per PIXELS': coin_pixel_loss
            }
            writer.writerow(row)
            cls()
            for i in track(range(20), description="Made with 💙 by JojoXIX"):
                tidur.sleep(0.05)
            console.print(tableHasil)
            print("\n")
            console.print("Berhasil disimpan/update ke hasil.csv", style="bold cyan")
            tidur.sleep(4)
            cls()
            console.print("Made with 💙 by JojoXIX")
            console.print(tableHasil)
            console.print("Apakah ini seret?\nNggak, lu kurang bersyukur ☝️🤓", style="bold cyan")
            print("\n")
            input("Tekan enter untuk menutup...")
            cls()
            for i in track(range(20), description="Made with 💙 by JojoXIX"):
                tidur.sleep(0.05)
    elif response == 'n':
                cls()
                console.print("Made with 💙 by JojoXIX")
                console.print(tableHasil)
                console.print("Apakah ini seret?\nNggak, lu kurang bersyukur ☝️🤓", style="bold cyan")
                print("\n")
                input("Tekan enter untuk menutup...")
                cls()
                for i in track(range(20), description="Made with 💙 by JojoXIX"):
                    tidur.sleep(0.05)
    return Coin_value_c, Pixel_value_c

Coin_value, Pixel_value = get_input()
Hasil()
