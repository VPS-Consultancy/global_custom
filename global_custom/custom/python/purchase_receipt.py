import frappe
from frappe import _
def validate_return_receipt(doc,action):
    if doc.is_return:
        pi_list=frappe.db.get_list("Purchase Invoice Item",{'purchase_receipt':doc.return_against},"parent")
        pi_list=set(pi_list)
        for inv in pi_list:
            is_return=frappe.db.get_value("Purchase Invoice",inv,"is_return")
            if not is_return:
                return_inv = frappe.db.get_value("Purchase Invoice",{"return_against":inv,"is_return":1})
                if not return_inv:
                    frappe.throw(f"Unable to proceed bacause linked purchase invoice {inv} have no return invoice")


