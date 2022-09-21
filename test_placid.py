# Install the Python Requests library:
# `pip install requests`

import requests
import json
import urllib.request
import time
import base64
import streamlit as st

def send_request(supplier):
    try:
        response = requests.post(
            url="https://api.placid.app/api/rest/pdfs",
            headers={
                "Authorization": "Bearer placid-4vy7i9et7bd6o1t6-y5dgbpefc2thxuaj",
                "Content-Type": "application/json; charset=utf-8",
            },
            data=json.dumps({
                "pages": [
                    {
                        "template_uuid": "i7jghc291",
                        "layers": {
                            "Date_fin_contrat": {
                                "text": "DD/MM/JJ"
                            },
                            "Fournisseur_actuel": {
                                "text": supplier
                            },
                            "Adresse_site": {
                                "text": "Adresse"
                            },
                            "Conso_annuelle_ref": {
                                "text": "Conso_annuelle_ref"
                            },
                            "Num_compteur": {
                                "text": "XXXXXXX"
                            },
                            "Interlocuteur_tel": {
                                "text": "+336XXXXXXX"
                            },
                            "Interlocuteur_mail": {
                                "text": "younes@papernest.com"
                            },
                            "Interlocuteur_nom": {
                                "text": "Younes Bennani"
                            },
                            "Interlocuteur": {
                                "text": "Nom Prenom"
                            },
                            "Siret": {
                                "text": "SIRETXXXX"
                            },
                            "Raison_sociale": {
                                "text": "XXXXXXXX"
                            }
                        }
                    }
                ]
            })

        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
        id_pdf = json.loads(response.content.decode('utf-8'))["id"]
        url = None


        while url == None :
            pdf = requests.get(url = f"https://api.placid.app/api/rest/pdfs/{id_pdf}",headers={
                "Authorization": "Bearer placid-4vy7i9et7bd6o1t6-y5dgbpefc2thxuaj",
                "Content-Type": "application/json; charset=utf-8",
            })
            print(pdf.text)
            url = json.loads(pdf.text)['pdf_url']
            time.sleep(1)
        
        response = urllib.request.urlopen(url).read()
        local_file = open('test.pdf', 'wb')
        local_file.write(response)
        with open("test.pdf","rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
        return pdf_display

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

send_request("ENGIE")
