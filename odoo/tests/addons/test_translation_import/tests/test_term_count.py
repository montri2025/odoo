# -*- coding: utf-8 -*-

import odoo
from odoo.tests import common

class TestTermCount(common.TransactionCase):

    def test_count_term(self):
        """
        Should make sure we have as many translation entries as we wanted.
        """
        odoo.tools.trans_load(self.cr, 'test_translation_import/i18n/fr.po', 'fr_FR', verbose=False)
        ids = self.env['ir.translation'].search(
            [('src', '=', '1XBUO5PUYH2RYZSA1FTLRYS8SPCNU1UYXMEYMM25ASV7JC2KTJZQESZYRV9L8CGB')])
        self.assertEqual(len(ids), 2)
