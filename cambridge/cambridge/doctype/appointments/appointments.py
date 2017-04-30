# -*- coding: utf-8 -*-
# Copyright (c) 2015, vivek and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import datetime
from frappe.model.document import Document
from frappe.utils import flt, get_datetime, format_datetime

class Appointments(Document):
	def validate(self):
		cs = frappe.get_doc("Class Schedule", self.class_slot)
		if self.booked == "No":
			if self.status == "Seat Reserved":
				cs.occupancy = cs.occupancy - 1
				self.booked = "Yes"
		if self.booked == "Yes":
			if self.status == "Cancel":
				cs.occupancy = cs.occupancy + 1
				self.booked = "No"
		cs.title =  str(cs.from_time) + ' / R: ' + str(cs.occupancy)
		cs.class_title = str(cs.from_time) + '/' + str(cs.session_type) + '/' + str(cs.language) + '/ R: ' + str(cs.occupancy)
		cs.save()

		if self.registration:
			reg = frappe.get_doc("Registration", self.registration)
			reg.status = "Appointed"
			reg.appointment_status = self.status
			reg.save()


	def after_insert(self):
		reg = frappe.get_doc("Registration", self.registration)
		reg.appointment = self.name
		reg.save()
		if self.status == "Seat Confirmed":
			todo = frappe.new_doc("ToDo")
			todo.description = "Call: " + self.first_name + "on " + str(self.telephone_no)
			todo.call_back = "Yes"
			todo.reference_type = "Appointments"
			todo.reference_name = self.name
			todo.owner = self.owner
			todo.date = get_datetime(self.schedule_date) - datetime.timedelta(days= 1)
			todo.save()
