#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-String-Escape
Version  : 2010.002
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/E/EV/EVO/String-Escape-2010.002.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EV/EVO/String-Escape-2010.002.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libstring-escape-perl/libstring-escape-perl_2010.002-2.debian.tar.xz
Summary  : Backslash escapes, quoted phrase, word elision, etc.
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-String-Escape-license = %{version}-%{release}
Requires: perl-String-Escape-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
String::Escape
This module provides a flexible calling interface to some
frequently-performed string conversion functions, including applying
and expanding standard C/Unix-style backslash escapes like \n and \t, wrapping
and removing double-quotes, and truncating to fit within a desired length.

%package dev
Summary: dev components for the perl-String-Escape package.
Group: Development
Provides: perl-String-Escape-devel = %{version}-%{release}
Requires: perl-String-Escape = %{version}-%{release}

%description dev
dev components for the perl-String-Escape package.


%package license
Summary: license components for the perl-String-Escape package.
Group: Default

%description license
license components for the perl-String-Escape package.


%package perl
Summary: perl components for the perl-String-Escape package.
Group: Default
Requires: perl-String-Escape = %{version}-%{release}

%description perl
perl components for the perl-String-Escape package.


%prep
%setup -q -n String-Escape-2010.002
cd %{_builddir}
tar xf %{_sourcedir}/libstring-escape-perl_2010.002-2.debian.tar.xz
cd %{_builddir}/String-Escape-2010.002
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/String-Escape-2010.002/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Escape
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-String-Escape/048c9afd00f8a919908c5775cbee1c4c8527366a || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Escape.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Escape/048c9afd00f8a919908c5775cbee1c4c8527366a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
