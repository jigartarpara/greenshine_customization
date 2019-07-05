frappe.ui.form.on('Sales Order', {
    refresh: function(frm) {
        
          frm.add_custom_button(__("Work Order Schedule"), function(){
             
            frappe.model.open_mapped_doc({
              method: 
              "greenshine_customization.customization.salesorder.salesorder.make_work_order_schedule",
              frm: cur_frm
            })
          }, __("Make"));
        },
  
  });