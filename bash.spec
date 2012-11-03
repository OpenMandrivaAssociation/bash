%define i18ndate 20010626

Name:		bash
Version:	4.2
Release:	%mkrel 10
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
Patch1:		bash-2.02-security.patch
# ensure profile is read (Redhat)
Patch3:		bash-4.0-profile.patch
Patch4:		bash-2.05b-readlinefixes.patch
Patch6:		bash-2.04-compat.patch
#https://bugzilla.novell.com/attachment.cgi?id=67684
Patch100:	bash-3.1-extended_quote.patch
# Official upstream patches
# none
Patch1000:	bash-strcoll-bug.diff
Patch1003:	bash-2.05b-checkwinsize.patch
Patch1004:	bash-3.2-lzma-copmpletion.patch
# (fc) 3.2-12mdv speedup bash completion (Fedora) (Fedora bug #475229)
Patch1005:	bash-3.2-speed-completion.patch
# (fc) 3.2-12mdv fix format string
Patch1006:	bash-3.2-format-security.patch
# (proyvind): 4.2-5 add --rpm-requires option (Fedora) (mdvbz#61712)
Patch1007:	bash-requires.patch
Patch1008:	bash42-001
Patch1009:	bash42-002
Patch1010:	bash42-003
Patch1011:	bash42-004
Patch1012:	bash42-005
Patch1013:	bash42-006
Patch1014:	bash42-007
Patch1015:	bash42-008
Patch1016:	bash42-009
Patch1017:	bash42-010
Patch1018:	bash-ru-ua-l10n.patch
Patch1019:	bash42-011
Patch1020:	bash42-012
Patch1021:	bash42-013
Patch1022:	bash42-014
Patch1023:	bash42-015
Patch1024:	bash42-016
Patch1025:	bash42-017
Patch1026:	bash42-018
Patch1027:	bash42-019
Patch1028:	bash42-020
Patch1029:	bash42-021
Patch1030:	bash42-022
Patch1031:	bash42-023
Patch1032:	bash42-024
Patch1033:	bash42-025
Patch1034:	bash42-026
Patch1035:	bash42-027
Patch1036:	bash42-028
Patch1037:	bash42-029
Patch1038:	bash42-030
Patch1039:	bash42-031
Patch1040:	bash42-032
Patch1041:	bash42-033
Patch1042:	bash42-034
Patch1043:	bash42-035
Patch1044:	bash42-036
Patch1045:	bash42-037
Patch1046:	bash42-038
Patch1047:	bash42-039

BuildRequires:	autoconf2.5
BuildRequires:	bison
BuildRequires:	groff
BuildRequires:	libtermcap-devel
BuildRequires:	texinfo
Conflicts:	etcskel <= 1.63-11mdk
Conflicts:	fileutils < 4.1-5mdk
Conflicts:	setup < 2.7.4-1mdv
Obsoletes:	bash3 < 3.2.48
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

