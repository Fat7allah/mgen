__version__ = '0.0.2'

app_name = "mgen"
app_title = "Modern Generic ERP"
app_publisher = "Your Company"
app_description = "Modern Generic Enterprise Resource Planning System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "your.email@example.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mgen/css/mgen.css"
# app_include_js = "/assets/mgen/js/mgen.js"

# include js, css files in header of web template
# web_include_css = "/assets/mgen/css/mgen.css"
# web_include_js = "/assets/mgen/js/mgen.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mgen/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

before_install = "mgen.setup.before_install"
after_install = "mgen.setup.after_install"

# Uninstallation
# ------------

before_uninstall = "mgen.setup.before_uninstall"
after_uninstall = "mgen.setup.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mgen.setup.before_app_install"
# after_app_install = "mgen.setup.after_app_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mgen.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#     "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#     "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#     "ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#     "*": {
#         "on_update": "method",
#         "on_cancel": "method",
#         "on_trash": "method"
#     }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#     "all": [
#         "mgen.tasks.all"
#     ],
#     "daily": [
#         "mgen.tasks.daily"
#     ],
#     "hourly": [
#         "mgen.tasks.hourly"
#     ],
#     "weekly": [
#         "mgen.tasks.weekly"
#     ],
#     "monthly": [
#         "mgen.tasks.monthly"
#     ]
# }

# Testing
# -------

# before_tests = "mgen.install.before_tests"
