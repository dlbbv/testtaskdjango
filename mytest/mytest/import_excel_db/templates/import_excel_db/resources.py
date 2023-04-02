from import_export import resources
from import_excel_db.models import Employee


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee