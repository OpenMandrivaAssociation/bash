%define patchlevel %(echo %{version} |cut -d. -f3)
%define major %(echo %{version} |cut -d. -f1-2)
%define beta %{nil}

%global optflags %{optflags} -Oz

# Bash is our default /bin/sh
%bcond_without bin_sh

Summary:	The GNU Bourne Again shell (bash)
Name:		bash
Version:	5.2.37
%if "%{beta}" == ""
Release:	1
Source0:	ftp://ftp.gnu.org/pub/gnu/bash/%{name}-%{major}.tar.gz
%else
Release:	0.%{beta}1
Source0:	ftp://ftp.cwru.edu/pub/bash/%{name}-%{version}-%{beta}.tar.gz
%endif
Group:		Shells
License:	GPLv2+
URL:		https://www.gnu.org/software/bash/bash.html
Source3:	dot-bashrc
Source4:	dot-bash_profile
Source5:	dot-bash_logout
Source6:	alias.sh
Source7:	bashrc
Source8:	profile.d-bash

%if 0%{?patchlevel:%{patchlevel}}
# Upstream patches
%(for i in $(seq 1 %{patchlevel}); do echo Patch$i: ftp://ftp.gnu.org/pub/gnu/bash/bash-%{major}-patches/bash$(echo %{major} |sed -e 's,\.,,g')-$(echo 000$i |rev |cut -b1-3 |rev); done)
%endif

Patch1000:	bash-2.02-security.patch
# ensure profile is read (Redhat)
Patch1001:	bash-4.0-profile.patch
Patch1003:	bash-2.04-compat.patch
#https://bugzilla.novell.com/attachment.cgi?id=67684
Patch1004:	bash-4.3-extended_quote.patch
# Official upstream patches
# none
Patch1005:	bash-strcoll-bug.diff
Patch1007:	bash-3.2-lzma-copmpletion.patch
# (proyvind): 4.2-5 add --rpm-requires option (Fedora) (mdvbz#61712)
Patch1009:	bash-requires.patch
Patch1011:	bash-5.0-no-internal-libc.patch
Patch1012:	bash-5.0-no-Lusrlib.patch
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	groff
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	texinfo
BuildRequires:	pkgconfig(readline)
Requires:	filesystem
# explicit file provides
%if %{with bin_sh}
Provides:	/bin/sh
Provides:	/bin/bash
Provides:	/usr/bin/sh
Provides:	/usr/bin/bash
%endif
Suggests:	bash-doc
Suggests:	bashbug

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

%package -n bashbug
Summary:	Report a bug in bash
Group:		Shells

%description -n bashbug
bashbug is a shell script to help the user compose and mail bug reports
concerning bash in a standard format.

%package doc
Summary:	Documentation for the GNU Bourne Again shell (bash)
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
Obsoletes:	bash3-doc < 3.2.48
Provides:	bash3-doc = %{EVRD}
Conflicts:	bash < 4.4.19-1

%description doc
This package provides documentation for GNU Bourne Again shell (bash).

%prep
%if "%{beta}" != ""
%setup -q -n %{name}-%{version}-%{beta}
%else
%setup -q -n %{name}-%{major}
%endif
mv doc/README .

%autopatch -p0 -M 999
%autopatch -p1 -m 1000

sed -i -e 's,^#define.*CHECKWINSIZE_DEFAULT.*,#define CHECKWINSIZE_DEFAULT 1,' config-top.h

%build
export DEBUGGER_START_FILE="%{_datadir}/bashdb/bashdb-main.inc"

# Drag in support for aarch64-* and the likes
cp -a %{_datadir}/libtool/config/* .
cp -a %{_datadir}/libtool/config/* support/

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
    --with-installed-readline="%{_libdir}" \
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
    --enable-brace-expansion \
    --enable-cond-command \
    --enable-extended-glob \
    --enable-progcomp \
    --enable-arith-for-command

# We get rlbmutil.h from system readline
sed -i -e '/rlmbutil.h/d' Makefile

if ! %make_build; then
# Probably caused by too many parallel bits, let's try again
    make
fi

# all tests must pass
%check
make check

%install
%make_install

# beurk
rm -rf %{buildroot}%{_datadir}/locale/en@boldquot/ %{buildroot}%{_datadir}/locale/en@quot/

#Sucks
chmod +w doc/texinfo.tex
chmod 755 examples/misc/aliasconv.*
chmod 755 examples/misc/cshtobash
chmod 755 %{buildroot}%{_bindir}/bashbug

# Take out irritating ^H's from the documentation
mkdir tmp_doc
for i in $(/bin/ls doc/) ; \
    do cat doc/$i > tmp_doc/$i ; \
    cat tmp_doc/$i | perl -p -e 's/.//g' > doc/$i ; \
    rm tmp_doc/$i ; \
done
rmdir tmp_doc


%if %{with bin_sh}
ln -s %{_bindir}/bash %{buildroot}%{_bindir}/sh
%endif

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
install -m 644 bash.1 %{buildroot}%{_mandir}/man1/bash.1
install -m 644 rbash.1 %{buildroot}%{_mandir}/man1/rbash.1
install -m 644 bashbug.1 %{buildroot}%{_mandir}/man1/bashbug.1

for i in $(cat man.pages) ; do
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

ln -s bash %{buildroot}%{_bindir}/rbash

install -m 644 bash.info %{buildroot}%{_infodir}
)

%find_lang %{name}

# merges list
cat  %{name}.lang > files.list

# install documentation manually in expected place
install -d -m 755 %{buildroot}%{_docdir}/%{name}
install -m 644 README COMPAT NEWS NOTES POSIX CHANGES \
    %{buildroot}%{_docdir}/%{name}
cp -pr examples doc/*.ps doc/*.0 doc/*.html doc/article.txt \
    %{buildroot}%{_docdir}/%{name}

# post is in lua so that we can run it without any external deps.  Helps
# for bootstrapping a new install.
# Jesse Keating 2009-01-29 (code from Ignacio Vazquez-Abrams)
# Roman Rakus 2011-11-07 (code from Sergey Romanov) #740611
%post -p <lua>
nl = '\n'
sh = '/bin/sh'..nl
bash = '/usr/bin/bash'..nl
f = io.open('/etc/shells', 'a+')
if f then
    local shells = nl..f:read('*all')..nl
    if not shells:find(nl..sh) then f:write(sh) end
    if not shells:find(nl..bash) then f:write(bash) end
    f:close()
end

%postun -p <lua>
-- Run it only if we are uninstalling
if arg[2] == 0
then
    t={}
    for line in io.lines("/etc/shells")
    do
	if line ~= "/usr/bin/bash" and line ~= "/bin/sh"
	then
	    table.insert(t,line)
	end
    end

    f = io.open("/etc/shells", "w+")
    for n,line in pairs(t)
    do
	f:write(line.."\n")
    end
    f:close()
end

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/skel/.b*
%{_sysconfdir}/profile.d/60alias.sh
%{_sysconfdir}/profile.d/95bash-extras.sh
%config(noreplace) %{_sysconfdir}/bashrc
%{_bindir}/rbash
%{_bindir}/bash
%if %{with bin_sh}
%{_bindir}/sh
%endif

%files -n bashbug
%{_bindir}/bashbug
%doc %{_mandir}/man1/bashbug.1*

%files doc -f man.pages.filelist
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*
%{_infodir}/bash.info*
%{_mandir}/man1/bash.1*
%{_mandir}/man1/rbash.1*
%{_mandir}/man1/builtins.1*
