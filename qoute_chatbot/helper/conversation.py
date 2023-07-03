from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
import openai

from config import config


def get_location(query: str) -> str:
    response_schemas = [
        ResponseSchema(
            name="location", description="it is a location or a place.")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(
        response_schemas)
    format_instructions = output_parser.get_format_instructions()
    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(
                "try to extract a location or a place name from the question, if not found output -1.\n{format_instructions}\n{question}")
        ],
        input_variables=["question"],
        partial_variables={"format_instructions": format_instructions}
    )
    try:
        chat = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY)
        _input = prompt.format_prompt(question=query)
        print(_input.to_messages())
        response = chat(_input.to_messages())
        print(response)
        output = output_parser.parse(response.content)
        print(output)
        return {
            'status': 1,
            'location': output['location']
        }
    except:
        return {
            'status': -1,
            'location': -1
        }


openai.api_type = "azure"
openai.api_base = config.OPENAI_API_BASE
openai.api_version = config.AZURE_VERSION
openai.api_key = config.AZURE_OPENAI_API_KEY


def azure_chat_completion(messages: list) -> str:
    try:
        response = openai.ChatCompletion.create(
            engine="Prueba1",
            messages=messages,
            temperature=0.7,
            max_tokens=800,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None)
        return response['choices'][0]['message']['content']
    except:
        return config.ERROR_MESSAGE
