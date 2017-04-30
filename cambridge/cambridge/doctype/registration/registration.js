// Copyright (c) 2016, vivek and contributors
// For license information, please see license.txt




frappe.ui.form.on('Registration', {
	refresh: function(frm) {


 //Make System based on status
 if(frm.doc.status=="Process Payment"){
	 cur_frm.set_df_property("height", "reqd", 1);
	 cur_frm.set_df_property("weight", "reqd", 1);
	 cur_frm.set_df_property("birthday", "reqd", 1);
	 cur_frm.set_df_property("martial_status", "reqd", 1);
	 cur_frm.set_df_property("email", "reqd", 1);
	 cur_frm.set_df_property("nationality", "reqd", 1);
	 cur_frm.set_df_property("emirates", "reqd", 1);
	 cur_frm.set_df_property("occupation", "reqd", 1);
	 cur_frm.set_df_property("occupation_type", "reqd", 1);
	 cur_frm.set_df_property("y1", "reqd", 1);
	 cur_frm.set_df_property("y91", "reqd", 1);
	 cur_frm.set_df_property("y2", "reqd", 1);
	 cur_frm.set_df_property("y3", "reqd", 1);
	 cur_frm.set_df_property("y0", "reqd", 1);
	 cur_frm.set_df_property("y4", "reqd", 1);
	 cur_frm.set_df_property("gastric", "reqd", 1);
	 cur_frm.set_df_property("dundental_ulcer", "reqd", 1);
	 cur_frm.set_df_property("gallstones", "reqd", 1);
	 cur_frm.set_df_property("y5", "reqd", 1);
	 cur_frm.set_df_property("constipation", "reqd", 1);
	 cur_frm.set_df_property("colitis", "reqd", 1);
	 cur_frm.set_df_property("piles", "reqd", 1);
	 cur_frm.set_df_property("y6", "reqd", 1);
	 cur_frm.set_df_property("kidney_problem", "reqd", 1);
	 cur_frm.set_df_property("y8", "reqd", 1);
	 cur_frm.set_df_property("gout", "reqd", 1);
	 cur_frm.set_df_property("y9", "reqd", 1);
	 cur_frm.set_df_property("epilepsy", "reqd", 1);
	 cur_frm.set_df_property("y10", "reqd", 1);
	 cur_frm.set_df_property("y11", "reqd", 1);
	 cur_frm.set_df_property("bulmia", "reqd", 1);
	 cur_frm.set_df_property("y12", "reqd", 1);
	 cur_frm.set_df_property("y13", "reqd", 1);
	 cur_frm.set_df_property("y14", "reqd", 1);
	 cur_frm.set_df_property("y15", "reqd", 1);
	 cur_frm.set_df_property("y16", "reqd", 1);
	 cur_frm.set_df_property("y17", "reqd", 1);
	 cur_frm.set_df_property("slc", "reqd", 1);
	 cur_frm.set_df_property("exercise", "reqd", 1);
	 cur_frm.set_df_property("y21", "reqd", 1);
	 cur_frm.set_df_property("daily_intake_of_water", "reqd", 1);
	 cur_frm.set_df_property("reasons_for_weight_loss", "reqd", 1);
	 cur_frm.set_df_property("sbm", "reqd", 1);
	 cur_frm.set_df_property("lowest_weight", "reqd", 1);
	 cur_frm.set_df_property("highest_weight", "reqd", 1);
	 cur_frm.set_df_property("smoking", "reqd", 1);
	 cur_frm.set_df_property("alcohol", "reqd", 1);
	 cur_frm.set_df_property("q111", "reqd", 1);
	 cur_frm.set_df_property("y19", "reqd", 1);
	 cur_frm.set_df_property("y20", "reqd", 1);
	 cur_frm.set_df_property("diet_plan", "reqd", 1);
	 cur_frm.set_df_property("aim", "reqd", 1);
 }

  if(frm.doc.status=="Process Payment" && frm.doc.sex=="Female"){
		cur_frm.set_df_property("q8", "reqd", 1);
		cur_frm.set_df_property("q4", "reqd", 1);
		cur_frm.set_df_property("q7", "reqd", 1);
		cur_frm.set_df_property("q5", "reqd", 1);
		cur_frm.set_df_property("q6", "reqd", 1);
	}

// New Registration - Make Appointment

	if(frm.doc.status!="Active" && frm.doc.status!="Appointed" && frm.doc.__islocal != 1){
	frm.add_custom_button(__("Make Appointment"), function() {
	 frappe.model.open_mapped_doc({
		 method: "cambridge.cambridge.doctype.registration.registration.make_appointment",
		 frm: cur_frm
	 });
	}, __("Make"));
	}

//---- Can Make Customer if Registration Payment Free

		if(frm.doc.status!="Active" && frm.doc.status=="Process Payment" && frm.doc.__islocal != 1){
			frm.add_custom_button("Make Customer", function() {
				frappe.call({
					method: "cambridge.cambridge.doctype.registration.registration.make_customer",
					args:{"frm":frm.doc.name},
					callback: function(r) {
						var doclist = frappe.model.sync(r.message);
		        frappe.set_route("Form", doclist[0].doctype, doclist[0].name);
					}
				});
			}, __("Make"));

		}


  if(frm.doc.status!="On Hold" && frm.doc.__islocal != 1){
           frm.add_custom_button(__("Set On Hold"), function() {
					frm.doc.previous_state = frm.doc.status;
         	frm.doc.status = "On Hold";
					frm.refresh_field("status");
          frm.save();
    }); }

  if (frm.doc.status=="On Hold" && frm.doc.__islocal != 1){
       frm.add_custom_button(__("Unhold"), function() {
			frm.doc.status = frm.doc.previous_state;
			frm.refresh_field("status");
	   frm.save();
  }); }

	if(frm.doc.status=="Process Payment" && frm.doc.registration_payment=="Pending"){
					 frm.add_custom_button(__("Free Registration"), function() {
				   frm.doc.registration_payment = "Free";
					 frm.refresh_field("registration_payment");
					 frm.save();
		}); }

	if(frm.doc.status=="Process Payment" && frm.doc.registration_payment=="Free"){
		frm.add_custom_button(__("Payed Registration"), function() {
		frm.doc.registration_payment = "Pending";
		frm.refresh_field("registration_payment");
		frm.save();
	}); }



	}
});


