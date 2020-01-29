Name:           dxp
Version:        0.0.0
Release:        0
Distribution:   DXP
Group:          DXP
Vendor:         Sisal Digital Factory
Packager:       Alberto Clemente <alberto.clemente@sisal.it>
BuildArch:      noarch

Summary:        dxp

License:        Sisal
URL:            https://www.sisal.it
Source0:        dxp-%{version}.tar.gz

Requires:       dxp-common = %{version} dxp-backend = %{version} dxp-fronted = %{version}

%package common
Summary:        DXP Common
Group:          DXP
Requires:       bash

%package backend
Summary:        DXP Backend
Group:          DXP/Backend
Requires:       dxp-common = %{version}

%package frontend
Summary:        DXP Frontend
Group:          DXP/Frontend
Requires:       dxp-common = %{version}

%description

DXP

%description common

DXP Common

%description backend

DXP Backend

%description frontend

DXP Frontend

%prep
%setup -q


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
install -m 0111 common/dxp-common.txt %{buildroot}/%{_bindir}/dxp-common.txt
install -m 0111 backend/dxp-backend.txt %{buildroot}/%{_bindir}/dxp-backend.txt
install -m 0111 frontend/dxp-frontend.txt %{buildroot}/%{_bindir}/dxp-frontend.txt

%files
%files common
/%{_bindir}/dxp-common.txt
%files backend
/%{_bindir}/dxp-backend.txt
%files frontend
/%{_bindir}/dxp-frontend.txt

%pre
echo "Exec pre-install script for dxp"

%pre common
echo "Exec pre-install script for dxp-common"

%pre backend
echo "Exec pre-install script for dxp-backend"

%pre frontend
echo "Exec pre-install script for dxp-frontend"

%post
echo "Exec post-install script for dxp"

%post common
echo "Exec post-install script for dxp-common"

%post backend
echo "Exec post-install script for dxp-backend"

%post frontend
echo "Exec post-install script for dxp-frontend"

%preun
echo "Exec pre-uninstall script for dxp"

%preun common
echo "Exec pre-uninstall script for dxp-common"

%preun backend
echo "Exec pre-uninstall script for dxp-backend"

%preun frontend
echo "Exec pre-uninstall script for dxp-frontend"

%postun
echo "Exec post-uninstall script for dxp"

%postun common
echo "Exec post-uninstall script for dxp-common"

%postun backend
echo "Exec post-uninstall script for dxp-backend"

%postun frontend
echo "Exec post-uninstall script for dxp-frontend"

%doc



%changelog
