station = "ST-01"
status = "RUN"
line = f"Állomás: {station} | Állapot: {status}"
print(line)
with open("andon.log", "a", encoding="utf-8") as log:
    log.write(line + "\n")