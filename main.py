import os

if not os.path.exists("Profiles"):
    os.mkdir("Profiles")

allFiles = os.listdir("Profiles")
if not allFiles == []:
    for num, i in enumerate(allFiles):
        if i.endswith('.prof'):
            print(f"{num+1}: {i.replace('.prof', '')}")
else:
    print("No Profiles Found")
    exit()

while True:
    print("")
    inp = input("> ")
    try:
        if int(inp) <= len(allFiles):
            break
    except:
        pass

ProfileToCreate = int(inp)

while True:
    print("")
    name = input("NameOfTheProject> ")
    if not name == "":
        break

path = f"C:/Users/marti/Desktop/MyPrograms/{name}"
os.mkdir(path)

f = open(f"./Profiles/{allFiles[ProfileToCreate-1]}")
commands = f.read().split("\n")
f.close()

for i in commands:
    com = i[:3]
    if com == "crd":
        os.mkdir(f"{path}/{i.replace(i[:4], '')}")