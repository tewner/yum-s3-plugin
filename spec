Name:		yum-s3
Version:	0.2.4
Release:	1
Summary:	Amazon S3 plugin for yum.

Group:		unknown
License:	Apache License 2.0
URL:		git@github.com:NumberFour/yum-s3-plugin.git
Source0:	s3.py
Source1:	s3.conf
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

%description

%prep
cp -p %SOURCE0 %SOURCE1 .
find .

%install
rm -rf "${RPM_BUILD_ROOT}"

mkdir -p ${RPM_BUILD_ROOT}/etc/yum/pluginconf.d/
cp s3.conf ${RPM_BUILD_ROOT}/etc/yum/pluginconf.d/

mkdir -p ${RPM_BUILD_ROOT}/usr/lib/yum-plugins/
cp s3.py  ${RPM_BUILD_ROOT}/usr/lib/yum-plugins/

%clean
rm -rf "${RPM_BUILD_ROOT}"

%files
%defattr(-,root,root,-)
/etc/yum/pluginconf.d/s3.conf
/usr/lib/yum-plugins

%changelog
