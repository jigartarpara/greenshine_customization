frappe.ui.form.on('Payment Entry', {
    refresh: function(frm){
        frappe.call({
            method:"frappe.client.get_value",
            args: {
                doctype:"Naming Series Mapping",
                filters: {
                    naming_series:frm.doc.naming_series,
                },
                fieldname:["payment_type", "mode_of_payment"]
            }, 
            callback: function(r) { 
                console.log(r);
                if(r.message){
                    // set the returned value in a field
                    cur_frm.set_value("payment_type", r.message.payment_type);
                    cur_frm.set_value("mode_of_payment", r.message.mode_of_payment);
                }
            }
        })
    },
    naming_series: function(frm) {
        frappe.call({
            method:"frappe.client.get_value",
            args: {
                doctype:"Naming Series Mapping",
                filters: {
                    naming_series:frm.doc.naming_series,
                },
                fieldname:["payment_type", "mode_of_payment"]
            }, 
            callback: function(r) { 
                console.log(r);
                if(r.message){
                    // set the returned value in a field
                    cur_frm.set_value("payment_type", r.message.payment_type);
                    cur_frm.set_value("mode_of_payment", r.message.mode_of_payment);
                }
            }
        })
    },

});