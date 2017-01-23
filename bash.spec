%define i18ndate 20010626
%define patchlevel 11
%define major 4.4
%define snap %nil

Name:		bash
Version:	%{major}.%{patchlevel}
Release:	1
Summary:	The GNU Bourne Again shell (bash)
Group:		Shells
License:	GPLv2+
URL:		http://www.gnu.org/software/bash/bash.html
Source0:	ftp://ftp.gnu.org/pub/gnu/bash/%{name}-%{major}.tar.gz
Source3:	dot-bashrc
Source4:	dot-bash_profile
Source5:	dot-bash_logout
Source6:	alias.sh
Source7:	bashrc
Source8:	profile.d-bash

# Upstream patches
%(for i in `seq 1 %{patchlevel}`; do echo Patch$i: ftp://ftp.gnu.org/pub/gnu/bash/bash-%{major}-patches/bash`echo %{major} |sed -e 's,\\.,,g'`-`echo 000$i |rev |cut -b1-3 |rev`; done)

Patch1000:	bash-2.02-security.patch
# ensure profile is read (Redhat)
Patch1001:	bash-4.0-profile.patch
Patch1002:	bash-2.05b-readlinefixes.patch
Patch1003:	bash-2.04-compat.patch
#https://bugzilla.novell.com/attachment.cgi?id=67684
Patch1004:	bash-4.3-extended_quote.patch
# Official upstream patches
# none
Patch1005:	bash-strcoll-bug.diff
Patch1007:	bash-3.2-lzma-copmpletion.patch
# (proyvind): 4.2-5 add --rpm-requires option (Fedora) (mdvbz#61712)
Patch1009:	bash-requires.patch
Patch1010:	bash-ru-ua-l10n.patch
BuildRequires:	autoconf2.5
BuildRequires:	bison
BuildRequires:	groff
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	texinfo
BuildRequires:	readline-devel
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
%setup -q -n %{name}-%{major}
mv doc/README .

# Upstream patches
%(for i in `seq 1 %{patchlevel}`; do echo %%patch$i -p0; done)

%patch1000 -p1 -b .security
%patch1001 -p1 -b .profile
# 20060126 warly obsolete exept maybe for the replacement of @ by kH, this will have to be checked
#%patch1002 -p1 -b .readline
%patch1003 -p1 -b .compat
%patch1004 -p1 -b .extended_quote
%patch1005 -p1 -b .strcoll_bugx
%patch1007 -p1 -b .lzma
#patch1009 -p1 -b .requires~
# bash-ru-ua-l10n.patch
# Needs porting to 4.3
#patch1010 -p1 -b .ruua

sed -i -e 's,^#define.*CHECKWINSIZE_DEFAULT.*,#define CHECKWINSIZE_DEFAULT 1,' config-top.h

%build
export CC=gcc
export CXX=g++

export DEBUGGER_START_FILE="%{_datadir}/bashdb/bashdb-main.inc"

# Drag in support for aarch64-* and the likes
cp -a %_datadir/libtool/config/* .
cp -a %_datadir/libtool/config/* support/

# (tpg) remove built-in libraries
rm -rf lib/{readline,termcap}/*
touch lib/{readline,termcap}/Makefile.in # for config.status
sed -ri -e 's:\$[(](RL|HIST)_LIBSRC[)]/[[:alpha:]]*.h::g' Makefile.in

%configure \
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
' builtins.1 | tr -s ' ' '\n' | grep -v -E '^(printf|export|echo|pwd|test|true|false|kill)$' > man.pages
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
%{_mandir}/man1/rbash.1*
%{_mandir}/man1/builtins.1*
%{_bindir}/bashbug

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}/*
%exclude %{_docdir}/%{name}/README
