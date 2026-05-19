# Async LangChain + Gemini API example with error handling
import asyncio
import os
from dotenv import load_dotenv


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.exceptions import OutputParserException
from aiohttp import ClientError

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def async_gemini_call(prompt: str) -> str:
	try:
		llm = ChatGoogleGenerativeAI(
			model="gemini-2.5-flash", 
			google_api_key=GEMINI_API_KEY,
		)

		result = await llm.ainvoke(
            [HumanMessage(content=prompt)]
        )
		
		return str(result.content)
	except OutputParserException as e:
		return f"Parsing error: {e}"
	except ClientError as e:
		return f"Network error: {e}"
	except Exception as e:
		return f"Error: {e}"

async def main():
	prompt = "Explain the basics of LangChain in one paragraph."
	response = await async_gemini_call(prompt)
	print("Gemini response:", response)

if __name__ == "__main__":
	asyncio.run(main())
