# CSVUnNormalize
# Language: Python
# Input: TXT (file containing name of CSV file to reverse normalize and TXT file of total counts)
# Output: CSV (file will contain original counts)
# Tested with: PluMA 1.0, Python 2.7

PluMA plugin that can take a CSV file of samples and coutns and un-normalize each sample using
the provided TXT file which is a tab-delimited table of samples and counts.  Sample names in the TXT
file should match the sample names (rows) in the CSV file.  

The TXT file provided as the input file to the plugin is a two-lined file. The first line should contain the CSV file to 
un-normalize.  The second should be the name of the file of counts.

Un-normalization will be performed assuming the original normalization made all sample counts sum to 1.
