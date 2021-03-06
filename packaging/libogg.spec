Name:       libogg
Summary:    The Ogg bitstream file format library
Version:    1.2.1
Release:    2
Group:      System/Libraries
License:    BSD
URL:        http://www.xiph.org/
Source0:    http://downloads.xiph.org/releases/ogg/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
Libogg is a library for manipulating Ogg bitstream file formats.
Libogg supports both making Ogg bitstreams and getting packets from
Ogg bitstreams.

%package devel
Summary:    Files needed for development using libogg
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Libogg is a library used for manipulating Ogg bitstreams. The
libogg-devel package contains the header files and documentation
needed for development using libogg.

%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 

rm -rf $RPM_BUILD_ROOT%{_docdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libogg.so.*

%files devel
%dir %{_includedir}/ogg
%{_includedir}/ogg/ogg.h
%{_includedir}/ogg/os_types.h
%{_includedir}/ogg/config_types.h
%{_libdir}/libogg.so
%{_libdir}/pkgconfig/ogg.pc
%{_datadir}/aclocal/ogg.m4

