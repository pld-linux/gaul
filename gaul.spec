#
# TODO:
#       - Przet³umaczyæ %description

Summary:	Genetic Algorithm Utility Library
Summary(pl):	Biblioteka narzêdziowa algorytmów genetycznych
Name:		gaul
Version:	0.1846
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/gaul/%{name}-devel-%{version}-0.tar.gz
# Source0-md5:  1cce2bf4546ee4739f85076ab26ca983
URL:		http://gaul.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Genetic Algorithm Utility Library (GAUL) is an open source
programming library providing genetic algorithms. Both stead y-state
and generation based evolution is supported, together with the island
model. GAUL supports the Darwinian, Lamarckia n and Baldwininan
evolutionary schemes. Standard mutation, crossover and selection
operators are provided, while code hooks additionally allow custom
operators. Several non-evolutionary search heuristics are provided for
comparison and local sear ch purposes, including simplex method, hill
climbing, simulated annealling and steepest ascent. Much of the
functionality i s also available through a simple S-Lang interface.

%description -l pl
GAUL jest otwart± bibliotek± algorytmów genetycznych.

%package devel
Summary:	Header files for GAUL library
Summary(pl):	Pliki nag³ówkowe biblioteki GAUL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GAUL library.

%description devel -l pl
Pliki nag³ówkowe biblioteki GAUL.

%package static
Summary:	Static GAUL library
Summary(pl):	Statyczna biblioteka GAUL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GAUL library.

%description static -l pl
Statyczna biblioteka GAUL.

%prep
%setup -q -n %{name}-devel-%{version}-0

%build
%configure \
	--enable-g=no		\
	--enable-debug=no	\
	--enable-slang=no

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
