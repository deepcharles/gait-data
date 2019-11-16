# Data sets for the study of human locomotion with inertial measurements units


The data provided in this repository are described in the following article:
- Charles Truong, Rémi Barrois-Müller, Thomas Moreau, Clément Provost, Aliénor Vienne-Jumeau, Albane Moreau, Pierre-Paul Vidal, Nicolas Vayatis, Stéphane Buffat, Alain Yelnik, Damien Ricard, and Laurent Oudre, _A Data Set for the Study of Human Locomotion with Inertial Measurements Units_, Image Processing On Line, 9 (2019), pp. 381–390. [https://doi.org/10.5201/ipol.2019.265](https://doi.org/10.5201/ipol.2019.265)

Please cite this article whenever you want to make a reference to this data set.


A simple online exploration tool is available [online](http://ipolcore.ipol.im/demo/clientApp/demo.html?id=77777000084).
Data can be downloaded as a zipped archive (GaitData.zip, ~200MB):
- [link 1](https://mycore.core-cloud.net/index.php/s/sTk4Vq8N3zefvKH/download)
- [link 2](http://dev.ipol.im/~truong/GaitData.zip)

Once extracted, the data can be read using the following code snippets (in Python, R). Be sure to execute those lines while in the same directory as the extracted `GaitData` folder.

#### Python

Signals are loaded into [Pandas](https://pandas.pydata.org/) data frames. Please be sure to have it installed (`pip install pandas`).

```python
from load_data import get_code_list, load_trial, load_metadata


# Load and manipulate all signals and metadata.
all_codes = get_code_list()
print("There are {} trials.".format(len(all_codes)))
for code in all_codes:
    signal = load_trial(code)  # pandas data frame
    metadata = load_metadata(code)  # dictionary
    # Do something.
    # ...
```

#### R

Be sure to set the working directory (with the function `setwd`) to wherever the data file has been unzipped. To read JSON files, the package `jsonlite` must be installed.

```R
library("jsonlite")
code_list <- fromJSON("code_list.json")

for(code in code_list){
    signal <- read.csv(paste(code, ".csv", sep=""))
    metadata <- fromJSON(paste(code, ".json", sep=""))
    # Do something.
    # ...
}

```