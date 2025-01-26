import frappe
from frappe.model.document import Document

class Member(Document):
    def validate(self):
        self.validate_province_region()

    def validate_province_region(self):
        if self.province and self.region:
            province_doc = frappe.get_doc("Province", self.province)
            if province_doc.region != self.region:
                frappe.throw("الإقليم المحدد لا ينتمي إلى الجهة المحددة")
