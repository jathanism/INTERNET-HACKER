#!/usr/bin/env python

# !!!!!!!!!!!!!!!!!!! 0-DAY DO NOT DISTRIBUTE !!!!!!!!!!!!!!!!!!!!
# THIS IS AN INTERNET HACKER PROGRAM, PLEASE USE WITH APPLE CARE
# MR DA PLAGUE <sOcKeT@GmAiL.CoM>
# MINICOM <JaTHaN@gGMaiL.CoM>

__version__ = '1.5'
__author__ = 'MR DA PLAGUE'

import datetime
import socket
import struct
import random
import time
import sys


################
# Hacking Type #
################
#LOG_TYPE = 'HACKING INTERNET'
LOG_TYPE = 'HAXORING'

##################
# Attack Methods #
##################
# These should be "descriptive"  words (aka adjectives)
METHOD_PRE = (
    'integrated',
    'total',
    'systematized',
    'balanced',
    'parallel',
    'stealth',
    'solid-state',
    'mulching',
    'xmas',
    'malformed',
    'slapper',
    'king-kong',
    'puffing',
    'satellite',
    'multiprocessing',
    'multithreaded',
)
# These should be "business" words 
METHOD_MID = (
    'parcell',
    'monitored',
    'digital',
    'logistical',
    'quantum',
    'penetrated',
    'godzilla',
    'policy',
    'incremental'
    'cloud',
    'webscale',
    'mapreduced',
)
# These should be "action" words"
METHOD_END = (
    'recon',
    'detection',
    'lookup',
    'scan-method',
    'poke',
    'finger',
    'junk-punch',
    'hooker',
    'probulator',
    'finglonger',
)

#################
# Service Names #
#################
# These should be "actual" services
SERVICE_PRE = (
    'internet',
    'weblogic',
    'id',
    'web',
    'ftp',
    'xml',
    'cloud',
    'amazon',
    'ebay',
    'google'
)
# And these should just be ridiculous
SERVICE_END = (
    'badger',
    'sucker',
    'apache',
    'napster',
    'fungus',
    'meat',
)

################
# Action Names #
################
ACTIONS = (
    'CALLING TAFT',
    'LOGGING OFF IRC',
    'MOVING FUNDS INTO SWISS BANK ACCOUNT',
    'GAINING EYE OF THE TIGER',
    'REBOOTING ROUTERS',
    'USING PGP',
    'HIDING',
    'UPLOADING SPACE JAM', 
    'EMPTYING TRASHCAN', 
    'SENDING MSG_OOB', 
    'CALCULATING SENDMAIL AXIS',
    'MOUNTING FILESYSTEM READONLY',
    'RETICULATING SPLINES',
)

#############
# Fed Names #
#############
# Come on, be creative!
FEDS = (
    'FBI',
    'CIA',
    'RIAA',
    'AOL',
    'SWEDEN',
    'MADD',
    'UUNET',
    'NAMBLA',
    'WALMART',
    'PETA',
    'MPAA',
    'CERN',
    'NWA'
)

################
# Kill Methods #
################
KILL_METHODS = ( 
    'PING TIMED OUT',
    'SHOT DOWN BY NORTH KOREA',
    'EXPOSED BY WIKILEAKS',
    'CALL TRACED AND EXPLODED',
    'BLUESCREENED BY OVERHACK IDS LOCKING',
    'TALK SESSION TERMINATED',
    'ACCOUNT REMOVED BY COMPUSERVE',
    'FIREWALLED FROM EGYPT',
    'CONNECTION TIMED OUT',
    'FIREWALL 60% GONE',
    'HACKED BY CHINESE',
)

###########
# Banners #
###########
TAG = 'VERSION {0} BY {1}'.format(__version__, __author__)
BANNER = """
 ___ _   _ _____ _____ ____  _   _ _____ _____ 
|_ _| \ | |_   _| ____|  _ \| \ | | ____|_   _|
 | ||  \| | | | |  _| | |_) |  \| |  _|   | |  
 | || |\  | | | | |___|  _ <| |\  | |___  | |  
|___|_| \_| |_| |_____|_| \_\_| \_|_____| |_|  
                                               
 _   _    _    __  _____  ____  
| | | |  / \   \ \/ / _ \|  _ \ 
| |_| | / _ \   \  / | | | |_) |
|  _  |/ ___ \  /  \ |_| |  _ < 
|_| |_/_/   \_\/_/\_\___/|_| \_\

{tag}
""".format(tag=TAG)

