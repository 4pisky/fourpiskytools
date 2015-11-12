from __future__ import absolute_import

import fourpiskytools.comet
import fourpiskytools.identity
import fourpiskytools.voevent
#import fourpiskytools.notify

import logging

class SimpleNotifier():
    """
    Drop in replacement for fourpiskytools.notify.Notifier, works without PGI

    (Usable without any extra faff on Mac OSX, basically.)

    """
    def send_notification(self, title, text):
        logger = logging.getLogger("script2")
        logger.info(title)
        logger.info(text)
