import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_work_order_schedule(source_name, target_doc=None):
	target_doc = get_mapped_doc("Sales Order", source_name,
		{"Sales Order": {
			"doctype": "Work Order Schedule",
			"field_map": {
                "name": "sales_order",
				"customer": "customer",
              
				
			}
		}}, target_doc)

	return target_doc