OWNED = """
  ___                 _____     _ 
 / _ \__      ___ __ |___ /  __| |
| | | \ \ /\ / / '_ \  |_ \ / _` |
| |_| |\ V  V /| | | |___) | (_| |
 \___/  \_/\_/ |_| |_|____/ \__,_|
"""
    

# Classes
class ProgressMeter(object):
    """
    A progress meter. Duh.
    """
    def __init__(self, **kw):
        # What message do we want to display?
        self.message = kw.get('message', '')
        if self.message:
            self.message += ' '
        # What time do we start tracking our progress from?
        self.timestamp = kw.get('timestamp', time.time())
        # What kind of unit are we tracking?
        self.unit = str(kw.get('unit', ''))
        # Number of units to process
        self.total = int(kw.get('total', 100))
        # Number of units already processed
        self.count = int(kw.get('count', 0))
        # Refresh rate in seconds
        self.rate_refresh = float(kw.get('rate_refresh', .5))
        # Number of ticks in meter
        self.meter_ticks = int(kw.get('ticks', 60))
        self.meter_division = float(self.total) / self.meter_ticks
        self.meter_value = int(self.count / self.meter_division)
        self.last_update = None
        self.rate_history_idx = 0
        self.rate_history_len = 10
        self.rate_history = [None] * self.rate_history_len
        self.rate_current = 0.0
        self.last_refresh = 0
        self.prev_meter_len = 0

    def update(self, count, **kw):
        now = time.time()
        # Caclulate rate of progress
        rate = 0.0
        # Add count to Total
        self.count += count
        self.count = min(self.count, self.total)
        if self.last_update:
            delta = now - float(self.last_update)
            if delta:
                rate = count / delta
            else:
                rate = count
            self.rate_history[self.rate_history_idx] = rate
            self.rate_history_idx += 1
            self.rate_history_idx %= self.rate_history_len
            cnt = 0
            total = 0.0
            # Average rate history
            for rate in self.rate_history:
                if rate == None:
                    continue
                cnt += 1
                total += rate
            rate = total / cnt
        self.rate_current = rate
        self.last_update = now
        # Device Total by meter division
        value = int(self.count / self.meter_division)
        if value > self.meter_value:
            self.meter_value = value
        if self.last_refresh:
            if (now - self.last_refresh) > self.rate_refresh or \
                (self.count >= self.total):
                    self.refresh()
        else:
            self.refresh()

    def get_meter(self, **kw):
        bar = '-' * self.meter_value
        pad = ' ' * (self.meter_ticks - self.meter_value)
        perc = (float(self.count) / self.total) * 100
        message = self.message
        #return '[%s>%s] %d%%  %.1f/sec' % (bar, pad, perc, self.rate_current)
        return '%s[%s>%s] %d%%  %.1f/sec' % (message, bar, pad, perc, self.rate_current)

    def refresh(self, **kw):
        # Clear line and return cursor to start-of-line
        #if self.count >= self.total:
        #    sys.stdout.write('\n')
        #    return

        sys.stdout.write(' ' * self.prev_meter_len + '\x08' * self.prev_meter_len)
        # Get meter text
        meter_text = self.get_meter(**kw)
        # Write meter and return cursor to start-of-line
        sys.stdout.write(meter_text + '\x08'*len(meter_text))
        self.prev_meter_len = len(meter_text)

        # Are we finished?
        #if self.count >= self.total:
        #    sys.stdout.write('\n')

        sys.stdout.flush()
        # Timestamp
        self.last_refresh = time.time()


# Functions
def detect_service():
    """
    Generate a random attack method and service and go to town!
    """
    method = ' '.join(random.choice(m) for m in (METHOD_PRE, METHOD_MID, METHOD_END)) 
    service = ' '.join(random.choice(s) for s in (SERVICE_PRE, SERVICE_END)) + ' daemon'
    
    return method, service
    
def log(msg, log_type=LOG_TYPE):
    ts = datetime.datetime.now()
    print "%s [%s]: %s" % (ts.ctime(), log_type, msg)

def get_ip():
    """Generate a random IP address for attack vector."""
    max = 4294967295
    return socket.inet_ntoa(struct.pack('>L', socket.ntohl(random.randrange(1,max))))

