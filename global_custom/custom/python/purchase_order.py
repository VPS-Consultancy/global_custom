from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
import frappe

def make_custom_fields(update=True):
    custom_fields = {
        "Purchase Order": [
            {
                "fieldname": "po_itemwise_rate_details",
                "label": "Itemwise Rate Details",
                "fieldtype": "Table",
                "options": "Purchase Order Itemwise Rate Details",
                "insert_after": "items",
                "read_only": 1,
                "depends_on": "eval: doc.docstatus == 0",
            }
        ]
    }
    create_custom_fields(
        custom_fields, ignore_validate=frappe.flags.in_patch, update=update
    )

@frappe.whitelist()
def fetch_rate_details(item_code):
    doc_count = 0
    rate_details = []
    po_details = frappe.get_all('Purchase Order Item',['rate','parent'],{'item_code':item_code,'parenttype':'Purchase Order'},order_by="modified")
    for row in po_details[::-1]:
        if frappe.db.get_value('Purchase Order', row.parent,'docstatus') == 1:
            po_doc = frappe.get_doc('Purchase Order', row.parent)
            rate_details.append(
                {
                'purchase_order': row.parent,
                'date': po_doc.transaction_date,
                'supplier': po_doc.supplier, 
                'rate': row.rate}
            )
            doc_count += 1
        if doc_count == 5:
            break
    return rate_details

@frappe.whitelist()
def uom_list(item):
    uom_list=frappe.db.get_list('UOM Conversion Detail',{"parent":item},'uom')
    new_uoms = []
    for uom in uom_list:
        new_uoms.append(uom['uom'])
    return new_uoms



def update_po(doc, action):
	for row in doc.items:
		if row.item_code and row.uom:
			uom_list=frappe.db.get_list('UOM Conversion Detail',{"parent":row.item_code},'uom')
			new_uoms = []
			for uom in uom_list:
				new_uoms.append(uom['uom'])
			if row.uom not in new_uoms:
				frappe.throw((f"UOM {row.uom} is invalid for the item {row.item_code} in the row {row.idx}"))
