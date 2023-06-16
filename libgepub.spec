
%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define api_version	0.7
%define lib_major	0

%define lib_name	%mklibname gepub %{api_version} %{lib_major}
%define gi_name		%mklibname gepub-gir %{api_version}
%define develname	%mklibname -d gepub %{api_version}

Name:		libgepub
Version:	0.7.1
Release:	1
Summary:	Library for epub documents

Group:		System/Libraries
License:	LGPLv2+
URL:		https://git.gnome.org/browse/libgepub
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	meson

%description
libgepub is a GObject based library for handling and rendering epub
documents.

%package -n %{lib_name}
Summary:	Library for epub documents
Obsoletes:	%{_lib}gepub0.6_0 < %{EVRD}

%description -n %{lib_name}
libgepub is a GObject based library for handling and rendering epub
documents.

%package -n %{gi_name}
Summary:	GObject Introspection interface library for Gepub
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:	%{_lib}gepub-gir0.6 < %{EVRD}

%description -n %{gi_name}
GObject Introspection interface library for Gepub.

%package -n %{develname}
Summary:	Development files for %{name}
Requires:	%{lib_name} = %{version}-%{release}
Requires:	%{gi_name} = %{version}-%{release}
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
Obsoletes: %{_lib}gepub0.6-devel < %{EVRD}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -delete

%check
%meson_test

%files -n %{lib_name}
%license COPYING
%{_libdir}/libgepub-%{api_version}.so.%{lib_major}{,.*}

%files -n %{gi_name}
%{_libdir}/girepository-1.0/Gepub-%{api_version}.typelib

%files -n %{develname}
%{_includedir}/libgepub-%{api_version}/
%{_libdir}/libgepub-%{api_version}.so
%{_libdir}/pkgconfig/libgepub-%{api_version}.pc
%{_datadir}/gir-1.0/Gepub-%{api_version}.gir
