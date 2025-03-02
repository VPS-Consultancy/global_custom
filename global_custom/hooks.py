from . import __version__ as app_version

app_name = "global_custom"
app_title = "Global Custom"
app_publisher = "VPS Consultancy"
app_description = "Custom application"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vps@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/global_custom/css/global_custom.css"
# app_include_js = "/assets/global_custom/js/global_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/global_custom/css/global_custom.css"
# web_include_js = "/assets/global_custom/js/global_custom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "global_custom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "global_custom.install.before_install"
# after_install = "global_custom.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "global_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice": {
		"validate": [
			"global_custom.custom.python.sales_invoice.update_si_to_dn",
			"global_custom.custom.python.sales_invoice.restrict_role"
		],
		"on_cancel": "global_custom.custom.python.sales_invoice.unlink"
	},
	"Purchase Receipt": {
		"validate":[
			"global_custom.custom.python.purchase_receipt.validate_return_receipt",
			"global_custom.custom.python.purchase_receipt.update_po_to_pr",
			"global_custom.custom.python.purchase_receipt.restrict_role"
		]
	},
	"Purchase Invoice": {
		"validate":[
			"global_custom.custom.python.purchase_invoice.update_pr_to_pi",
			"global_custom.custom.python.purchase_invoice.restrict_role"
		]

	},
	"Purchase Order": {
		"validate":"global_custom.custom.python.purchase_order.update_po"
	},
	"Delivery Note": {
		"validate":[
			"global_custom.custom.python.delivery_note.update_dn",
			"global_custom.custom.python.delivery_note.restrict_role"
		]
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"global_custom.tasks.all"
# 	],
# 	"daily": [
# 		"global_custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"global_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"global_custom.tasks.weekly"
# 	]
# 	"monthly": [
# 		"global_custom.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "global_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "global_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "global_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"global_custom.auth.validate"
# ]
doctype_js = {
    "Purchase Order": "custom/js/purchase_order.js",
	"Sales Invoice": "custom/js/sales_invoice.js",
	"Sales Order": 'custom/js/sales_order.js'

}
after_install = "global_custom.custom.python.purchase_order.make_custom_fields",
after_install = "global_custom.custom.python.sales_invoice.make_custom_fields"
