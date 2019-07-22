import frappe
def onload(doc, method):
    total = 0 
    total_month = 0
    test = 0
    for item in doc.items:
        total += item.total_year
        total_month += item.total_monthly
        test += item.amount
    doc.final_total = total
    doc.final_total_month = total_month 
    doc.total = test