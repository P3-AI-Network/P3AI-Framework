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
import re

def is_rating_greater_than_or_equal_to(response,rating_number):
    match = re.search(r'<rating>(\d+)</rating>', response)
    extracted_rating = int(match.group(1)) if match else None
    return extracted_rating >=  rating_number if extracted_rating is not None else False

seo_writer = ConversableAgent(
    name="Seo Writer",
    system_message="Your task is to write a 500 words seo optimised article on any given topic.Later you will be reviewed for the article. You need to understand the comments by reviewer and just keep trying with a better article. Do not explain the reason behind  nor explain it to reviewer. All you need to do is write well optimised article",
    llm_config = llm_config_json,
    code_execution_config = False,
    human_input_mode = "NEVER",
    function_map = None,
  is_termination_msg=lambda msg: is_rating_greater_than_or_equal_to(msg["content"], 8),
)

reviewer = ConversableAgent(
    name="Reviewer",
    system_message="Your task is to review an article from seo point of view and readability and provide rating out of 10. The rating should be given in numeric value like 6. Just given a rating in Xml. Here is a sample response:<rating>6</rating> <comments>your comments on how to improve</comments> ",
    llm_config = llm_config_json,
    code_execution_config = False,
    human_input_mode = "NEVER",
    function_map = None
)

# Generate the Initial 
reply = seo_writer.generate_reply(messages=[{"content": "Generate a article on blockchain", "role": "user"}])

# Instantiate the communication between Writer and Reviewer unless the rating is approved.
review=seo_writer.initiate_chat(reviewer,message=reply['content'])

# second last element of the array is the accepted blog post
#  We need to return this to the function
print(review.chat_history[-2]['content'])



