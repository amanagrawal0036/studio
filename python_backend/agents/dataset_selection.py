from database import create_connection, get_table_schema

class DatasetSelectionAgent:
    def select_dataset(self, query_or_plan):
        """
        Selects the relevant database tables and fields based on the query or plan.

        Args:
        query_or_plan: The user query string or a plan dictionary from a planner agent.

        Returns:
        A dictionary or other structure containing information about the selected dataset
        (e.g., list of table names, relevant fields).
        """
        print(f"DatasetSelectionAgent received input: {query_or_plan}")

        # Assuming query_or_plan is always a string user query for simplicity here
        # In a real scenario, it could be a plan dict as well.
        user_query = query_or_plan if isinstance(query_or_plan, str) else ""

        selected_tables = set() # Use a set to avoid duplicate table names
        relevant_fields = {}

        # Simple keyword-based selection for demonstration
        if "player" in user_query.lower() or "career" in user_query.lower() or "kohli" in user_query.lower() or "rohit" in user_query.lower(): # Added specific player names for better detection
            selected_tables.add("players")

        if "match" in user_query.lower() or "vs" in user_query.lower():
            selected_tables.add("matches")

        # Add more logic for other keywords, entities (teams, venues, etc.) and query types
        # based on your database schema and desired features.
        # You might need more sophisticated NLP techniques here for robust entity recognition.

        """

        # For simplicity in this step, we are not yet using get_table_schema to select fields.
        # The schema will be used by the SchemaCleaningAgent and TextToSQLAgent.

        print(f"DatasetSelectionAgent selected tables: {list(selected_tables)}") # Convert set to list for printing
        return {"selected_tables": list(selected_tables)} # Return as a dictionary

# Example usage (for testing)
# if __name__ == "__main__":
#     agent = DatasetSelectionAgent()
#
#     query1 = "career summary for Virat Kohli"
#     dataset_info1 = agent.select_dataset(query1)
#     print(f"Dataset Info 1: {dataset_info1}")
#
#     query2 = "match details for match 123"
#     dataset_info2 = agent.select_dataset(query2)
#     print(f"Dataset Info 2: {dataset_info2}")
#
#     plan_summary = {"agent": "SummaryPlanner", "parameters": {"player_name": "Rohit Sharma"}}
#     dataset_info3 = agent.select_dataset(plan_summary)
#     print(f"Dataset Info 3: {dataset_info3}")