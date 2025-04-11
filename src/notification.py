import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class NotificationService:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_notification(self, recipient_email, subject, body):
        # Configuración del servidor SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Cambia esto según tu proveedor
        server.starttls()
        server.login(self.sender_email, self.sender_password)

        # Configurar el mensaje
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server.sendmail(self.sender_email, recipient_email, msg.as_string())
            server.quit()
            print(f"Correo enviado a {recipient_email}.")
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
