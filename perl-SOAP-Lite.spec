%define upstream_name    SOAP-Lite
%define upstream_version 0.714

# Looks like we need only Provides exceptions now?
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(SOAP::Transport::TCP\\)'
%define __noautoprov 'perl\\(LWP::Protocol\\)'
%else
%define _requires_exceptions perl(MQSeries.*)\\|perl(MQClient.*)
%define _provides_exceptions perl(LWP::Protocol)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Client and server side SOAP implementation
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SOAP/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		SOAP-Lite-0.714-fix-ftp-transport-version-r391.patch

BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Crypt::SSLeay)
BuildRequires:	perl(FCGI)
BuildRequires:	perl(IO::Socket::SSL)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(MIME::Lite)
BuildRequires:	perl(MIME::Parser)
BuildRequires:	perl(HTTP::Daemon)
BuildRequires:	perl(Net::Jabber)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl(XML::Parser) >= 2.230.0
BuildRequires:	perl-devel

BuildArch:	noarch

%description
SOAP::Lite for Perl is a collection of Perl modules which provides a simple and
lightweight interface to the Simple Object Access Protocol (SOAP) both on
client and server side.

To learn about SOAP, go to http://www.soaplite.com/#LINKS for more
information.

This version of SOAP::Lite supports a subset of the SOAP 1.1
specification and has initial support for SOAP 1.2 specification.  See
http://www.w3.org/TR/SOAP for details.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

find examples -type f | xargs perl -pi \
    -e 's|^#!perl -w|#!%{__perl} -w|;' \
    -e 's|^#!d:\\perl\\bin\\perl.exe ||;'
find examples -type f -name *.bat | xargs rm -f 

%build
%__perl Makefile.PL INSTALLDIRS=vendor --noprompt
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README examples
%{_mandir}/*/*
%{_bindir}/*.pl
%{perl_vendorlib}/Apache
%{perl_vendorlib}/IO
%{perl_vendorlib}/SOAP
%{perl_vendorlib}/UDDI
%{perl_vendorlib}/XML
%{perl_vendorlib}/XMLRPC


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.712.0-2mdv2011.0
+ Revision: 667304
- mass rebuild

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.712.0-1mdv2011.0
+ Revision: 553046
- adding missing buildrequires:
- update to 0.712

* Mon Mar 22 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.711.0-1mdv2010.1
+ Revision: 526455
- update to 0.711

* Thu Oct 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.710.10-1mdv2010.0
+ Revision: 452000
- update to 0.710.10

* Wed Sep 30 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.710.9-1mdv2010.0
+ Revision: 451156
- update to 0.710.09

* Sun Sep 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.710.08-4mdv2010.0
+ Revision: 445869
- fix automatic dependencies (fix #3827)

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.710.08-3mdv2010.0
+ Revision: 426588
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.710.08-2mdv2009.1
+ Revision: 351742
- rebuild

* Mon Jul 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.710.08-1mdv2009.0
+ Revision: 235605
- update to new version 0.710.08

* Mon Jun 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.710.07-1mdv2009.0
+ Revision: 220162
- update to new version 0.710.07

* Sat Jun 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.710.06-1mdv2009.0
+ Revision: 216587
- update to new version 0.710.06

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.710.05-1mdv2009.0
+ Revision: 202030
- update to new version 0.710.05

* Wed Apr 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.71.04-1mdv2009.0
+ Revision: 196828
- update to new version 0.71.04

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.71.02-1mdv2009.0
+ Revision: 195129
- new version
  drop undocumented patch not applying anymore

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.69-3mdv2008.0
+ Revision: 67575
- rebuild


* Mon Jan 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.69-2mdv2007.0
+ Revision: 103017
- fix incompatibility with UNIVERSAL::require, using rt patch http://rt.cpan.org/Public/Bug/Display.html?id=16897
- Import perl-SOAP-Lite

* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.69-1mdv2007.0
- new version

* Mon Jul 24 2006 Emmanuel Andry <eandry@mandriva.org> 0.68-1mdv2007.0
- 0.68

* Tue Feb 07 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.67-1mdk
- 0.67

* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.66-1mdk
- new version
- rpmbuildupdate aware
- spec cleanup
- better summary

* Tue Jun 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.60-0.a.3mdk
- Rebuild

* Tue Apr 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.60-0.a.2mdk
- another buildrequires

* Tue Apr 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.60-0.a.1mdk
- 0.60a
- buildrequires

