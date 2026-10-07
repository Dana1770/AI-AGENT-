import time

LOG_FILE = "/home/dana/odoo.log"
def tail_logs():
    with open(LOG_FILE, "r") as file:
        file.seek(0, 2)

        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue

            if "ERROR" in line or "Traceback" in line:
                yield line