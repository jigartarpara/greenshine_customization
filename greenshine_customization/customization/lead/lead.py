import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_survey_form(source_name, target_doc=None):
	target_doc = get_mapped_doc("Lead", source_name,
		{"Lead": {
			"doctype": "Survey Form",
			"field_map": {
				"name": "lead",
				"lead_name": "company_name",
				"company_name": "name_of_kitchen",
				"email_id": "email",
				"mobile_no": "mobile"
			}
		}}, target_doc)

	return target_doc