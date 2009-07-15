#
Summary:	Sreadahead
Summary(pl.UTF-8):	Sreadahead
Name:		sreadahead
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://sreadahead.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	f9dc659f1bf209621a4f965decb14692
URL:		http://code.google.com/p/sreadahead/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Sreadahead is a daemon that reads data sequential by use from disk.
This is typically used to fetch information needed by the boot process
into memory as early as possible. Sreadahead thereby eliminates IO
wait times during the boot process which results in a faster startup.

%prep
%setup -q

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/%{name}
%dir /var/lib/sreadahead
%dir /var/lib/sreadahead/debugfs
