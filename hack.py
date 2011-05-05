#!/usr/bin/env python
# !!!!!!!!!!!!!!!!!!! 0-DAY DO NOT DISTRIBUTE !!!!!!!!!!!!!!!!!!!!
# THIS IS AN INTERNET HACKER PROGRAM, PLEASE USE WITH APPLE CARE
# MR DA PLAGUE <sOcKeT@GmAiL.CoM>

import socket
import struct
import random

import time, sys, math

class ProgressMeter(object):
    #ESC = chr(27)
    def __init__(self, **kw):
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
        return '[%s>%s] %d%%  %.1f/sec' % (bar, pad, perc, self.rate_current)

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


def detect_service(ip, port):
    m1 = ['integrated', 'total', 'systematized', 'balanced', 'parallel',
         'stealth', 'solid-state', 'mulching', 'xmas', 'malformed', 'slapper', 'king-kong', 'puffing']
    m2 = ['parcell','monitored', 'digital', 'logistical', 'quantum','penetrated', 'godzilla',
          'policy', 'incremental']
    m3 = ['recon', 'detection', 'lookup', 'scan-method', 'poke', 'finger', 'junk-punch', 'hooker']

    method = m1[random.randrange(0,len(m1))] + ' ' + \
             m2[random.randrange(0,len(m2))] + ' ' + \
             m3[random.randrange(0,len(m3))]
    
    s1 = ['internet', 'weblogic', 'id', 'web', 'ftp', 'xml', 'cloud', 'amazon', 'ebay', 'google']
    s2 = ['badger', 'sucker', 'apache', 'napster', 'fungus', 'meat']
    
    service = s1[random.randrange(0,len(s1))] + '-' + \
              s2[random.randrange(0,len(s2))] + ' daemon'

    return (method,service)
    
def log(type, msg):
    from datetime import datetime, date, time, timedelta
    if type == 'debug' and debug == 0:
        return
    if type == 'dev' and dev == 0:
        return
    ts = datetime.now()
    print "%s [%s]: %s" % ( ts.ctime(), type, msg )

def get_ip():
    max = 4294967295
    return socket.inet_ntoa(struct.pack('>L', socket.ntohl(random.randrange(1,max))))

def scan_ip(ip):
    max = 15 
    p = ProgressMeter(total=max)
    while max >= 0:
        p.update(1)
        max -= 1
        time.sleep(random.random())
    time.sleep(random.random())
    open_ports = random.randrange(0,
            random.randrange(1,25))
    if not open_ports:
        return None
    cnt = 0
    ret = {}
    while True:
        if cnt >= open_ports: 
            break
        num = random.randrange(0,65535)
        if not ret.has_key(num):
            ret[num] = 1 
            cnt += 1
    return ret.keys()
    
def check_for_feds():
    num_a = random.randrange(1, 4)
    num_b = random.randrange(1, 4)

    if num_a == num_b:
        return True 

    return False
    
def ping_ip(ip):
    n = random.randrange(0,4)
    if not n:
        time.sleep(random.random())
        return False
    return True

def hack_port(ip, port):
    max = 5
    p = ProgressMeter(total=max)
    while max >= 0:
        p.update(1)
        max -= 1
        time.sleep(random.random())

    return random.randrange(0, 2)
    
def kill_fed():
    kill_method = [ 'PING TIMED OUT',
                    'SHOT DOWN BY NORTH KOREA',
                    'EXPOSED BY WIKILEAKS',
                    'CALL TRACED AND EXPLODED',
                    'BLUESCREENED BY OVERHACK IDS LOCKING',
                    'TALK SESSION TERMINATED',
                    'ACCOUNT REMOVED BY COMPUSERVE',
                    'FIREWALLED FROM EGYPT'] 
    return kill_method[random.randrange(0, len(kill_method))]

def covert_action():
    action = [  'CALLING TAFT', 
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
                'MOUNTING FILESYSTEM READONLY']

    return action[random.randrange(0, len(action))]
                
