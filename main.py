#!/usr/bin/env python

from pywebio.input import input, NUMBER, TEXT, PASSWORD, input_group, slider
from pywebio.output import *
from pywebio import start_server
import re
import time
import argparse


def main1():
    image_login = open("login.png", "rb").read()
    image_register = open("register.png", "rb").read()

    def ce(email):
        sub = "@"
        if sub not in email:
            return "Wrong Format"

    def pa(password):

        if len(password) <= 8:
            return "Passwords must be 8 digits or more"

    def data_login():

        form = input_group("Login", [
            input('Email:', name='email', type=TEXT, validate=ce),
            input('Password:', name='password', type=TEXT, validate=pa),
        ], cancelable=True)

        return form

    def data_register():

        form1 = input_group("Register", [
            input("Name:", name="name", type=TEXT),
            input('Email:', name='email', type=TEXT, validate=ce),
            input('Password:', name='password', type=TEXT, validate=pa)
        ], cancelable=True)
        return form1

    
    put_row([put_markdown('# Parador Cruz de Tejeda').style("color: #746191;"),
             put_image(image_login,width="35px",height="35px").style("margin:auto").onclick \
                 (lambda: data_login()),
             put_image(image_register, width="35px", height="35px").style("margin:auto;").onclick(lambda: data_register())]).style("margin:auto;")

    imagen = open("flor.png", "rb").read()

    gif_image = open("gif_video.gif", "rb").read()

    paraiso = open("paraiso_video.gif", "rb").read()

    imagen1 = open("image_parador1.jpg", "rb").read()

    imagen2 = open("image_parador2.jpg", "rb").read()

    logo = open("logos.PNG", "rb").read()
    logo1 = open("parador_logo.PNG", "rb").read()

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    put_image(imagen, width="60px").style("margin:auto;")

    texto_cookies = 'Las cookies se utilizan para acceder y almacenar información en su dispositivo, para ofrecerle contenido ' \
                    'personalizado y anuncios basados en sus datos. Al elegir "Acepto", ' \
                    'usted reconoce el uso de cookies. Puede rechazar o retirar ' \
                    'el consentimiento seleccionando "No, gracias".'

    popup('Cookies', [
        put_text(texto_cookies).style("color: #746191"),
        put_buttons(["Acepto", "No, gracias"], onclick=lambda _: close_popup())

    ])

    put_text("El mayor sentido de emoción, pasión e inspiración").style("color: #9b80c4; font-size:20px;margin-top:40px; margin:auto;")

    put_row([put_column([put_image(imagen2, width="410px", height="190px"),
                         put_image(imagen1, width="410px", height="200px")]),
             put_image(gif_image, width="850px", height="400px")])

    put_text("¿Te imaginas en un paraíso natural en el corazón de la isla de Gran Canaria, "
             "con un spa y una piscina que se extiende hacia un pinar? Ese lugar existe. Es un lugar encantador "
             "con vistas a acantilados y barrancos con vista al mar, encima del cual se encuentra el Parador de Cruz "
             "de Tejeda. El hotel se encuentra a 35 kilómetros de Gran Canaria, rodeado de naturaleza a más de 1.500 "
             "metros sobre el nivel del mar, donde la mayoría de las carreteras del antiguo rey siguen siendo testigos "
             "de las huellas que dejan los senderistas. Nuestras habitaciones serán un sueño").style(
        "color: #9b80c4; font-size:20px;margin-top:40px")
    put_text("hecho realidad ofreciendo una vista de la inmensa caldera que emerge en "
             "todo su esplendor,").style("color: #8b72b0; font-size:20px;margin-left:4px;margin-top:-10px")

    put_text("excavada por el agua y hundida por los volcanes.").style("color: #8b72b0; font-size:20px;"
                                                                       "margin:auto")

    put_image(paraiso, width="1400px", height="500px")

    put_text("Servicios").style("color: #8b72b0; font-size:30px; margin-top:26px")

    put_image(logo, width="900px", height="45px")

    put_image(logo1, width="250px", height="40px")

    # put_processbar('bar')
    # for i in range(1, 11):
    # set_processbar('bar', i / 10)
    # time.sleep(0.1)
    # set_processbar("Processing", value=1 )

    put_text("El Parador de Cruz de Tejeda te espera, ubicado en un lugar glorioso desde el que podrás explorar "
             "la hermosa isla de Gran Canaria, considerada por muchos "
             "como un continente en").style("color:#8b72b0; font-size:20px;margin-top:10px;margin:auto")

    put_text("miniatura por la variedad de hermosos paisajes que alberga.").style("color:#8b72b0; "
                                                                                  "font-size:20px;margin-top:-8px;"
                                                                                  "margin:auto")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-p","--port",type=int,default=8080)
    args=parser.parse_args()

    start_server(main1,port=args.port)

