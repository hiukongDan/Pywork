import time
import sys
from os import system

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        system.exit("Usage: timerTest duration")
        
    duration = sys.argv[1]
    time.sleep(int(duration))
    print('\a')