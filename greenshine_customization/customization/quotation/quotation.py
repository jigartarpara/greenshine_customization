@frappe.whitelist()
    def make_contract(source_name, target_doc="None"):
        target_doc = get_mapped_doc("Site", source_name,
            {"Site": {
                "doctype": "Greenshine Contract",
                "field_map": {
                    "customer": "title"
                }
            }},target_doc)
        target_doc.quotation_to = "Site"
        target_doc.run_method("set_missing_values")
        target_doc.run_method("set_other_charges")
        target_doc.run_method("calculate_taxes_and_totals")

        return target_doc