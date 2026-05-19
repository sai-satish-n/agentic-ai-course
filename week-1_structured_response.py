import asyncio
import os
from dotenv import load_dotenv

from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class Ticket(BaseModel):
    category: str
    priority: str
    sentiment: str

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
)

parser = PydanticOutputParser(
    pydantic_object=Ticket,
)

async def main():
    prompt = f"""
    Analyze the customer complaint.

    {parser.get_format_instructions()}

    Complaint:
    "I was charged twice and support is not responding."
    """

    response = await llm.ainvoke(prompt)

    parsed = parser.parse(response.content)

    print(parsed)


if __name__ == "__main__":
	asyncio.run(main())