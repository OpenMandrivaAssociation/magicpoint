%define name	magicpoint
%define version 1.13a
%define release  5

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
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	imlib-devel
Buildrequires:  flex byacc
BuildRequires:	imake gccmakedep
Requires:	libjpeg-progs

%description
MagicPoint is an X11 based presentation tool. It is designed to make
simple presentations easy while making complicated presentations
possible. Its presentation file is just text so that you can create
presentation files quickly with your favorite editor (e.g. Emacs).

It includes a true type library for elegant looking text and effects.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure2_5x --enable-locale
xmkmf
make Makefiles
make CCOPTIONS="%optflags" EXTRA_LDOPTIONS="%ldflags"

%install
rm -fr %buildroot
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


%changelog
* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 1.13a-4mdv2011.0
+ Revision: 636123
- BR xmu
- tighten BR

* Thu Oct 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.13a-3mdv2011.0
+ Revision: 585548
- rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.13a-2mdv2010.0
+ Revision: 439696
- rebuild

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 1.13a-1mdv2009.1
+ Revision: 352959
- BR imlib-devel
- New version 1.13a (should fix #17010)
- drop p5

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.12a-3mdv2009.0
+ Revision: 241007
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jun 02 2007 Funda Wang <fwang@mandriva.org> 1.12a-1mdv2008.0
+ Revision: 34720
- fix file list
- BuildRequires imake
- Patch0 not needed
- New version
- bzunzip2 the patches
- Import magicpoint



* Sun Feb 13 2005 Frederic Lepied <flepied@mandrakesoft.com> 1.11b-1mdk
- New release 1.11b

* Thu Aug 19 2004 Pascal Terjan <pterjan@mandrake.org> 1.10a-3mdk
- rebuild for libintl
- patch4 (freetype inclusion)
- patch5 (missing decl, maybe due to gcc3.4)

* Sun Nov 16 2003 Pascal Terjan <CMoi@tuxfamily.org> 1.10a-2mdk
- add BuildRequires byacc

* Tue Nov 04 2003 Pascal Terjan <CMoi@tuxfamily.org> 1.10a-1mdk
- 1.10a
- add BuildRequires XFree86-devel for xmkmf
- update patch0

* Fri Apr 25 2003 Pixel <pixel@mandrakesoft.com> 1.09a-6mdk
- add "Buildrequires: flex"

* Wed Jul 17 2002 Pixel <pixel@mandrakesoft.com> 1.09a-5mdk
- add missing quote in /etc/emacs/site-start.d/magicpoint.el

* Tue Jul 09 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.09a-4mdk
- buildrequires freetype-devel

* Thu Oct 11 2001 Pixel <pixel@mandrakesoft.com> 1.09a-3mdk
- rebuilding for libpng3

* Mon Oct  8 2001 Pixel <pixel@mandrakesoft.com> 1.09a-2mdk
- better X11 font choosing (?)
- add require libjpeg-progs

* Sun Oct  7 2001 Pixel <pixel@mandrakesoft.com> 1.09a-1mdk
- fixes, cleanup, emacs mode by default...
- new version

* Mon Sep 03 2001 Yves Duret <yduret@mandrakesoft.com> 1.08a-2mdk
- added a Requires on fonts-ttf-japanese
- added -q option to %%setup

* Wed Jun 13 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.08a-1mdk
- 1.08a
- sanitized spec file (s/Copyright/License, etc.)

* Mon Dec 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.07a-1mdk
- new in contribs
