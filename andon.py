import sys
from datetime import datetime

station = "ST-01"
status = sys.argv[1] if len(sys.argv) > 1 else "RUN"
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
line = f"{time} | Állomás: {station} | Állapot: {status}"
if status == "STOP":
    line += "  <<< WARNING: station stopped! Call maintenance."
elif status == "WAIT":
    line += "  <<< Várakozás anyagra"
elif status == "IDLE":
    line += "  <<< Idle: no order"
print(line)
with open("andon.log", "a", encoding="utf-8") as log:
    log.write(line + "\n")
