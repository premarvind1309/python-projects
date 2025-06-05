import pywhatkit

# Phone number must include country code (e.g., +91 for India)
phone_number = "+917396688722"
message = "Hello from Python! 🚀"
send_hour = 11  #  PM
send_minute = 53  # 3:30 PM

# Send the message
pywhatkit.sendwhatmsg(phone_number, message, send_hour, send_minute)
