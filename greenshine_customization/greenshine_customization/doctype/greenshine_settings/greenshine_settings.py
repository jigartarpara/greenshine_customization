# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

class GreenshineSettings(Document):
	def validate(self):
		if self.enable_greenshine == 1:
			# setup_custom_fields()
			pass

@frappe.whitelist()
def setup_custom_fields():
	custom_fields = {
		"Lead": [
			dict(
				fieldname='greenshine_survey_form',
				label='Greenshine Survey Form ',
				fieldtype='Link',
				options='Survey Form',
				insert_after='source'
			),
					
		]
	}

	create_custom_fields(custom_fields)
	frappe.msgprint("Custome Field update done.")