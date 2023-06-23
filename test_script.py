# from langchain.output_parsers import ResponseSchema
# from langchain.output_parsers import StructuredOutputParser
# from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI

# from config import config

# chat = ChatOpenAI(temperature=0.0, openai_api_key=config.OPENAI_API_KEY)

# location_schema = ResponseSchema(
#     name='location',
#     description='Was the location, may be a city or place. If not found, output -1.'
# )

# template = '''User query will be in Spanish language, For the following text, extract the following information: \
# location: Was the location, may be a city or place. If not found, output -1. \
# text: {text} \
# {format_instructions}'''

# response_schemas = [location_schema]

# output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# format_instructions = output_parser.get_format_instructions()

# prompt = ChatPromptTemplate.from_template(template=template)

# def get_location(query: str) -> dict:
#     messages = prompt.format_messages(text=query, 
#                                     format_instructions=format_instructions)
#     try:
#         response = chat(messages)
#         output = output_parser.parse(response.content)
#         return {
#             'status': 1,
#             'location': output['location']
#         }
#     except:
#         return {
#             'status': 0,
#             'location': -1
#         }

# import json

# import requests

# from config import config

# def get_price(location: str) -> dict:
#     try:
#         payload = ""
#         response = requests.request("GET", config.BACKEND_URL, data=payload)
#         response = json.loads(response.text)
#         price = 0.0
#         for r in response:
#             if r['ciudad'] == location:
#                 price += float(r['precio'])
        
#         if price == 0.0:
#             return f"We don't have price for the {location}."
#         else:
#             return f'The price of the location {location} is {round(price, 2)}.'
#     except:
#         return 'We are facing a technical issue at this time.'
    
    