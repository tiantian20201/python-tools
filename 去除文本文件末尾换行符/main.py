txt = ""
with open("get.txt",encoding="utf-8") as f:
    while True:
        line = f.readline().strip("'\n")
        if not line:
            break
        txt += "url." + line.strip() +" = item.get('"+line.strip()+"')," + "\n"


'url.page=item.get(page)'
print(txt)
with open("res.txt","w") as file:
    file.write(txt)
