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

// frappe.ui.form.on("Quotation Item", {
//     refresh: function(frm) {
//         // make calculation on the fields
//         var a = frm.doc.amount * frm.doc.frequency;
//         var b = ( frm.doc.amount * frm.doc.frequency ) * frm.doc.frequency_month
//         frm.set_value("total_monthly", a);
//         frm.set_value("total_year", b);
//         frm.refresh_field("total_monthly, total_year");

//     }
// });

frappe.ui.form.on('Quotation Item', {
	item_code: function(frm, cdt, cdn) {
		console.log("Item table")
		var child = locals[cdt][cdn];
		console.log(child.frequency_month);
		console.log(child);
    }
})


