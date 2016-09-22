%global commit0 d1be8c43a82a4320306c8e835a86fdb7b2574ca7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           	libunarr
Version:		1.0      
Release:          git%{shortcommit0}%{?dist}
%if %{defined suse_version}
Group:            Development/Libraries/C and C++
%endif

Summary:        A decompression library

%if 0%{?suse_version}
License:      	LGPL-2.0
%else
License:      	LGPLv2+	
%endif

URL:            	https://github.com/zeniko/unarr
Source0:		https://github.com/zeniko/unarr/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
#Source1:	https://raw.githubusercontent.com/selmf/unarr/master/CMakeLists.txt
Source1:		CMakeLists.txt

BuildRequires: 	cmake
%if 0%{?suse_version}
BuildRequires: 	zlib-devel
BuildRequires: 	libbz2-devel
%else
BuildRequires: 	zlib-devel
BuildRequires: 	bzip2-devel
%endif

%description
A lightweight decompression library with support for rar, tar and zip
archives

%if 0%{?suse_version}
%package -n %{name}1
Group:            Development/Libraries/C and C++
Summary:        A decompression library

%description -n %{name}1
A lightweight decompression library with support for rar, tar and zip
archives

%package       devel
Group:            Development/Libraries/C and C++
Summary:        Development files for %{name}1
Requires:       %{name}1%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%else
%package       devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%endif

%prep
%setup -qn unarr-%{commit0}
cp -p %SOURCE1 .

%build
%cmake 
#-DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f {} ';'
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

%changelog
* Fri Oct 23 2015 herr_k
- 
