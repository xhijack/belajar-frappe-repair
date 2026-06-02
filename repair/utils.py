import frappe

def validate_duplicate_si(doc, method):
    if doc.order_repair:
        si = frappe.db.exists("Sales Invoice", {"order_repair": doc.order_repair, "name": ["!=", doc.name], "docstatus": 1})
        if si:
            frappe.throw("Sales Invoice {} already linked to this Order Repair".format(si))