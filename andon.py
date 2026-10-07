from datetime import datetime

station = "ST-01"
status = "WAIT"
time = datetime.now().strftime("%Y-%m-%d %H:%M:%M")
line = f"{time} | Állomás: {station} | Állapot: {status}"
if status == "STOP":
    line += "  <<< WARNING: station stopped!"
elif status == "WAIT":
    line += "  <<< Várakozás anyagra"
print(line)
with open("andon.log", "a", encoding="utf-8") as log:
    log.write(line + "\n")
