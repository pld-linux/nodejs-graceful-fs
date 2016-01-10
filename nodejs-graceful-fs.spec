%define		pkg	graceful-fs
Summary:	A drop-in replacement for the fs module, making various improvements
Name:		nodejs-%{pkg}
Version:	3.0.2
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/graceful-fs/-/%{pkg}-%{version}.tgz
# Source0-md5:	d1a68537b1610dc18a1b896b10f6052d
URL:		https://github.com/isaacs/node-graceful-fs
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs >= 0.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The improvements are meant to normalize behavior across different
platforms and environments, and to make filesystem access more
resilient to errors.

Improvements over fs module:
- Queues up `open` and `readdir` calls, and retries them once
  something closes if there is an EMFILE error from too many file
  descriptors.
- fixes `lchmod` for Node versions prior to 0.6.2.
- implements `fs.lutimes` if possible. Otherwise it becomes a noop.
- ignores `EINVAL` and `EPERM` errors in `chown`, `fchown` or `lchown`
  if the user isn't root.
- makes `lchmod` and `lchown` become noops, if not available.
- retries reading a file if `read` results in EAGAIN error.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p *.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
