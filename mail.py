import os,json,random
from time import sleep
try :
      import requests
      from colorama import init,Fore
except ImportError:
      print("\r[!] Module not installed",end=" ",flush=True)
      sleep(2)
      print("\r[↓] Installing module…",end=" ",flush=True)
      os.system("pip install -r requirements.txt")
      sleep(2)
      print(f"\r[√] Done!",end=" ",flush=True)
      sleep(2)
      os.system("python mail.py")

#Color
init(autoreset=True)
W = Fore.WHITE
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
R = Fore.RED
L = "\033[1;97m"
rgb = random.choice([G,Y,C])
#MainCode

def clear():
    os.system("clear")

def baris():
    print(f"{R}－"*27)

def back():
    input(f"{W}[  {rgb}Press Enter To Back  {W}]")
    sleep(2)
    os.system("python mail.py")

def banner():
    clear()
    print(f"""{L}
             {rgb}╔╦╗{W}┌─┐┌┬┐┌─┐  {rgb}╔╦╗ {W}┌─┐ ┬ ┬
              {rgb}║ {W}├┤ │││├─┘  {rgb}║║║ {W}├─┤ │ │
              {rgb}╩ {W}└─┘┴ ┴┴    {rgb}╩ ╩ {W}┴ ┴ ┴ ┴─┘
              {rgb}https://github.com/AinxBOT""")
    baris()

class Temp:
    def __init__(self,basetoken):
        self.ua = {"host": "mob2.temp-mail.org","authorization": basetoken,"user-agent": "4.01","accept": "application/json","accept-encoding": "gzip"}
        self.ses = requests.Session()
        self.ses.headers.update(self.ua)
    def get_mail(self):
        try :
             req = self.ses.get("https://mob2.temp-mail.org/mailbox").text
             if "@" in str(req):
                 return json.loads(req)["mailbox"]
             else:
                 exit(f"{R}[!] Please generate new mail")
        except Exception as e:
             exit(f"{R}[!] {W}Program stopped : {rgb}{e}")
    def new_mail(self):
        try :
             req = self.ses.post("https://mob2.temp-mail.org/mailbox").text
             if "@" in str(req):
                 token = json.loads(req)["token"]
                 with open("token.txt","w") as tkn:
                      tkn.write(token)
                 self.ses.headers.update({"authorization":token})
                 return json.loads(req)["mailbox"]
             else:
                 exit(f"{R}[!] Failed generate new mail")
        except Exception as e:
             exit(f"{R}[!] {W}Program stopped : {rgb}{e}")
    def get_inbox(self):
        try :
             req = self.ses.get("https://mob2.temp-mail.org/messages").text
             if '"messages":[]' in str(req):
                 print(f"{R}[!] {W}No messages yet.")
                 baris()
                 while True:
                      lagi = input(f"{rgb}[?] {W}Reload? {W}({rgb}Y{W}/{rgb}N{W}) : {rgb}")
                      if lagi == "Y" or lagi == "y":
                         mail.get_inbox()
                      else:
                         exit(f"{R}[!] {W}Program stopped")
             else:
                 print(f"{rgb}[📥] {W}List inbox : {rgb}{json.loads(req)['mailbox']}")
                 for x in json.loads(req)["messages"]:
                     print (f"{rgb}[>>] {W}From : {rgb}{x['from'].replace('<','(').replace('>',')')}\n[>>] {W}subject : {rgb}{x['subject']}\n[>>] {W}Message : {rgb}{x['bodyPreview']}")
                     baris()
                 while True:
                      lagi = input(f"{rgb}[?] {W}Reload? {W}({rgb}Y{W}/{rgb}N{W}) : {rgb}")
                      if lagi == "Y" or lagi == "y":
                         mail.get_inbox()
                      else:
                         exit(f"{G}[√] {W}Program finished")
        except Exception as e:
             exit(f"{R}[!] {W}Program stopped : {rgb}{e}")

def menu():
    print(f"{rgb}01). {W}Get email\n{rgb}02). {W}New email\n{rgb}03). {W}Get inbox\n{rgb}00). {W}Exit")
    pilih = input(f"{rgb}[?] {W}>>  {rgb}")
    baris()
    if pilih == "01" or pilih == "1":
       print(f"{rgb}[!] {W}Copy the email address below…\n{G}[√] {W}Email : {rgb}{mail.get_mail()}")
       baris()
       back()
    elif pilih == "02" or pilih == "2":
       new = mail.new_mail()
       print(f"{rgb}[!] {W}Copy the new email address below…\n{G}[√] {W}Email : {rgb}{new}")
       baris()
       back()
    elif pilih == "03" or pilih == "3":
       mail.get_inbox()
    elif pilih == "00" or pilih == "0":
       exit(f"{G}[√] {W}Program closed")
    else:
       print(f"{R}[!] {W}Wrong input")
       sleep(2)
       os.system("python mail.py")
if __name__=="__main__":
    banner()
    try :
          tkn = open("token.txt","r").read()
          mail = Temp(tkn)
    except FileNotFoundError:
          tkn = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiMWU5MDE3M2UzYzVlNDg0YTg0MjM5ZWRiMDdiYTI1ODgiLCJtYWlsYm94IjoicGVraXhvNDgxOEB0YWNpbWFpbC5jb20iLCJpYXQiOjE3NTE0Njk3MTN9.IElozw8nOo129S_wAyOKyYGrqhCTiWfkMa4hmYGyOs8"
          mail = Temp(tkn)
          new = mail.new_mail()
    menu()
