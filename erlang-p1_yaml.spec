%global srcname p1_yaml
# Erlang packages don't seem to ship debug files, as the build process does not generate them
%global debug_package %{nil}


Name: erlang-%{srcname}
Version: 1.0.0
Release: %mkrel 2
Group:   Development/Java
Summary: An Erlang wrapper for libyaml "C" library
License: ASL 2.0
URL: https://github.com/processone/%{srcname}/
Source0: https://github.com/processone/%{srcname}/archive/%{version}.tar.gz

Requires: erlang-erts
Requires: erlang-p1_utils
BuildRequires: erlang-rebar
BuildRequires: erlang-rpm-macros
BuildRequires: erlang-eunit
BuildRequires: erlang-p1_utils
BuildRequires: yaml-devel


%description
P1 YAML is an Erlang wrapper for libyaml "C" library.


%prep
%autosetup -n %{srcname}-%{version}


%build
%rebar_compile


%install
install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib
install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/ebin

install -pm644 ebin/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/ebin/
install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib

%files
%license COPYING
%doc README.md
%{_libdir}/erlang/lib/%{srcname}-%{version}



%changelog
* Sat May 07 2016 neoclust <neoclust> 1.0.0-2.mga6
+ Revision: 1010426
- imported package erlang-p1_yaml