frappe.ui.form.on("Registration", "validate", function(frm) {


    if (frm.doc.no_children < frm.doc.overweight_children) {
        msgprint("Overweight Children should is more than No of Children, PLease check");
        validated = false;
    }

     frm.doc.customer_name = frm.doc.first_name + " " + frm.doc.middle_name + " " + frm.doc.last_name
});


frappe.ui.form.on("Registration", "height", function(frm, doctype, name) {
  var v1 = frm.doc.height * 0.01;
  frm.doc.bmi = frm.doc.weight / (v1 * v1);
	if(frm.doc.bmi < 20){frm.doc.bmi_scale="Underweight"}
	if(frm.doc.bmi >= 20 && frm.doc.bmi <= 25){frm.doc.bmi_scale="Healthy weight"}
	if(frm.doc.bmi >= 25 && frm.doc.bmi <= 30){frm.doc.bmi_scale="Overweight"}
	if(frm.doc.bmi >= 30 && frm.doc.bmi <= 39){frm.doc.bmi_scale="Obese Weight"}
	if(frm.doc.bmi >= 40){frm.doc.bmi_scale="Very Obese"}
  refresh_field("bmi");
	refresh_field("bmi_scale");
});

frappe.ui.form.on("Registration", "weight", function(frm, doctype, name) {
  var v1 = frm.doc.height * 0.01;
  frm.doc.bmi = frm.doc.weight / (v1 * v1);
	if(frm.doc.bmi < 20){frm.doc.bmi_scale="Underweight"}
	if(frm.doc.bmi >= 20 && frm.doc.bmi <= 25){frm.doc.bmi_scale="Healthy weight"}
	if(frm.doc.bmi >= 25 && frm.doc.bmi <= 30){frm.doc.bmi_scale="Overweight"}
	if(frm.doc.bmi >= 30 && frm.doc.bmi <= 39){frm.doc.bmi_scale="Obese Weight"}
	if(frm.doc.bmi >= 40){frm.doc.bmi_scale="Very Obese"}

  refresh_field("bmi");
	refresh_field("bmi_scale");
});

frappe.ui.form.on("Registration", "birth_date", function(frm, doctype, name) {
  var v1 = 0;
  v1 = frappe.datetime.get_diff(frappe.datetime.get_today(), frm.doc.birth_date);
  frm.doc.age = Math.floor((v1).toFixed(2) / 365.25);
  refresh_field("age");
});

