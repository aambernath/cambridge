# -*- coding: utf-8 -*-
# Copyright (c) 2015, vivek and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, flt, getdate, validate_email_add, today, add_years
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.utils import getdate, validate_email_add, today, add_years
from erpnext.setup.doctype.sms_settings.sms_settings import send_sms
from frappe.utils import flt, get_datetime, format_datetime

class Registration(Document):
	def validate(self):
		if self.call_back_date != None:
			todo = frappe.new_doc("ToDo")
			todo.description = "Call: " + self.first_name + "on " + str(self.telephone_no)
			todo.call_back = "Yes"
			todo.reference_type = "Registration"
			todo.reference_name = self.name
			todo.owner = self.owner
			todo.date = get_datetime(self.call_back_date)
			todo.save()
		self.disable_customer()
		self.enable_customer()
		self.referral()


	def referral(self):
		if self.referred_by !=None:
			ref = frappe.new_doc("Referral")
			ref.customer = self.referred_by
			ref.date = self.registration_date
			ref.registration = self.name
			ref.status = "To Pay"
			ref.save()

	def disable_customer(self):
		if self.customer and self.status=="On Hold":
			cust = frappe.get_doc("Customer", self.customer)
			cust.disabled = 1
			cust.save()

	def enable_customer(self):
		if (self.status!="On Hold" and self.registration_payment=="Complete"):
			cust = frappe.get_doc("Customer", self.customer)
			cust.disabled = 0
			cust.save()



@frappe.whitelist()
def make_appointment(source_name, target_doc=None):
    appointment = get_mapped_doc("Registration", source_name, 	{
		"Registration": {
			"doctype": "Appointments"
			}
		  })
    return appointment

@frappe.whitelist()
def make_customer(frm):
	reg = frappe.get_doc("Registration", frm)
	if reg.registration_partner:
		ref = frappe.get_doc("Registraion", reg.registration_partner)
		cust = frappe.new_doc("Customer")
		cust.first_name = ref.first_name
		cust.last_name = ref.last_name
		cust.customer_name = str(ref.first_name) + ' ' + str(ref.last_name)
		cust.customer_group = "Individual"
		cust.customer_type = "Individual"
		cust.territory = ref.emirates
		cust.telephone_no = ref.telephone_no
		cust.height = ref.height
		cust.weight = ref.weight
		cust.refistration = frm
		cust.insert()
		rlist = []
		rlist.append(ref.telephone_no)
		send_sms(rlist, "You have been registered successfully", "Cambridge")

	test = frappe.new_doc("Customer")
	test.first_name = reg.first_name
	test.last_name = reg.last_name
	test.customer_name = str(reg.first_name) + ' ' + str(reg.last_name)
	test.customer_group = "Individual"
	test.customer_type = "Individual"
	test.territory = reg.emirates
	test.sex = reg.sex
	test.age = reg.age
	test.telephone_no = reg.telephone_no
	test.height = reg.height
	test.weight = reg.weight
	test.registration = frm
	test.insert()
	rlist = []
	rlist.append(reg.telephone_no)
	send_sms(rlist, "You have been registered successfully", "Cambridge")
	if reg.registration_payment == "Free":
		reg.registration_payment = "Complete"
		reg.save()
		return test
	if reg.registration_payment	== "Pending":
		si = frappe.new_doc("Sales Invoice")
		si.customer = test.name
		si.is_pos = 1
		si.is_registration = 1
		si.debit_to = "Registrations - CHFDXB"
		si.append("items", {
		"item_code": "Registration Charge",
		"qty": 1
		})
		si.set_missing_values()
		return si


@frappe.whitelist()
def on_hold(frm, reg):
	cust = frappe.get_doc("Customer", frm)
	cust.disabled = 1
	cust.save()


@frappe.whitelist()
def un_hold(frm, reg):
	reg = frappe.get_doc("Registration", reg)
	if reg.registration_payment=="Complete":
		reg.status="Active"
		cust = frappe.get_doc("Customer", frm)
		cust.disabled = 0
		cust.save()
	else:
		reg.status="Draft"
	reg.save()
	return cust





@frappe.whitelist()
def validate_mobile(frm):
	list = frappe.get_all('Registration', filters={'telephone_no':frm}, fields=['first_name', 'last_name', 'telephone_no'])
	return list

@frappe.whitelist()
def validate_name(first_name, last_name):
	list = frappe.get_all('Registration', filters={'first_name':first_name, 'last_name':last_name}, fields=['first_name', 'last_name', 'telephone_no'])
	return list
