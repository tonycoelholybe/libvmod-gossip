Summary: Gossip VMOD for Varnish
Name: vmod-gossip
Version: 1.0
Release: 1%{?dist}
License: BSD
URL: https://github.com/carlosabalde/libvmod-gossip
Group: System Environment/Daemons
Source0: libvmod-gossip.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish >= 4.1.0
BuildRequires: make, python-docutils, varnish >= 4.1.0

%description
Gossip VMOD for Varnish

%prep
%setup -n libvmod-gossip

%build
./autogen.sh
./configure --prefix=/usr/ --docdir='${datarootdir}/doc/%{name}'
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} check

%install
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnish*/vmods/
%doc /usr/share/doc/%{name}/*
%{_mandir}/man?/*

%changelog
* Sat May 12 2018 Carlos Abalde <carlos.abalde@gmail.com> - 1.0-1.20180512
- Initial version.