import datetime
import json
import subprocess

hariMeninggal = datetime.datetime(2022,8,21,10)

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

malamPertama =  hariMeninggal + datetime.timedelta(days=penjumlahanHari)
malamKedua = malamPertama + datetime.timedelta(days=1)
malamKeTujuh = malamPertama +datetime.timedelta(days=5)
malamKeEmpatPuluh = malamPertama +datetime.timedelta(days=38)
malamKeSeratus = malamPertama +datetime.timedelta(days=98)
malamKeSeribu = malamPertama +datetime.timedelta(days=998)

print("Malam 1 yaitu", malamPertama.strftime("%d %B %Y"))
print("Malam 2 yaitu", malamKedua.strftime("%d %B %Y"))
print("Malam 7 yaitu", malamKeTujuh.strftime("%d %B %Y"))
print("Malam 40 yaitu", malamKeEmpatPuluh.strftime("%d %B %Y"))
print("Malam 100 yaitu", malamKeSeratus.strftime("%d %B %Y"))
print("Malam 1000 yaitu", malamKeSeribu.strftime("%d %B %Y"))

