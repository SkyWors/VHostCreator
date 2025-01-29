import os

domain = input("Domaine : ")
path = input("Chemin : ")

template = open("template.conf", "r").read()

template = template.replace("{domain}", domain)
template = template.replace("{path}", path)

with open("/etc/apache2/sites-available/" + domain + ".conf", "w") as file:
	file.write(template)

try:
	os.symlink("/etc/apache2/sites-available/" + domain + ".conf", "/etc/apache2/sites-enabled/" + domain + ".conf")
except Exception:
	print("Le lien symbolique existe déjà.")

with open("/etc/hosts", "a") as file:
	file.write("127.0.0.1\t" + domain + "\n")

os.system("systemctl reload apache2")
