# TODO: fix strange modules install dir?
#
# Conditional build:
%bcond_with	tests	# do perform "make test" (some tests fail, probably specific env. is expected)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Device::Cdio - Perl bindings for CD input and control library (libcdio)
Summary(pl.UTF-8):	Device::Cdio - wiązania Perla do biblioteki wejścia i sterowania CD (libcdio)
Name:		perl-Device-Cdio
Version:	0.4.0
Release:	1
License:	GPL v3+
Group:		Development/Languages/Perl
Source0:	http://ftp.gnu.org/gnu/libcdio/Device-Cdio-v%{version}.tar.gz
# Source0-md5:	5f5695c0997383b9b622704176ae4a39
Patch:		%{name}-update.patch
URL:		http://search.cpan.org/dist/Device-Cdio/
BuildRequires:	libcdio-devel >= 0.92
BuildRequires:	perl-ExtUtils-CBuilder >= 0.28
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Module-Build >= 0.38 
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.08
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	swig-perl
Requires:	libcdio >= 0.92
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Device::Cdio contains Perl bindings for CD input and control library
(libcdio).

%description -l pl.UTF-8
Device::Cdio zawiera wiązania Perla do biblioteki wejścia i sterowania
CD (libcdio).

%prep
%setup -q -n Device-Cdio-v%{version}
%patch0 -p1

# force swig rebuild
%{__rm} *_wrap.c

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT \
	config='optimize=%{rpmcflags}'
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Changes README.md THANKS
%{perl_vendorarch}/Device/Cdio.pm
%{perl_vendorarch}/Device/Cdio
%{perl_vendorarch}/perlcdio.pm
%attr(755,root,root) %{perl_vendorarch}/perlcdio.so
%{perl_vendorarch}/perliso9660.pm
%attr(755,root,root) %{perl_vendorarch}/perliso9660.so
%{perl_vendorarch}/perlmmc.pm
%attr(755,root,root) %{perl_vendorarch}/perlmmc.so
%{_mandir}/man3/Device::Cdio*.3pm*
%{_mandir}/man3/perlcdio.3pm*
%{_mandir}/man3/perliso9660.3pm*
%{_mandir}/man3/perlmmc.3pm*
