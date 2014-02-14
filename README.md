# Add SJR data to VIVO

SJR -- the Scientific Journal Rankings -- are open source rankings of journals
produced by [SciMago](http://www.scimagojr.com/journalrank.php)

The rankings are scores for each journal based on citations.  Higher scores
indicate more citations.

The data is freely available from SciMago and can be downloaded to a CSV file.
From there, a simple python script matches the ISSN of journals in VIVO to the
ISSN in the SciMago data.  If a match occurs, the SJR score for the journal is
updated if found, or added if new.

The code here requires an ontology extension.  At UF, the extension creates
a journal data property called ufVivo:sjr.
