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
				fieldname='sales_person',
				label='Sales Person ',
				fieldtype='Link',
				options='Sales Person',
				insert_after='contact_name'
			),
			dict(
				fieldname='contact_no',
				label='Contact_no ',
				fieldtype='Data',
				insert_after='sales_person'
			),
			dict(
				fieldname='position',
				label='Position',
				fieldtype='Data',
				insert_after='order_type'
			),
			dict(
				fieldname='email',
				label='Email ',
				fieldtype='Data',
				insert_after='position'
			),
			dict(
				fieldname='greenshine',
				label='Greenshine ',
				fieldtype='Section Break',
				insert_after='position'
			),
			dict(
				fieldname='subject',
				label='Subject',
				fieldtype='Select',
				Options='Quotation for cleaning and degreasing kitchen duct\nQuotation for water tank cleaning and disinfection\nQuotation for drain line cleaning\nQuotation for grease trap cleanin\nQuotation for pest control',
				insert_after='greenshine',
			),
			dict(
				fieldname='cb',
				fieldtype='Column Break',
				insert_after='subject',
			),
			dict(
				fieldname='location_area',
				label='Location ',
				fieldtype='Link',
				options='Location',
				insert_after='cb',
			),
			dict(
				fieldname='sc1',
				label='Terms ',
				fieldtype='Section Break',
				insert_after='location_area',
			),
			dict(
				fieldname='greenshine_terms',
				label='Quote Intro ',
				fieldtype='Link',
				options='Terms and Conditions',
				insert_after='sc1',
			),
			dict(
				fieldname='term_detail',
				label='Description ',
				fieldtype='Text Editor',
				fetch_from='greenshine_terms.terms',
				insert_after='greenshine_terms',
			),
			dict(
				fieldname='final_total_month',
				label='Final Total Month ',
				fieldtype='Currency',
				read_only='1',
				insert_after='in_words',
			),
			dict(
				fieldname='final_total',
				label='Final Total ',
				fieldtype='Currency',
				read_only='1',
				insert_after='final_total_month',
			),	
			
		],
		"Quotation Item": [
			dict(
				fieldname='location',
				label='Location Area',
				fieldtype='Link',
				options='Location Area',
				insert_after='customer_item_code'
			),
			dict(
				fieldname='_location',
				label='Location ',
				fieldtype='Link',
				options='Location',
				insert_after='location',
			),
			dict(
				fieldname='total_one_time',
				label='Total One Time ',
				fieldtype='Currency',
				read_only='1',
				insert_after='stock_uom'
			),		
			dict(
				fieldname='frequency',
				label='Frequency',
				fieldtype='Currency',
				insert_after='total_one_time'
			),
			dict(
				fieldname='frequency_month',
				label='Frequency Month',
				fetch_from='uom.frequency_month',
				fieldtype='Float',
				insert_after='stock_qty',
				read_only='0',
			),
			dict(
				fieldname='total_monthly',
				label='Total Monthly',
				fieldtype='Currency',
				read_only='1',
				insert_after='frequency_month'
			),	
			dict(
				fieldname='total_year',
				label='Total/Year',
				fieldtype='Currency',
				read_only='1',
				insert_after='total_monthly'
			),
		],
		"Sales Order Item": [
			dict(
				fieldname='location',
				label='Location Area ',
				fieldtype='Link',
				options='Location Area',
				insert_after='customer_item_code'
			),
			dict(
				fieldname='_location',
				label='Location ',
				fieldtype='Link',
				options='Location',
				insert_after='location',
			),
			dict(
				fieldname='total_one_time',
				label='Total One Time ',
				fieldtype='Currency',
				read_only='1',
				insert_after='stock_uom'
			),		
			dict(
				fieldname='frequency',
				label='Frequency',
				fieldtype='Currency',
				insert_after='total_one_time'
			),
			dict(
				fieldname='frequency_month',
				label='Frequency Month',
				fetch_from='uom.frequency_month',
				fieldtype='Float',
				read_only='1',
				insert_after='stock_qty'
			),
			dict(
				fieldname='total_monthly',
				label='Total Monthly',
				fieldtype='Currency',
				read_only='1',
				insert_after='frequency_month'
			),	
			dict(
				fieldname='total_year',
				label='Total/Year',
				fieldtype='Currency',
				read_only='1',
				insert_after='total_monthly'
			),
		],
		"Sales Invoice Item": [
			dict(
				fieldname='location',
				label='Location Area',
				fieldtype='Link',
				options='Location Area',
				insert_after='customer_item_code'
			),
			dict(
				fieldname='_location',
				label='Location ',
				fieldtype='Link',
				options='Location',
				insert_after='location',
			),
			dict(
				fieldname='total_one_time',
				label='Total One Time ',
				fieldtype='Currency',
				read_only='1',
				insert_after='stock_uom'
			),	
			dict(
				fieldname='comletion_date',
				label='Completion Date ',
				fieldtype='Date',
				insert_after='quantity_and_rate'
			),	
			dict(
				fieldname='frequency',
				label='Frequency',
				fieldtype='Currency',
				insert_after='total_one_time'
			),
			dict(
				fieldname='frequency_month',
				label='Frequency Month',
				fieldtype='Float',
				fetch_from='uom.frequency_month', 
				read_only='1',
				insert_after='stock_qty'
			),
			dict(
				fieldname='total_monthly',
				label='Total Monthly',
				fieldtype='Currency',
				insert_after='frequency_month'
			),	
			dict(
				fieldname='total_year',
				label='Total/Year',
				fieldtype='Currency',
				read_only='1',
				insert_after='total_monthly'
			),
		],
		"UOM": [
			dict(
				fieldname='frequency_month',
				label='Frequency Month ',
				fieldtype='Data',
				insert_after='must_be_whole_number'
			),
		],
		"Sales Invoice": [
			dict(
				fieldname='customer_lpo',
				label='Customer LPO ',
				fieldtype='Data',
				insert_after='customer_name'
			),
			dict(
				fieldname='gsi_ref',
				label='GSI Ref ',
				fieldtype='Link',
				options='Quotation',
				insert_after='customer_lpo'
			),
			dict(
				fieldname='old_gsi',
				label='GSI ',
				fieldtype='Data',
				read_only='1',
				insert_after='due_date'
			),
			dict(
				fieldname='location_area',
				label='Location Area ',
				fieldtype='Link',
				options='Location Area',
				insert_after='gsi_ref'
			),
		],
		"Sales Order": [
			dict(
				fieldname='customer_lpo',
				label='Customer LPO ',
				fieldtype='Data',
				insert_after='customer_name'
			),
			dict(
				fieldname='gsi_ref',
				label='GSI Ref ',
				fieldtype='Link',
				options='Quotation',
				insert_after='customer_lpo'
			),
		],
		"Customer": [
			dict(
				fieldname='customer_lpo',
				label='Customer LPO ',
				fieldtype='Data',
				insert_after='lead_name'
			),
		]

	}

	create_custom_fields(custom_fields)
	frappe.msgprint("Custome Field update done.")