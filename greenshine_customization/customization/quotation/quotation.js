console.log("Hello world");
frappe.ui.form.on('Quotation', {
	refresh: function(frm) {
		frm.add_custom_button(__('Make Contract'), function() {
				// frappe.call({
				// 	method:"greenshine_customization.greenshine_customization.Quotation.make_contract",
				// })
		}).addClass("btn-primary");
	}
});