frappe.ui.form.on("Registration", "no_weeks", function(frm, doctype, name) {
 if (frm.doc.weight && frm.doc.height){
	if(frm.doc.sex == "Male"){
	 frm.doc.bmr =  (10 * frm.doc.weight) + (6.25 * frm.doc.height) - (5 *frm.doc.age) + 5;
         }
        if(frm.doc.sex == "Female"){
	 frm.doc.bmr =  (10 * frm.doc.weight) + (6.25 * frm.doc.height) - (5 *frm.doc.age) - 161;
         }
         frm.doc.wloss_week = (((frm.doc.bmr * frm.doc.pratio) - frm.doc.calorie_intake) / 1000) * frm.doc.no_weeks;
         frm.doc.week_to_reach_goal = (frm.doc.weight - frm.doc.aim) / (((frm.doc.bmr * frm.doc.pratio) - frm.doc.calorie_intake)/1000);

    }
	refresh_field("pratio")
	refresh_field("bmr")
  refresh_field("week_to_reach_goal");
  refresh_field("wloss_week");
});


frappe.ui.form.on("Registration", "aim", function(frm, doctype, name) {
 if (frm.doc.weight && frm.doc.height){
	if(frm.doc.sex == "Male"){
	 frm.doc.bmr =  (10 * frm.doc.weight) + (6.25 * frm.doc.height) - (5 *frm.doc.age) + 5;
         }
        if(frm.doc.sex == "Female"){
	 frm.doc.bmr =  (10 * frm.doc.weight) + (6.25 * frm.doc.height) - (5 *frm.doc.age) - 161;
         }
         frm.doc.wloss_week = (((frm.doc.bmr * frm.doc.pratio) - frm.doc.calorie_intake) / 1000) * frm.doc.no_weeks;
         frm.doc.week_to_reach_goal = (frm.doc.weight - frm.doc.aim) / (((frm.doc.bmr * frm.doc.pratio) - frm.doc.calorie_intake)/1000);

    }
	refresh_field("pratio")
	refresh_field("bmr")
  refresh_field("week_to_reach_goal");
  refresh_field("wloss_week");
});





frappe.ui.form.on("Registration", "telephone_no", function(frm, doctype, name) {

				frappe.call({
			    method: "cambridge.cambridge.doctype.registration.registration.validate_mobile",
			    args: {
			        "frm" : frm.doc.telephone_no,
			    },
			    callback: function (r) {
			        console.log(r['message'].message);


			            if (r.message.length > 0) {
			                var html_str = '<b>Customer / Registrations</b><br><table class="table table-bordered" width="100%"><thead><tr>' +
			                    '<th bgcolor="#F7FFFE">First Name</th><th bgcolor="#F7FFFE">Last Name</th><th bgcolor="#F7FFFE">Mobile No</th></tr></thead>' +
			                    '<tbody>'

			                for (i = 0; i < r.message.length; i++) {

			                        html_str += '<tr><td>' + r.message[i].first_name + '</td><td>' + r.message[i].last_name + '</td><td>' +
			                            r.message[i].telephone_no + '</td></tr>'

			                    }


			                html_str += '</tbody></table>'


			                console.log(html_str);
			                msgprint(html_str);
										}
			          }

			    });
			});

			frappe.ui.form.on("Registration", "last_name", function(frm, doctype, name) {

							frappe.call({
						    method: "cambridge.cambridge.doctype.registration.registration.validate_name",
						    args: {
						        "first_name" : frm.doc.first_name,
										"last_name" : frm.doc.last_name
						    },
						    callback: function (r) {
						        console.log(r['message'].message);


						            if (r.message.length > 0) {
						                var html_str = '<b>Registrations</b><br><table class="table table-bordered" width="100%"><thead><tr>' +
						                    '<th bgcolor="#F7FFFE">First Name</th><th bgcolor="#F7FFFE">Last Name</th><th bgcolor="#F7FFFE">Mobile No</th></tr></thead>' +
						                    '<tbody>'

						                for (i = 0; i < r.message.length; i++) {

						                        html_str += '<tr><td>' + r.message[i].first_name + '</td><td>' + r.message[i].last_name + '</td><td>' +
						                            r.message[i].telephone_no + '</td></tr>'

						                    }


						                html_str += '</tbody></table>'


						                console.log(html_str);
						                msgprint(html_str);
													}
						          }

						    });
						});
