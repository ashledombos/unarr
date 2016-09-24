%define major	1
%define libname	%mklibname unarr %{major}
%define devname %mklibname -d unarr
%define date	20160923

Name:		unarr
Version:	0
Release:	1.%{date}
Group:		Development/C
Summary:	A decompression library
License:	LGPLv2+

URL:            https://github.com/zeniko/unarr
# git clone https://github.com/zeniko/unarr.git
# git archive --format=tar --prefix unarr-0-$(date +%Y%m%d)/ HEAD | xz -vf > unarr-0-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}-%{date}.tar.xz
Source1:        https://raw.githubusercontent.com/selmf/unarr/master/CMakeLists.txt

BuildRequires: 	cmake(ZLIB)
BuildRequires: 	pkgconfig(zlib)
BuildRequires: 	bzip2-devel

%description
A lightweight decompression library with support for rar, tar and zip
archives

%package -n %{libname}
Summary:        A decompression library

%description -n %{libname}
A lightweight decompression library with support for rar, tar and zip
archives

%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn %{name}-%{version}-%{date}
cp -p %SOURCE1 .
sed -i s'!DESTINATION lib!DESTINATION %_lib!g' CMakeLists.txt 

%build
%cmake 
%make

%install
%makeinstall_std -C build LIBDIR=%{_libdir}
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/lib%{name}.so
