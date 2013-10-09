%define i18ndate 20010626

Name:		bash
Version:	4.2
Release:	17
Summary:	The GNU Bourne Again shell (bash)
Group:		Shells
License:	GPLv2+
URL:		http://www.gnu.org/software/bash/bash.html
Source0:	ftp://ftp.gnu.org/pub/gnu/bash/%{name}-%{version}.tar.gz
Source1:	%{SOURCE0}.sig
Source2:	ftp://ftp.gnu.org/pub/gnu/bash/bash-doc-3.2.tar.bz2
Source3:	dot-bashrc
Source4:	dot-bash_profile
Source5:	dot-bash_logout
Source6:	alias.sh
Source7:	bashrc
Source8:	profile.d-bash
Patch1:		ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-001
Patch2:		ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-002
Patch3:		ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-003
Patch4:		ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-004
Patch5:		ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-005
Patch6:		ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-006
Patch7:		ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-007
Patch8:		ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-008
Patch9:		ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-009
Patch10:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-010
Patch11:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-011
Patch12:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-012
Patch13:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-013
Patch14:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-014
Patch15:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-015
Patch16:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-016
Patch17:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-017
Patch18:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-018
Patch19:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-019
Patch20:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-020
Patch21:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-021
Patch22:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-022
Patch23:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-023
Patch24:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-024
Patch25:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-025
Patch26:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-026
Patch27:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-027
Patch28:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-028
Patch29:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-029
Patch30:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-030
Patch31:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-031
Patch32:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-032
Patch33:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-033
Patch34:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-034
Patch35:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-035
Patch36:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-036
Patch37:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-037
Patch38:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-038
Patch39:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-039
Patch40:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-040
Patch41:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-041
Patch42:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-042
Patch43:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-043
Patch44:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-044
Patch45:	ftp://ftp.gnu.org/gnu/bash/bash-%{version}-patches/bash42-045

Patch200: 	bash-4.2-multibyte.patch
Patch1000:	bash-2.02-security.patch
# ensure profile is read (Redhat)
Patch1001:	bash-4.0-profile.patch
Patch1002:	bash-2.05b-readlinefixes.patch
Patch1003:	bash-2.04-compat.patch
#https://bugzilla.novell.com/attachment.cgi?id=67684
Patch1004:	bash-3.1-extended_quote.patch
# Official upstream patches
# none
Patch1005:	bash-strcoll-bug.diff
Patch1006:	bash-2.05b-checkwinsize.patch
Patch1007:	bash-3.2-lzma-copmpletion.patch
# (fc) 3.2-12mdv fix format string
Patch1008:	bash-3.2-format-security.patch
# (proyvind): 4.2-5 add --rpm-requires option (Fedora) (mdvbz#61712)
Patch1009:	bash-requires.patch
Patch1010:	bash-ru-ua-l10n.patch
BuildRequires:	autoconf2.5
BuildRequires:	bison
BuildRequires:	groff
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	texinfo
Conflicts:	etcskel <= 1.63-11mdk
Conflicts:	fileutils < 4.1-5mdk
Conflicts:	setup < 2.7.4-1mdv
# explicit file provides
Provides:	/bin/sh

%description
Bash is a GNU project sh-compatible shell or command language
interpreter. Bash (Bourne Again shell) incorporates useful features
from the Korn shell (ksh) and the C shell (csh). Most sh scripts
can be run by bash without modification.

Bash offers several improvements over sh, including command line
editing, unlimited size command history, job control, shell
functions and aliases, indexed arrays of unlimited size and 
integer arithmetic in any base from two to 64. Bash is ultimately
intended to conform to the IEEE POSIX P1003.2/ISO 9945.2 Shell and
Tools standard.

%package doc
Summary:	Documentation for the GNU Bourne Again shell (bash)
Group:		Books/Computer books
Requires:	%{name} = %{version}-%{release}
Obsoletes:	bash3-doc < 3.2.48
Provides:	bash3-doc

%description doc
This package provides documentation for GNU Bourne Again shell (bash).

%prep
%setup -q -a 2
mv doc/README .

%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0
%patch12 -p0
%patch13 -p0
%patch14 -p0
%patch15 -p0
%patch16 -p0
%patch17 -p0
%patch18 -p0
%patch19 -p0
%patch20 -p0
%patch21 -p0
%patch22 -p0
%patch23 -p0
%patch24 -p0
%patch25 -p0
%patch26 -p0
%patch27 -p0
%patch28 -p0
%patch29 -p0
%patch30 -p0
%patch31 -p0
%patch32 -p0
%patch33 -p0
%patch34 -p0
%patch35 -p0
%patch36 -p0
%patch37 -p0
%patch38 -p0
%patch39 -p0
%patch40 -p0
%patch41 -p0
%patch42 -p0
%patch43 -p0
%patch44 -p0
%patch45 -p0

