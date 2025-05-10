import os
from langchain_google_generativeai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser


class TextToSQLAgent:
    def __init__(self):
        self.api_key = "AIzaSyAmhHkeeHTSSl-B5quRWebacPYsafYYSvM"  # Replace with your actual API key
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=self.api_key)
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=self.api_key)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a highly skilled SQL expert. Your task is to convert natural language questions into accurate SQL queries based on the provided database schema.
Ensure your generated SQL is correct and directly executable.

Database Schema:
{schema_info}

Constraints:
- Only use the tables and columns provided in the schema.
- Do not include any explanatory text or markdown, just the SQL query.
- Assume the user wants data from the 'wicketwise.db' database.
"""),
            ("user", "Generate the SQL query for the following request:\n{natural_language_request}\n\nSQL Query:")
        ])

        # You can add few-shot examples here to improve performance.
        # Example:
        # self.prompt = ChatPromptTemplate.from_messages([
        #    ("system", "...schema and constraints..."),
        #    ("user", "Get all players."),
        #    ("assistant", "SELECT * FROM players;"),
        #    ("user", "Get the number of matches played in Mumbai."),
        #    ("assistant", "SELECT COUNT(*) FROM matches WHERE venue = 'Mumbai';"),
        #    ("user", "Generate the SQL query for the following request:\n{natural_language_request}\n\nSQL Query:")
        # ])

        self.chain = self.prompt | self.llm | StrOutputParser()

    def generate_sql(self, user_query: str, schema_info: str) -> str:
        response = self.chain.invoke({
            "schema_info": schema_info,
            "schema_info": schema_info,
            "natural_language_request": user_query
        })
        return response.strip()


class TextToSQLAgent:
    def __init__(self):
        # Placeholder for your Gemini API key
        self.api_key = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
        if self.api_key == "YOUR_GEMINI_API_KEY_HERE":
            print("Warning: GEMINI_API_KEY environment variable not set. Using placeholder.")


if __name__ == '__main__':
    # Example Usage (for testing)
    agent = TextToSQLAgent()

    sample_schema = """
    Tables:
    players (player_id INTEGER PRIMARY KEY, name TEXT, nationality TEXT, role TEXT)
    matches (match_id INTEGER PRIMARY KEY, date DATE, venue TEXT, team1 TEXT, team2 TEXT, winner TEXT)
    player_stats (stat_id INTEGER PRIMARY KEY, match_id INTEGER, player_id INTEGER, runs INTEGER, wickets INTEGER, catches INTEGER)
    """

    sample_query = "Get the total runs scored by Virat Kohli in all matches."

    generated_sql = agent.generate_sql(sample_query, sample_schema)
    print(f"Natural Language Request: {sample_query}")
    print(f"Generated SQL Query:\n{generated_sql}")

    sample_query_2 = "List all matches played at Wankhede Stadium."
    generated_sql_2 = agent.generate_sql(sample_query_2, sample_schema)
    print(f"\nNatural Language Request: {sample_query_2}")
    print(f"Generated SQL Query:\n{generated_sql_2}")
