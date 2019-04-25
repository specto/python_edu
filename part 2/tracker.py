import subprocess
import json
import threading
import time
from flask import Flask


NAMES = {
    "12:34:56:00:00:00": "Sample Device",
}
SCAN_INTERVAL = 10  # seconds

macs = []
app = Flask(__name__)


def get_macs():
    # sigkill is sent to all children,
    # so this will die and probably spew errors on stderr
    proc = subprocess.run(
        'sudo arp-scan -I wlp2s0 -l'.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL
    )

    lines = proc.stdout.decode().strip().split('\n')
    # remove pointless text
    lines = lines[2:-3]

    macs = [line.split('\t')[1] for line in lines]

    return macs


@app.route("/who/")
def get_users():
    return json.dumps([
        NAMES[mac]
        for mac in macs
        if mac in NAMES
    ])


class Scanner(threading.Thread):
    def __init__(self):
        super().__init__()
        # tell thread it's a daemon, so parent can exit
        self.daemon = True

    def run(self):
        global macs

        while True:
            macs = get_macs()
            time.sleep(SCAN_INTERVAL)


scanner = Scanner()
scanner.start()

# if thread is not daemon:
# first ^C kill the server, second one kills the scanner
# when scanner is a daemon it exits as soon as the server exits
# alternative: tell scanner it should exit, and join it

# flask traps KeyboardInterrupts and exits
app.run()
