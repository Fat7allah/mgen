import frappe
from frappe import _
from frappe.model.document import Document

class AcademicYear(Document):
    def validate(self):
        self.validate_dates()
        self.validate_active_year()
    
    def validate_dates(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            frappe.throw(_("End Date cannot be before Start Date"))
    
    def validate_active_year(self):
        if self.is_active:
            # Deactivate other active academic years
            active_years = frappe.get_all("Academic Year",
                filters={"is_active": 1, "name": ["!=", self.name]})
            for year in active_years:
                doc = frappe.get_doc("Academic Year", year.name)
                doc.is_active = 0
                doc.save()
