from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

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
