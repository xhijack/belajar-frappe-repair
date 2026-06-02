frappe.ui.form.on("Customer", {
    refresh: function(frm) {
        frm.add_custom_button(__('Create Repair Order'), function() {
            frappe.call({
                'method': "repair.api.create_repair_order",
                'args': {
                    'customer': frm.doc.name
                },
            })
        }).addClass("btn-primary");
    }
})