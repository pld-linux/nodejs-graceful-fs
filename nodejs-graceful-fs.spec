%define		pkg	graceful-fs
Summary:	'fs' module with incremental back-off on EMFILE
Name:		nodejs-%{pkg}
Version:	1.1.4
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/node-graceful-fs
Source0:	http://registry.npmjs.org/graceful-fs/-/%{pkg}-%{version}.tgz
# Source0-md5:	21817800c3cf55b78c710063821fe5d6
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Just like node.js' fs module, but it does an incremental back-off when
EMFILE is encountered. Useful in asynchronous situations where one
needs to try to open lots and lots of files.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
