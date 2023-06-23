Translating DNA to amino acids
==============================

DNA is basically a physical code that is present in every living organism's cell. Think of it as a serial number . To encode DNA into amino acids it should be broken down into codons 

**Codons** are groups of three DNA bases, each of which corresponds to either an **amino acid** or a **STOP**, which terminates transcription.

A visual example would look something like this; the picture mentions the "start codon", methionone, which is the typical start codon in most eukaryotic organisms. The picture also talks about **mRNA** translation, using uracil/U instead of thymine/T. It turns out that mRNA is one-to-one with DNA (RNA transcriptase produces RNA from DNA in the nucleus). We'll be working with DNA in this class.

.. image:: /assets/images/cs515/Week5/ed3bfd85b8ec88f74515e63649b9dcd5c976e21e.png

Now that we have codons, these codon could be checked against a translation table which basically holds the respective amino acid:

.. code-block:: 

    {
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
            'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
            'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

To encode DNA into amino acids:

* Break down the DNA string into codons (i.e., groups of three)
* Look each codon up in the table
* Return the list of corresponding amino acids