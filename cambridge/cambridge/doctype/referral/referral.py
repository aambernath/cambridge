# -*- coding: utf-8 -*-
# Copyright (c) 2015, vivek and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate,flt, cstr,random_string

class Referral(Document):
	pass

@frappe.whitelist()
def credit_customer(frm):
	pe = frappe.new_doc("Journal Entry")
	pe.voucher_type = "Credit Note"
	pe.posting_date = frappe.utils.nowdate()
	pe.append("accounts", {"account": "Registrations - CHFDXB", "debit_in_account_currency": 50})
	pe.append("accounts", {"account": "Debtors - CHFDXB", "party_type": "Customer", "party": frm, "credit_in_account_currency": 50})
	pe.save()
    	return pe
