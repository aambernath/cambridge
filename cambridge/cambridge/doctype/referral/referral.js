// Copyright (c) 2016, vivek and contributors
// For license information, please see license.txt

frappe.ui.form.on('Referral', {
	refresh: function(frm) {

	}
});


frappe.ui.form.on('Referral', {
	refresh: function(frm) {
		frm.add_custom_button("Credit Customer", function() {
			frappe.call({
				method: "cambridge.cambridge.doctype.referral.referral.credit_customer",
				args:{"frm":frm.doc.customer},
				callback: function(r) {
					var doclist = frappe.model.sync(r.message);
					frappe.set_route("Form", doclist[0].doctype, doclist[0].name);
				}
			});
		});



}
});
