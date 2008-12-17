%define name	bash
%define version	3.2
%define release	%mkrel 12
%define i18ndate	20010626

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	The GNU Bourne Again shell (bash)
Group:		Shells
License:	GPL
URL:		http://www.gnu.org/software/bash/bash.html
Source0:	ftp://ftp.gnu.org/pub/gnu/bash/bash-%{version}.tar.bz2
Source1:	ftp://ftp.gnu.org/pub/gnu/bash/bash-doc-%{version}.tar.bz2

Source2:	dot-bashrc
Source3:	dot-bash_profile
Source4:	dot-bash_logout
Source5:	alias.sh
Source6:	bashrc


Patch1:         bash-2.02-security.patch.bz2
# ensure profile is read (Redhat)
Patch3:         bash-2.03-profile.patch
Patch4:         bash-2.05b-readlinefixes.patch.bz2
Patch6:         bash-2.04-compat.patch.bz2

Patch80:	bash-2.05b-builtins.patch.bz2
#https://bugzilla.novell.com/attachment.cgi?id=67684
Patch100:	bash-3.1-extended_quote.patch.bz2

# Official upstream patches
Patch101: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-001
Patch102: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-002
Patch103: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-003
Patch104: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-004
Patch105: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-005
Patch106: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-006
Patch107: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-007
Patch108: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-008
Patch109: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-009
Patch110: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-010
Patch111: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-011
Patch112: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-012
Patch113: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-013
Patch114: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-014
Patch115: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-015
Patch116: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-016
Patch117: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-017
Patch118: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-018
Patch119: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-019
Patch120: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-020
Patch121: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-021
Patch122: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-022
Patch123: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-023
Patch124: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-024
Patch125: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-025
Patch126: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-026
Patch127: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-027
Patch128: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-028
Patch129: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-029
Patch130: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-030
Patch131: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-031
Patch132: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-032
Patch133: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-033
Patch134: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-034
Patch135: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-035
Patch136: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-036
Patch137: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-037
Patch138: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-038
Patch139: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-039
Patch140: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-040
Patch141: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-041
Patch142: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-042
Patch143: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-043
Patch144: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-044
Patch145: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-045
Patch146: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-046
Patch147: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-047
Patch148: ftp://ftp.gnu.org/gnu/bash/bash-3.2-patches/bash32-048

Patch1000:	bash-strcoll-bug.diff.bz2
Patch1003:	bash-2.05b-checkwinsize.patch.bz2
Patch1004:	bash-3.2-lzma-copmpletion.patch
# (fc) 3.2-12mdv speedup bash completion (Fedora) (Fedora bug #475229)
Patch1005:	bash-3.2-speed-completion.patch
# (fc) 3.2-12mdv fix format string
Patch1006:	bash-3.2-format-security.patch
BuildRequires:	autoconf2.5
BuildRequires:	bison
BuildRequires:	libtermcap-devel
BuildRequires:	texinfo
Conflicts:	etcskel <= 1.63-11mdk
Conflicts:	fileutils < 4.1-5mdk
Conflicts:	setup < 2.7.4-1mdv
BuildRoot:	%{_tmppath}/%{name}-%{version}
Obsoletes: 	bash3
Provides:	bash3
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
Group:		Books/Computer books
Summary:	Documentation for the GNU Bourne Again shell (bash)
Requires:	bash = %{version}
Obsoletes:	bash3-doc
Provides:	bash3-doc

%description doc
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

Bash is the default shell for Mandriva Linux. You should install
bash because of its popularity and power. You'll probably end up
using it.

This package include doc guid examples and manual for zsh.

%prep
%setup -q -n bash-%{version} -a 1
mv doc/README .

%patch1 -p1 -b .security
%patch3 -p1 -b .profile

# 20060126 warly obsolete exept maybe for the replacement of @ by kH, this will have to be checked
#%patch4 -p1 -b .readline
%patch6 -p1 -b .compat

%patch101 -p0 -b .pl001
%patch102 -p0 -b .pl002
%patch103 -p0 -b .pl003
%patch104 -p0 -b .pl004
%patch105 -p0 -b .pl005
%patch106 -p0 -b .pl006
%patch107 -p0 -b .pl007
%patch108 -p0 -b .pl008
%patch109 -p0 -b .pl009
%patch110 -p0 -b .pl010
%patch111 -p0 -b .pl011
%patch112 -p0 -b .pl012
%patch113 -p0 -b .pl013
%patch114 -p0 -b .pl014
%patch115 -p0 -b .pl015
%patch116 -p0 -b .pl016
%patch117 -p0 -b .pl017
%patch118 -p0 -b .pl018
%patch119 -p0 -b .pl019
%patch120 -p0 -b .pl020
%patch121 -p0 -b .pl021
%patch122 -p0 -b .pl022
%patch123 -p0 -b .pl023
%patch124 -p0 -b .pl024
%patch125 -p0 -b .pl025
%patch126 -p0 -b .pl026
%patch127 -p0 -b .pl027
%patch128 -p0 -b .pl028
%patch129 -p0 -b .pl029
%patch130 -p0 -b .pl030
%patch131 -p0 -b .pl031
%patch132 -p0 -b .pl032
%patch133 -p0 -b .pl033
%patch134 -p0 -b .pl034
%patch135 -p0 -b .pl035
%patch136 -p0 -b .pl036
%patch137 -p0 -b .pl037
%patch138 -p0 -b .pl038
%patch139 -p0 -b .pl039
%patch140 -p0 -b .pl040
%patch141 -p0 -b .pl041
%patch142 -p0 -b .pl042
%patch143 -p0 -b .pl043
%patch144 -p0 -b .pl044
%patch145 -p0 -b .pl045
%patch146 -p0 -b .pl046
%patch147 -p0 -b .pl047
%patch148 -p0 -b .pl048

