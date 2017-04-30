# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "cambridge"
app_title = "Cambridge"
app_publisher = "vivek"
app_description = "App for Cambridge Flow"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "vivek@quarkcs.com"
app_license = "MIT"



fixtures = ["Custom Field"]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cambridge/css/cambridge.css"
# app_include_js = "/assets/cambridge/js/cambridge.js"

# include js, css files in header of web template
# web_include_css = "/assets/cambridge/css/cambridge.css"
# web_include_js = "/assets/cambridge/js/cambridge.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "cambridge.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cambridge.install.before_install"
# after_install = "cambridge.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cambridge.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events
doc_events ={
    "Sales Invoice":{
        "on_submit": "cambridge.common.change_payment_registration"
    },
    "Quotation":{
        "on_submit": "cambridge.common.reserve_quote_items"
    },
    "Customer":{
        "after_insert": "cambridge.common.change_registration_status"

    }
}
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"cambridge.tasks.all"
# 	],
# 	"daily": [
# 		"cambridge.tasks.daily"
# 	],
# 	"hourly": [
# 		"cambridge.tasks.hourly"
# 	],
# 	"weekly": [
# 		"cambridge.tasks.weekly"
# 	]
# 	"monthly": [
# 		"cambridge.tasks.monthly"
# 	]
# }
calendars = ["Class Schedule"]
# Testing
# -------

# before_tests = "cambridge.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "cambridge.event.get_events"
# }
