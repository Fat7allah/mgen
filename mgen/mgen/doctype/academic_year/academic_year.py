import frappe
from frappe.model.document import Document

class AcademicYear(Document):
    def validate(self):
        # Ensure only one active academic year
        if self.is_active:
            active_years = frappe.get_all(
                "Academic Year",
                filters={"is_active": 1, "name": ["!=", self.name]}
            )
            if active_years:
                frappe.throw("There can only be one active academic year at a time.")
        
        # Ensure end date is after start date
        if self.start_date and self.end_date and self.start_date > self.end_date:
            frappe.throw("End date cannot be before start date.")
