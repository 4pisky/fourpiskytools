from __future__ import absolute_import, print_function
import pytest
import os
import sys
import subprocess


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