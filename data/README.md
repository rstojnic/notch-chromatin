Data used to infer chromatin states
================

To save space the data in stored in [7zip](http://www.7-zip.org/) format. You will need to decompress the files before using them.

## Data matrices

* [scikit-BG3Kc-K56ac.tsv.7z](https://github.com/rstojnic/notch-chromatin/data/scikit-BG3Kc-K56ac.tsv.7z) -  main dataset used for chromatin state inference. BG3 and Kc data are appended into a single large matrix. See below for the corresponding tiles coordinate file. 

* [scikit-BG3Kc-K56ac-postActivation.tsv.7z](https://github.com/rstojnic/notch-chromatin/data/scikit-BG3Kc-K56ac-postActivation.tsv.7z) -  dataset with H3K56ac after Notch activation. Note that all other datasets (except H3K56ac) are before Notch activation. 

* [scikit-BG3S2Kc.tsv.7z](https://github.com/rstojnic/notch-chromatin/data/scikit-BG3S2Kc.tsv.7z) -  dataset from 3 cell lines (in order: BG3-S2-Kc) and without H3K56ac. 

* [tiles.bed.gz](https://github.com/rstojnic/notch-chromatin/data/tiles.bed.gz) -  Genomic coordinates of 200bp tiles used to create the dataset. 

## modENCODE datasets

The following dataset were used:

Dataset | BG3 | Kc167 | S2
--------|-----|-------|----
H1 | modEncode_3299 | modEncode_5134 | modEncode_3300
H2Bubi | modEncode_288 | modEncode_289 | modEncode_290
H3 | modEncode_3302 | modEncode_4179 | modEncode_3301
H3K18ac | modEncode_291 | modEncode_2996 | modEncode_292
H3K23ac | modEncode_293 | modEncode_2998 | modEncode_294
H3K27ac | modEncode_295 | modEncode_3757 | modEncode_296
H3K27me1 | modEncode_3941 | modEncode_3942 | modEncode_3943
H3K27me2 | modEncode_2999 | modEncode_3758 | modEncode_3000
H3K27me3 | modEncode_297 | modEncode_5136 | modEncode_298
H3K36me1 | modEncode_299 | modEncode_3003 | modEncode_3170
H3K36me3 | modEncode_301 | modEncode_302 | modEncode_303
H3K4me1 | modEncode_2653 | modEncode_3760 | modEncode_304
H3K4me2 | modEncode_2654 | modEncode_4935 | modEncode_2655
H3K4me3 | modEncode_967 | modEncode_3761 | modEncode_305
H3K79me1 | modEncode_3005 | modEncode_3762 | modEncode_2658
H3K79me2 | modEncode_306 | modEncode_3763 | modEncode_307
H3K9ac | modEncode_3765 | modEncode_3007 | modEncode_309
H3K9acS10P | modEncode_2659 | modEncode_3009 | modEncode_2660
H3K9me1 | modEncode_3768 | modEncode_3769 | modEncode_3770
H3K9me2 | modEncode_310 | modEncode_938 | modEncode_311
H3K9me3 | modEncode_312 | modEncode_3013 | modEncode_313
H4K16ac | modEncode_316 | modEncode_318 | modEncode_319
H4K20me1 | modEncode_3286 | modEncode_3287 | modEncode_3014

Data can be downloaded from [http://intermine.modencode.org](http://intermine.modencode.org). We used the final processed ChIP profiles. 

DNAseI hypersensitivity (DHS) data was downloaded from [http://compbio.med.harvard.edu/flychromatin/data.html](http://compbio.med.harvard.edu/flychromatin/data.html).

