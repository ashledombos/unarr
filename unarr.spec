%define api	1.0
%define major	0
%define libname	%mklibname unarr %{api} %{major}
%define devname %mklibname -d unarr %{api}

Summary:        A decompression library
Name:		        libunarr
Version:	      1.0.0
Release:	      1
License:	      LGPLv2+
Group:	        Development/Libraries/C and C++

URL:            https://github.com/zeniko/unarr
Source0:        https://github.com/selmf/unarr/archive/master.zip
#Source0:		    https://github.com/zeniko/unarr/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
#Source1:        https://raw.githubusercontent.com/selmf/unarr/master/CMakeLists.txt
#Source1:       CMakeLists.txt

BuildRequires: 	cmake(ZLIB)
BuildRequires: 	pkgconfig(zlib)
BuildRequires: 	bzip2-devel

%description
A lightweight decompression library with support for rar, tar and zip
archives

%package -n %{libname}
Group:          Development/Libraries/C and C++
Summary:        A decompression library

%description -n %{libname}
A lightweight decompression library with support for rar, tar and zip
archives

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:	      %{libname} = %{version}-%{release}
Provides:	      %{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn unarr-%{commit0}
cp -p %SOURCE1 .

%build
%cmake 
#-DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.a' -exec rm -f {} ';'

%if 0%{?suse_version}
%post -n%{name}1 -p /sbin/ldconfig
%postun -n%{name}1 -p /sbin/ldconfig

%files -n %{name}1
%{_libdir}/*.so.1*

%else
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/%{name}.so.1*
%endif

%files devel
%{_includedir}/*
%{_libdir}/%{name}.so
