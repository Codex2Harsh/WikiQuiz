import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from schemas import WikiQuizResponse
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

def generate_quiz_content(text: str, url: str) -> WikiQuizResponse:
    
    structured_llm = llm.with_structured_output(WikiQuizResponse)
    
    # Prompt
    prompt_template = """
    You are an AI teacher. Analyze the following Wikipedia text and generate a structured quiz JSON.
    
    Input Text:
    {text}
    
    Requirements:
    1. Title: Use the main topic title.
    2. URL: Use this URL: {url}
    3. Summary: A concise 2-sentence summary of the topic.
    4. Key Entities: Extract key people, organizations, and locations.
    5. Sections: List the main section headers covered in the text.
    6. Quiz: Generate 5 distinct multiple-choice questions (mix of Easy, Medium, Hard).
       - Provide 4 options for each.
       - Provide the correct answer text.
       - Provide a short explanation referencing the text.
    7. Related Topics: Suggest 3 wikipedia topics for further reading.
    
    Return the result strictly in the requested JSON format.
    """
    
    prompt = PromptTemplate(
        input_variables=["text", "url"],
        template=prompt_template
    )
  
    chain = prompt | structured_llm
    
    try:
        response = chain.invoke({"text": text, "url": url})
        return response
    except Exception as e:
        print(f"LLM Error: {e}")
        raise e