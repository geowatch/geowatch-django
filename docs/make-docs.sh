#!/bin/bash
rm -fr source-code/modules
sphinx-apidoc -e -o source-code/modules ./../geowatchdjango/
make html
