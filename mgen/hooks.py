app_name = "mgen"
app_title = "MGEN"
app_publisher = "Your Company"
app_description = "Modern Generic Enterprise Resource Planning System"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "your.email@example.com"
app_license = "MIT"

# Includes in <head>
app_include_js = ["/assets/mgen/js/mgen.js"]
app_include_css = ["/assets/mgen/css/mgen.css"]

# Fixtures
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["module", "=", "MGEN"]]
    },
    {
        "doctype": "Property Setter",
        "filters": [["module", "=", "MGEN"]]
    },
    {
        "doctype": "Workspace",
        "filters": [["module", "=", "MGEN"]]
    },
    {
        "doctype": "Profession",
        "filters": [["name", "like", "%"]]
    },
    {
        "doctype": "Region",
        "filters": [["name", "like", "%"]]
    },
    {
        "doctype": "Member Role",
        "filters": [["name", "like", "%"]]
    },
    {
        "doctype": "Academic Year",
        "filters": [["name", "like", "%"]]
    }
]

# Document Events
doc_events = {
    "Academic Year": {
        "validate": "mgen.mgen.doctype.academic_year.academic_year.validate"
    }
}

# Website
website_route_rules = [
    {"from_route": "/mgen", "to_route": "MGEN"}
]
