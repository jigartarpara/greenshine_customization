// Copyright (c) 2019, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('Naming Series Mapping', {
	refresh: function(frm) {
		frappe.call({
			method:"greenshine_customization.greenshine_customization.doctype.naming_series_mapping.naming_series_mapping.get_series",
			callback:function(r){
				$.each(r.message, function(key, value){
					set_field_options(key, value)
				})
			}
		})
	},
});