%patch200 -p1

%patch1000 -p1 -b .security
%patch1001 -p1 -b .profile
# 20060126 warly obsolete exept maybe for the replacement of @ by kH, this will have to be checked
#%patch1002 -p1 -b .readline
%patch1003 -p1 -b .compat
%patch1004 -p0 -b .extended_quote
%patch1005 -p1 -b .strcoll_bugx
%patch1006 -p1 -b .checkwinsize
%patch1007 -p1 -b .lzma
%patch1008 -p1 -b .format-security
%patch1009 -p1 -b .requires~
# bash-ru-ua-l10n.patch
%patch1010 -p1 -b .ruua

%build
%global optflags %{optflags} -Os
export DEBUGGER_START_FILE="%{_datadir}/bashdb/bashdb-main.inc"

# Drag in support for aarch64-* and the likes
cp -a %_datadir/libtool/config/* .
cp -a %_datadir/libtool/config/* support/

%configure2_5x \
    --enable-command-timing \
    --disable-rpath \
    --enable-history \
    --enable-job-control \
    --enable-multibyte \
    --enable-readline \
    --with-installed-readline \
    --without-gnu-malloc \
    --without-bash-malloc \
    --disable-strict-posix-default \
    --enable-select \
    --enable-prompt-string-decoding \
    --enable-process-substitution \
    --enable-alias \
    --enable-bang-history \
    --enable-coprocesses \
    --enable-directory-stack \
    --enable-brace-expansion

%make

# all tests must pass
%check
make check

%install
%makeinstall_std

# beurk
rm -rf %{buildroot}%{_datadir}/locale/en@boldquot/ %{buildroot}%{_datadir}/locale/en@quot/

#Sucks
chmod +w doc/texinfo.tex
chmod 755 examples/misc/aliasconv.*
chmod 755 examples/misc/cshtobash
chmod 755 %{buildroot}%{_bindir}/bashbug

# Take out irritating ^H's from the documentation
mkdir tmp_doc
for i in `/bin/ls doc/` ; \
	do cat doc/$i > tmp_doc/$i ; \
	cat tmp_doc/$i | perl -p -e 's/.//g' > doc/$i ; \
	rm tmp_doc/$i ; \
	done
rmdir tmp_doc

mkdir -p %{buildroot}/bin
( cd %{buildroot} && mv usr/bin/bash bin/bash )
( cd %{buildroot}/bin && ln -s bash sh )

# make builtins.1 and rbash.1 with bash.1 in place (fix mdv#51379)
(cd doc
mkdir tmp_fix_so
cd tmp_fix_so
cp ../builtins.1 ../rbash.1 .
sed -e '/^.if \\n(zZ=1 .ig zZ/,/^.zZ/d' ../bash.1 > bash.1
soelim builtins.1 > ../builtins.1
sed -e '/^.if \\n(zY=1 .ig zY/,/^.zY/d' ../bash.1 > bash.1
soelim rbash.1    > ../rbash.1
)

# make manpages for bash builtins as per suggestion in DOC/README
(cd doc
sed -e '
/^\.SH NAME/, /\\- bash built-in commands, see \\fBbash\\fR(1)$/{
/^\.SH NAME/d
s/^bash, //
s/\\- bash built-in commands, see \\fBbash\\fR(1)$//
s/,//g
b
}
d
' builtins.1 | tr -s ' ' '\n' | grep -v -E '^(printf|export|echo|pwd|test|kill)$' > man.pages
# tr is needed because there are few commands in a row separated with a whilespace
# tr is needed because there are few commands in a row separated with a whilespace
install -m 644 builtins.1 %{buildroot}%{_mandir}/man1/builtins.1

install -m 644 rbash.1 %{buildroot}%{_mandir}/man1/rbash.1

for i in `cat man.pages` ; do
# install man-page
	echo .so man1/builtins.1 > %{buildroot}%{_mandir}/man1/$i.1
# now turn man.page into a filelist for the man subpackage
	echo "%{_mandir}/man1/$i.1%{_extension}" >> ../man.pages.filelist
done

cat man.pages |tr -s ' ' '\n' |sed '
1i\
%defattr(0644,root,root,0755)
s:^:%{_mandir}/man1/:
s/$/.1%{_extension}/
' > ../man.pages

mkdir -p %{buildroot}%{_sysconfdir}/skel
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/skel/.bashrc
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/skel/.bash_profile
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/skel/.bash_logout
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/profile.d/60alias.sh
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/bashrc
install -m 644 %{SOURCE8} %{buildroot}%{_sysconfdir}/profile.d/95bash-extras.sh

ln -s bash %{buildroot}/bin/rbash

install -m 644 bash.info %{buildroot}%{_infodir}
)

%find_lang %{name}

# merges list
cat man.pages.filelist %{name}.lang > files.list

# install documentation manually in expected place
install -d -m 755 %{buildroot}%{_docdir}/%{name}
install -m 644 README COMPAT NEWS NOTES POSIX CHANGES \
    %{buildroot}%{_docdir}/%{name}
cp -pr examples doc/*.ps doc/*.0 doc/*.html doc/article.txt \
    %{buildroot}%{_docdir}/%{name}

%files -f files.list
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/README
%config(noreplace) %{_sysconfdir}/skel/.b*
%{_sysconfdir}/profile.d/60alias.sh
%{_sysconfdir}/profile.d/95bash-extras.sh
%config(noreplace) %{_sysconfdir}/bashrc
/bin/rbash
/bin/bash
/bin/sh
%{_infodir}/bash.info*
%{_mandir}/man1/bash.1*
%{_mandir}/man1/rbash.1*
%{_mandir}/man1/builtins.1*
%{_mandir}/man1/bashbug.1*
%{_bindir}/bashbug

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}/*
%exclude %{_docdir}/%{name}/README


%changelog
* Sun Jan  6 2013 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.2-13
- update to patchlevel 42
- build against libncursesw rather than libtermcap

* Wed Aug 22 2012 Danila Leontiev <danila.leontiev@rosalab.ru> 4.2-11.2
- Updated release version

* Mon Aug 20 2012 Danila Leontiev <danila.leontiev@rosalab.ru> 4.2-10
- Sync with Mandriva for fix CVE-2012-3410
- Reapplyed patch bash-4.2-multibyte.patch

* Thu Aug 09 2012 Oden Eriksson <oeriksson@mandriva.com> 4.2-9.1
- apply official patches 011 to 037 (033 fixes CVE-2012-3410)
- rearrange patches and drop redundant ones

* Tue Aug 23 2011 Alexander Barakin <abarakin@mandriva.org> 4.2-9mdv2011.0
+ Revision: 696288
- sync with cooker
- update ru and ua l10n

* Sun Jun 19 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.2-7
+ Revision: 686020
- add patches 009 and 010 from upstream

* Wed Apr 20 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.2-6
+ Revision: 656351
- add 8 patches from upstream
- enable checks

* Sun Mar 06 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.2-5
+ Revision: 642353
- add --rpm-requires patch (#61712)

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 4.2-4
+ Revision: 639962
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - store bash documentation in /usr/share/doc/bash, not in /usr/share/doc/bash-doc

* Tue Feb 22 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.2-3
+ Revision: 639373
- drop conflicting 'false.1' man page as well

* Tue Feb 22 2011 Eugeni Dodonov <eugeni@mandriva.com> 4.2-2
+ Revision: 639299
- Do not build true manpage, provided by coreutils (#62590)

* Mon Feb 21 2011 Eugeni Dodonov <eugeni@mandriva.com> 4.2-1
+ Revision: 639152
- Reenable ru localization.
- Update to bash 4.2.
  Drop upstream patches.

* Sun Oct 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.1-8mdv2011.0
+ Revision: 586309
- add two patches from upstream

* Sun Aug 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.1-7mdv2011.0
+ Revision: 564597
- add upstream patches 006 and 007
- compile with -Os flag
- enable few options in configure script

* Mon May 31 2010 Eugeni Dodonov <eugeni@mandriva.com> 4.1-6mdv2010.1
+ Revision: 546801
- Revert change in HISTIGNORE, proper fix will be in mc package.

* Mon May 31 2010 Eugeni Dodonov <eugeni@mandriva.com> 4.1-5mdv2010.1
+ Revision: 546784
- Work around mc messing up bash history (#59547)

* Wed Mar 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 4.1-4mdv2010.1
+ Revision: 530535
- apply pending official patches

* Fri Mar 05 2010 Claudio Matsuoka <claudio@mandriva.com> 4.1-3mdv2010.1
+ Revision: 514787
- Add extra bash settings provided by Eric Piel (#27126)

* Wed Jan 13 2010 Eugeni Dodonov <eugeni@mandriva.com> 4.1-2mdv2010.1
+ Revision: 490840
- Disable displaying of control characters in ls command by default, as it has security consequences (CVE-2010-0002, #56882).

* Sun Jan 03 2010 Funda Wang <fwang@mandriva.org> 4.1-1mdv2010.1
+ Revision: 485797
- New version 4.1
- drop 4.0 patches

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - /etc/profile.d/alias.sh should not be executable, but should have an order prefix

* Tue Oct 06 2009 Thierry Vignaud <tv@mandriva.org> 4.0-7mdv2010.0
+ Revision: 454756
- package CHANGE in doc

* Fri Sep 18 2009 Eugeni Dodonov <eugeni@mandriva.com> 4.0-6mdv2010.0
+ Revision: 444369
- Updated to patchset 33.

* Sun Aug 30 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.0-5mdv2010.0
+ Revision: 422505
- synch patches with upstream (225,226,227 and 228)
- tune up configure options

* Tue Jul 28 2009 Frederic Crozat <fcrozat@mandriva.com> 4.0-4mdv2010.0
+ Revision: 402384
- Update default configuration to use same prompt for xterm and screen titles (Fedora)
- Add warning in default configuration hinting users to create a separate file in /etc/profile.d (Fedora)

* Thu Jun 18 2009 Wanderlei Cavassin <cavassin@mandriva.com.br> 4.0-3mdv2010.0
+ Revision: 387176
- make builtins.1 and rbash.1 with in place bash.1 pertinent lines,
  avoiding problem in sourcing a compressed man (fix mdv #51379)

* Tue Jun 02 2009 Eugeni Dodonov <eugeni@mandriva.com> 4.0-2mdv2010.0
+ Revision: 382268
- Updated to official patchset 24.

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 4.0-1mdv2010.0
+ Revision: 370148
- new version
- drop documentation, not available for this version anymore

* Wed Feb 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.2.48-3mdv2009.1
+ Revision: 344740
- rebuild against new readline

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.2.48-2mdv2009.1
+ Revision: 339012
- drop fedora catch-all completion patch, as it break completion definition output format, causing troubles in indirect completions such as sudo

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - bunzip all patches

* Mon Jan 12 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2.48-1mdv2009.1
+ Revision: 328797
- update to new version 3.2.48
- patches from 101 to 148 were merged upstream
- new license policy
- fix mixture of tabs and spaces
- better description for doc subpackage
- disable rpath
- enable few configure options
- versionate obsoletes
- spec file clean

* Wed Dec 17 2008 Frederic Crozat <fcrozat@mandriva.com> 3.2-12mdv2009.1
+ Revision: 315133
- Remove dietlibc build, useless
- Remove patches 13 (no longer needed), 90 (replaced by configuration in setup package)
- Regenerate patch 3, 135
- Patch1005 (Behdad): speedup bach completion (Fedora bug #475229)
- Patch1006: fix format string

* Fri Dec 05 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-11mdv2009.1
+ Revision: 310749
- update to official patch level 48
- re-enable official patches 20 to 25, #35880 seems to be fixed

* Fri Dec 05 2008 Pixel <pixel@mandriva.com> 3.2-10mdv2009.1
+ Revision: 310732
- .bash_profile: calling keychain is already done in /etc/profile.d/99keychain.sh (fixes #46045)

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - remove rather usless info in description

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 3.2-9mdv2009.0
+ Revision: 264327
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Thierry Vignaud <tv@mandriva.org> 3.2-8mdv2009.0
+ Revision: 218046
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 05 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-7mdv2008.1
+ Revision: 115767
- skip patches 21 to 25 to, as they don't apply cleanly when removing patch 20
- don't apply official patch 020, it seems to be responsible for bug #35880

* Thu Nov 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-6mdv2008.1
+ Revision: 113958
- update to current official patchset
- test profile scriptlet readability, not executability

* Fri Aug 31 2007 Pixel <pixel@mandriva.com> 3.2-5mdv2008.0
+ Revision: 76690
- cleanup temp variable (#31851)

* Sat Aug 11 2007 Olivier Blin <blino@mandriva.org> 3.2-4mdv2008.0
+ Revision: 61891
- fix man page extension (using _extension macro)
- really add patches 16 and 17 (not twice again patch 15)

  + Thierry Vignaud <tv@mandriva.org>
    - use color by default for egrep & grep

  + Anssi Hannula <anssi@mandriva.org>
    - add note about upgrading into alias.sh

  + Jérôme Soyer <saispo@mandriva.org>
    - Bump release
    - Add two patches

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - add lzma support to bash completion (P1004)

* Mon Apr 30 2007 Pixel <pixel@mandriva.com> 3.2-2mdv2008.0
+ Revision: 19543
- explicit file provide /bin/sh

* Thu Apr 19 2007 Jérôme Soyer <saispo@mandriva.org> 3.2-1mdv2008.0
+ Revision: 14985
- Apply Upstream patch

