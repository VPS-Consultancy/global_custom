frappe.ui.form.on('Sales Invoice Item', {
	items_add: function(frm){
    console.log('Add row clicked')
		frm.set_df_property('si_itemwise_rate_details', 'hidden', 1);
	},
  item_code: function (frm, cdt, cdn) {
    var d = locals[cdt][cdn]
    const set_fields = ['rate','date','customer','sales_invoice'];
    if(!d.item_code){
      cur_frm.set_df_property('si_itemwise_rate_details', 'hidden', 1);
    }
    if(d.item_code){
      cur_frm.set_df_property('si_itemwise_rate_details', 'hidden', 0);
      frappe.call({
        method: "global_custom.custom.python.sales_invoice.fetch_rate_details",
        args: {
          item_code: d.item_code
        },
        freeze: true,
        callback: function (r) {
            if(r.message) {
                cur_frm.set_value('si_itemwise_rate_details', []);
                $.each(r.message, function(i, d) {
                    var row = cur_frm.add_child('si_itemwise_rate_details');
                    for (let key in d) {
                        if (d[key] && in_list(set_fields, key)) {
                            row[key] = d[key];
                        }
                    }
                });
            }
            refresh_field('si_itemwise_rate_details');
        }
      })
    }
  }
});