%patch80 -p0 -b .fix_so

%patch1000 -p1 -b .strcoll_bugx
%patch1003 -p1 -b .checkwinsize
%patch1004 -p1 -b .lzma
%patch1005 -p1 -b .speed
%patch1006 -p1 -b .format-security
%patch100 -p0 -b .quote

echo %{version} > _distribution
echo %{release} > _patchlevel
sed -i -e s/mdk// _patchlevel

%build
#libtoolize --copy --force

#export CFLAGS="$RPM_OPT_FLAGS"
#export CONFIGURE_TOP=".."
export DEBUGGER_START_FILE="%{_datadir}/bashdb/bashdb-main.inc"
%configure2_5x \
    --disable-command-timing
%make 
#CFLAGS="$RPM_OPT_FLAGS"
# all tests must pass
%check
make check

%install
rm -rf %{buildroot}

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
pushd %{buildroot} && mv usr/bin/bash bin/bash && popd
pushd %{buildroot}/bin && ln -s bash sh && popd
pushd %{buildroot}/bin && ln -sf bash bash3 && popd

# make manpages for bash builtins as per suggestion in DOC/README
cd doc
sed -e '
/^\.SH NAME/, /\\- bash built-in commands, see \\fBbash\\fR(1)$/{
/^\.SH NAME/d
s/^bash, //
s/\\- bash built-in commands, see \\fBbash\\fR(1)$//
s/,//g
b
}
d
' builtins.1 > man.pages
install -m 644 builtins.1 %{buildroot}%{_mandir}/man1/builtins.1

install -m 644 rbash.1 %{buildroot}%{_mandir}/man1/rbash.1

for i in `cat man.pages` ; do
  echo .so man1/builtins.1 > %{buildroot}%{_mandir}/man1/$i.1
done

# now turn man.pages into a filelist for the man subpackage

cat man.pages |tr -s ' ' '\n' |sed '
1i\
%defattr(0644,root,root,0755)
s:^:%{_mandir}/man1/:
s/$/.1%{_extension}/
' > ../man.pages

perl -p -i -e 's!.*/(printf|export|echo|pwd|test|kill).1%{_extension}!!' ../man.pages

mkdir -p %buildroot%{_sysconfdir}/skel
mkdir -p %buildroot%{_sysconfdir}/profile.d
install -m 644 %{SOURCE2} %buildroot%{_sysconfdir}/skel/.bashrc
install -m 644 %{SOURCE3} %buildroot%{_sysconfdir}/skel/.bash_profile
install -m 644 %{SOURCE4} %buildroot%{_sysconfdir}/skel/.bash_logout
install -m 755 %{SOURCE5} %buildroot%{_sysconfdir}/profile.d/alias.sh
install -m 644 %{SOURCE6} %buildroot%{_sysconfdir}/bashrc

ln -s bash %buildroot/bin/rbash

# These're provided by other packages
rm -f %buildroot{%_infodir/dir,%_mandir/man1/{echo,export,kill,printf,pwd,test}.1}

cd ..

install -m 644 doc/bash.info %buildroot%{_infodir}/

%clean
rm -rf %{buildroot}

%files -f man.pages
%defattr(-,root,root)
%doc README CHANGES
%config(noreplace) %{_sysconfdir}/skel/.b*
%{_sysconfdir}/profile.d/alias.sh
%config(noreplace) %{_sysconfdir}/bashrc
/bin/rbash
/bin/bash
/bin/bash3
/bin/sh
%{_infodir}/bash.info*
%{_mandir}/man1/bash.1*
%{_mandir}/man1/rbash.1*
%{_mandir}/man1/builtins.1*
%{_mandir}/man1/bashbug.1*
%{_bindir}/bashbug
%exclude %{_datadir}/locale/ru/LC_MESSAGES/bash.mo

%files doc
%defattr(-,root,root)
%doc COMPAT NEWS NOTES POSIX
%doc examples/bashdb/ examples/functions/ examples/misc/
%doc examples/scripts.noah/ examples/scripts.v2/ examples/scripts/
%doc examples/startup-files/
%doc doc/*.ps doc/*.0 doc/*.html doc/article.txt
