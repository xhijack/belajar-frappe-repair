from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def after_migrate():
    custom_fields = {
        "Customer": [
            {
                "fieldname": "status",
                "label": "Status",
                "fieldtype": "Select",
                "options": "\nDikerjakan\nSelesai",
                "insert_after": "customer_group"
            }
        ],
        "Sales Invoice": [
            {
                "fieldname" : "order_repair",
                "label": "Order Repair",
                "fieldtype": "Link",
                "options": "Order Repair",
                "insert_after": "customer_name"
            }
        ]
    }

    create_custom_fields(custom_fields)