# -*- coding: utf-8 -*-
# Copyright 2014 Graeme Gellatly
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Pricelist Extensions',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'category': 'Sales & Purchases',
    'author': 'O4SB - Graeme Gellatly',
    'website': 'https://o4sb.com',
    'depends': ['product', 'sale'],
    "summary": "This module implements many2many products in pricelists.",
    'data': ['views/product_pricelist_view.xml',
             'views/product_price_category_view.xml',
             'security/ir.model.access.csv',
             ],
    'installable': True,
    'active': False,
}
