from rest_framework import serializers
from .models import Company, Employee, Partnership


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]



class EmployeeSerializer(serializers.ModelSerializer):
    position = ChoiceField(choices=Employee.POSITION_CHOICES)

    class Meta:
        model = Employee
        fields = ['id', 'username', 'age', 'company', 'position'] 


class CompanySerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'emp_num', 'adress', 'employees']    
        read_only_fields = ['emp_num', 'employees']

    def get_employees(self, instance):
        employees = instance.employees.order_by('position')
        return EmployeeSerializer(employees, many=True).data


class CompanyEmployeeSerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ['employees']    
        read_only_fields = ['employees']

    def get_employees(self, instance):
        employees = instance.employees.order_by('position')
        return EmployeeSerializer(employees, many=True).data


class PartnershipSerializer(serializers.ModelSerializer):
    Partnership.com_1_employees = Partnership.com_1
    Partnership.com_2_employees = Partnership.com_2
    com_1_employees = CompanyEmployeeSerializer(read_only=True)
    com_2_employees = CompanyEmployeeSerializer(read_only=True)
    
    class Meta:
        model = Partnership
        fields = ['id', 'name', 'com_1', 'com_1_employees', 'com_2', 'com_2_employees'] 

