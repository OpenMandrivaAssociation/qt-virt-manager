Summary:	Qt Virtual Machine Manager
Name:		qt-virt-manager
Version:	0.22.45
Release:	1
License:	GPLv2+
URL:		https://github.com/F1ash/qt-virt-manager
Source0:        https://github.com/F1ash/qt-virt-manager/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(libvirt)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(spice-protocol)
BuildRequires:  pkgconfig(libcacard)
BuildRequires:  cmake
BuildRequires:	cmake(qtermwidget5)
BuildRequires:  typelib(SpiceClientGLib)
Requires:	libvirt-utils
Requires:       qemu
#Requires:      spice-server-client
#Requires:       spice-vdagent
# for scrubbing (optional)
#Requires:       scrub
# for ssh-transported remote connections (optional)
Requires:       nc6

%description
Qt Virtual Machine Manager provides a graphical tool for
administering virtual machines for QEMU/KVM, Xen, and LXC
and other Virtual Entities.
Start, stop, add or remove virtual devices, connect to a
graphical or serial console, and see resource usage
statistics for existing VMs on local or remote machines.
Uses libvirt as the backend management API.

%prep
%setup -q
%cmake_qt5 -DBUILD_QT_VERSION=5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%license LICENSE
%doc README.md Licenses Changelog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/256x256/apps/virtual-engineering.png
