# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class NamingSeriesMapping(Document):
	pass

@frappe.whitelist()
def get_series():
	return {
		"naming_series" : frappe.get_meta("Payment Entry").get_options("naming_series") or "SO-Shopify-",
	}