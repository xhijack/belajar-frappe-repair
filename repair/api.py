import frappe


@frappe.whitelist()
def change_status(current_status, name):
    if current_status == "Pending":
        frappe.db.set_value("Order Repair", name, "status", "Progress")
    elif current_status == "Progress":
        frappe.db.set_value("Order Repair", name, "status", "Completed")

@frappe.whitelist()
def create_sales_invoice(name):
    order_repair = frappe.get_doc("Order Repair", name)
    if order_repair.status != "Completed":
        frappe.throw("Order Repair {} is not completed".format(name))

    sales_invoice = frappe.new_doc("Sales Invoice")
    sales_invoice.customer = order_repair.customer
    sales_invoice.order_repair = name
    for item in order_repair.items:
        sales_invoice.append("items", {
            "item_code": item.item_code,
            "item_name": item.item_name,
            "qty": item.qty,
            "rate": item.rate,
            "total": item.total
        })
    sales_invoice.insert()
    return sales_invoice.name

