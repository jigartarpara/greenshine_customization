frappe.ui.form.on("Quotation tem", {
    refresh: function(frm) {
        // make calculation on the fields
        var a = frm.doc.amount * frm.doc.frequency;
        var b = ( frm.doc.amount * frm.doc.frequency ) * frm.doc.frequency_month
        frm.set_value("total_monthly", a);
        frm.set_value("total_year", b);
        frm.refresh_field("total_monthly, total_year");

    }
});
