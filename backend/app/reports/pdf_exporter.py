
class PDFExporter:
    def export(self, report_text: str, output_file: str):
        with open(output_file, "w") as f:
            f.write(report_text)
        return output_file
