from socket import *
import base64
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com' # Fill in start   #Fill in end
mailPort = 465
# Create a TCP socket called clientSocket
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
# Fill in end
clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.connect((mailserver, mailPort))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Authentication using base64
# For Gmail, it is recommended to create an "app password" and
# use that value in the password field instead of the regular password.
# username and password values should be enclosed in quotes:
# Example: username = "sample@gmail.com"
username = "trushbball@gmail.com"# Fill in start   #Fill in end
password = "haogpujfvpfiiplb"# Fill in start   #Fill in end
base64_str = ("\x00" + username + "\x00" + password).encode()
base64_str = base64.b64encode(base64_str)
authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
clientSocket.send(authMsg)
recv_auth = clientSocket.recv(1024)
print(recv_auth.decode())

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "Mail from: <{}>\r\n".format(username)
clientSocket.send(mailFrom.encode())
recv5 = clientSocket.recv(1024)
print(recv5)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptto = "RCPT To: <{}>\r\n".format(username)
clientSocket.send(rcptto.encode())
recv6 = clientSocket.recv(1024)
print(recv6)
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = 'DATA\r\n'
clientSocket.send(data.encode())
recv7 = clientSocket.recv(1024)
print(recv7)
# Fill in end

# Send message data.
# Fill in start
clientSocket.send("Subject: {}\n".format(msg).encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv8 = clientSocket.recv(1024)
print(recv8)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCMD = 'QUIT\r\n'
clientSocket.send(quitCMD.encode())
recv9 = clientSocket.recv(1024)
print(recv9)

clientSocket.close()
print("Done")
# Fill in end