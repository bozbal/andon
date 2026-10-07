from datetime import datetime

station = "ST-01"
status = "WAIT"
<<<<<<< HEAD
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
=======
time = datetime.now().strftime("%Y-%m-%d %H:%M:%M")
>>>>>>> 864b652 (feat: add timesatmp to status line)
line = f"{time} | Állomás: {station} | Állapot: {status}"
if status == "STOP":
    line += "  <<< FIGYELEM: az állomás áll!"
elif status == "WAIT":
    line += "  <<< Várakozás anyagra"
print(line)
with open("andon.log", "a", encoding="utf-8") as log:
    log.write(line + "\n")