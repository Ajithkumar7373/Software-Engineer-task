from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma:2b",
    temperature=0,
    max_tokens=None,
    max_retries=2
)

def get_answer(question: str) -> str:
    response = llm.invoke(question)
    return response.content
