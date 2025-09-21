%undefine _debugsource_packages
Name:           xdg-desktop-portal-cosmic
Version:        1.0.0
%define beta beta.1
Release:        %{?beta:0.%{beta}.}1
Summary:        COSMIC xdg portal
License:        GPL-3.0-only
Group:          Desktop/COSMIC
URL:            https://github.com/pop-os/xdg-desktop-portal-cosmic
Source0:        https://github.com/pop-os/xdg-desktop-portal-cosmic/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  clang-devel
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xdg-desktop-portal)
BuildRequires:  pkgconfig(xkbcommon)

%description
This package contains the xdg portal implementation for COSMIC DE.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
# Build failure workaround: https://github.com/pop-os/cosmic-files/issues/392#issuecomment-2308954953
export VERGEN_GIT_COMMIT_DATE="$(date --utc '+%Y-%m-%d %H:%M:%S %z')"
export VERGEN_GIT_SHA=$_commit
%make_build

%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix}

%files
%license LICENSE
%{_libexecdir}/%{name}
%{_datadir}/icons/hicolor/scalable/actions/{screenshot-screen-symbolic,screenshot-selection-symbolic,screenshot-window-symbolic}.svg
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.cosmic.service
%{_datadir}/xdg-desktop-portal/cosmic-portals.conf
%{_datadir}/xdg-desktop-portal/portals/cosmic.portal
