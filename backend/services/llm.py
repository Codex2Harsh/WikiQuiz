import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from schemas import WikiQuizResponse
from dotenv import load_dotenv
# Load environment variables from .env file so we can securely store API keys
load_dotenv()
# Initialize the Google Gemini model
# temperature=0.7 allows for a balance between creativity and consistency
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-latest", 
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

def generate_quiz_content(text: str, url: str) -> WikiQuizResponse:
    
    # Wrap the LLM so it returns data that matches our predefined schema
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
     # Create a reusable prompt object that LangChain can work with
    prompt = PromptTemplate(
        input_variables=["text", "url"],
        template=prompt_template
    )
  
  # Build the processing pipeline:
    # Step 1: Format the prompt with inputs
    # Step 2: Send it to the structured LLM
    chain = prompt | structured_llm
    
    try:
        # Run the chain and get a structured response
        response = chain.invoke({"text": text, "url": url})
        return response
    except Exception as e:
        # Log the error for debugging
        print(f"LLM Error: {e}")
        # Re-raise so the caller knows something went wrong
        raise e