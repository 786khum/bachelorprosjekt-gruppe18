from core.prompts import build_prompt

def generate_answer(user_message: str) -> str:
    prompt = build_prompt(user_message)

    # TODO: Bytt ut med Gemini / OpenAI senere
    mock_reply = f"(Mock svar) Du spurte: '{user_message}'. Dette blir senere ekte KI-svar."
    
    return mock_reply
