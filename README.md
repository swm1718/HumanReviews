# Human Reviews for Speaker Diarization
This GitHub site sets out the results of the human reviews speaker diarization experiments carried out for the paper ``Studying Human-Based Speaker Diarization and Comparing to State-of-the-Art Systems`` by Simon W. McKnight, Aidan O. T. Hogg, Vincent W. Neo and Patrick A. Naylor presented at APSIPA 2022.

## Reviews
The review was carried out on section AMI 2008a just over 5 minutes long (00:00:30.0 to 00:05:30.5 hrs:mins:secs).

## Resources
The relevant materials are:
- The ``Instructions for Reviewers`` pdf file.
- The ``Reviews`` folder that contains 13 human reviews with no prior information.
- The ``Reviews_SAD`` folder that contains 10 human reviews starting from the ground truth speech segments (not distinguishing individual speakers).
- The ``Reviews_Blank`` folder that contains 10 human reviews starting from the blank ground truth speaker segment labels.

One of the Jupyter notebooks ``humanTests2.ipynb`` used to inspect and explore the results is also included along with the custom dependencies ``AnalyseResults.py``, ``evaluateResults.py`` and ``OverlapFunctions.py``, these are a bit of a mess.  The cells that run ``dscore`` refer to the diarization scoring package at https://github.com/nryant/dscore.

A simple Colab notebook as been set up at https://colab.research.google.com/drive/1KC4DoTxI8ATUXksW7T1BvPTEorYxKxQH or https://tinyurl.com/4ys4ba7t that can be tested.
