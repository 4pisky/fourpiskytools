#!/usr/bin/env python
"""
Send an alert containing sky co-ordinates to a remote broker.
"""

import fourpiskytools
from fourpiskytools.identity import id_keys
from fourpiskytools.voevent import create_basic_location_alert
import voeventparse as vp
from datetime import datetime
import pytz

example_identity = {
    id_keys.address : 'voevent.organization.tld',
    id_keys.stream : 'ProjectFooAlerts',
    id_keys.shortName : 'ProjectFoo',
    id_keys.contactName : "Jo Bloggs",
    id_keys.contactEmail : "jb@observatory.org",
    }


#For submitting a packet to the 4PiSky Broker:
# host = 'voevent.4pisky.org'

# For testing locally
# (must have an instance of Comet running, see:
# http://comet.transientskp.org/en/1.2.1/usage/broker.html#invoking-comet )
host = 'localhost'


# Event generated by some telescope-data processing pipeline...
# Dummy values:
ra,dec = 90.0,-45.0
positional_error = 0.1 #degrees error radius
event_datetime = datetime(year=2000,month=1,day=1,hour=0,minute=0,
                          tzinfo=pytz.UTC)

alert_packet = create_basic_location_alert(example_identity,
                                       # role = vp.definitions.roles.observation,
                                       role = vp.definitions.roles.test,
                                       description="Y2K Bug",
                                       ra=ra,
                                       dec=dec,
                                       err=positional_error,
                                       event_time=event_datetime)

# See voevent-parse docs for detailed example of creating / modifying a packet:
# http://voevent-parse.readthedocs.org/en/0.7.0/examples.html#author-a-new-voevent-packet

# Dump a copy of the packet to the current directory for manual inspection
with open('alert_packet.xml','wb') as f:
    vp.dump(alert_packet, f)

fourpiskytools.comet.send_voevent(alert_packet, host=host)
