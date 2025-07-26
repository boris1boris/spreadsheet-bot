
def export_to_excel(spreadsheet, filename):
    df = spreadsheet.to_dataframe()
    df.to_excel(filename, index=False)
