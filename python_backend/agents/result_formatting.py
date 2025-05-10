import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class ResultFormattingAgent:
    def __init__(self, google_api_key: str):
        self.llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key="AIzaSyAmhHkeeHTSSl-B5quRWebacPYsafYYSvM")

    def format_results(self, query_results: any, original_query: str, analysis_results: any = None) -> tuple[str, bool]:
        """
        Formats the query results and analysis into a natural-language response.

        Args:
            query_results: The results obtained from the database queries.
            original_query: The user's original query.
            analysis_results: Optional results from hypothetical analysis.

        Returns:
            A tuple containing the natural-language string summarizing the results and a boolean indicating if a chart is needed.
        """
        # Construct a prompt for the LLM to format the results
        prompt_template = """
        You are a helpful assistant that summarizes data about cricket, specifically focusing on IPL statistics.
        Based on the following query and data, provide a concise and easy-to-understand summary.

        User Query: {original_query}

        Data: {query_results}

        {analysis_section}

        Format the information clearly and directly answer the user's question.
        """

        analysis_section = ""
        if analysis_results:
            analysis_section = f"\nHypothetical Analysis: {analysis_results}"

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["original_query", "query_results", "analysis_section"]
        )

        chain = LLMChain(llm=self.llm, prompt=prompt)

        # Determine if a chart is needed (placeholder logic)
        print("Chart generation triggered (placeholder)")
        # In a real application, you would call a charting library or service here

        response = chain.run(original_query=original_query, query_results=query_results, analysis_section=analysis_section)

        return response, needs_chart

    def _determine_if_chart_needed(self, original_query: str, query_results: list, analysis_results: any) -> bool:
        """
        Placeholder logic to determine if a chart is needed.
        This would involve analyzing the query and results structure.
        """
        # Example placeholder: suggest a chart if there are multiple data points
        needs_chart = False
        # Suggest a chart if there are multiple data points (e.g., for historical trends or comparisons)
        if isinstance(query_results, list) and len(query_results) > 1:
            needs_chart = True
        # Suggest a chart for head-to-head comparisons
        if "vs" in original_query.lower() or "head to head" in original_query.lower():
            needs_chart = True
        # Always consider charting hypothetical analysis results for visualization
        if analysis_results:
            needs_chart = True

        return False

# Example Usage (requires setting GOOGLE_API_KEY environment variable)
if __name__ == "__main__":
    # In a real application, the API key would be loaded securely
    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.")
    else:
        formatter = ResultFormattingAgent(google_api_key=google_api_key)

        sample_query_results = [
            {"match": "Match 1", "runs": 50, "balls": 30},
            {"match": "Match 2", "runs": 75, "balls": 45},
        ] # Example with multiple data points
        sample_original_query = "Tell me about Player X's last two innings."

        formatted_response, needs_chart = formatter.format_results(sample_query_results, sample_original_query)
        print("Formatted Response:")
        print(formatted_response, needs_chart)

        sample_analysis_results = "Based on CSK's home ground factors, Kohli might have averaged 55."
        formatted_response_with_analysis = formatter.format_results(
            sample_query_results, sample_original_query, analysis_results=sample_analysis_results
        )
        print("\nFormatted Response with Analysis:")
        print(formatted_response_with_analysis)
