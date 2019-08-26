Mobile Service Management v11
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