def find_fed():
    feds = ['FBI', 'CIA', 'RIAA', 'AOL', 'SWEDEN', 'MADD', 'UUNET', 'NAMBLA', 'WALMART', 'PETA']

    return feds[random.randrange(0, len(feds))]


if __name__ == '__main__':

    banner = """
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

VERSION 1.1 BY MR DA PLAGUE!
    """

    owned = """
  ___                 _____     _ 
 / _ \__      ___ __ |___ /  __| |
| | | \ \ /\ / / '_ \  |_ \ / _` |
| |_| |\ V  V /| | | |___) | (_| |
 \___/  \_/\_/ |_| |_|____/ \__,_|
    """
    
    print banner
    while True:
        print ''
        log('HACKING INTERNET',"finding internet target...")
        ip = get_ip()
        log('HACKING INTERNET',"`- found internet target %s BEGIN INTERNET HACKING!" % ip)
        log('HACKING INTERNET','| `-  HACKING PING ON TARGET %s' % ip)
        if not ping_ip(ip):
            log('HACKING INTERNET','| `-  COULD NOT HACK A PING ON TARGET %s' % ip)
            continue
        log('HACKING INTERNET','| | `-  ATTEMPTING HACKING SCAN OF INTERNET PORTS ON TARGET %s' % ip)
        ports = scan_ip(ip)
        if not ports:
            log('HACKING INTERNET','| | `-  COULD NOT HACK INTERNET IP %s (NO HACKER SLOTS OPEN)' % ip)
            continue
        log('HACKING INTERNET','| | `-  %d INTERNET PORTS ON %s THAT MAY BE INTERNET HACKABLE!1!!1' % \
            (len(ports), ip))
        log('HACKING INTERNET','| | `-  BEGNINNING INTERNET HACKING OF PORTS ON %s' % (ip))
        for port in ports:
            (method,service) = detect_service(ip,port)
            log('HACKING INTERNET', '| | | `-   DETECTED SERVICE %s on %d using HACKER METHOD: %s' % (service, port, method))
            log('HACKING INTERNET', '| | | `-   Attempting Transmission Control Protocol hacking of' \
                ' port %d on host %s' % (port, ip)) 
            if hack_port(ip, port):
                log('HACKING INTERNET', '| | | | `-  %s:%d WAS SUCCESSFULLY INTERNET HACKERED!' % (ip, port))
                log('HACKING INTERNET', '| | | | `-     ___                 _____     _')
                log('HACKING INTERNET', '| | | | `-    / _ \__      ___ __ |___ /  __| |')
                log('HACKING INTERNET', '| | | | `-   | | | \ \ /\ / / \'_ \  |_ \ / _` |') 
                log('HACKING INTERNET', '| | | | `-   | |_| |\ V  V /| | | |___) | (_| |')
                log('HACKING INTERNET', '| | | | `-    \___/  \_/\_/ |_| |_|____/ \__,_|')
                log('HACKING INTERNET', '| | | |')
                # print owned
                continue
            else:
                log('HACKING INTERNET', '| | | | `-  %s:%d COULD NOT BE TCP INTERNET HACKED!' % (ip, port))

            if check_for_feds() == True:
                fed    = find_fed()
                action = covert_action()
                how    = kill_fed()
                
                log('HACKING INTERNET', '| | | | `- **************************************************************')
                log('HACKING INTERNET', '| | | | `- * WARNING WARNING WARNING WARNING WARNING WARNING WARNING WA *')
                log('HACKING INTERNET', '| | | | `- **************************************************************')
                log('HACKING INTERNET', '| | | | `- DETECTED %s MONITORING OUR HACKING, ATTEMPTING COVERT ACTIONS!' % fed) 
                log('HACKING INTERNET', '| | | | | `-  %s...' % action)
                hack_port(1, 1)
                log('HACKING INTERNET', '| | | | | `-  ZOOMING IN...') 
                hack_port(1, 1)
                log('HACKING INTERNET', '| | | | | `-  ENHANCING...')
                hack_port(1, 1)
                log('HACKING INTERNET', '| | | | | `-  %s %s!!!!!' % (fed, how))


