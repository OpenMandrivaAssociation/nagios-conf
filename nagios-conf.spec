Summary:	This package contains sample configuration for nagios
Name:		nagios-conf
Version:	3.0
Release:	6
License:	GPL
Group:		Networking/Other
URL:		https://www.nagios.org/
Source0:	sample.cfg
Requires:	nagios
Requires:	nagios-check_disk
Requires:	nagios-check_http
Requires:	nagios-check_load
Requires:	nagios-check_ping
Requires:	nagios-check_procs
Requires:	nagios-check_ssh
Requires:	nagios-check_swap
Requires:	nagios-check_users
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains sample configuration for nagios.

%prep

%setup -q -T -c -n %{name}-%{version}

cp %{SOURCE0} sample.cfg

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/nagios/conf.d

install -m0644 sample.cfg %{buildroot}%{_sysconfdir}/nagios/conf.d/

%post
%{_initrddir}/nagios condrestart >/dev/null 2>&1 || :

%postun
if [ "$1" = "0" ]; then
    %{_initrddir}/nagios condrestart >/dev/null 2>&1 || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/nagios/conf.d/sample.cfg



%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0-5mdv2011.0
+ Revision: 620471
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 3.0-4mdv2010.0
+ Revision: 430148
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 3.0-3mdv2009.0
+ Revision: 253499
- rebuild

* Wed Jan 30 2008 Oden Eriksson <oeriksson@mandriva.com> 3.0-1mdv2008.1
+ Revision: 160256
- import nagios-conf


* Wed Jan 30 2008 Oden Eriksson <oeriksson@mandriva.com> 3.0-1mdv2008.1
- initial Mandriva package
