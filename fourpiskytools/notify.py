"""
Choose an appropriate method of providing notifications
based on the available modules.
"""

try:
    # Inspired by http://askubuntu.com/questions/108764,
    # with several tweaks and fixes applied.
    from pgi.repository import Notify
    from pgi.repository import GObject

    class Notifier(GObject.Object):
        """
        On *buntu systems, displays a message as a system notification.
        """
        def __init__(self):
            super(Notifier, self).__init__()
            Notify.init("VOEvent Notifications")

        def send_notification(self, title, text, icon="mail-unread"):
            n = Notify.Notification.new(title, text, icon=icon)
            n.show()

except ImportError:
    import logging

    class Notifier(object):
        """
        Writes a message to the log.
        """
        def send_notification(self, title, text):
            logger = logging.getLogger("notifier")
            logger.info(title)
            logger.info(text)
