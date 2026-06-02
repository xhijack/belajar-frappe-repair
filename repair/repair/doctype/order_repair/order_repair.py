# Copyright (c) 2026, PT Sopwer Tekonologi Indonesia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class OrderRepair(Document):
	def validate(self):
		docs = frappe.db.exists("Order Repair", {"status": "Progress", "customer": self.customer, "docstatus": 1}	)
		if docs:
			frappe.throw("Customer {} has order in progress".format(self.customer))

		frappe.db.set_value("Customer", self.customer, "status", "Dikerjakan")