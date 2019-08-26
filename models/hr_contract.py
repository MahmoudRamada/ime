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
</odoo> """
