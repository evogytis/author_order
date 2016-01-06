## Very Little Gravitas (VLG) - a script to randomly order a list of authors

Gytis Dudas<sup>1</sup>

<sup>1</sup>Institute of Evolutionary Biology, University of Edinburgh, Edinburgh, UK


### Input

The input for this script is a tab-delimited text file that contains the names of the authors and their affiliations, e.g.:

A. Johnson  University of Wherever, Middle of Nowhere, Antarctica; University of That Other Place, No Place in Particular, Antarctica

B. Johnson  Department of No One's Business, Same Place, Same Continent

C. Johnson  Institute of Stood Far Back When Gravitas Was Handed Out, Culture Sphere, Milky Way; Gravitas, What Gravitas? Consortium, Culture Sphere, Milky Way


If an author has more than one affiliation each should be separated by a semicolon (;).

### Running the script

To run the script simply direct the script to the file that contains the author list and their affiliations, followed by a seed:

``python random_author_order.py -i [path to input file] -s [seed]``

If the seed is not specified or is an invalid (i.e. non-integer) value it will default the seed to 666.

### Output

The output will look something like this:

``python random_author_order.py -i example_list.txt -s 2``

Author file is: example_list.txt

Seed: 2

C. Johnson	1,2

A. Johnson	3,4

B. Johnson	5

1 Institute of Stood Far Back When Gravitas Was Handed Out, Culture Sphere, Milky Way, 

2 Gravitas, What Gravitas? Consortium, Culture Sphere, Milky Way, 

3 University of Wherever, Middle of Nowhere, Antarctica, 

4 University of That Other Place, No Place in Particular, Antarctica, 

5 Department of No One's Business, Same Place, Same Continent

The file and the seed used will be visible, followed by a random order of the authors with their affiliations numbered and displayed further down.
