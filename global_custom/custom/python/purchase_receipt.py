from math import pi
import frappe
from frappe import _
def validate_return_receipt(doc,action):
    if doc.is_return:
        pi_list=frappe.db.get_list("Purchase Invoice Item",{'purchase_receipt':doc.return_against},"parent")
        new_pi_list = []
        for inv in pi_list:
            if not inv['parent'] in new_pi_list:
                new_pi_list.append(inv['parent'])
        for inv in new_pi_list:
            is_return=frappe.db.get_value("Purchase Invoice",inv,"is_return")
            if not is_return:
                return_inv = frappe.db.get_value("Purchase Invoice",{"return_against":inv,"is_return":1})
                if not return_inv:
                    frappe.throw(f"Unable to proceed bacause linked purchase invoice {inv} have no return invoice")


@frappe.whitelist()
def uom_list(item):
    uom_list=frappe.db.get_list('UOM Conversion Detail',{"parent":item},'uom')
    new_uoms = []
    for uom in uom_list:
        new_uoms.append(uom['uom'])
    return new_uoms



def update_po_to_pr(doc, action):
	for row in doc.items:
		if row.item_code and row.uom:
			uom_list=frappe.db.get_list('UOM Conversion Detail',{"parent":row.item_code},'uom')
			new_uoms = []
			for uom in uom_list:
				new_uoms.append(uom['uom'])
			if row.uom not in new_uoms:
				frappe.throw((f"UOM {row.uom} is invalid for the item {row.item_code} in the row {row.idx}"))
