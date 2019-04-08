# CTSgetPy
***
Python interface to the [Chemical Translation Service (CTS)] (http://cts.fiehnlab.ucdavis.edu/)

## Installation
	pip install git+git://github.com/hcji/CTSgetPy@master
	
## Usage
### Import package
	from CTSgetPy import *

### View possible translation options between > 200 databases.
	CTS_options()
	
### Example usage
	# single target, single identifier
	CTSget('KEGG', 'PubChem SID', 'C00001', top_only=True) 
	CTSget('KEGG', 'PubChem SID', 'C00001', top_only=False) 
	# multi targets, single identifier
	CTSget('KEGG', ['PubChem CID', 'PubChem SID'], 'C00001')
	# multi target, multi identifiers	
	CTSget('KEGG', ['PubChem CID', 'PubChem SID'], ['C00001', 'C00002']) 