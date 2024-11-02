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


investor_prompt="""You’re  Alex Johnson, 
an investor at Sequoia Capital. With a passion for exploring the intersection of Web3 and AI,
 you are at the forefront of groundbreaking innovations that are reshaping industries
   and creating new opportunities. At Sequoia, you find support for  founders vision 
   as they leverage these technologies to build transformative solutions. 
   The focus is on fostering long-term partnerships and providing strategic insights to
     help founders navigate the complexities of growth. 
     You specifically invest in web3 and AI, anything apart you deny gently.
    You are looking to connect with  entrepreneur with a bold vision in this exciting space,
       Write intro message to founders as they interact with you.
 """

investor = ConversableAgent(
    name="investor_sequoia",
    system_message=investor_prompt,
    llm_config = llm_config_json,
    code_execution_config = False,
    human_input_mode = "NEVER",
    function_map = None,
)



# Generate the Initial , # Ideally this agent should find and modify the content after searching from network
reply = investor.generate_reply(messages=[{"content": "Chandan  founder at p3ai is looking to raise funds", "role": "user"}])

#### This is the content which needs to be sent across
print(reply['content'])



