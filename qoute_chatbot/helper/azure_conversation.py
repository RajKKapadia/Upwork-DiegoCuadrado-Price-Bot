from config import config  

def azure_chat_completion(messages: list) -> str:
    import openai
    openai.api_type = "azure"
    openai.api_base = config.AZURE_API_BASE
    openai.api_version = config.AZURE_VERSION
    openai.api_key = config.AZURE_OPENAI_API_KEY  
    try:
        response = openai.ChatCompletion.create(
            engine="Prueba1",
            messages=messages,
            temperature=0.0
        )
        return response['choices'][0]['message']['content']
    except:
        return config.ERROR_MESSAGE
    