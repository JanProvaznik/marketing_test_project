#!/usr/bin/env python
import codecs

from pywebio.input import input, NUMBER, TEXT, PASSWORD, input_group, slider
from pywebio.output import *
from pywebio import start_server
from bs4 import BeautifulSoup
import re
import time
import argparse
import smtplib
from email_creator import create_email

class Usuario:
    def __init__(self,email,name,password):
        self.email=email
        self.name=name
        self.password=password

def main1():
    image_login = open("login.png", "rb").read()
    image_register = open("register.png", "rb").read()
    cheering_cat = open("cheering_cat.gif", "rb").read()

    def ce(email):

        sub = "@"
        if sub not in email:
            return "Wrong Format"

    def pa(password):

        if len(password) < 8:
            return "Passwords must be 8 digits or more"

    lista = [Usuario('j.a.n.provaznik@email.cz','Jan','12345678')]
    
    def send_email():
        sender_email = "cruzdetejeda10@gmail.com"
        rec_email = lista[-1].email # we want to send to the last added
        password = "cruzdetejeda123"


        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        print("Login success")
        message = create_email("email.html", "Parador Cruz de Tejeda", f"Parador Cruz de Tejeda <{sender_email}>",rec_email)
        bytemessage = message.as_bytes()
        server.sendmail(sender_email, rec_email,bytemessage )
        #print("Email has been sent to", rec_emailbytemessage )
    def registered(email):
        if email not in [x.email for x in lista]:
            return "Credenciales incorrectas"
    # HACK correct is having hash of password
    def correct_password(email,password):
        users = [x for x in lista if x.email==email]
        if not users:
            return False
        user=users[0]
        if user.password == password:
            return True
        return False

    def data_register():

        form1 = input_group("Registrarse", [
            input("Nombre:", name="name", type=TEXT),
            input('Email:', name='email', type=TEXT, validate=ce),
            input('Contrase??a:', name='password', type=TEXT, validate=pa)
        ], cancelable=True)
        if form1 != None:
            popup(f"Gracias {form1['name']}, se ha registrado correctamente!")
            lista.append(Usuario(form1['email'],form1['name'],form1["password"]))
        send_email()

    def data_login():

        form = input_group("Login", [
            input('Email:', name='email', type=TEXT, validate=registered),
            input('Contrase??a:', name='password', type=TEXT),
        ], cancelable=True)
        if form != None and correct_password(form['email'],form['password']):
            popup(f"Se ha iniciado sesi??n correctamente!",
                  put_image(cheering_cat, width="150px", height="150px").style("text-align:center"))
        else: popup("Contrase??a incorrecta")
        return form

    put_markdown('# Parador Cruz de Tejeda').style("color: #746191;margin:auto;text-align:center")

    imagen = open("flower_main.gif", "rb").read()

    put_row([put_image(image_login, width="40px", height="40px").style("margin:auto").onclick \
                 (lambda: data_login()),
             put_image(imagen, width="80px").style("margin:auto; margin-top:1px; text-align:center"),
             put_image(image_register, width="40px", height="40px").style("margin:auto;").onclick(
                 lambda: data_register())]).style("margin:auto; margin-top:10px")

    gif_image = open("gif_video.gif", "rb").read()

    paraiso = open("pic_fullscreen.gif", "rb").read()

    imagen1 = open("image_parador1.jpg", "rb").read()

    imagen2 = open("image_parador2.jpg", "rb").read()
    logo = open("logos.png", "rb").read()

    logo1 = open("parador_logo.PNG", "rb").read()

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    texto_cookies = 'Las cookies se utilizan para acceder y almacenar informaci??n en su dispositivo, para ofrecerle contenido ' \
                    'personalizado y anuncios basados en sus datos. Al elegir "Acepto", ' \
                    'usted reconoce el uso de cookies. Puede rechazar o retirar ' \
                    'el consentimiento seleccionando "No, gracias".'

    popup('Cookies', [
        put_text(texto_cookies).style("color: #746191;margin:auto"),
        put_buttons(["Acepto", "No, gracias"], onclick=lambda _: close_popup()).style(
            "margin:auto;margin-top:10px; text-align:center")

    ])

    put_text("~El mayor sentido de emoci??n, pasi??n e inspiraci??n~").style(
        "color: #9b80c4; font-size:20px;margin:auto;margin-top:20px;margin-bottom:10px;text-align:center")

    put_row([put_column([put_image(imagen2, width="410px", height="190px"),
                         put_image(imagen1, width="410px", height="200px")]),
             put_image(gif_image, width="850px", height="400px")])

    put_text("??Te imaginas en un para??so natural en el coraz??n de la isla de Gran Canaria, "
             "con un spa y una piscina que se extiende hacia un pinar? Ese lugar existe. Es un lugar encantador "
             "con vistas a acantilados y barrancos con vista al mar, encima del cual se encuentra el Parador de Cruz "
             "de Tejeda. El hotel se encuentra a 35 kil??metros de Gran Canaria, rodeado de naturaleza a m??s de 1.500 "
             "metros sobre el nivel del mar, donde la mayor??a de las carreteras del antiguo rey siguen siendo testigos "
             "de las huellas que dejan los senderistas. Nuestras habitaciones ser??n un sue??o hecho realidad ofreciendo "
             "una vista de la inmensa caldera que emerge en todo su esplendor, excavada por el agua y hundida por los "
             "volcanes.").style("color: #9b80c4; font-size:20px;margin-top:40px;text-align:center")

    put_image(paraiso, width="1200px", height="350px").style("margin-top:10px")

    put_text("Servicios").style("color: #8b72b0; font-size:32px; margin-top:26px;text-align:center")

    put_image(logo, width="900px", height="150px").style("margin-top:-15px")

    put_text("El Parador de Cruz de Tejeda te espera, ubicado en un lugar glorioso desde el que podr??s explorar "
             "la hermosa isla de Gran Canaria, considerada por muchos como un continente en miniatura por la variedad "
             "de hermosos paisajes que alberga.").style("color:#8b72b0; font-size:20px;margin:"
                                                        "auto;margin-top:0px;text-align:center")

    put_text("Habitaci??n Doble Est??ndar").style("color: #8b72b0; font-size:30px; margin-top:26px;text-align:center")

    habitaciones = open("habitaciones.gif", "rb").read()

    columns = put_column(
        [put_text("Caracter??sticas").style("font-size:24px;color:#483a5c;margin:auto; text-align:center"),
         put_text("Tama??o de la Habitaci??n:").style("font-size:18px;color:#8b72b0;margin:auto; text-align:center"),
         put_text("24 m2").style("color:#8b72b0;margin:auto;margin-top:-2px; text-align:center"),
         put_text("Habitaci??n amplia y luminosa con aire acondicionado, conexi??n gratuita a internet por cable, "
                  "minibar y TV v??a sat??lite.").style("color:#8b72b0;margin:auto; text-align:center"),
         put_text("Ba??o Privado:").style("font-size:18px;color:#483a5c;margin:auto; text-align:center"),
         put_text("???Ba??era ???Secador de Pelo ???Bidet").style(
             "color:#8b72b0;margin:auto;margin-top:-5px; text-align:center"),
         put_text("Equipamiento de la habitaci??n:").style(
             "font-size:18px;color:#483a5c;margin:auto;margin-top:-5px; text-align:center"),
         put_text("???Armario ???Escritorio ???Minibar ???T??lefono ???AC ???Televisi??n ???Caja Fuerte ???Servicio Despertador"
                  "???Suelo de Baldosa/M??rmol ???Calefacci??n").style(
             "color:#8b72b0;margin:auto;margin-top:-5px; text-align:center"),
         put_text("No se puede fumar").style("color:#8b72b0;margin:auto; text-align:center"),
         put_text("Hay parking gratis p??blico en las inmediaciones. No se puede "
                  "reservar.").style("color:#8b72b0;margin:auto; text-align:center"),
         put_text("Precio:").style("font-size:18px;color:#483a5c;margin:auto; text-align:center"),
         put_text("Sin Desayuno Ni Cena Incluido: 100~130???/por noche ").style(
             "color:#8b72b0;margin:auto; text-align:center"),
         put_text("Con Desayuno Sin Cena Incluido: 119~168???/por noche ").style(
             "color:#8b72b0;margin:auto; text-align:center"),
         put_text("Con Desayuno y Cena Incluido: 151~232???/por noche ").style(
             "color:#8b72b0;margin:auto; text-align:center"),
         put_text("Impuestos y Cargos Incluidos, Cancelaci??n GRATIS y Sin Pago Por Adelanto  ").style(
             "color:#8b72b0;margin"
             ":auto; text-align:center")

         ])
    scroll = put_scrollable(columns, height=320, keep_bottom=True)
    put_row([put_image(habitaciones, width="500px", height="320px"),
             scroll
             ])
    white1 = open("white1.png", "rb").read()
    white2 = open("white2.png", "rb").read()
    put_text("Habla con Nuestro Chatbot!").style("color: #8b72b0; font-size:28px; margin-top:26px;text-align:center")
    dancing = open("dancing.gif", "rb").read()

    put_row([put_image(white1, width="100px", height="60px"),
             put_image(dancing, width="270px", height="270px"),
             put_image(white2, width="100px", height="60px")
             ])
    put_text("Confirme su estancia en el Hotel Parador Cruz de Tejeda con nuestro Chatbot de ??ltima generaci??n! "
             "Permite una reserva f??cil, c??moda y instant??nea totalmente GRATIS, desarrollada por "
             "nuestros expertos.").style("color: #8b72b0;font-size:20px;margin-top:10px;text-align:center")
    put_text("??A que esperas? Desc??rgala aqu??:").style(
        "color: #8b72b0;font-size:20px;margin-top:10px;text-align:center")

    put_row([put_image(white1, width="50px", height="50px"),
             put_link("Descargar App",
                      "https://drive.google.com/uc?export=download&confirm=-Ejh&id=1BSFvy9fI5LUzerSpdGxB12rqjYZVO3Oe"). \
            style("color: #483a5c;font-size:20px;margin-top:10px;margin-left:140px;margin:auto;text-align:center"),
             put_image(white2, width="50px", height="50px")
             ])
    map = open("screenshot_map.PNG", "rb").read()

    cat = open("gif_cat.gif", "rb").read()

    insta_pic = open("insta_pic.png", "rb").read()
    facebook_pic = open("facebook_pic.png", "rb").read()
    twitter_pic = open("twitter_pic.png", "rb").read()

    link1 = put_link("Instagram", "https://www.instagram.com/paradores/").style("color: #8b72b0;margin:auto")
    link2 = put_link("Twitter", "https://twitter.com/paradores?lang=es").style("color: #8b72b0;margin:auto")
    link3 = put_link("Facebook", "https://es-es.facebook.com/paradores").style("color: #8b72b0;margin:auto")

    put_tabs([
        {'title': 'Contacto', 'content': [
            put_table([
                ['Tipo', 'Detalle'],
                ['Email', 'cruzdetejeda10@gmail.com', ],
                ['Tel??fono', '9209102019'],
                [put_image(insta_pic, width="20px", height="20px"), link1],
                [put_image(twitter_pic, width="20px", height="20px"), link2],
                [put_image(facebook_pic, width="20px", height="20px"), link3]
            ]).style("color: #8b72b0;margin:auto")
        ]},
        {'title': 'Ubicaci??n', 'content': put_image(map, width="500px", height="350px")},
        {'title': ':)', 'content': [
            put_image(cat, width="250px", height="250px")
        ]},
    ]).style("margin-top:50px")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main1, port=args.port)
