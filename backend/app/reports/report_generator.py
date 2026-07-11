
    class ReportGenerator:
        def generate(self, analysis_results: dict) -> str:
            return f'''
# Executive Summary

{analysis_results.get("summary","")}

# Sentiment

{analysis_results.get("sentiment","")}

# Keywords

{analysis_results.get("keywords","")}
'''
