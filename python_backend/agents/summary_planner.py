from abc import ABC, abstractmethod

class Planner(ABC):
    @abstractmethod
    def plan(self, user_input: str) -> dict:
        from .dataset_selection import DatasetSelectionAgent
        from .schema_cleaning import SchemaCleaningAgent
        from .text_to_sql import TextToSQLAgent
        from .sql_debugging import SQLDebuggingAgent
        from .hypothetical_analysis import HypotheticalAnalysisAgent
        from .result_formatting import ResultFormattingAgent
        pass

from ..database import create_connection # Import create_connection from database.py

import re

class SummaryPlanner(Planner):
    def plan(self, user_query: str) -> dict:
        """
        Plans the steps for generating a career summary based on the user query.
        """
        # Simple parsing to extract player name.
        # This could be made more sophisticated with NLU.
        match = re.search(r"career summary for (.*)", user_query, re.IGNORECASE)
        player_name = match.group(1).strip() if match else None

        if not player_name:
            return {"error": "Could not identify player name in the query."}

        # Instantiate agents
        dataset_selection_agent = DatasetSelectionAgent()
        schema_cleaning_agent = SchemaCleaningAgent()
        text_to_sql_agent = TextToSQLAgent()
        sql_debugging_agent = SQLDebuggingAgent()
        result_formatting_agent = ResultFormattingAgent()

        connection = None
        try:
            # Create database connection
            connection = create_connection('wicketwise.db')

            # Call agents in sequence
            selected_dataset = dataset_selection_agent.select_dataset(user_query=user_query)
            cleaned_schema = schema_cleaning_agent.clean_schema(selected_dataset=selected_dataset)
            sql_query = text_to_sql_agent.generate_sql(cleaned_schema=cleaned_schema, task=f"get career statistics for {player_name}")
            query_results = sql_debugging_agent.debug_sql(sql_query=sql_query, db_connection=connection)
            final_result = result_formatting_agent.format_results(query_results=query_results, original_query=user_query)
            return {"result": final_result}
        finally:
            if connection:
                connection.close()

if __name__ == '__main__':
    # Example usage:
    planner = SummaryPlanner()
    user_query = "I need the career summary for Virat Kohli"
    execution_plan = planner.plan(user_query)
    import json
    print(json.dumps(execution_plan, indent=2))

    user_query_no_player = "I need a career summary"
    execution_plan_no_player = planner.plan(user_query_no_player)
    print(execution_plan_no_player)
