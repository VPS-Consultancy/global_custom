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

{% include 'erpnext/selling/sales_common.js' %};
frappe.provide("erpnext.accounts");


erpnext.accounts.SalesInvoiceController = erpnext.selling.SellingController.extend({
delivery_note_btn: function() {
  var me = this;
  this.$delivery_note_btn = this.frm.add_custom_button(__('Delivery Note'),
    function() {
      erpnext.utils.map_current_doc({
        method: "erpnext.stock.doctype.delivery_note.delivery_note.make_sales_invoice",
        source_doctype: "Delivery Note",
        target: me.frm,
        date_field: "posting_date",
        setters: {
          customer: me.frm.doc.customer || undefined,
          posting_date: undefined
        },
        get_query: function() {
          var filters = {
            docstatus: 1,
            company: me.frm.doc.company,
            is_return: 0
          };
          if(me.frm.doc.customer) filters["customer"] = me.frm.doc.customer;
          return {
            query: "erpnext.controllers.queries.get_delivery_notes_to_be_billed",
            filters: filters
          };
        }
      });
    }, __("Get Items From"));
}
})