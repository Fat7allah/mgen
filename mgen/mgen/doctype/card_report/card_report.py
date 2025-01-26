import frappe
from frappe.model.document import Document

class CardReport(Document):
    def validate(self):
        self.validate_province_region()
        self.calculate_amounts()

    def validate_province_region(self):
        if self.province and self.region:
            province_doc = frappe.get_doc("Province", self.province)
            if province_doc.region != self.region:
                frappe.throw("الإقليم المحدد لا ينتمي إلى الجهة المحددة")

    def calculate_amounts(self):
        # Calculate total amount (100 DH per card)
        self.total_amount = self.card_count * 100

        # Calculate remaining amount
        self.remaining = self.total_amount - self.payment

        # Calculate shares
        self.office_share = self.total_amount * 0.5  # 50%
        self.region_share = self.total_amount * 0.2  # 20%
        self.province_share = self.total_amount * 0.3  # 30%
