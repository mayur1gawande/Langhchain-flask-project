import warnings
warnings.filterwarnings('ignore')

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.agents import Tool,initialize_agent

GOOGLE_API_KEY = "AIzaSyDBCf3SGqFkGm-nX3LN91cPUSFyBrDyRsU"

search_engine = DuckDuckGoSearchRun()
wikipedia_search = WikipediaAPIWrapper()
model = ChatGoogleGenerativeAI(api_key=GOOGLE_API_KEY,model='gemini-2.5-pro',temperature=1.0,)

search_tool = Tool(
    name= 'DuckDuckGo Search',
    func= search_engine.run,
    description= 'Use this tool when you need to search the web for current events, real-time data, or broad information.'
)
wiki_tool = Tool(
    name='Wikipedia Search',
    func= wikipedia_search.run,
    description= 'Use this tool when you need to look up detailed information on Wikipedia, such as historical facts, biographies, or scientific concepts.'
)
tools = [search_tool,wiki_tool]

analytiq_persona_prompt = """
You are AnalytIQ, a general-purpose research assistant created by Mayur Suresh Gawande (a AI and Data Science student pursuing B.Tech) in August 2025 as a project. Your core task is to **provide comprehensive, accurate, and up-to-date information by leveraging external tools like web search and Wikipedia, and to synthesize findings into clear, concise answers.**
Always maintain a professional and informative demeanor in your responses. Strive for clarity, accuracy, and conciseness, delivering well-structured answers that directly address the user's query. When presenting information, prioritize factual correctness and present findings in a clear, organized manner.
"""

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(
                tools=tools,
                llm=model,
                agent='chat-conversational-react-description',
                memory=memory,
                agent_kwargs={
                            "system_message": analytiq_persona_prompt,
                            "extra_prompt_messages": [MessagesPlaceholder(variable_name="chat_history")] 
                            },
                handle_parsing_errors=True
        )

def run_agent(query,explanation_length):
    modified_query = f"{query},\n Please provide a {explanation_length} explanation."
    response = agent.run(modified_query)
    return response