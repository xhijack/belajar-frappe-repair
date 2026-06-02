import frappe

def validate_duplicate_si(doc, method):
    if doc.order_repair:
        si = frappe.db.exists("Sales Invoice", {"order_repair": doc.order_repair, "name": ["!=", doc.name], "docstatus": 1})
        if si:
            frappe.throw("Sales Invoice {} already linked to this Order Repair".format(si))

def update_repair_order_payment_status(doc, method):
    if doc.order_repair:
        frappe.db.set_value("Order Repair", doc.order_repair, "payment_status", "Invoiced")


def update_order_repair_in_pe(doc, method):
    for si in doc.references:
        if si.reference_doctype == "Sales Invoice":
            order_repair = frappe.db.get_value("Sales Invoice", si.reference_name, "order_repair")
            doc.reference_no = order_repair

def update_repair_order_payment_status_in_pe(doc, method):
    if doc.reference_no and doc.status == "Submitted":
        frappe.db.set_value("Order Repair", doc.reference_no, "payment_status", "Paid")