def scan_ip(ip, max=15):
    """
    Scans an IP. Detects and returns a set of open ports.
    """
    # Update progress with the fancy bar!
    msg = 'SCANNING'
    progress = ProgressMeter(message=msg, total=max)
    while max >= 0:
        progress.update(1)
        max -= 1
        time.sleep(random.random())

    # Sleep randomly to throw off our victim!
    time.sleep(random.random())
    open_ports = random.randrange(0, random.randrange(1,25))

    # Retun if 
    if not open_ports:
        return None

    # Collect open ports. Keep going til we get max # unique.
    portset = set()
    while True:
        cnt = len(portset)
        if cnt >= open_ports: 
            break
        portnum = random.randrange(0,65535)
        portset.add(portnum)

    return portset
    
def check_for_feds():
    num_a = random.randrange(1, 4)
    num_b = random.randrange(1, 4)

    return num_a == num_b
    
def ping_ip(ip):
    """Pings an IP, duh. Sleeps randomly if it fails. Duh."""
    n = random.randrange(0,4)
    if not n:
        time.sleep(random.random())
        return False
    return True

def hack_port(max=5):
    """Hacks a ping on IP:port. Serious business."""
    msg = 'HACKING'
    progress = ProgressMeter(message=msg, total=max)
    while max >= 0:
        progress.update(1)
        max -= 1
        time.sleep(random.random())

    return random.randrange(0, 2)
    
def kill_fed():
    """Kills a Fed. Dope!"""
    return random.choice(KILL_METHODS)

def covert_action():
    """Determine a covert action! Secret Squirrel."""
    return random.choice(ACTIONS)
                
def find_fed():
    """Retrieve a Fed to be killed later. Hopefully."""
    return random.choice(FEDS)

def hack(ip):
    """
    Hacks an Internet IP. Use with caution!!
    """
    # So we can tell each hack apart
    print 
    log("Finding Internet target...")
    log("`- Found Internet target %s BEGIN INTERNET HACKING!" % ip)

    # Try to hack a ping!
    log('| `- HACKING PING ON TARGET: %s' % ip)
    if not ping_ip(ip):
        log('| `- COULD NOT HACK A PING ON TARGET %s' % ip)
        return

    # Try to hack a scan!
    log('| | `- ATTEMPTING HACKING SCAN OF INTERNET PORTS ON TARGET %s' % ip)
    ports = scan_ip(ip)
    if not ports:
        log('| | `- COULD NOT HACK INTERNET IP %s (NO HACKER SLOTS OPEN)' % ip)
        return

    # Ok we're ready to hack!
    log('| | `- %d INTERNET PORTS ON %s THAT MAY BE INTERNET HACKABLE!1!!1' % (len(ports), ip))
    log('| | `- BEGNINNING INTERNET HACKING OF PORTS ON %s' % (ip))

    # Iterate ports and go to town!!
    for port in ports:
        # Let's get a service and choose the right hacker method
        method, service = detect_service()
        log('| | | `- SERVICE DETECTED: %s on port %d' % (service, port))
        log('| | | `- HACKER METHOD: %s' % method)
        log('| | | `- Attempting TCP hacking of port %d on host %s' % (port, ip)) 

        # Aww yeah we got one!
        if hack_port():
            log('| | | | `- %s:%d WAS SUCCESSFULLY INTERNET HACKERED!' % (ip, port))
            log('| | | | `-    ___                 _____     _ ')
            log('| | | | `-   / _ \__      ___ __ |___ /  __| |')
            log("| | | | `-  | | | \ \ /\ / / '_ \  |_ \ / _` |") 
            log('| | | | `-  | |_| |\ V  V /| | | |___) | (_| |')
            log('| | | | `-   \___/  \_/\_/ |_| |_|____/ \__,_|')
            log('| | | |')
            return

        # Or not (sad face)
        else:
            log('| | | | `- %s:%d COULD NOT BE TCP INTERNET HACKED!' % (ip, port))

        # Beware of feds!!
        if check_for_feds():
            fed = find_fed()
            action = covert_action()
            how  = kill_fed() # Serious business.
                
            # FUCK!!!
            log( '| | | | `- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            log( '| | | | `- ! WARNING WARNING WARNING WARNING WARNING WARNING WARNING !')
            log( '| | | | `- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            log( '| | | | `- DETECTED %s MONITORING OUR HACKING, ATTEMPTING COVERT ACTIONS!' % fed) 
            log( '| | | | | `- %s...' % action)
            hack_port()
            log( '| | | | | `- ZOOMING IN...') 
            hack_port()
            log( '| | | | | `- ENHANCING...')
            hack_port()

            # Whew!
            log( '| | | | | `- %s %s!!!!!' % (fed, how))

def main():
    """So elegant."""
    print BANNER

    while True:
        ip = get_ip()
        hack(ip)

if __name__ == '__main__':
    main()
