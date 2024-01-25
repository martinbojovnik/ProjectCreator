import os

if not os.path.exists("Profiles"):
    os.mkdir("Profiles")

if not os.path.exists("confi.conf"):
    with open("confi.conf") as fp:
        while True:
            dir = input("Write Projects Directory> ")
            try:
                if os.path.exists("dir"):
                    fp.write(f"path={dir}")
                    break
            except:
                pass
with open("confi.conf") as fp:
    config = fp.read().split("\n")

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

path = f"{config[0][5:]}/{name}"
os.mkdir(path)

f = open(f"./Profiles/{allFiles[ProfileToCreate-1]}")
commands = f.read().split("\n")
f.close()

for i in commands:
    com = i[:3]
    os.system(f"cd {path}")
    if com == "crd":
        os.mkdir(f"{path}/{i.replace(i[:4], '')}")
    elif com == "crf":
        with open(f"{path}/{i.replace(i[:4], '')}", 'w') as fp:
            pass
    elif com == "cmd":
        os.system(i.replace(i[:4], ''))