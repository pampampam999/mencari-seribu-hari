import datetime
import json
import subprocess

hariMeninggal = datetime.datetime(2023,5,7,18)

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
    current_date = now.strftime("%Y/%m/%d")
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

    
else:
    penjumlahanHari = 1
    print("Di atas jam 7 malam")

malamPertama =  hariMeninggal + datetime.timedelta(days=penjumlahanHari)


print("Malam pertama yaitu", malamPertama)
print("Malam kedua yaitu")

