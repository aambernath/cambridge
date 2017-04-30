// Copyright (c) 2016, vivek and contributors
// For license information, please see license.txt
frappe.ui.form.on("Appointments", "onload", function(frm){
	cur_frm.set_query("class_slot", function(){
		return {
			"filters": [
				["schedule_date", ">=", frm.doc.date],
        ["occupancy", ">", 0]

			]
		}
	});
});
