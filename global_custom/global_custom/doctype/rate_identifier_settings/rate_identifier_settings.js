// Copyright (c) 2021, VPS Consultancy and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rate Identifier Settings', {
	get_rate: function(frm) {
		frm.clear_table('purchase_order_itemwise_rate_details');
		frm.clear_table('sales_invoice_itemwise_rate_details');
		const po_set_fields = ['rate','date','supplier','purchase_order'];
		const si_set_fields = ['rate','date','customer','sales_invoice'];
		if(frm.doc.item && frm.doc.date){
			frappe.call({
			method: "global_custom.global_custom.doctype.rate_identifier_settings.rate_identifier_settings.fetch_rate_details",
			args: {
				item:frm.doc.item,
				date:frm.doc.date
			},
			freeze: true,
			callback: function (r) {
				if(r.message) {
					cur_frm.set_value('purchase_order_itemwise_rate_details', []);
					$.each(r.message[0], function(i, d) {
						var row = cur_frm.add_child('purchase_order_itemwise_rate_details');
						for (let key in d) {
							if (d[key] && in_list(po_set_fields, key)) {
								row[key] = d[key];
							}
						}
					});
					cur_frm.set_value('sales_invoice_itemwise_rate_details', []);
					$.each(r.message[1], function(i, d) {
						var row = cur_frm.add_child('sales_invoice_itemwise_rate_details');
						for (let key in d) {
							if (d[key] && in_list(si_set_fields, key)) {
								row[key] = d[key];
							}
						}
					});
				}
				refresh_field('purchase_order_itemwise_rate_details');
				refresh_field('sales_invoice_itemwise_rate_details');
			}
		})
		}
		else{
			refresh_field('purchase_order_itemwise_rate_details');
			refresh_field('sales_invoice_itemwise_rate_details');
			frappe.throw(__('Kindly select date and item to fetch rate details'))
		}
	}
});
