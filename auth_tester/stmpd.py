from smtpd import DebuggingServer
import asyncore

x = DebuggingServer( ('127.0.0.1', 8585) , None )
asyncore.loop()