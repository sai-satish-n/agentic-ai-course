
# allows to ask questions about wikipedia articles, and get the answer from the article content.
from langchain_community.tools import WikipediaQueryRun

#we can use to fetch the content using the API wrapper
from langchain_community.utilities import WikipediaAPIWrapper
api_wrapper = WikipediaAPIWrapper(
    wiki_client=None,
    top_k_results=1, 
    doc_content_chars_max=100
)
wiki_tool = WikipediaQueryRun(
    api_wrapper=api_wrapper
)

response = wiki_tool.run("father of computer science")

# Print response
print(response)