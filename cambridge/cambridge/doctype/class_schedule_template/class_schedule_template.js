// Copyright (c) 2017, vivek and contributors
// For license information, please see license.txt

frappe.ui.form.on('Class Schedule Template', {
	refresh: function(frm) {
		frm.add_custom_button("Create Now", function() {
			frappe.call({
				method: "cambridge.cambridge.doctype.class_schedule_template.class_schedule_template.make_class",
				args:{"name":frm.doc.name},
				callback: function(r) {
					frappe.msgprint("Class Schedule Created");

				}
			});
		});
	}
});
