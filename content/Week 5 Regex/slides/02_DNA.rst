Running example: DNA and amino acid motifs
==========================================

Bioinformatics uses computational methods to ask biology questions; a great deal of bioinformatics has to do with DNA, RNA, and genomic sequencing. It's a common activity to look for particular sequences in a list of DNA or RNA bases, or to look for particular `"motifs" in sequences <https://en.wikipedia.org/wiki/Sequence_motif>`_ of bases or the amino acids they encode.

As our running example, we'll be thinking about DNA and amino acid motifs. By way of reminder, the `DNA bases <https://en.wikipedia.org/wiki/DNA>`_ are:

* `cytosine <https://en.wikipedia.org/wiki/Cytosine>`_, written C
* `guanine <https://en.wikipedia.org/wiki/Guanine>`_, written G
* `adenine <https://en.wikipedia.org/wiki/Adenine>`_, written A
* `thymine <https://en.wikipedia.org/wiki/Thymine>`_, written T
  
Every three DNA bases is a codon denoting a particular amino acid (or the STOP code); `Wikipedia has a nice table explaining the encoding <https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables#Standard_DNA_codon_table>`_.

To work with DNA and amino acids in Python, we can encode them as strings. For DNA, it's straightforward: "CGA" corresponds to the DNA strand containing cytosine, guanine, and then adenine.

For amino acids, it's slightly more complex. We can use the `IUPAC notation <https://en.wikipedia.org/wiki/International_Union_of_Pure_and_Applied_Chemistry#Amino_acid_and_nucleotide_base_codes>`_ for the amino acids we'll see:

.. code-block:: 

    A     Alanine
    C     Cysteine
    D     Aspartic acid
    E     Glutamic acid
    F     Phenylalanine
    G     Glycine
    H     Histidine
    I     Isoleucine
    K     Lysine
    L     Leucine
    M     Methionine
    N     Asparagine
    P     Proline
    Q     Glutamine
    R     Arginine
    S     Serine
    T     Threonine
    V     Valine
    W     Tryptophan
    Y     Tyrosine
    _     Translation stop 

So ``'NRSA'`` represents the sequence of amino acids Asparagine, Arginine, Serine, Alanine.

