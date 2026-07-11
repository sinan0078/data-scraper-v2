
from app.reports.report_generator import ReportGenerator

class ReportService:
    def __init__(self):
        self.generator = ReportGenerator()

    def create_report(self, analysis_results):
        return self.generator.generate(analysis_results)
