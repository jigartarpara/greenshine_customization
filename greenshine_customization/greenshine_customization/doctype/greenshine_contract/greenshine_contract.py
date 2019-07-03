# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt, nowdate, getdate


class GreenshineContract(Document):
	pass

@frappe.whitelist()
def make_contract(source_name, target_doc=None):

	doclist = get_mapped_doc("Quotation", source_name, {
			"Quotation": {
				"doctype": "Greenshine Contract",
				"field_map": {
				"customer_name": "party_name",
				"items": "contract_pricing_details_one_year",
				"location_area": "location",
				"tc_name": "tc_name",
				"terms": "terms",
				
			}
			}
		}, target_doc)

	# postprocess: fetch shipping address, set missing values

	return doclist