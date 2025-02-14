import ast
from typing import List

# from deepsearcher.configuration import llm
from deepsearcher.agent.prompt import get_reflect_prompt
from deepsearcher.vector_db.base import RetrievalResult
from deepsearcher import configuration


def generate_gap_queries(original_query: str, all_sub_queries: List[str], all_chunks: List[RetrievalResult]) -> List:
    llm = configuration.llm
    reflect_prompt = get_reflect_prompt(question=original_query, mini_questions=all_sub_queries, mini_chuncks=[chunk.text for chunk in all_chunks])
    chat_response = llm.chat([{"role": "user", "content": reflect_prompt}])
    response_content = chat_response.content
    return llm.literal_eval(response_content)