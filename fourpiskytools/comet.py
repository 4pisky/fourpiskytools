from __future__ import absolute_import, print_function
import logging
import subprocess
import voeventparse
import tempfile
import textwrap
logger = logging.getLogger(__name__)

def send_voevent(voevent, host='localhost', port=8098):
    """
    Send a voevent to a broker using the comet-sendvo publishing tool.

    Args:
        voevent: A voeventparse voevent object.
        host (string): IP address or hostname of VOEvent broker.
        port (int): Port, default 8098.
    """
    tf = tempfile.TemporaryFile()
    voeventparse.dump(voevent, tf)
    tf.seek(0)
    # tf.close()
    try:
        cmd = ['comet-sendvo']
        cmd.append('--host=' + host)
        cmd.append('--port=' + str(port))
        subprocess.check_call(cmd, stdin=tf)
    except subprocess.CalledProcessError as e:
        logger.error("send_voevent failed")
        raise e
    
    
def dummy_send_to_comet_stub(voevent, host='localhost', port=8098):
    tf = tempfile.NamedTemporaryFile(delete=False)
    print(textwrap.dedent("""\
    *************
     Would have sent a VOEvent to node: {host}:{port};
    Copy of XML dumped to: {fname}
    *************
    """.format(host=host, port=port, fname=tf.name)))
    voeventparse.dump(voevent, tf)
    tf.close()
    # raise subprocess.CalledProcessError(1, 'dummyvosend')


