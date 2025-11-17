Finding motifs by hand
======================

Write a function ``find_nglycosylation_motif`` that scans a list of amino acids to find the index of the beginning of an N-glycosylation motif; if it's not found, you should raise a ``ValueError``.

For example:

.. code-block:: 

    >>> find_nglycosylation_motif(list('AAMNLSRPPT'))
    3
    >>> find_nglycosylation_motif(list('MNPSNTTT'))
    4
    >>> find_nglycosylation_motif(list('PATTY'))
    ValueError: N-glycosylation motif not found

Write tests (using doctest or unittest or ``assert``) to check your work. (We won't be 'marking' it---convince yourself you got it right!)

.. challenge:: 

    # define find_nglycosylation_motif
    