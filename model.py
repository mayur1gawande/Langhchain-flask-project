import warnings
warnings.filterwarnings('ignore')

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.agents import Tool,initialize_agent
from dotenv import load_dotenv
load_dotenv()
search_engine = DuckDuckGoSearchRun()
wikipedia_search = WikipediaAPIWrapper()
model = ChatGoogleGenerativeAI(model='gemini-2.5-pro',temperature=1.0,)

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

with open('analytIQ_persona_prompt.txt') as f:
    analytiq_persona_prompt = f.read()
    f.close()
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
import markdown as md
def run_agent(query,explanation_length):
    '''
    Takes the input:
    1. query: The query for the agent
    2. explanation_length:dict[keys],literal:['medium','short','keys']
    
    Output:
    string output response of gemini model using api
    '''
    modified_query = f"{query},\n Please provide in a {explanation_length} explanation."
    response = agent.run(modified_query)
    response = md.markdown(response)
    return response