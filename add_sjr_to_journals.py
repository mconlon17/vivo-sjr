#!/usr/bin/env/python
"""
    add_sjr_to_journals.py -- Given a CSV file of SJR for each journal
    identified by ISSN, and journals from VIVO, update the SJR value of
    the journal in VIVO.

    Version 0.1 MC 2014-01-10
    --  Works as expected
"""

__author__ = "Michael Conlon"
__copyright__ = "Copyright 2014, University of Florida"
__license__ = "BSD 3-Clause license"
__version__ = "0.1"

import vivotools as vt
from datetime import datetime

print datetime.now(), "Start"
print datetime.now(), "Make raw journal dictionary"
raw_journal_dictionary = vt.make_journal_dictionary(debug=True)
print datetime.now(), "Journal dictionary has ", len(raw_journal_dictionary),\
    "entries"
print datetime.now(), "Fix Journal dictionary"
journal_dictionary = {}
for raw_issn in sorted(raw_journal_dictionary.keys()):
    issn = raw_issn.replace('-', '')
    journal_dictionary[issn] = raw_journal_dictionary[raw_issn]

print datetime.now(), "Read SJR data"
sjr_data = vt.read_csv("sjr_data.csv")
print datetime.now(), "Make SJR dictionary"
sjr_dictionary = {}
for key in sjr_data.keys():
    row = sjr_data[key]
    sjr_dictionary[row['ISSN']] = row['SJR']

print datetime.now(), "Process dictionaries"
issns = journal_dictionary.keys() + sjr_dictionary.keys()
ardf = vt.rdf_header()
srdf = vt.rdf_header()
for issn in issns:
    if issn in sjr_dictionary and issn in journal_dictionary:

    # ISSN is in both, update SJR in VIVO

        [add, sub] = vt.update_data_property(journal_dictionary[issn],\
            "ufVivo:sjr", None, sjr_dictionary[issn])
        ardf = ardf + add
        srdf = srdf + sub

    elif issn in sjr_dictionary:

    # ISSN is not in VIVO, so skip it

        continue

    else:

    # ISSN is only in VIVO, so skip it

        continue
ardf = ardf + vt.rdf_footer()
srdf = srdf + vt.rdf_footer()
print datetime.now(), "Write files"
add_file = open("add.rdf", "w")
sub_file = open("sub.rdf", "w")
print >>add_file, ardf
print >>sub_file, srdf
add_file.close()
sub_file.close()

print datetime.now(), "Finished"
