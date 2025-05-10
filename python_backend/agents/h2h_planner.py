from .planner import Planner
from typing import Dict, Any

from .dataset_selection import DatasetSelectionAgent
from .schema_cleaning import SchemaCleaningAgent
from .text_to_sql import TextToSQLAgent
from .sql_debugging import SQLDebuggingAgent
from .result_formatting import ResultFormattingAgent
from .. import database # Assuming database.py is in the parent directory

class H2HPlanner(Planner):
    def plan(self, user_input: str) -> Dict[str, Any]:
        """
        Plans the steps for a Head-to-Head analysis based on user input.

        Args:
            user_input: The user's query (e.g., "Team A vs Team B").

        Returns:
            A dictionary outlining the plan, including parallel branches.
        """
        # Simple parsing to extract team names (can be improved)
        teams = user_input.lower().replace(" vs ", " ").split()
        if len(teams) != 2:
            # Handle cases where parsing fails
            return {"error": "Could not identify two teams in the query."}

        team1, team2 = teams

        conn = None
        try:
            conn = database.create_connection('wicketwise.db')

            # Instantiate agents
            dataset_selection_agent = DatasetSelectionAgent()
            schema_cleaning_agent = SchemaCleaningAgent()
            text_to_sql_agent = TextToSQLAgent()
            sql_debugging_agent = SQLDebuggingAgent()
            result_formatting_agent = ResultFormattingAgent()

            # Placeholder for parallel execution logic
            # In a real implementation, you would use threading or asyncio
            # to run these branches concurrently.

            # Branch 1: Team 1 vs Team 2 analysis
            selected_dataset_1 = dataset_selection_agent.select_dataset(f"{team1} vs {team2} analysis", conn)
            cleaned_schema_1 = schema_cleaning_agent.clean_schema(selected_dataset_1)
            sql_query_1 = text_to_sql_agent.generate_sql(cleaned_schema_1, f"Analyze {team1} vs {team2}")
            results_1 = sql_debugging_agent.debug_sql(sql_query_1, conn)

            # Branch 2: Team 2 vs Team 1 analysis
            selected_dataset_2 = dataset_selection_agent.select_dataset(f"{team2} vs {team1} analysis", conn)
            cleaned_schema_2 = schema_cleaning_agent.clean_schema(selected_dataset_2)
            sql_query_2 = text_to_sql_agent.generate_sql(cleaned_schema_2, f"Analyze {team2} vs {team1}")
            results_2 = sql_debugging_agent.debug_sql(sql_query_2, conn)

            # Combine results and format
            combined_results = {
                f"{team1}_vs_{team2}": results_1,
                f"{team2}_vs_{team1}": results_2
            }
            final_result = result_formatting_agent.format_results(combined_results, user_input)

            return final_result

        except Exception as e:
            # Handle any exceptions during the process
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()


if __name__ == "__main__":
    # Example usage
    h2h_planner = H2HPlanner()
    user_query = "Mumbai Indians vs Chennai Super Kings"
    h2h_plan = h2h_planner.plan(user_query)
    import json
    print(json.dumps(h2h_plan, indent=4))