import gi
gi.require_version("Notify", "0.7")
from gi.repository import Notify

# Init notifications
Notify.init("MyProgram")

def notify():
	# Create a new notification
	n = Notify.Notification.new("Default Title","Default Body")

	# Update the title / body
	n.update("Hello","World!")

	# Show it
	n.show()

if __name__ == '__main__':
	notify()
