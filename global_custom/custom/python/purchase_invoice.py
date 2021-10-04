from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
import frappe

@frappe.whitelist()
def uom_list(item):
    uom_list=frappe.db.get_list('UOM Conversion Detail',{"parent":item},'uom')
    new_uoms = []
    for uom in uom_list:
        new_uoms.append(uom['uom'])
    return new_uoms

def update_pr_to_pi(doc, action):
	for row in doc.items:
		if row.item_code and row.uom:
			uom_list=frappe.db.get_list('UOM Conversion Detail',{"parent":row.item_code},'uom')
			new_uoms = []
			for uom in uom_list:
				new_uoms.append(uom['uom'])
			if row.uom not in new_uoms:
				frappe.throw(_(f"UOM {row.uom} is invalid for the item {row.item_code} in the row {row.idx}"))
