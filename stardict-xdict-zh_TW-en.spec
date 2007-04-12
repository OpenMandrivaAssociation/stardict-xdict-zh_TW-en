%define	version	2.4.2
%define release %mkrel 4
%define dict_format_version	2.4.2

Summary:	xdict Traditional Chinese -> English dictionary for stardict 2
Name:		stardict-xdict-zh_TW-en
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-xdict-ce-big5-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
Xdict is an old English to Chinese dictionary application.
This package contains xdict database converted into stardict format.

%prep
%setup -q -n stardict-xdict-ce-big5-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 * $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*


