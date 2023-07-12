from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI

from config import config

def get_location(query: str) -> str:
    response_schemas = [
        ResponseSchema(
            name="location", description="it is a location.")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(
        response_schemas)
    format_instructions = output_parser.get_format_instructions()
    prompt = ChatPromptTemplate(
        messages=[
            HumanMessagePromptTemplate.from_template(
                "try to extract a location from the question, if not found output -1.\n{format_instructions}\n{question}")
        ],
        input_variables=["question"],
        partial_variables={"format_instructions": format_instructions}
    )
    try:
        chat = ChatOpenAI(temperature=0, openai_api_key=config.OPENAI_API_KEY, openai_api_base='')
        print(chat)
        _input = prompt.format_prompt(question=query)
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
