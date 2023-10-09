# 
# revad spec file
#

Name: revad
Summary: REVA for CERNBox
Version: 0.0.47
Release: 1%{?dist}
License: AGPLv3
BuildRoot: %{_tmppath}/%{name}-buildroot
Group: CERN-IT/ST
ExclusiveArch: x86_64
Source: %{name}-%{version}.tar.gz

%description
This RPM provides REVA for CERNBox, built from github.com/cernbox/reva

# Don't do any post-install weirdness, especially compiling .py files
%define __os_install_post %{nil}

%prep
%setup -n %{name}-%{version}

%install
rm -rf %buildroot/
mkdir -p %buildroot/usr/bin
mkdir -p %buildroot/etc/revad
mkdir -p %buildroot/var/log/revad
mkdir -p %buildroot/var/run/revad
install -m 755 revad %buildroot/usr/bin/revad

%clean
rm -rf %buildroot/

%preun

%post

%files
%defattr(-,root,root,-)
/etc/revad
/var/log/revad
/var/run/revad
/usr/bin/revad


%changelog
* Wed Aug 23 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.47
- v0.0.47
* Fri Aug 18 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.46
- v0.0.46
* Wed Aug 16 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.45
- v0.0.45
* Mon Aug 14 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.44
- v0.0.44
* Fri Jul 21 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.43
- v0.0.43
* Tue Jun 06 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.42.experimental
- v0.0.42.experimental
* Mon Jun 05 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.41
- v0.0.41
* Fri May 12 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.40
- v0.0.40
* Wed May 10 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.39
- v0.0.39
* Fri May 05 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.38
- v0.0.38
* Thu Apr 20 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.37
- v0.0.37
* Mon Apr 17 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.36
- v0.0.36
* Wed Apr 12 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.35
- v0.0.35
* Tue Apr 11 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.34
- v0.0.34
* Tue Apr 11 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.33
- v0.0.33
* Tue Apr 04 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.32
- v0.0.32
* Wed Mar 22 2023 cernbox-admins[bot] <cernbox-admins@cern.ch> 0.0.31
- v0.0.31
* Wed Mar 15 2023 Giuseppe Lo Presti <lopresti@cern.ch> 0.0.30
- v0.0.30
* Tue Mar 14 2023 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.29
- v0.0.29
* Mon Feb 06 2023 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.28
- v0.0.28
* Tue Jan 24 2023 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.27
- v0.0.27
* Sat Dec 03 2022 Giuseppe Lo Presti <giuseppe.lopresti@cern.ch> 0.0.26
- Temporary patch
* Fri Dec 02 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.25
- v0.0.25
* Fri Dec 02 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.24
- v0.0.24
* Tue Nov 29 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.23
- v0.0.23
* Mon Nov 07 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.22
- v0.0.22
* Thu Nov 03 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.21
- v0.0.21
* Wed Oct 19 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.20
- v0.0.20
* Wed Oct 19 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.19
- v0.0.19
* Mon Oct 17 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.18
- v0.0.18
* Thu Oct 13 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.17
- v0.0.17
* Tue Oct 11 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.16
- v0.0.16
* Fri Oct 07 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.15
- v0.0.15
* Tue Oct 04 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.14
- v0.0.14
* Thu Sep 29 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.13
- v0.0.13
* Wed Sep 21 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.12
- v0.0.12
* Wed Sep 21 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.11
- v0.0.11
* Wed Sep 14 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.10
- v0.0.10
* Tue Sep 13 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.9
- v0.0.9
* Wed Sep 07 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.8
- v0.0.8
* Wed Sep 07 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.7
- v0.0.7
* Thu Aug 25 2022 Diogo Castro <diogo.castro@cern.ch> 0.0.6
- Do not lowercase case sensitive hash (fix public links)
* Tue Aug 16 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.5
- v0.0.5
* Thu Aug 11 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.4
- v0.0.4
* Thu Jul 14 2022 Gianmaria Del Monte <gianmaria.del.monte@cern.ch> 0.0.2
- v0.0.2
* Thu Jul 07 2022 Hugo Gonzalez Labrador <hugo.gonzalez.labrador@cern.ch> 0.0.1
- v0.0.1

