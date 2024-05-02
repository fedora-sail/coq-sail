Name:           coq-sail
Version:        0.17.1
Release:        %autorelease
Summary:        Coq support library for Sail instruction set models

License:        Sail
URL:            https://github.com/rems-project/%{name}
Source0:        https://github.com/rems-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  coq
BuildRequires:  bbv
BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-dune >= 2.7

%global debug_package %{nil}

%description
Sail is a language for describing the instruction-set architecture (ISA) semantics of processors. Sail aims to provide a engineer-friendly, vendor-pseudocode-like language for describing instruction semantics. It is essentially a first-order imperative language, but with lightweight dependent typing for numeric types and bitvector lengths, which are automatically checked using Z3. It has been used for several papers, available from http://www.cl.cam.ac.uk/~pes20/sail/.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc README.md CHANGELOG.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
