# -*- coding: utf-8 -*-
# Copyright (c) 2017, vivek and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import datetime
from frappe.model.document import Document

class ClassScheduleTemplate(Document):
	pass


@frappe.whitelist()
def make_class(name):
	cst = frappe.get_doc("Class Schedule Template", name)
	weeks = int(cst.auto_create + 1)
	for i in range(1, weeks):
		cs = frappe.new_doc("Class Schedule")
		cs.language = cst.language
		cs.session_type = cst.session_type
		cs.max_occupancy = cst.max_occupancy
		cs.occupancy = cst.max_occupancy
		cs.schedule_date = cst.schedule_date + datetime.timedelta(days= 7*i)
		cs.from_time = cst.from_time
		cs.to_time = cst.to_time
		cs.class_title = cs.schedule_date.strftime('%b-%d') + "/" + str(cs.from_time) + "/" + cs.session_type + "/" + str(cs.max_occupancy)
		cs.title = cs.class_title
		cs.consultant = cst.consultant
		cs.save()
