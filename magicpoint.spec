%define name	magicpoint
%define version 1.13a
%define release %mkrel 1

Summary:	Presentation tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD like
URL:		http://member.wide.ad.jp/wg/mgp/
Group:		Office
Source:		ftp://sh.wide.ad.jp/WIDE/free-ware/mgp/%{name}-%{version}.tar.gz
Patch0:         magicpoint-1.10a-remove-rpath.patch
Patch1:         magicpoint-1.09a-defaults-to-latin1.patch
Patch2:         magicpoint-1.09a-emacs-mode--add-font-lock.patch
Patch3:         magicpoint-1.09a-xfont-force-same-one.patch
#Patch4:         magicpoint-1.10a-freetype.patch
#Patch5:         magicpoint-1.10a-missing-decl.patch
BuildRoot:	%_tmppath/%{name}-buildroot
Buildrequires:  freetype-devel flex byacc X11-devel
BuildRequires:	imake gccmakedep
Requires:	libjpeg-progs
#Requires:	fonts-ttf-japanese

%description
MagicPoint is an X11 based presentation tool. It is designed to make
simple presentations easy while making complicated presentations
possible. Its presentation file is just text so that you can create
presentation files quickly with your favorite editor (e.g. Emacs).

It includes a true type library for elegant looking text and effects.

%prep
rm -rf %{buildroot}

%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch4 -p0
#%patch5 -p0

%build
%configure2_5x --enable-locale
xmkmf -a
make Makefiles


%install
%makeinstall_std install.man

install -m 644 -D contrib/mgp-mode.el %{buildroot}%{_datadir}/emacs/site-lisp/mgp-mode.el

install -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat <<EOF >%{buildroot}%{_sysconfdir}/emacs/site-start.d/%{name}.el
(autoload 'mgp-mode "mgp-mode" "MagicPoint editing mode" t)
(add-to-list 'auto-mode-alist '("\\\\.mgp$" . mgp-mode))
EOF

#clean cvs things
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done
rm -rf %{buildroot}/usr/X11R6/lib*/X11/doc/html    

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc COPYRIGHT FAQ README* RELNOTES SYNTAX USAGE
%doc sample/
%{_datadir}/emacs/site-lisp/*
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*
%{_bindir}/*
%{_mandir}/*/*
%{_prefix}/lib/X11/mgp/*
