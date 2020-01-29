#!/bin/bash
rpmbuild --define "%_topdir $(pwd)/$1" -bb $1/SPECS/$1.spec
