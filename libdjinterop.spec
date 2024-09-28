Summary:	C++ library providing access to DJ record libraries
Summary(pl.UTF-8):	Biblioteka C++ zapewniająca dostęp do bibliotek płyt dla DJ-ów
Name:		libdjinterop
Version:	0.21.0
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/xsco/libdjinterop/tags
Source0:	https://github.com/xsco/libdjinterop/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1b9fb484069230302a2beeeb42867a45
URL:		https://github.com/xsco/libdjinterop
BuildRequires:	boost-devel >= 1.65.1
BuildRequires:	cmake >= 3.10
# C++17
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sqlite3-devel >= 3.11
BuildRequires:	zlib-devel >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdjinterop is a C++ library that allows access to database formats
used to store information about DJ record libraries.

This library currently supports:
- Engine Library, as used on "Prime"-series DJ equipment.

%description -l pl.UTF-8
libdjinterop to biblioteka C++ umożliwiająca dostęp do formatów baz
danych używanych do przechowywania informacji o bibliotekach płyt dla
DJ-ów.

Biblioteka obecnie obsługuje:
- bibliotekę Engine, używaną przez sprzęt DJ z serii Prime.

%package devel
Summary:	Header files for DjInterop library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki DjInterop
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7
Requires:	sqlite3-devel >= 3.11
Requires:	zlib-devel >= 1.2.8

%description devel
Header files for DjInterop library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki DjInterop.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libdjinterop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdjinterop.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdjinterop.so
%{_includedir}/djinterop
%{_pkgconfigdir}/djinterop.pc
%{_libdir}/cmake/DjInterop
