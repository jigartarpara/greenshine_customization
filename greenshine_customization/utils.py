import frappe
def on_update(doc, method):
    print("Data ")
    print(doc)
    print(method)
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
    # doc.save()
    # frappe.db.commit()