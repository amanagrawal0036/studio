import sqlite3
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI

class SQLDebuggingAgent:
    def __init__(self, gemini_api_key: str):
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key="AIzaSyAmhHkeeHTSSl-B5quRWebacPYsafYYSvM")
        self.debug_prompt = PromptTemplate(
            input_variables=["sql_query", "error_message", "schema"],
            template="The following SQL query failed with the given error message.\n\n"
                     "SQL Query: {sql_query}\n\n"
                     "Error Message: {error_message}\n\n"
                     "Database Schema: {schema}\n\n"
                     "Analyze the error and the query based on the provided schema, and provide a corrected SQL query. "
                     "If you cannot fix it, respond with 'ERROR'."
        )
        self.debug_chain = LLMChain(llm=self.llm, prompt=self.debug_prompt)
        self.retries = 3  # Number of retries
        # Placeholder: In a real application, you'd pass the database connection here
        # or have a method to execute queries.
        # For now, this method focuses on getting the corrected query from the LLM.

    def debug_sql(self, sql_query: str, connection: sqlite3.Connection, schema: str):
        """Attempts to execute a SQL query and uses LLM to debug if it fails."""
        for attempt in range(self.retries):
            try:
                cursor = connection.cursor()
                cursor.execute(sql_query)
                results = cursor.fetchall()
                return results  # Return results on success
            except sqlite3.Error as e:
                error_message = str(e)
                print(f"SQL execution failed (Attempt {attempt + 1}/{self.retries}): {error_message}")
                if attempt < self.retries - 1:
                    sql_query = self.debug_chain.run(
                        sql_query=sql_query,
                        error_message=error_message,
                        schema=schema
                    ).strip()
        raise Exception(f"SQL query failed after {self.retries} attempts: {error_message}")  # Raise exception if debugging fails
