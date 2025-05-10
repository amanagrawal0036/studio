from typing import Dict, Any

import database
from .dataset_selection import DatasetSelectionAgent
from .planner import Planner
from .result_formatting import ResultFormattingAgent
from .schema_cleaning import SchemaCleaningAgent
from .sql_debugging import SQLDebuggingAgent
from .text_to_sql import TextToSQLAgent


class QueryPlanner(Planner):
    def plan(self, user_input: str) -> Dict[str, Any]:
        """
        Creates a plan for answering a direct query.

        Args:
            user_input: The user's query string.

        Returns:
            A dictionary outlining the steps for the query answering process.
        """
        # Instantiate agents
        dataset_selection_agent = DatasetSelectionAgent()
        schema_cleaning_agent = SchemaCleaningAgent()
        text_to_sql_agent = TextToSQLAgent()
        sql_debugging_agent = SQLDebuggingAgent()
        result_formatting_agent = ResultFormattingAgent()

        # Execute agent steps and pass data
        selected_dataset = dataset_selection_agent.select_dataset(user_input)
        cleaned_schema = schema_cleaning_agent.clean_schema(selected_dataset)
        sql_query = text_to_sql_agent.generate_sql(cleaned_schema, user_input)

        conn = database.create_connection('wicketwise.db')
        query_results = sql_debugging_agent.debug_sql(sql_query, conn)
        conn.close()

        formatted_result = result_formatting_agent.format_results(query_results, user_input)

        return formatted_result


if __name__ == '__main__':
    # Example Usage (for testing purposes)
    query = "runs scored by Virat Kohli at Wankhede Stadium"
    planner = QueryPlanner()
    execution_plan = planner.plan(query)
    import json
    print(json.dumps(execution_plan, indent=2))