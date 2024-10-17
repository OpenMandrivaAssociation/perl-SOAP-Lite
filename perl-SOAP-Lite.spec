%define modname	SOAP-Lite
%define modver	1.20

# Looks like we need only Provides exceptions now?
%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(SOAP::Transport::TCP\\)'
%define __noautoprov 'perl\\(LWP::Protocol\\)'
%else
%define _requires_exceptions perl(MQSeries.*)\\|perl(MQClient.*)
%define _provides_exceptions perl(LWP::Protocol)
%endif

Summary:	Client and server side SOAP implementation
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	14
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/SOAP/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
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
BuildRequires:	perl-JSON-PP
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}
%autopatch -p1

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
%{_bindir}/*.pl
%{perl_vendorlib}/Apache
%{perl_vendorlib}/SOAP
%{_mandir}/man1/*
%{_mandir}/man3/*

