#!/usr/bin/env python
"""
Processes a received VOEvent packet.

Accept a VOEvent packet via standard input. Parse it using voeventparse,
then just print the IVORN, Author IVORN and authoring timestamp.

Can be tested at the command line by running (for example):

   cat test_packet.xml | ./process_voevent_from_stdin.py

"""

import sys
import voeventparse
import datetime


def main():
    stdin = sys.stdin.read()
    v = voeventparse.loads(stdin)
    handle_voevent(v)
    return 0

def handle_voevent(v):
    ivorn = v.attrib['ivorn']
    author_ivorn = v.Who.AuthorIVORN
    author_timestamp = v.Who.Date
    now = datetime.datetime.utcnow()
    print "At {0}, received VOEvent with IVORN {1}".format(now, ivorn)
    print "Authored by {0} at {1}".format(author_ivorn, author_timestamp)

if __name__ == '__main__':
    sys.exit(main())
