from __future__ import unicode_literals
import frappe
from frappe.utils import cint, cstr, flt, getdate, validate_email_add, today, add_years
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from erpnext.manufacturing.doctype.bom.bom import validate_bom_no
from dateutil.relativedelta import relativedelta
from erpnext.stock.doctype.item.item import validate_end_of_life
from erpnext.manufacturing.doctype.workstation.workstation import WorkstationHolidayError, NotInWorkingHoursError
from erpnext.projects.doctype.timesheet.timesheet import OverlapError
from erpnext.stock.doctype.stock_entry.stock_entry import get_additional_costs
from erpnext.manufacturing.doctype.manufacturing_settings.manufacturing_settings import get_mins_between_operations
from erpnext.stock.stock_balance import get_planned_qty, update_bin_qty
from erpnext.manufacturing.doctype.bom.bom import get_bom_items_as_dict
from erpnext.stock.utils import get_bin




def change_payment_registration(si, method):
	cust = frappe.get_doc("Customer", si.customer)
	reg = frappe.get_doc("Registration", cust.registration)
	if si.is_registration:
		reg.registration_payment = "Complete"
		reg.save()

def change_registration_status(cust, method):
	reg = frappe.get_doc("Registration", cust.registration)
	reg.status = "Active"
	reg.customer = cust.name
	reg.registration_date = today()
	reg.save()
	fp = frappe.new_doc("Follow up")
	fp.customer = cust.name
	fp.date = today()
	fp.diet_plan = reg.diet_plan
	fp.sex = reg.sex
	fp.age = reg.age
	fp.height = reg.height
	fp.current_kg = reg.weight
	fp.current_bmi = reg.bmi
	fp.save()


@frappe.whitelist()
def sms_list(send_list):
	sms = frappe.new_doc("SMS Center")
	sms.receiver_list = send_list
	return sms


def reserve_quote_items(quote, method):
	transfer = frappe.new_doc("Stock Entry")
	transfer.purpose = "Material Transfer"
	transfer.from_warehouse = "Stores - CHF"
	transfer.to_warehouse= "Reserved - CHF"
	for item in quote.items:
		transfer.append("items", {
		"item_code": item.item_code,
		"item_name": item.item_name,
		"description": item.description,
		"qty": item.qty,
		"uom": item.uom,
		"stock_uom": item.uom,
		"conversion_factor": 1,
		"batch_no": item.batch_no
		})
	transfer.save()
	transfer.submit()
