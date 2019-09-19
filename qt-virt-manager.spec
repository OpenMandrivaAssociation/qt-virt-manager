Summary:	Qt Virtual Machine Manager
Name:		qt-virt-manager
Version:	0.70.91
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
BuildRequires:  pkgconfig(libvncclient)
BuildRequires:  pkgconfig(libcacard)
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel
BuildRequires:  spice-gtk-devel
BuildRequires:  krdc-devel
BuildRequires:  qt5-linguist-tools
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
%make_build -C build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md Licenses Changelog
%{_bindir}/qt5-virt-manager
%{_bindir}/qt5-remote-viewer
%{_datadir}/applications/qt5-*.desktop
%{_datadir}/qt5-virt-manager
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/mime/packages/*.xml
