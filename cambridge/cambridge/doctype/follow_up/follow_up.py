# -*- coding: utf-8 -*-
# Copyright (c) 2015, vivek and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt, cint, getdate

class Followup(Document):

	def validate(self):
		self.input_values()
		self.calculate_actual_weight_loss()
		self.calculate_suggested_weight_loss()
		self.calculate_difference()


	def input_values(self):
		self.height = frappe.db.get_value("Customer", self.customer, "height")
		self.birth_date = frappe.db.get_value("Customer", self.customer, "birth_date")
		self.sex = frappe.db.get_value("Customer", self.customer, "sex")
		self.calorie_intake = frappe.db.get_value("Diet Plan", self.diet_plan, "intake")
		self.physical_activity = frappe.db.get_value("Customer", self.customer, "physical_activity")
		self.pratio = frappe.db.get_value("Physical Activity", self.physical_activity, "ratio")
		self.age = ((frappe.utils.datetime.date.today() - frappe.utils.data.getdate(self.birth_date)).days) /  365.25
		self.no_of_days = (frappe.utils.data.getdate(self.date) - frappe.utils.data.getdate(self.last_followup_date)).days

	def calculate_actual_weight_loss(self):
		self.actual_weight_loss = flt(self.previous_weight) - flt(self.current_kg)

	def calculate_suggested_weight_loss(self):
		if self.sex == "Male":
				self.bmr = (10 * self.current_kg) + (6.25 * self.height) + (5 * self.age) + 5;
		if self.sex == "Female":
				self.bmr = (10 * self.current_kg) + (6.25 * self.height) + (5 * self.age) - 161;

		self.suggested_weight_loss = (((flt(self.bmr) * flt(self.pratio)) - flt(self.calorie_intake)) / 1000) * (flt(self.no_of_days) / 7)

	def calculate_difference(self):
		if (self.height and self.current_kg) > 0:
			self.difference = flt(self.suggested_weight_loss) - flt(self.actual_weight_loss)
			hs = (flt(self.height) * flt(self.height)) * 0.0001
			self.current_bmi = flt(self.current_kg) / hs

@frappe.whitelist()
def get_last_follow_up(frm):
	list = frappe.db.sql("""select current_kg, date, diet_plan from `tabFollow up` where customer=%s order by date desc limit 2""", frm)
	return list
