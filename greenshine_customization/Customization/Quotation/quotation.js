frappe.ui.form.on('Quotation', {
	refresh: function(frm) {
		if(!frm.doc.__islocal){

			frm.add_custom_button(__('Make Contract'), function() {
				frappe.call({
					method:"greenshine_customization.greenshine_customization.Quotation.make_contract",
				})
			}).addClass("btn-primary");
		}
	}
});


