Motifs
======

In genomics, a `motif <https://en.wikipedia.org/wiki/Sequence_motif>`_ is a commonly appearing pattern that geneticists believe is related to biological function of the molecule the genes generate (e.g., the protein that the ribosome will construct using the DNA). There are many such motifs. For example, the N-glycosylation motif is of the form asparagine (N) followed by any amino acid but proline (P), followed by serine (S) or threonine (T), followed by any amino acid but proline (P). We might write this motif as something like:

.. code-block:: 

    N[not P][ST][not P]

Bioinformaticists are often interested in identifying such motifs. Finding these motifs in DNA help predict the the function of genes: which proteins do they encode and what can we guess about those proteins' structures?