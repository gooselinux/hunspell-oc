Name: hunspell-oc
Summary: Occitan hunspell dictionaries
Version: 0.5
Release: 3.1%{?dist}
Source: https://addons.mozilla.org/en-US/firefox/downloads/file/34604/occitan-languedocien-%{version}-fx+tb+sm.xpi
Group: Applications/Text
URL: https://addons.mozilla.org/en-US/firefox/addon/8235
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3+
BuildArch: noarch
BuildRequires: redland

Requires: hunspell

%description
Occitan hunspell dictionaries.

%prep
%setup -q -c -n hunspell-oc

%build
rdfproc hunspell-oc parse install.rdf
rdfproc hunspell-oc print | grep install-manifest | grep -v targetApplication | sed -e 's/.*#//' | sed -e 's/], "/: /'| sed -e 's/"}//' > CREDITS

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/oc-FR.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/oc_FR.aff
cp -p dictionaries/oc-FR.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/oc_FR.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc CREDITS
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Sep 20 2008 Caolan McNamara <caolanm@redhat.com> - 0.5-1
- initial version
