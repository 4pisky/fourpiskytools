#!/usr/bin/env python
"""
Processes a received VOEvent packet.

Accept a VOEvent packet via standard input. Parse it using voeventparse,
then decide what kind of packet it is, and what to do accordingly.
(In this example, we just write notifications to the desktop / print to the
command line in all cases, but you could imagine triggering different
telescopes, emailing different people, etc.)

Can be tested at the command line by running (for example):

   cat test_packet.xml | ./process_voevent_from_stdin.py

"""

import sys
import voeventparse

import logging
logging.basicConfig(filename='script2.log',level=logging.INFO)
logger = logging.getLogger('notifier')
logger.handlers.append(logging.StreamHandler(sys.stdout))

from fourpiskytools.notify import Notifier

def main():
    stdin = sys.stdin.read()
    v = voeventparse.loads(stdin)
    handle_voevent(v)
    return 0

def handle_voevent(v):
    if is_grb(v):
        handle_grb(v)
    elif is_ping_packet(v):
        handle_ping_packet(v)
    else:
        handle_other(v)

def is_grb(v):
    ivorn = v.attrib['ivorn']
    if ivorn.find("ivo://nasa.gsfc.gcn/SWIFT#BAT_GRB_Pos") == 0:
        return True
    return False

def is_ping_packet(v):
    ivorn = v.attrib['ivorn']
    role = v.attrib['role']
    ivorn_tail = ivorn.rsplit('/', 1)[-1]
    stream = ivorn_tail.split('#')[0]
    if ( role == voeventparse.definitions.roles.test and
         stream == 'TEST'
        ):
        return True
    return False

def handle_grb(v):
    ivorn = v.attrib['ivorn']
    coords = voeventparse.pull_astro_coords(v)
    text = "Swift packet received, coords are {}".format(coords)
    n = Notifier()
    n.send_notification(title="NEW SWIFT GRB!",
                        text=text)
    handle_other(v)

def handle_ping_packet(v):
    n = Notifier()
    n.send_notification(title="Ping!",
                        text="Packet received matches 'ping packet' filter.")
    handle_other(v)

def handle_other(v):
    ivorn = v.attrib['ivorn']
    n = Notifier()
    n.send_notification(title="VOEvent received",
                        text="IVORN: "+ivorn)

if __name__ == '__main__':
    sys.exit(main())
