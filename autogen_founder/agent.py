from autogen import ConversableAgent
from pprint import pprint
from rich import print
from dotenv import load_dotenv
import os
load_dotenv()
gemini_api_key = os.getenv('GEMINI_KEY')
llm_config_json={
         "model": "gemini-1.5-flash",
         "api_key": gemini_api_key,
         "api_type": "google"
    }


founder_prompt="""You are Chandan Kumar, a young founder working in the space of web3 and AI. 
You are building open network and communication for AI agents which aims at creating a secure, 
collaborative ecosystem where AI agents can freely interact, transact, and learn from each other
 across a global, permissionless network.
Your project, P3AI, is dedicated to building an infrastructure that empowers AI agents
 with decentralized identities, enabling seamless, trustless communication across platforms. 
 This innovation has the potential to redefine digital interactions, allowing for transparent, 
 secure data sharing while preserving user autonomy and privacy. With a deep understanding of 
 both blockchain and AI, you’re pushing forward a future where AI not only operates 
 autonomously but also contributes actively to a decentralized economy.
 You are looking to raise funds from investors. Write a short intro message as you interact with Investors
 
 """

founder = ConversableAgent(
    name="founderAgent",
    system_message=founder_prompt,
    llm_config = llm_config_json,
    code_execution_config = False,
    human_input_mode = "NEVER",
    function_map = None,
)



# Generate the Initial , # Ideally this agent should find and modify the content after searching from network
reply = founder.generate_reply(messages=[{"content": "Investor Sequoia Capital is active investing in AI agents and Web3", "role": "user"}])

#### This is the content which needs to be sent across
print(reply['content'])



