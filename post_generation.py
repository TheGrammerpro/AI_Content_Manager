from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()


class GeneratePost:
    def __init__(self, business, temporal_theme):
        if temporal_theme is dict:  # If it's a holiday, the theme is not a dict
            self.context = f"Today is {temporal_theme['day']} and the season is {temporal_theme['season']}"
        else:
            self.context = temporal_theme
        self.ai_prompt = ""
        self.business = business
        self.rules = ("-Make a paragraph that doesn't exceed 280 characters including spaces and hashtags.\n"
                      "-Your output should contain only the paragraph\n"
                      "-No leading or ending brackets\n"
                      "-No introduction such as 'here is the paragraph you requested'\n"
                      "-Mention one or two relevant hashtags\n")  # Rules to ensure output is production ready
        self.generate_prompt()

    def generate_prompt(self):
        prompt_template = f"""
        Answer the query based only on the following context:

        {self.context}

        ---

        Answer the question above based on the following guidelines:
        Create a prompt for yourself in order to optimize your output. Your prompt should indicate that the role you 
        will be holding is a good social media content manager for "Business name: {self.business["name"]} and 
        business function: {self.business["theme"]}" who creates the most suitable post to the context above. 
        Your prompt should take into consideration the context and get you to provide an engaging and fun post for a 
        business that aims to have a great brand image on Twitter.\n
        Rules:\n
        *Your output should contain only the prompt\n
        *No introduction such as 'here is the prompt you requested'\n
        *No extra sentences outside the prompt such as 'Anything else?'\n"""

        # Langchain based API to call local AI/ LLM model (Llama3) and get its output:
        llm1 = Ollama(model="llama3")
        self.ai_prompt = llm1.invoke(prompt_template)

    def create_post(self):
        prompt_template = f"""
        Answer the query based only on the following prompt:

        {self.ai_prompt}

        ---

        Adhere to the following rules while creating your output:
        {self.rules}"""  # Final prompt containing all needed context

        # Langchain based API to call local AI/ LLM model (Llama3) and get its output:
        llm1 = Ollama(model="llama3")
        result = llm1.invoke(prompt_template)
        print(result)
        return result
