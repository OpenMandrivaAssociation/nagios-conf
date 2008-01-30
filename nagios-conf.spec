Summary:	This package contains sample configuration for nagios
Name:		nagios-conf
Version:	3.0
Release:	%mkrel 1
License:	GPL
Group:		Networking/Other
URL:		http://www.nagios.org/
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

