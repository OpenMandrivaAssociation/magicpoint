%define name	magicpoint
%define version 1.11b
%define release 1mdk

Summary:	Presentation tool
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD like
URL:		http://member.wide.ad.jp/wg/mgp/
Group:		Office
Source:		ftp://sh.wide.ad.jp/WIDE/free-ware/mgp/%{name}-%{version}.tar.bz2
Patch0:         magicpoint-1.10a-remove-rpath.patch.bz2
Patch1:         magicpoint-1.09a-defaults-to-latin1.patch.bz2
Patch2:         magicpoint-1.09a-emacs-mode--add-font-lock.patch.bz2
Patch3:         magicpoint-1.09a-xfont-force-same-one.patch.bz2
#Patch4:         magicpoint-1.10a-freetype.patch.bz2
Patch5:         magicpoint-1.10a-missing-decl.patch.bz2
BuildRoot:	%_tmppath/%{name}-buildroot
Buildrequires:  freetype-devel flex byacc XFree86-devel
Requires:	fonts-ttf-japanese libjpeg-progs

%description
MagicPoint is an X11 based presentation tool. It is designed to make
simple presentations easy while making complicated presentations
possible. Its presentation file is just text so that you can create
presentation files quickly with your favorite editor (e.g. Emacs).

It includes a true type library for elegant looking text and effects.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch4 -p0
%patch5 -p0

%build
%configure2_5x --enable-locale
xmkmf -a
make

%install
%makeinstall_std install.man

install -m 644 -D contrib/mgp-mode.el $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/mgp-mode.el

install -d $RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d
cat <<EOF >$RPM_BUILD_ROOT%{_sysconfdir}/emacs/site-start.d/%{name}.el
(autoload 'mgp-mode "mgp-mode" "MagicPoint editing mode" t)
(add-to-list 'auto-mode-alist '("\\\\.mgp$" . mgp-mode))
EOF

#clean cvs things
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done
rm -rf $RPM_BUILD_ROOT/usr/X11R6/lib*/X11/doc/html    

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc COPYRIGHT FAQ README* RELNOTES SYNTAX USAGE
%doc sample/
%{_datadir}/emacs/site-lisp/*
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*
/usr/X11R6/bin/*
/usr/X11R6/man/*/*
/usr/X11R6/lib/X11/mgp