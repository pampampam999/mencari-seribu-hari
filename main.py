#import datetime
from datetime import date,timedelta,datetime
import json
import subprocess
from time import strftime

d1 = date(1900, 1, 1)

hari = [
  'senin',
  'selasa',
  'rabu',
  'kamis',
  'jum`at',
  'sabtu',
  'minggu'
]

pasaran = [
  'pahing',
  'pon',
  'wage',
  'kliwon',
  'legi'
]

# constant variable for coloring output
TXT_WHITE = "\033[1;37m"
TXT_GRAY = "\033[0;37m"
TXT_CYAN = "\033[0;36m"
TXT_PURPLE = "\033[0;35m"
TXT_BLUE = "\033[0;34m"
TXT_YELLOW = "\033[0;33m"
TXT_BOLD_GREEN = "\033[1;32m"
TXT_BOLD_RED = "\033[0;31m"
TXT_DEFAULT = "\033[0m"
TXT_BOLD_DEFAULT = "\033[1;39m"

# formula untuk mencari pasaran https://github.com/lantip/pasaran/blob/master/weton.py
def pasaran_formula(dateinput):
    datebase    = datetime.strptime('1 1 1800', '%d %m %Y')

    # find the difference between now and base date, in days
    if dateinput > datebase:
        diff        = dateinput - datebase
    else:
        diff    = datebase - dateinput
    diffdays    = diff.days

    # find the modulo by 5
    modulo      = diffdays % 5
    return modulo

# formula untuk mencari weekday https://github.com/lantip/pasaran/blob/master/weton.py
def WeekFinder(weekday, pasar, year):
    WEEK    = {'senin':0,'selasa':1,'rabu':2,'kamis':3,'jumat':4,'sabtu':5,'minggu':6}
    MONTH   = {'januari':1,'februari':2,'maret':3,'april':4,'mei':5,'juni':6,\
    'juli':7,'agustus':8,'september':9,'oktober':10,'november':11,'desember':12}
    PASARAN = {'pon':0, 'wage':1, 'kliwon':2, 'legi':3, 'pahing':4}

    year    = int(year)
    day     = WEEK[weekday]
    month   = MONTH['januari']
    dt      = date(year,int(month),1)
    dow_lst = []
    while dt.weekday() != day:
        dt = dt + timedelta(days=1)
    lst_month = MONTH.values()
    #lst_month.sort()
    for mont in lst_month:
        while dt.month == mont:
            modulo = pasaran_formula(datetime.combine(dt,datetime.min.time()))
            if modulo == PASARAN[pasar]:
                dow_lst.append(dt)
            dt = dt + timedelta(days=7)
    return dow_lst


def mencari_pasaran(pasaran,tahun):
    var = pasaran.split()
    #year        = input('Mencari pasaran di Tahun: '+'\n')
    year        = tahun
    listdays    = WeekFinder(var[0].lower(), var[1].lower(), year)
    for key,day in enumerate(listdays):
        #print(day) # type datetime.date
        # print(key)
        #print (TXT_YELLOW+var[0]+" "+var[1]+TXT_DEFAULT+" ("+str(key)+") :")
        print(str(day)+" "+var[0]+" "+var[1]+"")

def main():
    # Input
    hariMeninggal = datetime(2022,8,21,6)
    print(hariMeninggal.strftime('%d %m %Y %H:%M:%S'))


    #Perhitungan
    # 7 Hari
    penjumlahanHari = 0
    if int(hariMeninggal.strftime('%H')) < 17:
        penjumlahanHari = 0
        print("Sebelum Jam Lima")
    elif int(hariMeninggal.strftime('%H')) >17 and int(hariMeninggal.strftime('%H')) < 19:
        print("Dianta jam 5 dan jam 7 malam")
        
        now = datetime.datetime.now()
        #current_date = now.strftime("%Y/%m/%d")
        current_date = hariMeninggal.strftime("%Y/%m/%d") #modif
        jakarta_city_code = "1301"
        result = subprocess.run(["curl", f"https://api.myquran.com/v1/sholat/jadwal/{jakarta_city_code}/{current_date}"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        result_json = json.loads(result.stdout)
        # print(result_json["data"]["lokasi"])
        # print(result_json["data"]["daerah"])
        # print(f'Hari/Tanggal: {result_json["data"]["jadwal"]["tanggal"]}')
        # print(f'- imsak {result_json["data"]["jadwal"]["imsak"]}')
        # print(f'- subuh {result_json["data"]["jadwal"]["subuh"]}')
        # print(f'- terbit {result_json["data"]["jadwal"]["terbit"]}')
        # print(f'- dhuha {result_json["data"]["jadwal"]["dhuha"]}')
        # print(f'- dzuhur {result_json["data"]["jadwal"]["dzuhur"]}')
        # print(f'- ashar {result_json["data"]["jadwal"]["ashar"]}')
        # print(f'- maghrib {result_json["data"]["jadwal"]["maghrib"]}') #Ini saja yang  di pakai
        # print(f'- isya {result_json["data"]["jadwal"]["isya"]}')

        waktuMaghrib = result_json["data"]["jadwal"]["maghrib"]
        waktuMaghrib = waktuMaghrib.split(':')
        print(waktuMaghrib)

        #apakah sesudah maghrib?
        if int(hariMeninggal.strftime("%H")) == int(waktuMaghrib[0]):
            print("Waktu sama di lanjut pengecekan menit")
            #Pengecekan menit
            if int(hariMeninggal.strftime("%M")) >= int(waktuMaghrib[1]):
                print("Setelah waktu maghrib")
                penjumlahanHari = 1
        elif int(hariMeninggal.strftime("%H")) > int(waktuMaghrib[0]):
            print("Setelah waktu maghrib")
            penjumlahanHari = 1
        else:
            print("Kurang dari waktu maghrib")


    else:
        penjumlahanHari = 1
        print("Di atas jam 7 malam")

    #perhitungan selisih
    d0 = date(22,8,21)
    beda = d0 - d1
    #print(beda.days)

    #menentukan hari
    harike = (beda.days) % 7

    #menentukan pasaran
    pasaranke = (beda.days) % 5

    print(hari[harike],pasaran[pasaranke])

    malamPertama =  hariMeninggal + timedelta(days=penjumlahanHari)
    malamKedua = malamPertama + timedelta(days=1)
    malamKeTujuh = malamPertama +timedelta(days=5)
    malamKeEmpatPuluh = malamPertama +timedelta(days=38)
    malamKeSeratus = malamPertama +timedelta(days=98)
    malamKeSeribu = malamPertama +timedelta(days=998)

    print("Malam 1 yaitu", malamPertama.strftime("%d %B %Y"))
    print("Malam 2 yaitu", malamKedua.strftime("%d %B %Y"))
    print("Malam 7 yaitu", malamKeTujuh.strftime("%d %B %Y"))
    print("Malam 40 yaitu", malamKeEmpatPuluh.strftime("%d %B %Y"))
    print("Malam 100 yaitu", malamKeSeratus.strftime("%d %B %Y"))
    print("Malam 1000 yaitu", malamKeSeribu.strftime("%d %B %Y"))

    #mecnari pasaran pada tahun tertentu
    mencari_pasaran("minggu wage",2024)

# PR
# https://tjerdastangkas.blogspot.com/2011/06/program-konversi-kalender-masehi.html
#