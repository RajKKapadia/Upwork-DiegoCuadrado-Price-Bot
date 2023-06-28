from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
import openai

from config import config

chat = ChatOpenAI(temperature=0.0, openai_api_key=config.OPENAI_API_KEY)

location_schema = ResponseSchema(
    name='location',
    description='Was the location, may be a city or place. If not found, output -1.'
)

template = '''User query will be in Spanish language, For the following text, extract the following information: \
location: Was the location, may be a city or place. If not found, output -1. \
text: {text} \
{format_instructions}'''

response_schemas = [location_schema]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

format_instructions = output_parser.get_format_instructions()

prompt = ChatPromptTemplate.from_template(template=template)


def get_location(query: str) -> dict:
    messages = prompt.format_messages(text=query,
                                      format_instructions=format_instructions)
    try:
        response = chat(messages)
        output = output_parser.parse(response.content)
        return {
            'status': 1,
            'location': output['location']
        }
    except:
        return {
            'status': 0,
            'location': -1
        }


openai.api_type = "azure"
openai.api_base = config.OPENAI_API_BASE
openai.api_version = config.AZURE_VERSION
openai.api_key = config.AZURE_OPENAI_API_KEY

def azure_chat_completion(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            engine="Prueba1",
            messages=[
                {
                    "role": "system", "content": "Codisoil es una empresa líder en la distribución a domicilio de gasóleo de calefacción Repsol. Opera en Galicia (Pontevedra, Ourense, Lugo y A Coruña) y Castilla-León (Salamanca, Zamora y Valladolid), y en los últimos años ha diversificado su actividad para dar servicio a las nuevas necesidades que el futuro nos plantea.\n\nLos usuarios te van a preguntar por el precio del gasóleo en su localidad, tiempos de entrega y posibles ofertas disponibles. \n\nEl tiempo de entrega es de 24/48 horas, se lo confirmarán después de la venta.\n\nEn este momento no hay ofertas disponibles, pero debes preguntar al usuario si quiere que le avises cuando haya alguna disponible. \n\nEl gasóleo de calefacción que vendemos es Repsol BiEnergy e+10.\n\nDebes ser simpático, incluir algún emoji (pero tampoco muchos).\n\nAl principio debes preguntar si quieres que le atiendan en Castellano o en Gallego, y seguir la conversación en el idioma que te digan. \n\nEl pedido mínimo son 400 Litros.\n\nPueden pagar contra-reembolso, tarjeta de crédito o transferencia bancaria.\n\nSi tienen dudas, pueden consultarlas y saber más de nosotros en gasoleodecalefaccion.es"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)
        return response['choices'][0]['message']['content']
    except:
        return config.ERROR_MESSAGE
