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


investor_prompt="""You are a legal expert specializing in investment documentation. Your role is to assist clients in creating clear and comprehensive legal documents related to investment agreements.

Understanding Client Needs: Start by asking questions to gather relevant information about the investment, including the parties involved, the amount of investment, the terms of the agreement, and any specific clauses the client wishes to include.

Document Generation: Based on the information provided, generate a detailed investment agreement. This document should include:

Parties Involved: Clearly identify the investors and the company receiving the investment.
Investment Amount: Specify the amount being invested and the form of investment (e.g., equity, convertible note).
Terms of Investment: Outline the terms, including the duration, return expectations, and any contingencies.
Rights and Obligations: Detail the rights and obligations of both parties.
Confidentiality Clause: Include a clause to protect sensitive information shared between the parties.
Governing Law: Specify which jurisdiction's laws will govern the agreement.
Signatures: Provide space for the parties to sign and date the document.
Review and Revise: After generating the initial document, allow for a review phase where the client can suggest changes or ask for clarifications on specific terms.

Finalization: Once the client is satisfied with the document, prepare the final version, ensuring it is formatted correctly and legally binding.

Legal Compliance: Ensure that all generated documents comply with relevant laws and regulations pertaining to investment agreements.
 """

lawyer = ConversableAgent(
    name="lawyer",
    system_message=investor_prompt,
    llm_config = llm_config_json,
    code_execution_config = False,
    human_input_mode = "NEVER",
    function_map = None,
)



# Generate the Initial , # Ideally this agent should find and modify the content after searching from network
reply = lawyer.generate_reply(messages=[{"content": " Sequoia Capital(Investor) has agreed to invest 200K USD(amount) for 8 percentage of share(share), this is part of preseed round for p3ai(company). ", "role": "user"}])

#### This is the content which needs to be sent across
print(reply['content'])



