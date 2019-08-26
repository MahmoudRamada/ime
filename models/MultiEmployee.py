# -*- coding: utf-8 -*-

from odoo import models, api, fields, _
from odoo.exceptions import Warning


class MultiEmployee(models.Model):
    _name = 'multi.employee'

    multi_emplyee_id = fields.Many2one('multi.contract')
    employee_id = fields.Many2one('hr.employee', "Employee")
    name = fields.Char("Employee name")
    wage = fields.Integer('Wage', required=True)
    struct_id = fields.Many2one(
        'hr.payroll.structure', string='Salary Structure', required=True)
    working_hours = fields.Many2one('resource.calendar', 'Working Hours')
    active = fields.Boolean("Active Employee")
    Emp_id = fields.Many2one('mobile.service')

class MultiContract(models.Model):
    _name = 'multi.contract'

    employee_ids = fields.One2many(
       'multi.employee', 'multi_emplyee_id', 'Employee(s)')
    # contract_id = fields.Many2one('mobile.service')
#     set selected employee in wizard
    @api.model
    def default_get(self, fields):
        res = super(MultiContract, self).default_get(fields)
        employees = self.env['hr.employee'].browse(
            self._context.get('active_ids', False))
        emp_list = []
        for employee in employees:
            emp_list.append(
                (0, 0, {'employee_id': employee.id, 'active': True}))
        res['employee_ids'] = emp_list
        return res

#     create selected employee's contract
    @api.multi
    def multi_employee_contract(self):

        multi_employees = self.env['multi.employee'].search(
            [('active', '=', True)])
        contract_id = \
            self.env['hr.contract'].search([('employee_id', 'in', [
                emp.employee_id.id for emp in self.employee_ids]),
                ('state', 'not in', ['close'])], order="date_start desc")
        if contract_id:
            raise Warning(_('Contract already exist of employee = %s.')
                          % ",".join(
                [contract.employee_id.name for contract in contract_id]))
        for emp_id in self.employee_ids:
            contract_vals = \
                self.env['hr.contract'].create(
                    {'name': emp_id.employee_id.name + '\'s contract',
                     'employee_id': emp_id.employee_id.id,
                     'job_id': emp_id.employee_id.job_id.id,
                     'department_id': emp_id.employee_id.department_id.id,
                     'wage': emp_id.wage,
                     'struct_id': emp_id.struct_id.id,
                     'working_hours': emp_id.working_hours.id})
            action = self.env.ref('hr_contract.action_hr_contract').read()[0]
            action['views'] = [
                (self.env.ref('hr_contract.hr_contract_view_form').id, 'form')]
            action['res_id'] = contract_vals.id

        multi_employees.unlink()
        return action


