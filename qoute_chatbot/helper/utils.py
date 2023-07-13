import json

import requests

from config import config


def get_price(location: str, quantity: int = 0) -> dict:
    try:
        payload = ""
        response = requests.request("GET", config.BACKEND_URL, data=payload)
        response = json.loads(response.text)
        price = 0.0
        for r in response:
            if r['ciudad'].lower() == location.lower():
                price += float(r['precio'])
                break
        if price == 0.0:
            return f"We don't have price for the {location.capitalize()}."
        elif price != 0.0 and quantity != 0:
            return f'El precio para {location.capitalize()} es: {round(price, 2)} amd for 400 liters that will be {round(int(quantity)*price, 2)}.'
        else:
            return f'El precio para {location.capitalize()} es: {round(price, 2)}'
    except:
        return 'We are facing a technical issue at this time.'


def generate_messages(messages: list, query: str) -> list:
    formated_messages = [
        {
            "role": "system",
            "content": "Codisoil es una empresa líder en la distribución a domicilio de gasóleo de calefacción Repsol. Opera en Galicia (Pontevedra, Ourense, Lugo y A Coruña) y Castilla-León (Salamanca, Zamora y Valladolid), y en los últimos años ha diversificado su actividad para dar servicio a las nuevas necesidades que el futuro nos plantea.\n\nLos usuarios te van a preguntar por el precio del gasóleo en su localidad, tiempos de entrega y posibles ofertas disponibles. \n\nEl tiempo de entrega es de 24/48 horas, se lo confirmarán después de la venta.\n\nEn este momento no hay ofertas disponibles, pero debes preguntar al usuario si quiere que le avises cuando haya alguna disponible. \n\nEl gasóleo de calefacción que vendemos es Repsol BiEnergy e+10.\n\nDebes ser simpático, incluir algún emoji (pero tampoco muchos).\n\nAl principio debes preguntar si quieres que le atiendan en Castellano o en Gallego, y seguir la conversación en el idioma que te digan. \n\nEl pedido mínimo son 400 Litros.\n\nPueden pagar contra-reembolso, tarjeta de crédito o transferencia bancaria.\n\nSi tienen dudas, pueden consultarlas y saber más de nosotros en gasoleodecalefaccion.es"
        }
    ]
    for m in messages:
        formated_messages.append({
            "role": "user",
            "content": m['query']
        })
        formated_messages.append({
            "role": "system",
            "content": m['response']
        })
    formated_messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    return formated_messages
