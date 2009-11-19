%global pkg_name kc

%bcond_without doc
%bcond_without prof

# ghc does not emit debug information
%global debug_package %{nil}

Name:           %{pkg_name}
Version:        0.0.1
Release:        1.%{?dist}
Summary:        A command-line tool for keepalived.conf
Group:          Applications/System
License:        BSD
URL:            http://github.com/maoe/%{pkg_name}
#Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
# fedora ghc archs:
ExclusiveArch:  %{ix86} x86_64 ppc alpha
BuildRequires:  ghc, ghc-rpm-macros
%if %{with doc}
BuildRequires:  ghc-doc
%endif
%if %{with prof}
BuildRequires:  ghc-prof
%endif

%description
A command-line tool (kc) for keepalived.conf

%prep
if [ -d %{pkg_name} ]; then
  cd %{pkg_name}
  git pull
else
  git clone git://github.com/maoe/%{pkg_name}.git
fi


%build
cd %{pkg_name}
%cabal_configure --ghc %{?with_prof:-p}
%cabal build
%ghc_gen_scripts


%install
rm -rf $RPM_BUILD_ROOT
cd %{pkg_name}
%{__install} -D -m 755 dist/build/kc/kc $RPM_BUILD_ROOT/%{_bindir}/kc


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/kc

%changelog
* Thu Nov 19 2009 Mitsutoshi Aoe <maoe.maoe@gmail.com> - 0.0.1-1
- initial revision
