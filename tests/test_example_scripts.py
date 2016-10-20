from __future__ import absolute_import, print_function
import pytest
import os
import sys
import subprocess
import voeventparse as vp
import fourpiskytools
from fourpiskytools.identity import id_keys

example_identity = {
    id_keys.address : 'voevent.organization.tld',
    id_keys.stream : 'ProjectFooAlerts',
    id_keys.shortName : 'ProjectFoo',
    id_keys.contactName : "Jo Bloggs",
    id_keys.contactEmail : "jb@observatory.org",
    }

def run_command(command_and_args_list, stdin_bytes=None):
    """
    Convenience routine, subprocess.check_call does not accept input on py27.

    cf
    http://stackoverflow.com/questions/10103551/
    """
    print("Running", command_and_args_list)
    proc = subprocess.Popen(
        command_and_args_list,
        stdin=subprocess.PIPE,
    )
    if stdin_bytes is not None:
        proc.communicate(stdin_bytes)
    proc.wait()
    return proc.returncode


examples_folder = os.path.join(os.path.dirname(__file__), os.pardir,
                               'examples')


def test_ping_broker():
    script_path = os.path.join(examples_folder, 'ping_broker.py')
    retcode = run_command([script_path], None)
    assert  retcode == 0

def test_send_alert():
    script_path = os.path.join(examples_folder, 'send_alert.py')
    retcode = run_command([script_path], None)
    assert  retcode == 0

def test_process_voevent_script_1():
    script_path = os.path.join(examples_folder, 'process_voevent_from_stdin_1.py')
    test_packet = fourpiskytools.voevent.create_test_packet(example_identity)
    retcode = run_command([script_path], vp.dumps(test_packet))
    assert retcode == 0

def test_process_voevent_script_2():
    script_path = os.path.join(examples_folder, 'process_voevent_from_stdin_2.py')
    test_packet = fourpiskytools.voevent.create_test_packet(example_identity)
    retcode = run_command([script_path], vp.dumps(test_packet))
    assert retcode == 0