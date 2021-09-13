frappe.ui.form.on('Sales Invoice Item', {
	item_code:function(frm,cdt, cdn){
	    var d=locals[cdt][cdn];
	    frappe.call({
	        method:"global_custom.custom.python.sales_invoice.uom_list",
	        args:{
	            'item': d.item_code
	        },
	        callback : function(r){
	            frm.fields_dict.items.grid.get_field(
          "uom"
        ).get_query = function () {
          return {
            filters: [["name", "in", r.message]],
          }
          };
	        }
	    })
	},
	uom:function(frm,cdt, cdn){
	    var d=locals[cdt][cdn];
	    frappe.call({
	        method:"global_custom.custom.python.sales_invoice.uom_list",
	        args:{
	            'item': d.item_code
	        },
	        callback : function(r){
	            frm.fields_dict.items.grid.get_field(
          "uom"
        ).get_query = function () {
          return {
            filters: [["name", "in", r.message]],
          }
          };
	        }
	    })
	}
})