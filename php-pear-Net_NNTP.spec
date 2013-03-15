%define		_class		Net
%define		_subclass	NNTP
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.4.0
Release:	8
Summary:	Communicate with an NNTP server
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_NNTP/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Complete class for communicating with an NNTP server (this is: the
USENET), including: post, view, list, authentication, overview, header
manipulation, NNTP commands debugger, etc.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-7mdv2012.0
+ Revision: 742160
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-6
+ Revision: 679475
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-5mdv2011.0
+ Revision: 613733
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.0-4mdv2010.1
+ Revision: 468711
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.4.0-3mdv2010.0
+ Revision: 441488
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4.0-2mdv2009.1
+ Revision: 322494
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.4.0-1mdv2009.0
+ Revision: 278932
- update to new version 1.4.0

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-2mdv2009.0
+ Revision: 236991
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-1mdv2007.0
+ Revision: 82374
- Import php-pear-Net_NNTP

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-1mdk
- 1.3.3
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- initial Mandriva package (PLD import)

