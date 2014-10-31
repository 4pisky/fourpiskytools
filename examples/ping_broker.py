"""
Send a test packet to a remote broker, to verify that packet submission is
working correctly.
"""

import fourpiskytools
from fourpiskytools.identity import id_keys

example_identity = {
    id_keys.address : 'voevent.organization.tld',
    id_keys.stream : 'ProjectFooAlerts',
    id_keys.shortName : 'ProjectFoo',
    id_keys.contactName : "Jo Bloggs",
    id_keys.contactEmail : "jb@observatory.org",
    }


#For testing with 4PiSky Broker:
# host = 'voevent.4pisky.org'

#For testing locally
# (must have an instance of Comet running, see:
# http://comet.transientskp.org/en/1.2.1/usage/broker.html#invoking-comet )
host = 'localhost'


test_packet = fourpiskytools.voevent.create_test_packet(example_identity)
fourpiskytools.comet.send_voevent(test_packet, host=host)
