%define _rver 3.2
%define i18ndate 20010626

Summary:	The GNU Bourne Again shell (bash)
Name:		bash
Version:	%{_rver}.48
Release:	%mkrel 2
Group:		Shells
License:	GPLv2+
URL:		http://www.gnu.org/software/bash/bash.html
Source0:	ftp://ftp.gnu.org/pub/gnu/bash/bash-%{version}.tar.gz
Source1:	%{SOURCE0}.sig
Source2:	ftp://ftp.gnu.org/pub/gnu/bash/bash-doc-%{_rver}.tar.bz2
Source3:	dot-bashrc
Source4:	dot-bash_profile
Source5:	dot-bash_logout
Source6:	alias.sh
Source7:	bashrc
Patch1:		bash-2.02-security.patch
# ensure profile is read (Redhat)
Patch3:		bash-2.03-profile.patch
Patch4:		bash-2.05b-readlinefixes.patch
Patch6:		bash-2.04-compat.patch
Patch80:	bash-2.05b-builtins.patch
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
BuildRequires:	autoconf2.5
BuildRequires:	bison
BuildRequires:	libtermcap-devel
BuildRequires:	texinfo
Conflicts:	etcskel <= 1.63-11mdk
Conflicts:	fileutils < 4.1-5mdk
Conflicts:	setup < 2.7.4-1mdv
Obsoletes:	bash3 < 3.2.48
Provides:	bash3
# explicit file provides
Provides:	/bin/sh
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch80 -p0 -b .fix_so
%patch1000 -p1 -b .strcoll_bugx
%patch1003 -p1 -b .checkwinsize
%patch1004 -p1 -b .lzma
#%patch1005 -p1 -b .speed
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
    --disable-command-timing \
    --disable-rpath \
    --enable-history \
    --enable-job-control \
    --enable-multibyte \
    --enable-readline

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

mkdir -p %{buildroot}%{_sysconfdir}/skel
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/skel/.bashrc
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/skel/.bash_profile
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/skel/.bash_logout
install -m 755 %{SOURCE6} %{buildroot}%{_sysconfdir}/profile.d/alias.sh
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/bashrc

ln -s bash %{buildroot}/bin/rbash

# These're provided by other packages
rm -f %{buildroot}{%{_infodir}/dir,%{_mandir}/man1/{echo,export,kill,printf,pwd,test}.1}

cd ..

install -m 644 doc/bash.info %{buildroot}%{_infodir}/

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
