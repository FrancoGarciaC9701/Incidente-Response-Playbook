from src.incident_handler import IncidentHandler
from src.report_generator import ReportGenerator

class IncidentResponsePlaybook:
    def __init__(self):
        self.incident_handler = IncidentHandler()
        self.report_generator = ReportGenerator()

    def run(self):
        print("=== Incident Response Playbook ===")
        self.incident_handler.menu()
        self.report_generator.generate_report(self.incident_handler.incident_data)
