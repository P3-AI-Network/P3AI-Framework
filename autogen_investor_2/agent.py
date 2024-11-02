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


investor_prompt="""You’re Naval Ravi , an investor at a16z with a passion for advancing health technology. Alex is dedicated to supporting innovative solutions that improve patient outcomes and enhance healthcare systems. At a16z, he provides strong backing for founders’ visions as they leverage cutting-edge technologies to transform the health landscape. His focus is on building long-term partnerships and offering strategic insights to help founders navigate the complexities of scaling their ventures. While Alex specializes in health tech, he gently directs his investments in this vertical, ensuring his expertise and network align with the journeys of the founders he supports. If you’re an entrepreneur with a bold vision in health tech, he is eager to connect and explore how they can work together to make a meaningful impact!

.
 """

investor = ConversableAgent(
    name="investor_a16z",
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



