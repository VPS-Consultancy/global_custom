# Copyright (c) 2021, VPS Consultancy and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate

class RateIdentifier(Document):
	pass

@frappe.whitelist()
def fetch_rate_details(date, item):
    po_doc_count = 0
    po_rate_details = []
    si_doc_count = 0
    si_rate_details = []
    si_details = frappe.get_all('Sales Invoice Item',['rate','parent'],{'item_code':item,'parenttype':'Sales Invoice'},order_by="modified")
    po_details = frappe.get_all('Purchase Order Item',['rate','parent'],{'item_code':item,'parenttype':'Purchase Order'},order_by="modified")
    for row in po_details[::-1]:
        if frappe.db.get_value('Purchase Order', row.parent,'docstatus') == 1:
            po_doc = frappe.get_doc('Purchase Order', row.parent)
            if po_doc.transaction_date == getdate(date):
                po_rate_details.append(
                    {
                    'purchase_order': row.parent,
                    'date': po_doc.transaction_date,
                    'supplier': po_doc.supplier, 
                    'rate': row.rate}
                )
                po_doc_count += 1
        if po_doc_count == 5:
            break

    for row in si_details[::-1]:
        if frappe.db.get_value('Sales Invoice', row.parent,'docstatus') == 1:
            si_doc = frappe.get_doc('Sales Invoice', row.parent)
            if si_doc.posting_date == getdate(date):
                si_rate_details.append(
                    {
                    'sales_invoice': row.parent,
                    'date': si_doc.posting_date,
                    'customer': si_doc.customer, 
                    'rate': row.rate}
                )
                si_doc_count += 1
        if si_doc_count == 5:
            break
    return [po_rate_details, si_rate_details]