%patch1 -p1 -b .security
%patch3 -p1 -b .profile
# 20060126 warly obsolete exept maybe for the replacement of @ by kH, this will have to be checked
#%patch4 -p1 -b .readline
%patch6 -p1 -b .compat
%patch1000 -p1 -b .strcoll_bugx
%patch1003 -p1 -b .checkwinsize
%patch1004 -p1 -b .lzma
%patch1006 -p1 -b .format-security
%patch1007 -p1 -b .requires~
%patch100 -p0 -b .quote
%patch1008 -p0 -b .001
%patch1009 -p0 -b .002
%patch1010 -p0 -b .003
%patch1011 -p0 -b .004
%patch1012 -p0 -b .005
%patch1013 -p0 -b .006
%patch1014 -p0 -b .007
%patch1015 -p0 -b .008
%patch1016 -p0 -b .009
%patch1017 -p0 -b .010
# bash-ru-ua-l10n.patch
%patch1018 -p1 -b .ruua
%patch1019 -p0 -b .011
%patch1020 -p0 -b .012
%patch1021 -p0 -b .013
%patch1022 -p0 -b .014
%patch1023 -p0 -b .015
%patch1024 -p0 -b .016
%patch1025 -p0 -b .017
%patch1026 -p0 -b .018
%patch1027 -p0 -b .019
%patch1028 -p0 -b .020
%patch1029 -p0 -b .021
%patch1030 -p0 -b .022
%patch1031 -p0 -b .023
%patch1032 -p0 -b .024
%patch1033 -p0 -b .025
%patch1034 -p0 -b .026
%patch1035 -p0 -b .027
%patch1036 -p0 -b .028
%patch1037 -p0 -b .029
%patch1038 -p0 -b .030
%patch1039 -p0 -b .031
%patch1040 -p0 -b .032
%patch1041 -p0 -b .033
%patch1042 -p0 -b .034
%patch1043 -p0 -b .035
%patch1044 -p0 -b .036
%patch1045 -p0 -b .037
%patch1046 -p0 -b .038
%patch1047 -p0 -b .039

echo %{version} > _distribution
echo %{release} > _patchlevel
sed -i -e s/mdk// _patchlevel

%build
export CFLAGS="%{optflags} -Os"
export CXXFLAGS="$CFLAGS"
# (tpg) Enable RECYCLES_PIDS feature
export CPPFLAGS="$CPPFLAGS -D_GNU_SOURCE -DRECYCLES_PIDS `getconf LFS_CFLAGS`"
export DEBUGGER_START_FILE="%{_datadir}/bashdb/bashdb-main.inc"

%configure2_5x \
    --enable-command-timing \
    --disable-rpath \
    --enable-history \
    --enable-job-control \
    --enable-multibyte \
    --enable-readline \
    --with-installed-readline \
    --with-gnu-malloc \
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
pushd %{buildroot} && mv usr/bin/bash bin/bash && popd
pushd %{buildroot}/bin && ln -s bash sh && popd
pushd %{buildroot}/bin && ln -sf bash bash3 && popd

# make builtins.1 and rbash.1 with bash.1 in place (fix mdv#51379)
pushd doc
mkdir tmp_fix_so
cd tmp_fix_so
cp ../builtins.1 ../rbash.1 .
sed -e '/^.if \\n(zZ=1 .ig zZ/,/^.zZ/d' ../bash.1 > bash.1
soelim builtins.1 > ../builtins.1
sed -e '/^.if \\n(zY=1 .ig zY/,/^.zY/d' ../bash.1 > bash.1
soelim rbash.1    > ../rbash.1
popd

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

perl -p -i -e 's!.*/(printf|export|echo|false|pwd|test|true|kill).1%{_extension}!!' ../man.pages

mkdir -p %{buildroot}%{_sysconfdir}/skel
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/skel/.bashrc
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/skel/.bash_profile
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/skel/.bash_logout
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/profile.d/60alias.sh
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/bashrc
install -m 644 %{SOURCE8} %{buildroot}%{_sysconfdir}/profile.d/95bash-extras.sh

ln -s bash %{buildroot}/bin/rbash

# These're provided by other packages
rm -f %{buildroot}{%{_infodir}/dir,%{_mandir}/man1/{echo,export,false,kill,printf,pwd,test,true}.1}

cd ..

install -m 644 doc/bash.info %{buildroot}%{_infodir}/

#find_lang %{name}

# merges list
cat man.pages > files.list

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
/bin/bash3
/bin/sh
%{_infodir}/bash.info*
%{_mandir}/man1/bash.1*
%{_mandir}/man1/rbash.1*
%{_mandir}/man1/builtins.1*
%{_mandir}/man1/bashbug.1*
%{_bindir}/bashbug
%{_localedir}/*/*/*.mo

%files doc
%{_docdir}/%{name}/*
%exclude %{_docdir}/%{name}/README
