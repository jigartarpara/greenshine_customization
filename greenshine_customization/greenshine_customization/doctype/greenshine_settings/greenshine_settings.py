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
		],
		"Quotation": [
			dict(
				fieldname='contact_name',
				label='Contact Name ',
				fieldtype='Data',
				insert_after='customer_name'
			),
			dict(
				fieldname='Position',
				label='Position ',
				fieldtype='Data',
				insert_after='contact_name'
			),
			dict(
				fieldname='greenshine',
				label='Greenshine ',
				fieldtype='Section Break',
				insert_after='ignore_pricing_rule'
			),
			dict(
				fieldname='subject',
				label='Subject',
				fieldtype='Select',
				Options='Quotation for cleaning and degreasing kitchen duct\nQuotation for water tank cleaning and disinfection\nQuotation for drain line cleaning\nQuotation for grease trap cleanin\nQuotation for pest control',
				insert_after='greenshine',
			),
			dict(
				fieldname='location_area',
				label='Location ',
				fieldtype='Link',
				options='Location',
				insert_after='subject',
			),	
		],
		"Quotation Item": [
			dict(
				fieldname='location',
				label='Location ',
				fieldtype='Link',
				options='Location Area',
				insert_after='customer_item_code'
			),
			dict(
				fieldname='total_one_time',
				label='Total One Time ',
				fieldtype='Float',
				insert_after='stock_uom'
			),		
			dict(
				fieldname='frequency',
				label='Frequency',
				fieldtype='Float',
				insert_after='total_one_time'
			),
			dict(
				fieldname='frequency_month',
				label='Frequency Month',
				fieldtype='Float',
				insert_after='stock_qty'
			),
			dict(
				fieldname='total_monthly',
				label='Total Monthly',
				fieldtype='Float',
				insert_after='frequency_month'
			),	
			dict(
				fieldname='total_year',
				label='Total/Year',
				fieldtype='Float',
				insert_after='total_monthly'
			),
		],
		"Sales Order Item": [
			dict(
				fieldname='location',
				label='Location ',
				fieldtype='Link',
				options='Location Area',
				insert_after='customer_item_code'
			),
			dict(
				fieldname='total_one_time',
				label='Total One Time ',
				fieldtype='Float',
				insert_after='stock_uom'
			),		
			dict(
				fieldname='frequency',
				label='Frequency',
				fieldtype='Float',
				insert_after='total_one_time'
			),
			dict(
				fieldname='frequency_month',
				label='Frequency Month',
				fieldtype='Float',
				insert_after='stock_qty'
			),
			dict(
				fieldname='total_monthly',
				label='Total Monthly',
				fieldtype='Float',
				insert_after='frequency_month'
			),	
			dict(
				fieldname='total_year',
				label='Total/Year',
				fieldtype='Float',
				insert_after='total_monthly'
			),
		],
		"Sales Invoice Item": [
			dict(
				fieldname='location',
				label='Location ',
				fieldtype='Link',
				options='Location Area',
				insert_after='customer_item_code'
			),
			dict(
				fieldname='total_one_time',
				label='Total One Time ',
				fieldtype='Float',
				insert_after='stock_uom'
			),		
			dict(
				fieldname='frequency',
				label='Frequency',
				fieldtype='Float',
				insert_after='total_one_time'
			),
			dict(
				fieldname='frequency_month',
				label='Frequency Month',
				fieldtype='Float',
				insert_after='stock_qty'
			),
			dict(
				fieldname='total_monthly',
				label='Total Monthly',
				fieldtype='Float',
				insert_after='frequency_month'
			),	
			dict(
				fieldname='total_year',
				label='Total/Year',
				fieldtype='Float',
				insert_after='total_monthly'
			),
		]
	}

	create_custom_fields(custom_fields)
	frappe.msgprint("Custome Field update done.")