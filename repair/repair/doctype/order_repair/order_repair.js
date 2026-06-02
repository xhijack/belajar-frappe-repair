// Copyright (c) 2026, PT Sopwer Tekonologi Indonesia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Order Repair", {
	refresh(frm) {
        //buat button
        if (frm.doc.docstatus === 1 && frm.doc.status !== "Completed") {
            frm.add_custom_button(__('Dikerjakan'), function() {
                frappe.call({
                    method: "repair.api.change_status",
                    args: {
                        current_status: frm.doc.status,
                        name: frm.doc.name
                    },callback: function(r) {
                        if (r.message) {
                            frappe.msgprint(r.message);
                            frm.reload_doc();
                        }
                    }
                })

            }
            ).addClass("btn-primary");
        }
        if (frm.doc.docstatus === 1 && frm.doc.status === "Completed") {
            frm.add_custom_button(__('Create Sales Invoice'), function() {
               frappe.call({
                method: "repair.api.create_sales_invoice",
                args: {
                    name: frm.doc.name
                },
                callback: function(r){
                    if (r.message){
                        frappe.set_route("Form","Sales Invoice", r.message)
                    }
                }
               })

            } 
            ).addClass("btn-primary");
        }
	},
    customer: function(frm) {
        alert('Customer changed');
    },
    price_list: function(frm) {
        calculate_row(frm)
    }
});


frappe.ui.form.on("Order Repair Item", {
    item_code(frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        let duplicate = frm.doc.items.some(item => item.item_code === row.item_code && item.name !== row.name);
        if (duplicate) {
            frappe.msgprint(__("Item code {0} already exists in the items table.", [row.item_code]));
            row.item_code = "";
            frm.refresh_field("items");
        }
    },
    qty(frm, cdt, cdn) {
        calculate_row(frm, cdt, cdn);
    },
    rate(frm, cdt, cdn) {
        calculate_row(frm, cdt, cdn);
    }
});

function calculate_row(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    row.total = flt(row.qty) * flt(row.rate);
    frm.refresh_field("items");
    calculate_total(frm);
}

function calculate_total(frm) {
    let total = 0;
    frm.doc.items.forEach(item => {
        total += flt(item.total);
    });
    frm.set_value("grand_total", total);
}