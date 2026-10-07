station = "ST-01"
status = "STOP"
line = f"Állomás: {station} | Állapot: {status}"
if status == "STOP":
    line += "  <<< FIGYELEM: az állomás áll!"
print(line)
with open("andon.log", "a", encoding="utf-8") as log:
    log.write(line + "\n")