Name: qt-virt-manager
Version: 0.72.99
Release: 3
Source0: https://github.com/F1ash/qt-virt-manager/archive/refs/tags/%{version}.tar.gz
Summary: A GUI application for managing virtual machines
URL: https://f1ash.github.io/qt-virt-manager/
License: GPL-2.0
Group: User Interface/Desktops
BuildRequires: qmake5
BuildRequires: cmake ninja
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(qtermwidget5)
BuildRequires: %mklibname -d krdccore-qt5
BuildRequires: pkgconfig(spice-client-glib-2.0)
Requires: qt-remote-viewer = %{EVRD}

%description
A GUI application for managing virtual machines.

%package -n qt-remote-viewer
Summary: Application for viewing desktops of remote (virtual) machines
Group: User Interface/Desktops

%description -n qt-remote-viewer
Application for viewing desktops of remote (virtual) machines

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/qt5-virt-manager
%{_datadir}/applications/qt5-virt-manager.desktop
%{_datadir}/icons/hicolor/256x256/apps/virtual-engineering.png
%{_datadir}/qt5-virt-manager

%files -n qt-remote-viewer
%{_bindir}/qt5-remote-viewer
%{_datadir}/applications/qt5-remote-viewer.desktop
%{_datadir}/icons/hicolor/256x256/apps/remote-desktop-viewer.png
%{_datadir}/mime/packages/qt-remote-viewer-mime.xml
