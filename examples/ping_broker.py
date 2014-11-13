#!/usr/bin/env python
"""
Send a test packet to a remote broker, to verify that packet submission is
working correctly.
"""

import fourpiskytools
from fourpiskytools.identity import id_keys
import voeventparse

import logging
logging.basicConfig()

example_identity = {
    id_keys.address : 'voevent.organization.tld',
    id_keys.stream : 'ProjectFooAlerts',
    id_keys.shortName : 'ProjectFoo',
    id_keys.contactName : "Jo Bloggs",
    id_keys.contactEmail : "jb@observatory.org",
    }


## For testing with 4PiSky Broker:
## (You will need to contact us first about whitelisting your IP address)
# host = 'voevent.4pisky.org'

## For testing locally
## (must have an instance of Comet running and set to receive submissions, see:
## http://comet.transientskp.org/en/1.2.1/usage/broker.html#invoking-comet )
host = 'localhost'


test_packet = fourpiskytools.voevent.create_test_packet(example_identity)

# Dump a copy of the test packet to the current directory for manual inspection
with open('test_packet.xml','w') as f:
    voeventparse.dump(test_packet, f)

fourpiskytools.comet.send_voevent(test_packet, host=host)
