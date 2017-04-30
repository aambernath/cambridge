// Copyright (c) 2016, vivek and contributors
// For license information, please see license.txt

frappe.ui.form.on('Follow up', {
	refresh: function(frm) {

	}
});


frappe.ui.form.on("Follow up", "customer", function(frm, doctype, name) {

				frappe.call({
			    method: "cambridge.cambridge.doctype.follow_up.follow_up.get_last_follow_up",
			    args: {
			        "frm" : frm.doc.customer,
			    },
			    callback: function (r) {
			        console.log(r.message[0][0]);
							frm.doc.last_followup_date = r.message[0][1];
							frm.doc.previous_weight = r.message[0][0];
							frm.doc.diet_plan = r.message[0][2];
							frm.refresh_field("last_followup_date");
							frm.refresh_field("previous_weight");
							frm.refresh_field("diet_plan");

			          }

			    });
			});
