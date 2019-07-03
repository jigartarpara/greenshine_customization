frappe.ui.form.on('Quotation', {
  refresh: function(frm) {
      
        frm.add_custom_button(__("Greenshine Contract"), function(){
           
          frappe.model.open_mapped_doc({
            method: 
            "greenshine_customization.greenshine_customization.doctype.greenshine_contract.greenshine_contract.make_contract",
            frm: cur_frm
          })
        }, __("Make"));
      },

});

frappe.ui.form.on('Quotation Item', {
	qty: function(frm, cdt, cdn) {
		calculate_change_data(frm,cdt,cdn);
    },
    frequency: function(frm, cdt, cdn) {
		calculate_change_data(frm,cdt,cdn);
    },
    rate: function(frm, cdt, cdn) {
		calculate_change_data(frm,cdt,cdn);
    },
    frequency_month: function(frm, cdt, cdn) {
		calculate_change_data(frm,cdt,cdn);
    },
})

var calculate_change_data = function(frm,cdt,cdn) {
    var child = locals[cdt][cdn];
    frappe.model.set_value(child.doctype, child.name, "total_one_time", child.qty*child.rate);       
    frappe.model.set_value(child.doctype, child.name, "total_monthly", child.total_one_time*child.frequency);       
    frappe.model.set_value(child.doctype, child.name, "total_year", child.total_monthly*child.frequency_month);       
}