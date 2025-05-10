from agents.planner import Planner
from typing import Dict, Any
import re
from .dataset_selection import DatasetSelectionAgent
from .schema_cleaning import SchemaCleaningAgent
from .text_to_sql import TextToSQLAgent
from .sql_debugging import SQLDebuggingAgent
from .hypothetical_analysis import HypotheticalAnalysisAgent
from .result_formatting import ResultFormattingAgent
from database import create_connection

class WhatIfPlanner(Planner):
    def plan(self, user_input: str) -> Dict[str, Any]:
        """
        Creates a plan for the What-If Analysis feature.

        Args:
            user_input: The user's query for the what-if scenario.

        Returns:
            A dictionary outlining the steps for the subsequent agents.
        """
        # Basic parsing to extract player and hypothetical team
        player_match = re.search(r"If (.*?) played", user_input, re.IGNORECASE) # type: ignore
        team_match = re.search(r"for (.*?), what would", user_input, re.IGNORECASE)

        player_name = player_match.group(1).strip() if player_match else "Unknown Player"
        hypothetical_team = team_match.group(1).strip() if team_match else "Unknown Team"

        dataset_selection_agent = DatasetSelectionAgent()
        schema_cleaning_agent = SchemaCleaningAgent()
        text_to_sql_agent = TextToSQLAgent()
        sql_debugging_agent = SQLDebuggingAgent()
        hypothetical_analysis_agent = HypotheticalAnalysisAgent()
        result_formatting_agent = ResultFormattingAgent()

        conn = None
        try:
            conn = create_connection('wicketwise.db')

            # Retrieve relevant real data
            selected_dataset = dataset_selection_agent.select_dataset(user_input)
            cleaned_schema = schema_cleaning_agent.clean_schema(selected_dataset)
            sql_query = text_to_sql_agent.generate_sql(cleaned_schema, user_input)
            real_data_results = sql_debugging_agent.debug_sql(sql_query, conn)

            # Perform hypothetical analysis
            hypothetical_results = hypothetical_analysis_agent.analyze(real_data_results, {"scenario": user_input, "player": player_name, "hypothetical_team": hypothetical_team})

            # Format the final result
            final_result = result_formatting_agent.format_results(hypothetical_results, user_input)
            return final_result
        finally:
            if conn:
                conn.close()

if __name__ == '__main__':
    # Example usage
    planner = WhatIfPlanner()
    query = "If Virat Kohli played for Mumbai Indians, what would his average be?"
    what_if_plan = planner.plan(query)
    import json
    print(json.dumps(what_if_plan, indent=2))