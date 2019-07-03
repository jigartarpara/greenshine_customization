frappe.ui.form.on('Lead', {
    refresh: function(frm) {
        if(!frm.doc.__islocal && frm.doc.survey_form){
            
        
            frm.add_custom_button(__("Survey Form"), function(){
                frappe.model.open_mapped_doc({
                    method: "greenshine_customization.customization.lead.lead.make_survey_form",
                    frm: cur_frm
                })
            }, __("Make"));
        }
        frm.add_custom_button(__("Survey Form"), function(){
            console.log(frm);
			debugger;
			frappe.set_route("List", "Survey Form",{"lead": frm.doc.name})
            
        }, __("View"));
        
        frm.add_custom_button(__("Quotation"), function(){
            //perform desired action such as routing to new form or fetching etc.
            console.log(frm);
			debugger;
			frappe.set_route("List", "Quotation",{"party_name": frm.doc.name})
            
        }, __("View"));
    }
});