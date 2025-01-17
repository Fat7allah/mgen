import frappe

def before_install():
    """Run before app installation"""
    pass

def after_install():
    """Run after app installation"""
    # Create default workspace
    create_default_workspace()

def before_uninstall():
    """Run before app uninstallation"""
    pass

def after_uninstall():
    """Run after app uninstallation"""
    pass

def create_default_workspace():
    """Create default workspace for MGEN"""
    if not frappe.db.exists("Workspace", "MGEN"):
        workspace = frappe.new_doc("Workspace")
        workspace.name = "MGEN"
        workspace.label = "MGEN"
        workspace.category = "Modules"
        workspace.is_standard = 1
        workspace.insert(ignore_permissions=True)
