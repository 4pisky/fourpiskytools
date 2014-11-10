from pgi.repository import Notify
from pgi.repository import GObject

# Inspired by http://askubuntu.com/questions/108764,
# with several tweaks and fixes applied.

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

