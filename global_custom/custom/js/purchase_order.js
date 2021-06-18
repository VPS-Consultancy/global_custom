cur_frm.cscript.item_code = function (frm, cdt, cdn) {
    var d = locals[cdt][cdn]
    const set_fields = ['rate','date','supplier','purchase_order'];
    if(!d.item_code){
      cur_frm.set_df_property('po_itemwise_rate_details', 'hidden', 1);
    }
    if(d.item_code){
      cur_frm.set_df_property('po_itemwise_rate_details', 'hidden', 0);
      frappe.call({
        method: "global_custom.custom.python.purchase_order.fetch_rate_details",
        args: {
          item_code: d.item_code
        },
        freeze: true,
        callback: function (r) {
            if(r.message) {
                cur_frm.set_value('po_itemwise_rate_details', []);
                $.each(r.message, function(i, d) {
                    var row = cur_frm.add_child('po_itemwise_rate_details');
                    for (let key in d) {
                        if (d[key] && in_list(set_fields, key)) {
                            row[key] = d[key];
                        }
                    }
                });
            }
            refresh_field('po_itemwise_rate_details');
        }
      })
    }
  }

frappe.ui.form.on('Purchase Order Itemwise Rate Details', {
	po_itemwise_rate_details_add: function(frm){
		frm.set_df_property('po_itemwise_rate_details', 'hidden', 1);
	}
});