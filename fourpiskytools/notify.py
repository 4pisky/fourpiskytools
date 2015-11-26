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
    try:
        from Foundation import NSBundle
        from objc import lookUpClass

        class Notifier(object):
            """
            On OSX displays a message in the Notification Center.
            """
            def __init__(self):
                # It's only possible to send notifications if we have a bundle
                # identifier set. This happens by default if using Python
                # installed as a Framework (e.g. the system Python), but isn't
                # set in a virtualenv.
                NSBundle.mainBundle().infoDictionary().setdefault(
                    "CFBundleIdentifier", "org.4pisky.tools")
                self.NSUserNotification = lookUpClass("NSUserNotification")
                NCenter = lookUpClass("NSUserNotificationCenter")
                self.center = NCenter.defaultUserNotificationCenter()

            def send_notification(self, title, text, icon="ignored"):
                n = self.NSUserNotification.alloc().init()
                n.setTitle_(title)
                n.setInformativeText_(text)
                self.center.scheduleNotification_(n)

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
