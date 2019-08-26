# -*- coding: utf-8 -*-

from odoo import models, api, _
from odoo import exceptions


class HrContract(models.Model):
    _inherit = 'hr.contract'

    @api.multi
    @api.constrains('employee_id')
    def _check_contract_for_same_employee(self):
        if self.employee_id:
            contract_id = self.env['hr.contract'].search(
                [('id', '!=', self.id),
                 ('employee_id', '=', self.employee_id.id),
                 ('state', 'not in', ['close'])])
            if contract_id:
                raise exceptions.ValidationError(
                    _('Contract can be only created if in expired state.'))



""" 
<odoo>
    <data>
        <!-- Multi Contract Confirmation Wizard -->
        <record id="multi_employee_contract_view_wiz" model="ir.ui.view">
            <field name="name">multi.contract.wiz.form.view</field>
            <field name="model">multi.contract</field>
            <field name="arch" type="xml">
                <form string="Confirm">
                    <field name="employee_ids">
                        <tree editable="bottom">
                            <field name="employee_id"/>
                            <field name="wage"/>
                            <field name="struct_id"/>
                            <field name="working_hours"/>
                        </tree>
                    </field>
                    
                    <h3>Click confirm to create multiple contracts of employees.</h3>
                    <footer>
                        <button name="multi_employee_contract" string="Confirm" type="object" class="oe_highlight" context="{'employee_ids':employee_ids}"/>
                        or
                        <button string="Cancel" class="oe_link" special="cancel"/>
                    </footer>
                </form>
            </field>
        </record>

        <!-- Assign Multiple Contract -->

        <record id="hr_employee_action_multiple_contract" model="ir.actions.act_window">
            <field name="name">Create Contract</field>
            <field name="type">ir.actions.act_window</field>
            <field name="res_model">multi.contract</field>
            <field name="view_type">form</field>
            <field name="view_mode">form</field>
            <field name="target">new</field>
        </record>
        
        <record id="hr_employee_action_multiple_contract_mutli" model="ir.values">
            <field name="model_id" ref="base.model_res_partner"/>
            <field name="name">Create Contract</field>
            <field name="key2">client_action_multi</field>
            <field name="value" eval="'ir.actions.act_window,' + str(ref('hr_employee_action_multiple_contract'))"/>
            <field name="key">action</field>
            <field name="model">hr.employee</field>
        </record>
      
    </data>
</odoo>




 Management v11
=============================
Module for mobile service shop daily activities

Features
========
* Service request creation.
* Assigning service request to technicians.
* Mobile service ticket generation.
* Service status tracking.
* Integrated with accounting and sales module.
* Access Rights From Multiple Level.
* Mobile complaint templates.
* Invoice for parts usage and service charges.
* Email notifications to customer.
* Parts inventory.

Installation
============
	- www.odoo.com/documentation/11.0/setup/install.html
	- Install our custom addon
	- You need 'report_xlsx' module in order to get XLSX report.
	- Install 'report_xlsx' from https://apps.odoo.com/apps/modules/11.0/report_xlsx/

Configuration
=============

    No additional configurations needed

Bug Tracker
===========
Bugs are tracked on GitHub Issues. In case of trouble, please check there if your issue has already been reported.

Developer: Milind Mohan @ cybrosys, Contact: odoo@cybrosys.com

Maintainer
----------

This module is maintained by Cybrosys Technologies.

For support and more information, please visit https://www.cybrosys.com.

class ResPartner(models.Model):
    _inherit = 'res.partner'
	_name = 'sm.person'
    amount = fields.Float('Price')
    fsm_person = fields.Boolean('Is a FS Worker')
    service_location_id = fields.Many2one('fsm.location',
                                          string='Primary Service Location')


sum_cost = fields.Float(compute='_compute_sum_cost', string='Indicative Costs Total')

    @api.depends('cost_ids.amount')
    def _compute_sum_cost(self):
        for contract in self:
            contract.sum_cost = sum(contract.cost_ids.mapped('amount'))

 _sql_constraints = [
        ('driver_id_unique', 'UNIQUE(driver_id)', 'Only one car can be assigned to the same employee!')
    ]

	driver_id = fields.Many2one('res.partner', 'Driver', track_visibility="onchange", help='Driver of the vehicle', copy=False)

default=lambda self: self.env.user, required=True)
 tag_ids = fields.Many2many('fleet.vehicle.tag', 'fleet_vehicle_vehicle_tag_rel', 'vehicle_tag_id', 'tag_id', 'Tags', copy=False)




 """
