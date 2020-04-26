import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"  # google server
sender_email = "24pill.code@gmail.com"  # Enter your address
receiver_email = "popecan1000@gmail.com"  # Enter receiver address
#password = input("Type your password and press enter: ")
message = """\
Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, "CodE_$2df72b81197134d95df9835503b4196f91e78096CodE_$")
    server.sendmail(sender_email, receiver_email, message)
