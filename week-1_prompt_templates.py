from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder

# Template string with placeholders
template_string = "Write a {length} blog post about {topic} for {audience}"

# Create the template with defined input variables
prompt_template = PromptTemplate(
    template=template_string,
    input_variables=["length", "topic", "audience"]
)

# Format with specific parameters
formatted_prompt = prompt_template.format(
    length="500-word",
    topic="machine learning",
    audience="beginners"
)
print(formatted_prompt)



chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant specializing in {domain}"),
    ("user", "{user_input}"),
    ("assistant", "I'll help you with {domain}. Let me analyze your request: {user_input}")
])
print(chat_template.format(domain="software engineering", user_input="What is the best way to learn Python?"))


template_with_history = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{user_input}")
])
print(template_with_history.format(user_input="What is the best way to learn Python?", chat_history=[
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a popular programming language known for its simplicity and versatility."}
]))


# Partial formatting for reusable templates
base_template = PromptTemplate.from_template(
    "As a {role}, analyze this {content_type}: {content}"
)

# Create specialized versions
marketing_template = base_template.partial(role="marketing expert")
technical_template = base_template.partial(role="technical writer")

# Use with specific content
marketing_prompt = marketing_template.format(
    content_type="product description",
    content="Our new AI-powered analytics platform"
)