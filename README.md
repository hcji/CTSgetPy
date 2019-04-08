# CTSgetPy
.. image:: https://travis-ci.com/hcji/CTSgetPy.svg?branch=master
    :target: https://travis-ci.org/hcji/CTSgetPy
***
Python interface to the [Chemical Translation Service (CTS)](http://cts.fiehnlab.ucdavis.edu/)

## Depends:
    pip install requests
	pip install tqdm
	pip install bs4

## Installation
	pip install git+https://github.com/hcji/CTSgetPy@master
	
## Usage
### Import package
	from CTSgetPy import CTSgetPy

### View possible translation options between > 200 databases.
	CTSgetPy.CTS_options()
	
### Example usage
	# single target, single identifier
	CTSgetPy.CTSget('KEGG', 'PubChem SID', 'C00001', top_only=True) 
	CTSgetPy.CTSget('KEGG', 'PubChem SID', 'C00001', top_only=False) 
	# multi targets, single identifier
	CTSgetPy.CTSget('KEGG', ['PubChem CID', 'PubChem SID'], 'C00001')
	# multi target, multi identifiers	
	CTSgetPy.CTSget('KEGG', ['PubChem CID', 'PubChem SID'], ['C00001', 'C00002']) 