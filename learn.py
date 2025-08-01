
# Get a new token: https://help.aliyun.com/document_detail/611472.html?spm=a2c4g.2399481.0.0
# from getpass import getpass
# DASHSCOPE_API_KEY = getpass()
DASHSCOPE_API_KEY = "sk-e6fc31bacfa045b1bdb61ecac5c51eb7"
import os
os.environ["DASHSCOPE_API_KEY"] = DASHSCOPE_API_KEY
from langchain_community.llms import Tongyi
from langchain_core.prompts import PromptTemplate
# print(Tongyi().invoke("What NFL team won the Super Bowl in the year Justin Bieber was born?"))
llm = Tongyi()
print(llm.invoke("What NFL team won the Super Bowl in the year Justin Bieber was born?"))

print("**********************")
template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)

chain = prompt | llm

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

print(chain.invoke({"question": question}))