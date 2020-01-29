#!/bin/bash
rpmbuild --define "%_topdir $(pwd)/dxp" -bb dxp/SPECS/dxp.spec
